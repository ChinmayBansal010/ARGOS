export type LatencyBucket = "fast" | "normal" | "slow" | "critical";

export function latencyBucket(milliseconds: number): LatencyBucket {
  if (!Number.isFinite(milliseconds) || milliseconds < 0) return "critical";
  if (milliseconds < 100) return "fast";
  if (milliseconds < 500) return "normal";
  if (milliseconds < 1000) return "slow";
  return "critical";
}
