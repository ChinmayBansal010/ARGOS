export function healthScore(healthy: number, total: number): number {
  if (!Number.isFinite(healthy) || !Number.isFinite(total) || total <= 0) return 0;
  return Math.max(0, Math.min(100, (healthy / total) * 100));
}
