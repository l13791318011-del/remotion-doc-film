# Assets & Style — 动效目录 / 音效资源 / 风格规范

把本地已安装 skill 里可复用的**资源与规范**集中搬运，避免每次重新翻找。
- 动效怎么实现 → `techniques.md`（参数）+ `code-recipes.md`（代码）
- 为什么这么定 → `skill-lessons.md`
- **有哪些可用 / 去哪下载 / 风格红线** → 本文件

---

# A. 动效资源目录

## A1. video-shotcraft 技法卡（本机 `~/.workbuddy/skills/video-shotcraft/references/shots/`）

约 130 张按类别归档的技法卡。**★ = 本片已落地验证**，其余是可选的语汇库。
用之前先问「这个效果对应我这个题材的哪一点」，一支片挑 3–5 个，别堆。

| 类别 | 技法卡（文件名） |
|---|---|
| **camera 运镜** | ★`overhead-camera-moves` · ★`crash-zoom-punch` · `depth-layer-moves` · `space-camera-moves` · `steep-tilt-glide` · `tension-camera-moves` · `graze-face-tour` · `cursor-flyover` · `basic-3d-scene` · `terminal-3d` |
| **typography 文字** | `blur-slide` · `brace-expand` · `countdown-arc-scatter` · `document-typewriter-reveal` · `flying-words` · `glitch-cycle` · `gradient-word-sweep` · `lead-word-zoom-assemble` · `marker-underline-title` · `outline-word-fill` · `paper-title-card` · `pill-slot-cycle` · `pill-chip-slot-cycle-handled` · `text-column-converge` · `title-demote-to-label` · `type-assembly-moves` · `type-entrance-moves` · `type-rhythm-sync` · `typewriter-moves` · `vertical-word-roll-blur-cycle` |
| **opening 开场** | `brand-ink-open` · `crane-rise-reveal` · `dataviz-landscape-open` · `fracture` · `icon-field-colorize` · `letterspace-materialize` · `magician-card-flourish` · `orbit-ring-title-open` · `spotlight-hero-card` · `stroke-segment-build` · `text-as-mask` |
| **ui-entrance 入场** | ★`draw-svg-trace` · `bezier-source-converge-merge` · `card-stack` · `carousel-3d` · `cloner-depth-echo` · `deck-deal-flyin` · `doc-park-left-pill-deal` · `element-body-moves` · `integration-hub-map` · `list-reveal` · `list-stack-press` · `neon-frame-forerun` · `neon-frame-orbit-drop` · `page-waterfall-wall` · `product-card-progressive-assemble` · `radial-wave` · `research-card-stack-scroll` · `row-embed` · `value-stagger-gradient` · `avatar-bracket-carousel` |
| **effects 特效** | ★`light-play-moves`（B 式 sheen） · ★`scan-bracket-sweep` · `assemble-then-type-flyin` · `aurora-bloom-bg-flip` · `brand-frame-snap` · `fui-hud-moves` · `glow-flyline-moves` · `icon-performance-moves` · `impact-feedback` · `radial-ripple-phone-chips` · `riso-print-hits` · `scanline-annotate-focus` · `scanline-assemble-flyin` · `slam-entrance-moves` · `spotlight-sweep-moves` |
| **data 数据** | `before-after-slider-scrub` · `chart-live-moves` · `gauge-readout-moves` · `scroll-brake-moves` · `timeline-travel` |
| **rhythm 节奏** | `beat-cut-moves` · `beat-step-list-theme-cycle` · `panel-grid-moves` · `quad-split-parallel-scenes` · `rhythm-interrupt-moves` · `sakuga-timing-shift` · `speed-ramp-freeze` · `trailer-grammar-moves` |
| **transition 转场** | `bottom-push-stack-wipe` · `card-flip-reveal` · `card-flock-tumble` · `circle-match-iris` · `gradient-transition` · `line-carry-transition` · `mosaic-reframe` · `page-turn-transitions` · `print-texture-transitions` · `shot-transitions` · `tear-streak-transitions` · `transition-hidden-cut` · `transition-travel` · `white-flash-logo-simplify-cut` · `wipe-transitions` |
| **interaction 交互** | `autolayout-gap-dial` · `canvas-materialize-moves` · `chip-grid-single-select-blackout` · `collab-cursor-moves` · `glass-pill-dictation-typing` · `hashtag-to-pill-materialize` · `picker-carousel-feature-cycle` · `segmented-thumb-hero` · `theme-switch-moves` · `type-and-filter` · `voice-waveform-live` |
| **outro 收尾** | `grain-dissolve` · `logo-shrink-wordmark-lockup` · `neon-triple-marquee` · `outro-group-photo-launch` · `ui-strip-away-outro` · `ui-to-brand-morph` |

