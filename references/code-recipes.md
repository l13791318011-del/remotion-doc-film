# Code Recipes — 可直接复制的 Remotion 纪录片骨架

全部代码摘自《1.5度》v34 成片（已通过 243.9s 全片渲染验证）。新建项目时按 §1→§10 顺序搭，参数改成自己的即可。
**纪律**：所有时间都从 `shotByKey()` 派生；所有视觉都是 `frame` 的纯函数；所有颜色来自 `C`。

---

## 1. 依赖与入口

```json
// package.json（关键依赖）
{
  "dependencies": {
    "remotion": "^4.0.0",
    "@remotion/cli": "^4.0.0",
    "react": "^18.3.1",
    "react-dom": "^18.3.1",
    "@fontsource/noto-sans-sc": "^5.0.0",
    "@fontsource/noto-serif-sc": "^5.0.0"
  }
}
```

```ts
// src/index.ts
import { registerRoot } from 'remotion';
import { Root } from './Root';
registerRoot(Root);
```

```tsx
// src/Root.tsx —— 注意 defaultProps 的 vo:false（无配音项目必关）
import React from 'react';
import { Composition } from 'remotion';
import { Film } from './film/Film';
import { TOTAL_DURATION } from './film/timeline';
import '@fontsource/noto-sans-sc/400.css';
import '@fontsource/noto-sans-sc/500.css';
import '@fontsource/noto-sans-sc/700.css';
import '@fontsource/noto-sans-sc/900.css';
import '@fontsource/noto-serif-sc/500.css';
import '@fontsource/noto-serif-sc/700.css';
import '@fontsource/noto-serif-sc/900.css';

export const Root: React.FC = () => (
  <Composition
    id="Film" component={Film}
    durationInFrames={TOTAL_DURATION}
    fps={30} width={1920} height={1080}
    defaultProps={{ bgm: true, vo: false }}
  />
);
```

```ts
// src/film/fonts.ts
export const FONT_FAMILY = '"Noto Sans SC", sans-serif';
export const SERIF_FAMILY = '"Noto Serif SC", serif';
```

---

## 2. 色板（唯一颜色来源）

```ts
// src/film/design.ts
export const C = {
  bg: '#0A0D11', panel: '#10161D', ink: '#E8EDF2', sub: '#93A1AC',
  sea: '#123049', seaDeep: '#0C2130', seaLite: '#1B4A6B', foam: '#7FA8C4',
  skyGrey: '#1A242C', skyGreyLite: '#27333C',
  mud: '#3A4238', mudLite: '#4A5242',
  desert: '#7A6242', desertLite: '#8F7650', desertDark: '#4E3E2A',
  asphalt: '#23262B', asphaltLite: '#3A3E44',
  heat: '#C96F3B', heatGlow: '#E09A5A',
  arcticGround: '#6E7B72', arcticSky: '#B9C4CA', ice: '#8FA3AD',
  danger: '#C0392B',
} as const;

export const ACCENT = '#E8B04B';  // 全片唯一强调色：只标"变化的/答案/重点词"
```

---

## 3. 时间轴（唯一事实源）

```ts
// src/film/timeline.ts
export const FPS = 30;

export interface ShotDef {
  key: string; from: number; dur: number;
  sub?: string;          // 该镜文字/旁白原文（文档性，也供 QA 对照）
  fadeIn: boolean;
  fadeOut: number;       // 仅元数据，不自动生效！见 §4
}

const raw: Omit<ShotDef, 'from'>[] = [
  { key: 's00z', dur: 96,  sub: '开场黑卡：20年之后，你会在哪里', fadeIn: true,  fadeOut: 0 },
  { key: 's00a', dur: 300, sub: '海水讲台：齐膝深发言',           fadeIn: true,  fadeOut: 0 },
  { key: 's01',  dur: 160, sub: '图瓦卢',                          fadeIn: true,  fadeOut: 0 },
  { key: 's02',  dur: 790, sub: '5毫米/条约/数字孪生',              fadeIn: false, fadeOut: 15 },
  // ... 插删镜头只改这里，其余全部自动跟随
];

export const SHOTS: ShotDef[] = (() => {
  let acc = 0;
  return raw.map((s) => { const def = { ...s, from: acc }; acc += s.dur; return def; });
})();

export const TOTAL_DURATION = SHOTS.reduce((a, s) => a + s.dur, 0);

export const shotByKey = (key: string): ShotDef => {
  const s = SHOTS.find((x) => x.key === key);
  if (!s) throw new Error(`unknown shot ${key}`);   // 拼错 key 立刻炸，别静默
  return s;
};
```

