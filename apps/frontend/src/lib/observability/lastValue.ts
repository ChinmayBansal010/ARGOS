export function lastValue(values: number[], fallback = 0): number {
  return values.length && Number.isFinite(values[values.length - 1]) ? values[values.length - 1] : fallback;
}
