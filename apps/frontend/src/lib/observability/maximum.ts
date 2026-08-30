export function maximum(values: number[]): number {
  const valid = values.filter(Number.isFinite);
  return valid.length ? Math.max(...valid) : 0;
}
