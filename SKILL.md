---
name: remotion-doc-film
description: Remotion 动效纪录片/短片制作与迭代 skill。适用于用 Remotion 构建时间轴驱动的动效短片（扁平矢量剪影风、黑屏大字幕卡、环境音+动效音效、无配音），或对已有 Remotion 项目做镜头增删、文案修正、字幕节奏调整、音效对位、衔接转场、QA 截图核验与正式渲染。触发词：Remotion、纪录片、短片、分镜、镜头、黑屏大字幕、QA 截图、contact sheet、渲染成片、字幕节奏、音效对位。
agent_created: true
---

# Remotion Doc Film（Remotion 动效纪录片工作流）

从《1.5度》气候纪录片（1920×1080@30fps，v1→v34）完整沉淀的工作流：时间轴单一事实源、帧级 QA 截图核验、动效音效对位、黑屏大字幕设计语言。

## 核心原则

1. **时间轴是唯一事实源**：所有镜头时长、入场时间、字幕文本都定义在 `timeline.ts` 的 SHOTS 数组（`{ key, dur, sub, fadeIn, fadeOut }`），from 自动累加。任何组件/音效/字幕引用时间一律用 `shotByKey('sXX').from` 派生，**绝不写裸帧号索引**——插删镜头才不会串位。
2. **先截图后成片**：任何修改必须先 `npx remotion still` 出关键帧 → ffmpeg hstack 拼对比图 → 看图核验 → 再全片渲染。用户明确要求过"先给我出截图，不要直接出视频"。
3. **文案零转述**：用户给的文案修正逐字替换，不润色不省略。中文为主，黑底卡片配英文衬线大写宽字距副句是全片双语语言。
4. **不加配音旁白**：只有 BGM + 环境音/动效音效（用户多次明确）。VO 相关渲染默认关闭（`vo: false`），否则缺失的 vo 文件会让渲染 404 失败。

## 项目结构（新项目按此搭建）

```
src/
├── Root.tsx            # Composition 入口，defaultProps { bgm: true, vo: false }
├── onefive/
│   ├── timeline.ts     # SHOTS 单一事实源 + shotByKey + TOTAL_DURATION
│   ├── design.ts       # 色板常量 C
│   ├── blocks.tsx      # 可复用积木：Shell/Cam/BlackCard/CornerSub/Sub/Particles/Grain...
│   ├── scenes.tsx      # 全部镜头组件 S01..SXX，按 key 注册
│   └── OnePointFive.tsx# SHOT_COMPONENTS 注册表 + SFX_TABLE + BGM/VO 挂载 + 全局暗角/颗粒
```

### 积木层（blocks.tsx）关键件

- **Shell**：场景外壳。`fadeIn/fadeInFrames/fadeOutFrames` **必须逐组件显式传**——timeline 里的 `fadeOut` 字段只是元数据，不会自动生效（本片曾因此整段开场→正片硬切无转场）。默认硬切是刻意的节奏，转场只在需要处加。
- **Cam**：运镜包装（s 起止缩放、origin 焦点防露边、drift 常动、crash-zoom-punch 撞停震屏）。
- **BlackCard**：黑屏大字幕卡（中文粗黑体大字 + 英文衬线副句 + 金色 accent 高亮 + 可选 rollAt 数字滚动 + 切片错位入场）。
- **CornerSub**：角标打字机字幕（逐行 cps≈2.2 字/帧打字 + 金色光标 + 行级 `hi` 字段金色重点标注）。
- **Sub/TypeText**：中英分轨双轨字幕（guizang 制式，见 references/techniques.md）。
- **Grain**：全局胶片颗粒（feTurbulence，每 2 帧重 seed）。

### 手法库（详见 references/techniques.md）

三套手法体系已融合并落地验证：**guizang fx-lab**（双轨字幕/切片错位/ConvergeRing/GlyphField/StreakField/OrbitDots/horizon 发光地平线）、**video-shotcraft**（draw-svg-trace 描线/scan-bracket-sweep 扫描括号）、**motion-design**（Grain/RollNum/overhead-camera-moves/crash-zoom-punch/light-play sheen）。写新镜头前先查手法库选语汇；粒子类组件必须纯时间函数+固定种子（seek-safe）。

### 视觉语言（用户确认过的风格基准）

- 黑屏大字幕卡 = 黑底（#05070A~#0A0D11）+ 特大号粗黑体 + 金色（#E8B04B）重点词/条款 + 辉光地平线；这是全片标志性形态，新片段必须延续。
- 深冷色调场景（海/冰/厂）→ 结尾暖光转折（#C08A45 系）。
- 知识卡/流程图：spring 滑入 + 条目错帧钉入，配 whoosh/pop 音效。

## 工作流

