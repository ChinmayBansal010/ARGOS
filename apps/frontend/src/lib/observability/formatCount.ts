export function formatCount(value: number): string {
  if (!Number.isFinite(value)) return "--";
  const absolute = Math.abs(value);
  if (absolute >= 1_000_000) return `${(value / 1_000_000).toFixed(1)}M`;
  if (absolute >= 1_000) return `${(value / 1_000).toFixed(1)}k`;
  return Math.round(value).toString();
}
