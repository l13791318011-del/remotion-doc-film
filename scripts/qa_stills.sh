#!/usr/bin/env bash
# qa_stills.sh — Remotion 关键帧批量截图 + contact sheet 拼图
# 用法:
#   bash qa_stills.sh <projectDir> <entrypoint> <compositionId> <outDir> <frame1> <frame2> ...
# 例:
#   bash qa_stills.sh ./one-point-five src/index.ts OnePointFive out/qa-v33 1245 1275 6700
# 产出:
#   <outDir>/f<frame>.png          每帧原始截图
#   <outDir>/sheet.png             6 帧一行 hstack 对比图（超过 6 帧自动分行）
set -euo pipefail

PROJECT="$1"; ENTRY="$2"; COMP="$3"; OUT="$4"; shift 4
FRAMES=("$@")
[ ${#FRAMES[@]} -eq 0 ] && { echo "usage: qa_stills.sh <projectDir> <entry> <comp> <outDir> <frame...>"; exit 1; }

mkdir -p "$OUT"
cd "$PROJECT"

for fr in "${FRAMES[@]}"; do
  npx remotion still "$ENTRY" "$COMP" "$OUT/f$fr.png" --frame="$fr" --log=error >/dev/null 2>&1 \
    || { echo "still failed at frame $fr"; exit 1; }
done

# 每行最多 6 帧
ROW=6
inputs=(); filter=""; idx=0; rows=0
for fr in "${FRAMES[@]}"; do
  inputs+=(-i "$OUT/f$fr.png"); idx=$((idx+1))
done
total=$idx
build_row() {
  local start=$1 count=$2 r=$3
  local s=""
  for ((k=0;k<count;k++)); do s+="[$((start+k))]"; done
  # 每行统一缩放到 3840 宽（各行高度按帧数自适应），保证 vstack 宽度一致
  filter+="${s}hstack=$count,scale=3840:-2[r$r];"
}
r=0; done_n=0
while [ $done_n -lt $total ]; do
  count=$(( total - done_n < ROW ? total - done_n : ROW ))
  build_row $done_n $count $r
  done_n=$((done_n+count)); r=$((r+1))
done
rows=$r
# 竖排所有行（单行时直接输出该行）
if [ "$rows" -eq 1 ]; then
  filter+="[r0]null[v]"
else
  concat=""
  for ((k=0;k<rows;k++)); do concat+="[r$k]"; done
  filter+="${concat}vstack=inputs=$rows[v]"
fi
ffmpeg -y -loglevel error "${inputs[@]}" -filter_complex "$filter" -map "[v]" "$OUT/sheet.png"
echo "OK -> $OUT/sheet.png (${total} frames)"
