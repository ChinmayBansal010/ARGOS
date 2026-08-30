export function formatRate(value: number): string {
  if (!Number.isFinite(value) || value < 0) return "--";
  if (value < 1) return `${value.toFixed(2)}/s`;
  if (value < 1000) return `${value.toFixed(1)}/s`;
  return `${(value / 1000).toFixed(1)}k/s`;
}