另有 `references/sequences/promo-energy-arc.md`（整套能量弧序列）、`references/music-beat-sync.md`（卡点）、
`references/aesthetic-rules.md`（判例式审美准则，见 §C4）、`references/final-review.md`（终检清单）。

## A2. guizang 视觉手法词汇表（`references/visual-vocabulary.md`）

| 组 | 手法（★ 有 fx-lab 可改写样例） | 表达 | 常见陷阱 |
|---|---|---|---|
| 开场钩子 | ★流线场/穿越、槽位轮换、真实界面微距、一句话逐字书写、数据先行 | 速度 / 重复痛点 / 直接进入 / 分量 / 用结果开场 | 平静题材用流线显得浮夸；没有来源的数字 |
| 品牌标志 | ★粒子汇聚成形、构造线与控制点、字标描边成实、挤出等距体块、形状变形 | 归一 / 精密 / 草图到成品 / 稳重 / 形变 | 变形中间态很丑；中文字体路径太复杂 |
| 舞台背景 | ★发光地平线、渐变场、★字符场、纸张与墨、网格与点阵、环境景深 | 仪式感 / 情绪 / 技术感 / 温度 / 秩序 / 真实 | 连续镜头都用地平线；纹理太重显脏 |
| 产品上镜 | 放大取景推拉、透视倾斜面板、平放看板飞越、沿 Z 抬起、★环绕、光标操作、真实打字 | 看清一件事 / 空间 / 全局 / 指出重点 / 多对一 / 可交互 | 3D 倾斜下手算落点会偏；点击后没有状态变化 |
| 章节文字 | 章节大字、★切片错位、逐字模糊入场、词语快切、光束扫过、衬线编辑感标题 | 换段 / 打断 / 精致 / 多小功能 / 强调 / 品位 | **把切片错位当默认标题入场**；每个元素都逐字模糊会单调 |
| 转场 | 硬切卡拍、穿越缩放、推近接续、白闪/黑场、遮罩擦除 | 冲击 / 进入内部 / 元素接续 / 大段落 / 并列 | 浅色↔深色长交叉淡化会中间发灰 → 用硬切或先模糊退场 |

**技术约束（通用）**：画面只由时间决定（seek-safe）；GSAP 挂主时间轴且 paused、`seek` 驱动；
canvas/WebGL 写成 `render(t)` 纯函数；随机数固定种子；一个 WebGL 画布一个场景，全片 ≤2–4 个上下文；
大面积 blur 会拖慢导出，先渲几帧估耗时。

## A3. motion-design / howseen 效果清单

- **motion-design**：Grain 颗粒 · RollNum 数字竖滚 · overhead-camera-moves · crash-zoom-punch · light-play sheen ·
  WobbleFilter 手绘 line boil · dot grid drift · Mask 词揭示 · velocity-derived trails。
- **howseen（可移植到 seek 架构的效果）**：liquid glass（canvas displacement）· goo · 6-blade iris ·
  variable-font squeeze · 3D cube · equalizer · blob mask · animated beam / border beam ·
  dotted grid · drifting blobs · sheen sweep · sparkles · masked text rise（translateY 105% + overflow hidden，词错帧 55ms）·
  flood（半径到四角 hypot ×1.05，0.30–0.35s）· glass / iris / morph shapes。
