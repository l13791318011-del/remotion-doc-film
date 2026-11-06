# remotion-doc-film

用 Remotion 以代码逐帧生成动效纪录片的实战工作流 skill（从 4 分钟气候纪录片《1.5度》项目沉淀而来）。

An agent skill for producing motion-documentary films entirely in Remotion — timeline management, per-frame QA, SFX alignment, black-card typography, and battle-tested pitfalls.

## 内容结构

```
remotion-doc-film/
├── SKILL.md                     # 主工作流 + 文档路由表
├── references/
│   ├── code-recipes.md          # 12 节可直接复制的 TSX 骨架（入口/色板/timeline/积木/合成根）
│   ├── assets-and-style.md      # 动效目录(130+技法卡) / 音效资源(ID表+下载+钉帧) / 风格规范与判例
│   ├── skill-lessons.md         # 从 6 类外部 skill 学到的方法论 + 否决清单
│   ├── techniques.md            # 已落地手法参数速查
│   ├── production-playbook.md   # 端到端流程 / QA 选帧 / 验收清单 / 反馈映射 / 排障
│   └── pitfalls.md              # 13 条踩坑记录与修复模式（含渲染性能复盘）
└── scripts/
    ├── qa_stills.sh             # 关键帧批量截图 + contact sheet 拼图
    └── bpm.py                   # 音频 BPM + 首拍相位分析（ffmpeg + numpy，无第三方音频库）
```

来源：用户下载的 motion-design / motion-design-howseen / hyperframes-student-kit，
以及环境自带的 guizang-product-video-skill / video-shotcraft / review-loop / sound-design /
video-storytelling / hyperframes-video-beats。哪些真正进片、哪些被否决、为什么剪辑类 skill 用不上，
都在 `references/skill-lessons.md` 里有完整账目。

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
