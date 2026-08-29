type IncidentBannerProps = { status: "operational" | "degraded" | "outage"; message: string };

const labels = { operational: "Operational", degraded: "Degraded", outage: "Outage" } as const;

export function IncidentBanner({ status, message }: IncidentBannerProps) {
  return <div role="alert" className="rounded-xl border border-zinc-800 bg-zinc-900/60 p-4"><div className="flex items-center justify-between gap-4"><span className="text-sm font-medium text-zinc-200">{labels[status]}</span><span className="text-xs uppercase tracking-wider text-zinc-500">Service status</span></div><p className="mt-2 text-sm text-zinc-500">{message}</p></div>;
}
