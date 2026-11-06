# remotion-doc-film

用 Remotion 以代码逐帧生成动效纪录片的实战工作流 skill（从 4 分钟气候纪录片《1.5度》项目沉淀而来）。

An agent skill for producing motion-documentary films entirely in Remotion — timeline management, per-frame QA, SFX alignment, black-card typography, and battle-tested pitfalls.

## 内容结构

```
remotion-doc-film/
├── SKILL.md                  # 主工作流：时间轴单一事实源 / 先截图后成片 / 节奏规则 / 声音体系
├── references/
│   ├── pitfalls.md           # 13 条实战踩坑记录与修复代码模式
│   └── techniques.md         # 手法库速查（字幕制式/运镜/粒子场/描线/音效对位，含参数）
└── scripts/
    ├── qa_stills.sh          # 关键帧批量截图 + contact sheet 拼图
    └── bpm.py                # 音频 BPM + 首拍相位分析（ffmpeg + numpy，无第三方音频库）
```

## 核心原则

1. **时间轴单一事实源** — 镜头定义全部集中在 `timeline.ts`，组件/字幕/音效一律用 `shotByKey()` 派生，绝不写裸帧号。
2. **先截图后成片** — still 关键帧 → ffmpeg 拼 contact sheet → 逐帧核验 → 再后台全片渲染（`--temp-dir` 必带，避免音频竞态）。
3. **转场显式声明** — 淡入淡出必须逐组件显式传，timeline 元数据字段不会自动生效。
4. **节奏规则** — 打字机字幕每字 ≈ 6.5 帧；黑屏大字幕卡停留 ≥ 2 秒。
5. **声音体系** — BGM 从第 0 帧贯穿（volume 函数做 swell）；SFX 按 spring 落定帧对位；不加配音。

## 用法（WorkBuddy / Claude Code skill）

把整个目录放到 `~/.workbuddy/skills/`（或 `.claude/skills/`）下即可被自动发现，触发场景如"做个 Remotion 短片/纪录片"。

## License

MIT