**帧号换算**：`绝对帧 = shotByKey('sXX').from + 镜头内局部帧`；`秒 = 帧 / 30`。
不要在 shell 里跑 `npx tsx -e` 求值（沙箱内会被 SIGTERM），手算或用下式：

```bash
python -c "d=[(k,n) for k,n in [('s00z',96),('s00a',300),('s01',160),('s02',790)]]; import itertools; a=0
for k,n in d: print(k,a); a+=n"
```

---

## 4. Shell（场景外壳：转场必须显式传）

```tsx
// src/film/blocks.tsx
import React from 'react';
import { AbsoluteFill, interpolate, useCurrentFrame, useVideoConfig } from 'remotion';
import { C } from './design';

interface ShellProps {
  bg?: string; fadeIn?: boolean; fadeInFrames?: number; fadeOutFrames?: number;
  zoom?: [number, number, number?]; children: React.ReactNode;
}

export const Shell: React.FC<ShellProps> = ({
  bg = C.bg, fadeIn = false, fadeInFrames = 12, fadeOutFrames = 0, zoom, children,
}) => {
  const f = useCurrentFrame();
  const { durationInFrames: seqDur } = useVideoConfig();
  const inO = fadeIn
    ? interpolate(f, [0, fadeInFrames], [0, 1], { extrapolateRight: 'clamp' }) : 1;
  const outO = fadeOutFrames > 0
    ? interpolate(f, [seqDur - fadeOutFrames, seqDur], [1, 0], {
        extrapolateLeft: 'clamp', extrapolateRight: 'clamp',
      }) : 1;
  const scale = zoom
    ? interpolate(f, [0, zoom[2] ?? 99999], [zoom[0], zoom[1]], { extrapolateRight: 'clamp' })
    : undefined;
  return (
    <AbsoluteFill style={{ backgroundColor: C.bg, overflow: 'hidden' }}>
      <AbsoluteFill style={{ opacity: inO * outO, overflow: 'hidden' }}>
        {/* 背景放在非缩放层：内容层有 1px 露边也不会露黑框 */}
        <AbsoluteFill style={{ background: bg }} />
        <AbsoluteFill style={{
          overflow: 'hidden',
          transform: scale ? `scale(${scale})` : undefined,
          transformOrigin: 'center center',
        }}>{children}</AbsoluteFill>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
```

> ⚠️ `timeline.ts` 的 `fadeOut` / `fadeIn` 字段**没人读取**，只是文档。想有转场，必须写
> `<Shell fadeIn fadeInFrames={22}>` 与 `<Shell fadeOutFrames={26}>`。整片曾因此出现"1.5℃ 大卡硬切进正片"的断缝。

---

## 5. 常用工具函数（缓动 / 软入 / 固定随机 / 关键词高亮）

```tsx
import { Easing, interpolate, useCurrentFrame } from 'remotion';

export const CAM_EASE = Easing.bezier(0.2, 0, 0.25, 1);       // 相机专用（先快后缓）
export const EASE_OUT = Easing.bezier(0.16, 1, 0.3, 1);        // 入场
export const EASE_IN  = Easing.bezier(0.6, 0, 0.9, 0.35);      // 出场（快点走）
export const EASE_IO  = Easing.bezier(0.65, 0, 0.35, 1);       // 两态之间

export const softIn = (f: number, at: number, dur = 20) =>
  interpolate(f, [at, at + dur], [0, 1], {
    extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: EASE_OUT,
  });

/** 浪线等连续微动（纯时间函数，seek-safe） */
export const waveOffset = (f: number, i: number, amp = 6, speed = 0.02) =>
  Math.sin(f * speed + i * 0.6) * amp;

/** 固定种子 PRNG：任何帧单独渲染结果必须一致，禁止 Math.random() */
export const mulberry32 = (seed: number): (() => number) => () => {
  seed |= 0; seed = (seed + 0x6D2B79F5) | 0;
  let t = Math.imul(seed ^ (seed >>> 15), 1 | seed);
  t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
  return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
};

export const ACCENT = '#E8B04B';
/** 字幕语法：[[关键词]] → 金色加粗 */
export const parseHighlights = (text: string): { t: string; hi: boolean }[] =>
  text.split(/(\[\[[^\]]+\]\])/g).filter(Boolean).map((seg) => {
    const m = seg.match(/^\[\[([^\]]+)\]\]$/);
    return m ? { t: m[1], hi: true } : { t: seg, hi: false };
  });
```

