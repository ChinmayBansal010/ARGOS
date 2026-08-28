type StatusBadgeProps = { status: "healthy" | "degraded" | "unhealthy" };

const labels: Record<StatusBadgeProps["status"], string> = {
  healthy: "Healthy",
  degraded: "Degraded",
  unhealthy: "Unhealthy",
};

export function StatusBadge({ status }: StatusBadgeProps) {
  return <span className="rounded-full border border-zinc-700 px-3 py-1 text-xs font-medium text-zinc-300">{labels[status]}</span>;
}
