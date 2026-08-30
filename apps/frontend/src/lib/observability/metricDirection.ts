export type MetricDirection = "positive" | "negative" | "neutral";

export function metricDirection(change: number, higherIsBetter: boolean): MetricDirection {
  if (!Number.isFinite(change) || change === 0) return "neutral";
  const improved = higherIsBetter ? change > 0 : change < 0;
  return improved ? "positive" : "negative";
}
