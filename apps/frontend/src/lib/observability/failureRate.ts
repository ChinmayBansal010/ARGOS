export function failureRate(failures: number, requests: number): number {
  if (!Number.isFinite(failures) || !Number.isFinite(requests) || requests <= 0) return 0;
  return Math.max(0, Math.min(100, (failures / requests) * 100));
}