### 1. 改镜头 / 加镜头

1. timeline.ts 改 `dur` 或插入新 `{ key }`（新组件在 scenes.tsx 实现，OnePointFive.tsx 注册）。
2. `npx tsc --noEmit -p .` 过类型。
3. 手算绝对帧：`abs = 该镜头之前所有 dur 之和 + 局部帧`（沙箱里别依赖 tsx -e，会被 SIGTERM）。
4. 校验总长红线（如 ≤4'30"=8100f）：`总帧数/30 = 秒`。

### 2. QA 截图核验

用 `scripts/qa_stills.sh`（见脚本头部注释）：批量出关键帧 + 自动拼 contact sheet，然后看图逐帧核对文字完整、位置、对齐。每次文案/布局改动都要截到"变化后的稳定帧"（打字字幕要截打完之后的帧）。

### 3. 渲染成片

```bash
npx remotion render src/index.ts <CompositionId> out/draft-vXX.mp4 --temp-dir=out/tmp-vXX --log=error
```

- **必须带 `--temp-dir`**（独立临时目录）：默认临时目录下音频资产有竞争 bug 会导致渲染失败。
- 用 run_in_background 跑，完成后 `ffprobe` 核对时长 + `ls -la` 核对文件大小（60s 片约 60MB）。
- 版本号递增（draft-v32 → v33...），交付前 present_files。

### 4. 字幕/文字节奏

- 阅读速度基准：每字 ≈6.5f + 余量；黑卡两行文字停留 **≥2 秒**，滚动数字需再留滚动时间。
- 用户反馈"文字变得太快"= 加长镜头 dur 并按顺序拉开各段文字窗口，同时把对位 SFX 的 from 一起移。
- 结尾卡停留要宽裕：淡出前给足完整显示时间（softIn 结束到 fadeOut 开始 ≥10f）。

### 5. 衔接与转场

- 大段落之间：上一镜 `fadeOutFrames`（0.5~0.9s）+ 下一镜 `fadeIn fadeInFrames`（~22f）淡黑缝合，BGM 不断即可无缝。
- 黑卡切点配一记低音 boom（fs-825964 类）做冲击对位。
- 五格快切等风格化硬切保留，不加转场。

### 6. 音效系统

- SFX_TABLE 全部按 `shotByKey('sXX').from + 偏移` 派生；动效音效对准 spring 落定帧、卡片钉入帧。
- 环境音用 `durationInFrames` 截断长素材，按镜头组覆盖（如 s01+s02 合并一段海浪）。
- Mixkit 直链：`https://assets.mixkit.co/active_storage/sfx/<id>/<id>-preview.mp3`，下载到 `public/audio/sfx/mx-<id>.mp3`。Freesound 素材保留 CREDITS 文件。
- BGM 贯穿全片：`<Sequence from={0}>` + volume 函数做淡入/段落 swell/结尾淡出（用户明确要求音乐从头到尾）。
- BPM/节拍分析用 `scripts/bpm.py`（pip 装不上库，只用 ffmpeg+numpy 手写管线）。注意：场景自身在动的镜头不要叠加节拍脉冲（用户否决过）。

## 已知坑（详见 references/pitfalls.md）

| 坑 | 解法 |
|---|---|
| `interpolate` 不支持 hex 颜色插值（TypeError） | 双层同形 rect/shape 交叉淡出替代 |
| still 能过、render 报音频 404 | still 不下载音频；检查所有 `<Audio>` 路径真实存在，VO 不用就 `vo:false` |
| 渲染失败 temp-dir 音频竞争 | `--temp-dir=out/tmp-vXX` 独立目录 |
| `draw<=0 return null` 链条完成即消失 | 生命周期判断改为 `f < start` 单侧 |
| 滚动数字 inline-block 换行破基线 | 透明占位 + 双绝对定位层 |
| timeline `fadeOut` 字段不生效 | Shell fadeOutFrames 逐组件显式传 |
| git clone 失败 | codeload tarball 通道装 skill |
| pip install 被沙箱 SIGTERM | ffmpeg→stdout→numpy 手写分析管线 |
| 渲染越来越慢 | 先归一化每帧成本再判断；实测音频非瓶颈、SVG 复杂度和机器负载才是——见 pitfalls #13 |

## 脚本

- `scripts/qa_stills.sh` — 关键帧批量截图 + contact sheet（用法见文件头）。
- `scripts/bpm.py` — 音频 BPM + 首拍相位（onset 自相关，无第三方音频库依赖）。

## 参考文档

- `references/techniques.md` — 三套手法库速查（guizang/shotcraft/motion-design，含参数与用点）。
- `references/pitfalls.md` — 全部踩坑记录与修复代码模式（含渲染性能复盘）。
