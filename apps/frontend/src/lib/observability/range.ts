export function range(values: number[]): number {
  const valid = values.filter(Number.isFinite);
  return valid.length ? Math.max(...valid) - Math.min(...valid) : 0;
}
