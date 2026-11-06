#!/usr/bin/env python3
# bpm.py — 音频 BPM + 首拍相位估计（onset 自相关）
# 依赖: numpy（无需 librosa/audio 库；pip 装不上的环境也能跑）
# 用法: python bpm.py <audio.mp3> [fps=30]
# 输出: BPM、拍长（帧@fps）、首拍相位（帧@fps）
# 原理: ffmpeg 解码为单声道 f32 PCM → 频谱 flux onset envelope →
#       60~180 BPM 区间自相关取峰 → onset 包络与拍网格互相关求相位。
import subprocess, sys
import numpy as np

def load_mono(path, sr=22050):
    cmd = ["ffmpeg", "-v", "error", "-i", path, "-ac", "1", "-ar", str(sr),
           "-f", "f32le", "-"]
    raw = subprocess.run(cmd, capture_output=True, check=True).stdout
    return np.frombuffer(raw, dtype=np.float32), sr

def onset_envelope(x, sr, hop=512):
    n = 1024
    win = np.hanning(n).astype(np.float32)
    frames = 1 + (len(x) - n) // hop
    S = np.empty((frames, n // 2 + 1), dtype=np.float32)
    for i in range(frames):
        seg = x[i * hop : i * hop + n] * win
        S[i] = np.abs(np.fft.rfft(seg))
    flux = np.diff(S, axis=0)
    flux[flux < 0] = 0
    return flux.sum(axis=1), sr / hop  # envelope, envelope fps

def main():
    path = sys.argv[1]
    fps = float(sys.argv[2]) if len(sys.argv) > 2 else 30.0
    x, sr = load_mono(path)
    env, efps = onset_envelope(x, sr)
    env = env - env.mean()
    ac = np.correlate(env, env, mode="full")[len(env) - 1:]
    lag_lo, lag_hi = int(efps * 60 / 180), int(efps * 60 / 60)  # 60~180 BPM
    lag = lag_lo + np.argmax(ac[lag_lo:lag_hi])
    bpm = 60.0 * efps / lag
    # 首拍相位：在最佳周期上滑动拍网格，取 onset 能量最大偏移
    best_p, best_e = 0, -1
    for p in range(lag):
        grid = np.arange(p, len(env), lag)
        e = env[grid].sum()
        if e > best_e:
            best_e, best_p = e, p
    beat_frames = best_p * fps / efps
    print(f"BPM = {bpm:.2f}")
    print(f"beat = {fps * lag / efps:.2f}f @{fps:.0f}fps  ({lag} env-lags)")
    print(f"phase = {beat_frames:.1f}f @{fps:.0f}fps")

if __name__ == "__main__":
    main()