---

## 6. Grain 全局颗粒（每帧都在动的最便宜一层）

```tsx
export const Grain: React.FC<{ opacity?: number }> = ({ opacity = 0.09 }) => {
  const f = useCurrentFrame();
  const { width, height } = useVideoConfig();
  return (
    <AbsoluteFill style={{ pointerEvents: 'none', mixBlendMode: 'overlay', opacity }}>
      <svg width={width} height={height}>
        <filter id="filmGrain" x="0" y="0" width="100%" height="100%">
          <feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves={2}
            seed={Math.floor(f / 2) % 97} stitchTiles="stitch" />
          <feColorMatrix type="saturate" values="0" />
        </filter>
        <rect width={width} height={height} filter="url(#filmGrain)" />
      </svg>
    </AbsoluteFill>
  );
};
```

> `feTurbulence` 是最贵的 SVG 滤镜。长片提速第一刀：把 `Math.floor(f/2)` 改成 `/4` 或降 `baseFrequency`，见 pitfalls #13。

---

## 7. RollNum 数字竖滚（占位 + 双绝对层）

```tsx
export const RollNum: React.FC<{ from: string; to: string; at: number }> = ({ from, to, at }) => {
  const f = useCurrentFrame();
  const k = interpolate(f, [at, at + 22], [0, 1], {
    extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: EASE_IO,
  });
  return (
    <span style={{ position: 'relative', display: 'inline-block', whiteSpace: 'pre' }}>
      <span style={{ visibility: 'hidden' }}>{to}</span>   {/* 不可见占位撑宽度 */}
      <span style={{ position: 'absolute', left: 0, top: 0,
        transform: `translateY(${-k * 115}%)`, opacity: 0.55 - k * 0.45,
        filter: `blur(${k * 2.5}px)` }}>{from}</span>
      <span style={{ position: 'absolute', left: 0, top: 0,
        transform: `translateY(${(1 - k) * 115}%)`,
        textShadow: `0 0 ${16 + k * 16}px rgba(232,176,75,${0.25 + k * 0.3})` }}>{to}</span>
      <span style={{ position: 'absolute', left: 0, bottom: '-0.06em', height: 4,
        width: `${k * 100}%`, borderRadius: 2,
        background: 'linear-gradient(90deg, #E8B04B, rgba(232,176,75,0.12))',
        boxShadow: '0 0 14px rgba(232,176,75,0.55)',
        opacity: k > 0.6 ? (k - 0.6) / 0.4 : 0 }} />
    </span>
  );
};
```

> 别用 inline-block + overflow 窗口：会把行盒撑成两行、基线崩掉。

---

## 8. CornerSub 角标打字机字幕（支持黄色重点标注）

```tsx
/** 放在 scenes.tsx 顶部；lines[].hi = 该行需要标金的原文片段 */
const CornerSub: React.FC<{
  lines: { t: string; at: number; hi?: string }[];
  pos?: 'tl' | 'bl'; size?: number; cps?: number;
}> = ({ lines, pos = 'tl', size = 34, cps = 2.2 }) => {
  const f = useCurrentFrame();
  return (
    <div style={{ position: 'absolute', left: 96,
      ...(pos === 'tl' ? { top: 104 } : { bottom: 116 }),
      display: 'flex', flexDirection: 'column', gap: 16,
      alignItems: 'flex-start', pointerEvents: 'none', zIndex: 5 }}>
      {lines.map((l, i) => {
        const n = Math.max(0, Math.floor((f - l.at) / cps));
        if (n <= 0) return null;
        const typing = n < l.t.length;
        const hiIdx = l.hi ? l.t.indexOf(l.hi) : -1;
        let body: React.ReactNode = l.t.slice(0, n);
        if (hiIdx >= 0 && n > hiIdx) {
          const hiEnd = Math.min(n, hiIdx + (l.hi as string).length);
          body = <>
            {l.t.slice(0, hiIdx)}
            <span style={{ color: ACCENT, textShadow: '0 0 18px rgba(232,176,75,0.35)' }}>
              {l.t.slice(hiIdx, hiEnd)}
            </span>
            {n > hiEnd ? l.t.slice(hiEnd, n) : null}
          </>;
        }
        return (
          <div key={i} style={{ fontFamily: FONT_FAMILY, fontWeight: 600, fontSize: size,
            color: '#F2F5F7', letterSpacing: '0.05em', lineHeight: 1.5,
            textShadow: '0 2px 20px rgba(0,0,0,0.6)', whiteSpace: 'pre' }}>
            {body}
            {typing ? <span style={{ color: ACCENT,
              opacity: Math.sin(f * 0.45) > 0 ? 0.85 : 0.1 }}>▏</span> : null}
          </div>
        );
      })}
    </div>
  );
};

// 用法（镜头内局部帧）
<CornerSub lines={[
  { t: '1.5 度是小岛屿国家联盟死命推动的', at: 84, hi: '死命推动' },
  { t: '最后 1.5 度被写进了协定',            at: 328, hi: '写进了协定' },
]} />
```

