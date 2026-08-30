import { percentile } from "./percentile";

export function p99(values: number[]): number {
  return percentile(values, 0.99);
}