- **可用库（必须能 seek）**：GSAP `tl.pause(); tl.totalTime(t+0.001,true); tl.totalTime(t,true)` ·
  WAAPI/CSS `document.getAnimations().forEach(a => {a.pause(); a.currentTime=t*1000})` ·
  Lottie `goToAndStop(t*1000)` · Anime.js `anim.seek(ms)`（建时 `autoplay:false`）·
  Theatre.js `sheet.sequence.position=t`（render 时丢掉 Studio）。
  **禁用**：只能实时跑的（Spline runtime、Unicorn Studio、CSS/framer-motion live）。
- **video-beats 整屏卡节拍类型**：full-screen crumpled paper（大段落转场/大数字/论点句）、
  beat types 决策表见 `~/.workbuddy/skills/hyperframes-video-beats/SKILL.md`。

## A4. 选效果的决策顺序

1. 先定「这一段要让观众记住什么」→ 2. 从题材推导出一个专属手法（而非从目录里挑好看的）→
3. 检查全片是否已用过同类手法（**一种手法全片只当一次主角**）→ 4. 查 `techniques.md` 参数 →
5. 查 `code-recipes.md` 代码 → 6. 出 still 验 → 7. 才可进全片。
⚠️ 稀缺性就是价值：sheen / horizon / crash-zoom / 切片错位这类仪式感效果，**全片各一次**。

---

# B. 音效与音乐资源

## B1. Mixkit SFX（本片 27 条 cue 的主要来源，免费商用）

```
下载直链模板：https://assets.mixkit.co/active_storage/sfx/<id>/<id>-preview.mp3
保存命名：    public/audio/sfx/mx-<id>.mp3
```

| ID | 声音 | 典型用途 |
|---|---|---|
| **1490** | Fast whoosh transition | 卡片滑入 / 换段（本片 4 张知识卡） |
| **3005** | Explainer pops | 条目/节点逐个钉入（本片 14 条） |
| **2379** | 纸张 | 插入页纸张展开（本片 s14b） |
| **2472** | 鸟鸣 | 清晨/暖光段（本片 s14d） |
| 1125 / 2568 / 1117 / 1113 / 1120 / 2573 | click / key / soft tick / check / toggle / toast | UI 交互 |
| 2364 / 2357 / 2925 | pop / bubble / soap | 轻提示 |
| 1489 / 1485 / 1143 | rise / flip / impact | 铺垫 / 翻页 / 冲击 |
| 1430 / 1433 | shutter / lens | 相机感 |
| 3083 / 2865 / 118 | sparkle / success / bread crunch | 完成 / 成功 / 质感 |
| w1490 / w1489 / w1485 | whoosh / rise / flip 的另一组编号 | 备选 |

> 搜索：`~/.workbuddy/skills/motion-design-howseen/scripts/mixkit_sfx_search.py <tag>`；
> 或抓流派页 HTML grep `sfx/[0-9]+/`。**Mixkit 搜索参数 `?q=` 无效**，要爬分类页。

## B2. Mixkit 音乐（BPM 与 drop 已实测，可直接当节拍基准）

