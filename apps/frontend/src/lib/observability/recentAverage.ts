import { average } from "./average";

export function recentAverage(values: number[], windowSize: number): number {
  const size = Math.max(1, Math.floor(windowSize));
  return average(values.slice(-size));
}
