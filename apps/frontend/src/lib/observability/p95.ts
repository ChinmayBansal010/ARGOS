import { percentile } from "./percentile";

export function p95(values: number[]): number {
  return percentile(values, 0.95);
}