**两种"文字速度"别混**：`cps=2.2` 是打字机**打出来**的速度（≈0.45 秒/字，戏剧性慢）；
`每字≈6.5f` 是**读完停留**的估算（0.22 秒/字），用来算 `until`/镜头时长。

---

## 9. 黑屏大字幕卡（全片标志性形态，独立镜头实现）

```tsx
/** 96 帧开场黑卡：金标 + 英文衬线副句 + 极弱呼吸辉光 */
export const S00Z: React.FC = () => {
  const f = useCurrentFrame();
  const o = softIn(f, 8, 22);
  const oEn = softIn(f, 42, 22);
  return (
    <Shell bg="#05070A" fadeIn fadeInFrames={18}>
      <AbsoluteFill style={{ justifyContent: 'center', alignItems: 'center' }}>
        <div style={{ position: 'absolute', left: '50%', top: '50%',
          width: 1180, height: 560, transform: 'translate(-50%, -50%)',
          borderRadius: '50%', pointerEvents: 'none',
          background: `radial-gradient(ellipse, rgba(233,238,242,${0.05 + Math.sin(f * 0.05) * 0.025}) 0%, rgba(233,238,242,0) 70%)` }} />
        <div style={{ textAlign: 'center', transform: `scale(${1 + Math.sin(f * 0.05) * 0.004})` }}>
          <div style={{ fontFamily: FONT_FAMILY, fontWeight: 900, fontSize: 118,
            color: C.ink, letterSpacing: '0.14em', lineHeight: 1.2, opacity: o,
            textShadow: '0 0 70px rgba(233,238,242,0.18)', whiteSpace: 'nowrap' }}>
            20 年之后，
            <span style={{ color: ACCENT, textShadow: '0 0 44px rgba(232,176,75,0.42)' }}>
              你会在哪里
            </span>
          </div>
          <div style={{ fontFamily: SERIF_FAMILY, fontWeight: 500, fontSize: 20,
            textTransform: 'uppercase', letterSpacing: '0.4em',
            color: 'rgba(233,238,242,0.45)', marginTop: 36, opacity: oEn }}>
            Twenty years from now, where will you be?
          </div>
        </div>
      </AbsoluteFill>
    </Shell>
  );
};
```

**黑卡配方**：`#05070A~#0A0D11` 底 · 中文 900 weight / 100~138px / 字距 0.14em · 唯一金标词 · 英文衬线 20px / 大写 / 0.4em / 45% 白 · 呼吸辉光幅度 ≤0.004 · 停留 ≥2 秒。
需要"原文/条款"仪式感时再加 `horizon` 发光地平线（见 techniques.md）。

---

## 10. 合成根组件：注册表 + SFX + BGM

