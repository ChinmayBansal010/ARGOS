type MetricTrendProps = { current: number; previous: number };

export function MetricTrend({ current, previous }: MetricTrendProps) {
  const delta = previous === 0 ? 0 : ((current - previous) / Math.abs(previous)) * 100;
  const direction = delta > 0 ? "up" : delta < 0 ? "down" : "flat";
  return <span className="text-xs text-zinc-500" aria-label={`Trend ${direction}`}>{delta > 0 ? "+" : ""}{delta.toFixed(1)}%</span>;
}
