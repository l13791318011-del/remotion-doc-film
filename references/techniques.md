# Techniques — 手法库速查（guizang fx-lab / video-shotcraft / motion-design 实战版）

来源项目《1.5度》已落地并验证的手法。每条：效果 → 关键参数 → 用在哪。实现见项目 blocks.tsx/scenes.tsx，新项目直接抄模式。

## guizang fx-lab（字幕与大字卡的主语言）

### 中英分轨·双轨字幕（TypeText/Sub 核心）
- 轨① 中文：所有行同级（37~42px/700/白 #F5F7F8、字距 0.04em、行高 1.6）；`[[关键词]]` 金色加粗；数字用 NumToken（spring 弹入+金色下划线）。
- 轨② 英文：衬线体全大写、宽字距 0.16em、19px、55% 白；入场带 tracking-in（字距 0.3→0.16 收拢）。
- 入场：整行 rise+fade（bezier(0.22,1,0.36,1) 14f），**逐字模糊只留给黑字卡大字时刻**——反单调原则。
- 排版：标点→空格一行化；不加底板，靠 textShadow 保证可读。
- 文案规范：能一行说完不放两行。

### 切片错位入场（BlackCard 大字）
- 文字切成横条，从不同方向偏移弹回对齐，配细光条扫过。用于黑屏大字幕卡的"仪式感"时刻，日常字幕不用（反单调）。

### 粒子/字符/流线场（纯时间函数，seek-safe）
- **ConvergeRing**：粒子从四周大环飞入汇成双环（mulberry32 固定种子、easeOutQuart、count≈300、dur 40f、fadeFrom 与真实主体交接）。用于徽章/数据登场前的"收束"。
- **GlyphField**：字符场 SVG 版——背景漂浮字符营造数据氛围。
- **StreakField**：放射流线场——冲刺/穿越感。
- **OrbitDots**：手工投影环绕——"正在被观测"的仪器感。
- 共同实现纪律：**任何帧单独渲染结果一致**（不依赖累积状态），随机数必须固定种子。

### horizon 发光地平线
- 暗色本体 + 辉光边缘（radial-gradient 金色 0.12~0.13 + 渐变细线 boxShadow）：文献/原文/大字卡登场的仪式感。黑卡标配。

## video-shotcraft（仪器测量感）

### draw-svg-trace 一笔描线
- 半径线/十字准星用 `strokeDasharray=L, strokeDashoffset=L*(1-prog)` 逐段画出（错帧 10f/条，ease-out cubic）。用于仪表/刻度盘的"正在被测量"。

### scan-bracket-sweep 取景括号+扫描光带
- 四角括号臂依次弹入（每臂错 4f，带 8% 过冲）；两趟竖向扫光（柔辉 0.07 + 光芯 2.4px 0.85 + 渐变拖尾，clipPath 限定区域），扫完即卸载。表达"只有光在读它"。

## motion-design（whaleyxbt）

### Grain 胶片颗粒（全局层）
- feTurbulence fractalNoise，**每 2 帧重 seed**，overlay 混合、opacity 0.09。全片统一质感。注意：feTurbulence 是最贵的 SVG 滤镜，长片可考虑隔帧或降分辨率（见 pitfalls 渲染性能）。

### RollNum 数字竖滚
- 透明占位撑布局 + 双绝对层（暗底亮面）滚动窗口；**inline-block 会换行破基线，必须占位+绝对定位**。

### overhead-camera-moves（A 式变体：升降臂沉降）
- 1.5x→1.0x 俯冲 + 俯角 -2.2°→0 回正 + origin 焦点防露边。用于俯拍开场。

### crash-zoom-punch（撞停款）
- 先缓 creep 后 ease-in 急推（origin 直推目标）→ 到顶帧撞停：震屏 amp·e^(−t/1.8) + 白闪一帧 + boom 音效对位。用于温度计爆表等"冲击到达"时刻。

### light-play B 式 sheen 单点扫光
- 45° 高光带（linear-gradient 0→0.14→0.2→0.14→0，mixBlendMode:screen）扫过标题区，28f 扫完即卸载。**全片只用一次**——稀缺性就是它的价值。

## 音效对位速查

| 事件 | 音效 | 对位点 |
|---|---|---|
| 卡片滑入 | mx-1490 whoosh | spring 起点 |
| 条目钉入 | mx-3005 pop | 各条目 spring 帧 |
| 黑卡切点 | fs-825964 boom | 切帧+2 |
| 冰裂/撕开 | fs-591152 | 撕开帧 |
| 光点亮起 | fs-495650 ping | 光点 pop 帧 |
| 环境音组 | 海浪/雨/干热风/蝉鸣 | 覆盖整镜头组，durationInFrames 截断 |

密度原则：每镜头 1~2 个事件音 + 1 条环境音；spring 落定帧 +2 对位。
