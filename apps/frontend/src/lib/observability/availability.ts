export function availability(upSeconds: number, totalSeconds: number): number {
  if (!Number.isFinite(upSeconds) || !Number.isFinite(totalSeconds) || totalSeconds <= 0) return 0;
  return Math.max(0, Math.min(100, (upSeconds / totalSeconds) * 100));
}