```
下载直链模板：https://assets.mixkit.co/music/<id>/<id>.mp3
```
| 曲目 | ID | BPM | drop / 备注 |
|---|---|---|---|
| mixkit-207 | 207 | 120 | drop 31.97s |
| mixkit-190 | 190 | 120 | drop bar8 = 16.01s |
| mixkit-129 | 129 | 120 | drop 16.09s |
| minimal-techno-01 | — | 119.99 | true drop 39.98s（自动网格差 2 拍） |
| Cat Walk (Arulo #371) | 371 | 130 | drop 14.769s |
| Waka Floka Type (Arulo #364) | 364 | trap | drop 14.75s |
| Driving Ambition | 32 | ~99 钢琴 | hit 37.66s |
| Classical vibes 4 | 684 | ~94 | lift ~7.95s |
| Head Bang | 357 | 74（half-time） | 4 小节安静前奏，drop 12.96s = beat16 |

**BPM 经验档位**：60–80 庄重 / 90–110 顺滑 / 115–123 精致高级 / >125 亢奋。
**找 drop 靠能量**，别信自动网格：逐小节低/全频能量，再在跳变附近 20–50ms 窗精修；
曲目起点 = `drop_in_song − drop_in_film`。本片 BGM 是用户提供的 `user-bgm.mp3`，实测 **60.1 BPM / beat 29.95f / 首拍相位 10.8f**（`scripts/bpm.py`）。

## B3. Freesound 选材工作流（`video-shotcraft/references/sfx-sourcing.md`）

```bash
# 1. 把画面写成声音需求：每个 cue 记「镜头/动作、声源材质、目标时长、攻击/尾音、许可」
#    例：纸卡滑入 = "paper slide", 0.2–0.8s, 干燥单次无长尾, CC0
python3 <skill>/assets/scripts/sfx-source.py search "paper slide" --max-duration 1 --limit 5 \
  --output /path/video/audio-search.json
# 2. 下载（默认仅 CC0；--license by 允许 CC BY；商用片不接受 BY-NC/Sampling+/未知许可）
python3 <skill>/assets/scripts/sfx-source.py get fs:12345 fs:67890 \
  --out-dir /path/video/public/audio/sfx
# 3. 单独分析处理后的文件
python3 <skill>/assets/scripts/sfx-source.py analyze public/audio/sfx/fs-12345.mp3 \
  --output audio-analysis.json
```
产物：`fs-<id>.mp3`（高质量**有损预览**，不是原始 WAV）、`audio-manifest.json`（来源/作者/素材页/许可URL/SHA-256/分析）、`FREESOUND-CREDITS.md`（CC BY 条目必须进发布页或成片署名）。
选材规则：以**声源匹配**为先，不搜抽象情绪；单击别选混有多个动作的长录音；下载量/评分只作辅助（多人评 4.4 比 6 人评 4.9 更可信）；
**工具只有元数据能力时如实写「未试听」，不要把波形分析描述成听感**；不能把预览转 WAV 标成原始无损。

**本片已用的 Freesound ID（语义映射，可直接复用）**

| ID | 语义 | 本片用法 |
|---|---|---|
| fs-578524 | 海浪 | 00-A 讲台 / 图瓦卢 s01–s02 环境音 |
| fs-825964 | 低频 boom | 00-B 一记 / 00-C 黑卡切点 / 两张黑字卡入场 / 45° 标注 |
| fs-643547 | 水声 | 00-D 融水 / s02 涨水 / 孟加拉洪水 |
| fs-852826 | 涨水 | s02 覆盖全镜 |
| fs-321648 | 雨声 | 孟加拉 s03–s04 |
| fs-785818 | 干热风 / 冷风 | 萨赫勒 s05–s06b / 北极 s10–s11 |
| fs-717893 | 蝉鸣热浪 | 新德里 s08–s09 |
| fs-591152 | 冰裂 / 撕开 | s11 两次裂缝 |
| fs-495650 | ping | s13 五个光点 / s14 事实卡数字滚动 |

## B4. 事件 → 声音映射表（`sound-design` skill + 本片实践）

| 画面事件 | 声音 | 对位方法 |
|---|---|---|
| 打字 | typing 逐字簇 | 跟随动画逐字节奏，±4–6ms 抖动、随机增益 |
| 词/行揭示 | whoosh + 落定 blip | 短、空气感 |
| 徽章/卡片弹入 | pop（一串音高递升） | spring 落定帧 |
| 旋钮卡档 | click + 调内 blip | 落到刻度那一帧 |
| 描线 / 构造线 | scratch | 与 strokeDashoffset 同步 |
| 铺垫 | riser（全片一次） | **恰好落在 hit 上**，声音先于画面开始 |
| 成功 / 到达 | chime（调内和弦） | payoff 帧 |
| hero 转场 | whoosh 进 + impact 落（全片一次） | 切点 |
| 垫底 | pad（hero 处 duck ~65%） | 贯穿 |
| 结构变化（换段/知识卡） | whoosh / glitch | 只给真正的换段，不给每个元素 |
| 连续运动（drift / 颗粒 / 旋转） | **保持安静** | Accent, don't narrate |

**音量层级**：hero hit 0.25–0.35 / 辅助 0.08–0.2 / pad ≈0.03 / 声像跟随画面左右（−1…+1）。
本片实际：BGM 0.26；环境音 0.16–0.5；boom 0.3–0.5；pop 0.24；ping 0.22–0.3。
**连发防机枪感**：双样本交替 + 音量阶梯递减（0.40→0.25）+ 间隔跟随动画加速；密到听不清就收成 swoosh 或淡出。
**收束句式**：`riser → impact → sparkle`（铺垫起 / 主体落地 / 余韵），按实际落点定间隔，不强行给每个结尾套。

## B5. 钉帧硬规则（含音画偏移补偿）

```ts
// 中央 SFX 表：相对 shot 起点钉帧，永不写裸绝对帧号
{ src: 'audio/sfx/mx-1490.mp3', from: shotByKey('s02').from + 336, volume: 0.26 }
```

**两条偏移（不补会叠加，实测最重一击晚 0.27s 就明显不同步）**：
```
Sequence.from = 目标峰值帧 − 音源峰值滞后帧 − 输出音轨偏移帧
```
1. **音源峰值滞后**：逐文件实测（点击/按键用**起音点**对齐；whoosh/impact/riser 用**峰值**对齐切点，声音要先开始）。
   `guizang` 提供 `scripts/sfx_landmarks.py` 测起音点/峰值时间/峰值电平；`syncOffset` 记进 plan。
2. **输出音轨偏移**：根因是 AAC encoder priming（48kHz 下典型 2048 samples = **1.28f@30fps**），
   ffmpeg 内置 aac ≈1024、fdk-aac 2048、Apple ≈2112 samples，不能预设常数。
   **按管线记录**（Remotion 版本 + codec + sample rate + 容器四要素），换任一项必须重测。
   实测方法：渲一段含 click 的成片，比对该 click 在音轨与画面上的帧差。

**其他**：动作声显式设 `durationInFrames` 贴动作时长（>5s 的环境/键盘长样本必须裁）；
impact 的自然混响可越过落点避免硬截；峰值低于 −12dB 的轻音先换更干净候选；
画面时长/顺序/动作峰值一变，**对应声音窗口与其后所有钉点全部复核**（本片 s14 加长时同步把 ping 从 +114 移到 +192）。

## B6. 混音与母带

- 目标 **−14 LUFS ±1**、true peak ≤ −1 dBFS（内部留 ≤ −2 dBFS 给 AAC 余量）；两遍 loudnorm。
- **主要由短 hit + 静音组成的混音到不了 −14，别硬压，改用持续声（pad / 长尾）补**。
- 最终编码：`scale=in_range=pc:out_range=tv:out_color_matrix=bt709,format=yuv420p` ·
  `-color_range tv -colorspace bt709` · libx264 crf16 · AAC 256k · `+faststart`。
- 验证：出 `wave.png`，每个瞬态落在节拍线上或稍后；落在两线之间 = 硬编码时间或 WAV 过期。
- **音效与配乐分工**：不要点击/提示音写进配乐，它们是独立音效、单独对位、单独让位；
  配乐编曲从分镜来（读文字/看操作的段落让出空间，乐器变少）。
- 配乐气质 → 配器：冷静高端=宽 supersaw+pluck+侧链底鼓；轻快=明亮键盘+马林巴；
  **温暖人文=钢琴/拨弦主导、慢速、长混响、少打击乐**（本片属此类）；有力紧凑=打击主导+上升音；安静专注=氛围铺底+稀疏铃音。
- **来源优先级**：① 用户给的曲子/已授权曲库（按其真实节拍重排切点）→ ② 本机真装好的生成模型（只有配置缓存不算）→
  ③ 代码原创合成（保留源码+固定随机种子，可复现）。**不要用来路不明的 BGM，不要扒参考视频的曲子，不要把示例曲改名当新配乐**。
- 留痕：`evidence/audio-selection.json` 记 music（来源/时长/BPM/调性/段落时间）与 sfx[]（作用/来源/许可/本地路径），
  未知写未知、不编造搜索经历；工程内保留 `CREDITS.md`。

---

# C. 风格规范

## C1. 本片风格基准（用户明确确认过，**新片段必须延续**）

> 用户原话：「咱们必须延续咱们现在的风格，以现在的风格为准，包括现在的黑屏大字幕形式，一定是那样的形态，不要受新脚本其他的影响」

- **黑屏大字幕卡 = 全片标志性形态**：`#05070A~#0A0D11` 底 + 特大中文粗黑体（118px / 900 / 0.14em）
  + 唯一金色 `#E8B04B` 重点词 + 英文衬线副句（20px / 全大写 / 0.4em / 45% 白）+ 极弱呼吸辉光 + 可选 horizon 发光地平线。
- **双语制式**：中文无衬线为主；英文衬线小字只作副句/落款，不与中文抢层级。
- **色彩叙事**：深冷色调（海/冰/厂，见 `design.ts` 的 `sea/ice/asphalt` 系）→ 结尾暖光转折（`#C08A45` 系）。
- **扁平矢量剪影**：人物/物件用纯色块+路径，不用渐变材质、不用拟真 3D、不用发光铬。
- **知识卡 / 流程图**：spring 滑入 + 条目错帧钉入（+16~18f 一档），配 whoosh/pop；排版不能太贴边，字号要够大。
- **五格快切**：风格化硬切，不加转场；每格独立色（`#2A5A62 → #2E4470 → #C08A45 → #C9853F → #5F8A4E`）。
- **全局层**：恒定暗角 + Grain 颗粒（0.09）；二者不抢戏、不参与叙事。
- **声音**：BGM 从第 0 帧贯穿；**无配音、无旁白、无对白字幕**；只有环境音 + 动效音效。

## C2. 通用风格硬规则（跨 skill 汇总）

| 规则 | 数值 / 要求 |
|---|---|
| 字族上限 | 最多 3 族（display serif / UI sans / mono）；本片 2 族 |
| 唯一强调色 | 全片一个 accent 且它要有含义；全是金色 = 没有金色；颜色只能来自 `C` |
| 每行一个 accent | 最多一个词/一段数字用金色 |
| 最低有效字高 | **字幕 ≥5% 帧高（1080p → ≥54px 实际像素）、辅助文字 ≥3%（≥32px）**；按最终像素量，不按 fontSize |
| 安全区 | 重要内容距画面边缘 ≥60px（本片角标 left 96 / top 104，合规） |
| 首帧 | 必须是完整可读的画面（平台抓它当封面），不能是等待入场的空底 |
| 一帧一个焦点 | 两个东西竞争时，其中一个等 |
| 文字静止 | **文字在被读的时候不能还在动**；落定后 hold ≥1s（品牌/结尾钩子 ≥2s） |
| 出场 | 快于入场（0.35–0.55s vs 0.7–1.25s），用 easeIn |
| 手机测试 | contact sheet 缩到 360px 宽，关键句仍可读 |
| 静音一句话测试 | 静音给人看，能用一句话概括就成立；犹豫 = 动得太多 |
| 一次只动一样 | 除非一个连续变换驱动全局；spring 阻尼比 ≥0.72、轻微过冲、绝不卡通弹跳 |
| 禁用 | 彩虹渐变 / 粒子滥用 / 发光铬 / emoji / lorem ipsum / 无意义 3D 翻转 / 彩虹大字 |
| 光效 | glint/sheen 不群发，一个镜头最多给主角一次，且要被圆角/overflow 裁进去；**全片只留 1–3 处** |
| 反单调 | 片内不能所有元素同一种入场/同一种转场；逐字模糊只留给黑卡大字时刻 |

## C3. 反「AI 味」自检（howseen / motion-design）

同一套形状系统贯穿全片、靠形变而非硬切 · 转场必须由画面里某个物体引发，不用通用擦除 ·
运动拖尾由速度派生而非假造 · **全片一个 hero 时刻**，为它铺路别提前花掉 ·
相机噪声只在暗场氛围片追求纪实感时用极小值，默认禁用 ·
信息密集镜头保持正视，风格化倾斜逐镜验证 · 飞入终点必须是真实槽位，元素不悬浮 ·
真实数据/真实组件优先，示意内容明确标注，**不虚构指标**。

## C4. 判例式审美准则精选（`video-shotcraft/references/aesthetic-rules.md`）

每条 = 规则 + 用户判例 + 自检问题。**这些判例和本项目的用户反馈高度一致**，等于是跨项目验证过的规律：

| 编号 | 规则 | 与本项目呼应 |
|---|---|---|
| **R1** | 承载信息的元素落定后静止 ≥1s 再切；停顿优先给想让观众记住的画面，别随手给普通卡片 | 用户「最后一幕的停留再久一点点」 |
| **R2** | 速度感来自加速度，不是匀速快；批量入场越来越快 + 末尾 0.5s 静止呼吸 | 匀速直线 = 廉价 PPT |
| **R3** | **节奏宁慢勿快**：初版默认放慢一档，主体动作弧 ≥3s；六次独立反馈全是「放慢/停留」，**从未有过「太慢」** | 用户两次要求放慢文字/加长停留 |
| **R4** | 卡点只约束时机不放大幅度；全画面级节拍冲击全片 ≤3 处、间隔 ≥16 拍，其余拍点只动元素层 | **本片用户直接否决了节拍脉冲** |
| **Q4** | 高光/扫光宁缺毋滥，不群发；否决常针对「实现得不好看」而非技术路径本身 | 本片 sheen 全片唯一一次 |
| **Q5** | 开场只给一个主角 + 一条完整动作弧，胜过群体群舞 | 本片开场是单张黑卡 |
| **Q11** | 要被读的文字有最低有效字高（字幕 ≥5% 帧高） | 见 §C2 |
| **S1** | 配乐与音效**按片种选**，不按事件选；电影系 SFX 词汇，禁游戏音包音色 | 本片温暖人文 = 钢琴主导 |
| **S3** | 声音在画面锁定后做；**时间线一动，SFX 全表重钉** | 本片 s14 加长时同步移 ping |
| **S4** | 拟音优先于装饰音：画面动作配该动作的真实声音，音频裁到与动作等长 | 冰裂/纸张/鸟鸣都是拟音 |
| **S5** | 音画对齐补两项偏移（见 §B5） | 未来项目必须实测 |
| **P1** | **交付前必须自己渲染截帧逐一检查，不把首检交给用户** | 本 skill「先截图后成片」 |
| **P2** | 参考素材先逐帧拆成手法清单，再逐镜判断适配性，不全局套用 | 「非必要不更改」 |
| **P3** | **指代含糊的反馈先确认对象；改错了整段干净 revert，不在错误版本上打补丁** | 本片误改末卡 → 用户纠正 → 完整撤回 |
| **P4** | 一种动画手法全片只当一次主角，重复镜头/信息一律删 | 反单调 |

> 准则可以有意识违反（风格需要时），但每次违反必须写进项目说明：违反了哪条、为什么。
> 验收时逐条输出 `编号 ✓` 或 `编号 ✗(镜头名/帧号)`。

## C5. 风格变更纪律（本片血泪）

- **以既有成片为准**：新脚本/新参考图只提供**内容与结构**，不带来新视觉语汇。
- **非必要不更改**：用户给开头/结尾脚本时，中段一帧不动；只动被点名的段落。
- **删改先确认范围**：「只删大陆轮廓」≠ 删整张数据图（地图框 + 经纬网格要保留）。
- **改错对象立刻整体 revert**，不在错误版本上打补丁。
- 收到模糊反馈（「结尾文字有点快」）先确认是**哪一段**，本片曾误改末卡被纠正为「从纬度之后」。
- 时长红线（如 ≤4'30"）超了**立刻上报**，不擅自砍内容。