```tsx
// src/film/Film.tsx
import React from 'react';
import { AbsoluteFill, Audio, Sequence, interpolate, staticFile } from 'remotion';
import { SHOTS, TOTAL_DURATION, shotByKey } from './timeline';
import { Grain } from './blocks';
import { S00Z, S00A, S01, S02 /* ... */ } from './scenes';

/** 每新增镜头必须在这里注册；拼错 key 立刻抛错，别静默黑屏 */
const SHOT_COMPONENTS: Record<string, React.FC> = {
  s00z: S00Z, s00a: S00A, s01: S01, s02: S02,
};

interface SfxCue { src: string; from: number; volume: number; durationInFrames?: number }

/** SFX 相对钉帧表：全部按 shot key 派生（不写裸索引） */
export const SFX_TABLE: SfxCue[] = [
  // 环境音：覆盖整镜头组，用 durationInFrames 截断长素材
  { src: 'audio/sfx/fs-578524.mp3', from: shotByKey('s00a').from + 10, volume: 0.5,
    durationInFrames: shotByKey('s00a').dur - 10 },
  // 事件音：对准 spring 落定帧
  { src: 'audio/sfx/mx-1490.mp3',  from: shotByKey('s02').from + 336, volume: 0.26 },
  // 条目逐帧错开钉入（+16~18f 一档）
  ...[358, 376, 394].map((o) => ({
    src: 'audio/sfx/mx-3005.mp3', from: shotByKey('s02').from + o, volume: 0.24,
  })),
];

export const Film: React.FC<{ bgm?: boolean; vo?: boolean }> = ({ bgm = true, vo = false }) => (
  <AbsoluteFill style={{ backgroundColor: '#0A0D11' }}>
    {SHOTS.map((s) => {
      const Comp = SHOT_COMPONENTS[s.key];
      if (!Comp) throw new Error(`missing component for ${s.key}`);
      return (
        <Sequence key={s.key} from={s.from} durationInFrames={s.dur} name={s.key}>
          <Comp />
        </Sequence>
      );
    })}

    {/* 恒定暗角（电影感，不动不抢戏） */}
    <AbsoluteFill style={{ pointerEvents: 'none',
      background: 'radial-gradient(ellipse 118% 108% at 50% 46%, rgba(0,0,0,0) 62%, rgba(0,0,0,0.34) 100%)' }} />
    <Grain opacity={0.09} />

    {/* BGM 从第 0 帧贯穿：片头 duck 0.7 → 关键镜头 swell 到 1 → 结尾淡出 */}
    {bgm ? (
      <Sequence from={0}>
        <Audio src={staticFile('audio/bgm/user-bgm.mp3')} loop
          volume={(f: number) => {
            const eFrom = shotByKey('s01').from;   // 改成自己的"推满"镜头
            const fadeIn = interpolate(f, [0, 45], [0, 1], { extrapolateRight: 'clamp' });
            const swell = interpolate(f, [eFrom - 55, eFrom + 35], [0.7, 1], {
              extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
            const fadeOut = interpolate(f, [TOTAL_DURATION - 140, TOTAL_DURATION - 10], [1, 0], {
              extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
            return 0.26 * fadeIn * swell * fadeOut;
          }} />
      </Sequence>
    ) : null}

    {SFX_TABLE.map((cue, i) => (
      <Audio key={`sfx-${i}`} src={staticFile(cue.src)} volume={cue.volume}
        {...(cue.durationInFrames ? { durationInFrames: cue.durationInFrames } : {})} />
    ))}

    {/* 无配音项目：vo 默认 false，且不要在 VO_TABLE 里给不存在的音频生成路径 */}
    {vo ? null : null}
  </AbsoluteFill>
);
```

---

## 11. 渲染 / QA 命令速查

```bash
# 类型检查（每次改完必跑）
npx tsc --noEmit -p .

# 单帧截图
npx remotion still src/index.ts Film out/qa/f1245.png --frame=1245 --log=error

# 批量截图 + 拼图（本 skill 脚本，每行最多 6 帧）
bash scripts/qa_stills.sh <projectDir> src/index.ts Film out/qa-vXX 244 658 1245 6700

# 局部放大（查错位，例：浇水有没有浇到叶子）
ffmpeg -y -loglevel error -i out/qa/f6830.png \
  -vf "crop=800:600:720:340,scale=1200:900" out/qa/zoom_water.png

# 全片渲染（必须 --temp-dir；后台跑；渲染期间别并行跑重活）
npx remotion render src/index.ts Film out/draft-vXX.mp4 \
  --temp-dir=out/tmp-vXX --log=error

# 只渲染一段做性能探针
npx remotion render src/index.ts Film out/perf.mp4 --frames=1300-1539 \
  --temp-dir=out/tmp-perf --log=error

# 交付前核验
ffprobe -v error -show_entries format=duration -of default=nw=1 out/draft-vXX.mp4
ls -la out/draft-vXX.mp4
```

## 12. 素材目录约定

```
public/audio/
├── bgm/user-bgm.mp3
├── sfx/
│   ├── mx-<id>.mp3        # Mixkit: https://assets.mixkit.co/active_storage/sfx/<id>/<id>-preview.mp3
│   ├── fs-<id>.mp3        # Freesound（保留 CREDITS.md 记录来源与许可）
│   └── CREDITS.md
└── vo/                    # 无配音项目保持为空，且 vo:false
```

**Mixkit 已验证 ID**：`1490` whoosh · `3005` explainer pop · `2379` 纸张 · `2472` 鸟鸣 ·
`1125` click · `2568` key · `1117` soft tick · `1113` check · `1143` impact · `3083` sparkle ·
`2865` success · `2364` pop · `2357` bubble · `1489` rise · `1485` flip。
（完整映射见 `references/skill-lessons.md` §3）
