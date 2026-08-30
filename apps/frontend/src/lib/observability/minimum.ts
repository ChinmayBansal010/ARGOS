export function minimum(values: number[]): number {
  const valid = values.filter(Number.isFinite);
  return valid.length ? Math.min(...valid) : 0;
}
