type HealthIndicatorProps = { status: "healthy" | "degraded" | "unhealthy" };

export function HealthIndicator({ status }: HealthIndicatorProps) {
  return <span aria-label={`Status: ${status}`} className="inline-flex h-2.5 w-2.5 rounded-full border border-zinc-500" data-status={status} />;
}
