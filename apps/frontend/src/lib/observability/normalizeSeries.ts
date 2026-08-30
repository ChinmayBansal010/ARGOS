export function normalizeSeries(values: number[]): number[] {
  return values.map(value => Number.isFinite(value) ? value : 0);
}
