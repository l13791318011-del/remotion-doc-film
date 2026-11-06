# Pitfalls — Remotion 短片流水线踩坑全记录（《1.5度》v1→v34 实战）

每条：现象 → 根因 → 修复模式。

## 渲染与资产

### 1. still 通过、render 报音频 404
- 现象：`remotion still` 任何帧都正常，`remotion render` 在下载 `http://localhost:3000/public/audio/vo/vo-s00a.mp3` 时 404 失败。
- 根因：still 不加载音频资产；render 会为所有挂载的 `<Audio>` 下载文件。`VO_TABLE` 按"有 sub 的镜头"自动生成 vo 路径，文件不存在只在视频渲染时爆。
- 修复：不用配音就 `defaultProps={{ bgm: true, vo: false }}`；VO_TABLE 只对真实存在的文件生成。新增镜头带 sub 时必查 `public/audio/vo/` 是否有对应文件。

### 2. 渲染中途失败（temp-dir 音频竞争）
- 现象：全片渲染随机失败，日志指向音频读取。
- 修复：每次渲染加独立临时目录 `--temp-dir=out/tmp-vXX`（vXX 递增），已成为默认实践。

### 3. pip install 被 SIGTERM
- 现象：沙箱内 `pip install librosa/imageio_ffmpeg` 直接被杀。
- 修复：只用 ffmpeg CLI + numpy 手写管线（见 scripts/bpm.py）。同理 `npx tsx -e "..."` 也会被 SIGTERM——帧号手算，别跑临时 TS。

### 4. git clone GitHub 失败
- 修复：codeload tarball 通道（`https://codeload.github.com/<owner>/<repo>/tar.gz/refs/heads/main`）下载解包，只抽需要的子目录。

## Remotion API

### 5. interpolate 颜色报 TypeError
- 现象：`interpolate(f, [0,1], ['#111','#333'])` 抛 `TypeError`。
- 根因：Remotion 的 interpolate 不支持 hex 颜色插值。
- 修复：两个同形/同位形状叠放，各自 opacity 交叉淡出（如手机熄屏动画=亮屏 rect 淡出、暗屏 rect 常驻）。

### 6. 条件挂载杀掉动画链
- 现象：图瓦卢涨水链条在"涨满"那一刻整条消失。
- 根因：组件内 `if (draw <= 0) return null`——draw 恰好在完成时 ≤0，整组被卸载。
- 修复：生命周期判断只用单侧 `if (f < start) return null`，结束态由 opacity/插值表达。

### 7. 滚动数字换行破基线
- 现象：数字从 1.1→1.5 滚动时 inline-block 换行成两行。
- 修复：渲染一个不可见占位（同字体同内容宽度）撑住布局，数字本体用两层绝对定位（亮层+暗层）做滚动窗口。

### 8. timeline 的 fadeOut 字段不生效
- 现象：timeline 里给镜头标了 `fadeOut: 15`，成片里全是硬切，开场→正片毫无衔接。
- 根因：`Shell` 组件的 `fadeOutFrames` 是 props，timeline 字段只是文档性元数据，没人读它。
- 修复：转场意图必须落到组件 `<Shell ... fadeOutFrames={26}>`。大段落缝合=上镜淡出 ~26f + 下镜 fadeIn ~22f；风格化快切保持硬切。

### 9. 长镜头"画面干等"
- 原则：字幕按阅读速度排（每字≈6.5f+余量），镜头内必须有持续动的东西（浪线 dashoffset、粒子、Cam drift、呼吸辉光）。静止>2s 的镜头要么加微动效要么砍时长。

## 声音设计

### 10. 节拍脉冲被否决
- 教训：全片统一 BPM 脉冲缩放会与"镜头自身在动"的段落打架，用户否决。节拍数据（bpm.py 产出）保留用于音效对位，不做画面脉冲。
- 音效对位实践：spring 落定帧 +2、卡片钉入逐帧错开（+16~18f 一档）、boom 放黑卡切点+2、环境音按镜头组覆盖并 `durationInFrames` 截断。

### 11. BGM 结构
- 用户最终要求：BGM 从第 0 帧贯穿到结尾。段落感用 volume 函数做：开头 duck 到 0.7 → 关键镜头落定时 55f 内 swell 到 1 → 结尾 140f 淡出。不要再做"前段无声只留环境音"。

## 协作与验收

### 12. 用户验收节奏
- 先截图后成片；用户会逐帧挑错（元素错位如"水没浇到叶子上"、车轮悬空 14px、旗子像门板）。
- 文案修正逐字执行，不合并不润色。
- "稍微慢一点点"= 加长镜头时长并顺序拉开文字窗口，同步移动对位 SFX；一次只动用户指名的那一段（改错段落会被纠正）。
- 时长红线类约束（如 ≤4分30秒）超了要立刻上报，不擅自砍。

## 13. 渲染越来越慢（《1.5度》v32→v34 实测复盘）

- 现象：全片 7067f→7316f（+3.5%），渲染时间 5m24s→10m15s（+90%）。单帧成本 45.8ms→84ms。
- 对照实验（240 帧/组，同机同时段）：
  - 音效密集段（s02，6 条 cue 叠加）37.1s；音效稀疏段（开场 dial）44.5s → **音频不是瓶颈，场景 SVG 复杂度才是**；
  - `--concurrency=2` 同段 50.5s，比默认并发慢 → CPU 核心充足，默认并发即最优，别乱调。
- 结论分层：
  1. **长期趋势 = 代码增长**：新增场景的 SVG 节点数、Particles、文字阴影、feTurbulence 都是每帧成本，只增不减；
  2. **短期跳变 = 环境因素**：v32→v33 代码只改了数字、每帧成本却 +71%，只能归因于机器状态——夜间连续渲染、后台 Remotion Studio/浏览器标签、渲染期间又跑其他 Bash 任务抢 CPU。
- 纪律：
  - 全片渲染前关掉 studio/预览，渲染后台跑时不再并行跑 ffmpeg/截图；
  - 比较渲染速度前先归一化（时间÷帧数=每帧成本），帧数涨 3% 时间涨 90% 时别误判成代码问题；
  - 定位瓶颈用 `--frames=x-y` 分段探针（240 帧一组足够），不要猜；
  - 单帧成本想压：Grain 隔帧/降分辨率、砍同屏 SVG 节点、合并 Audio cue（实测收益小）。
