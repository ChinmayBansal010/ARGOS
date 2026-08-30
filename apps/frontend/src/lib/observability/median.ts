import { percentile } from "./percentile";

export function median(values: number[]): number {
  return percentile(values, 0.5);
}
