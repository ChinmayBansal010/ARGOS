export function formatPercent(value: number, digits = 1): string {
  if (!Number.isFinite(value)) return "--";
  return `${value.toFixed(Math.max(0, digits))}%`;
}
