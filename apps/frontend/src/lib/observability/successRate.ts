export function successRate(successes: number, total: number): number {
  if (!Number.isFinite(successes) || !Number.isFinite(total) || total <= 0) return 0;
  return Math.max(0, Math.min(100, (successes / total) * 100));
}
