type HealthSummaryProps = { healthy: number; degraded: number; unhealthy: number };

export function HealthSummary({ healthy, degraded, unhealthy }: HealthSummaryProps) {
  const total = healthy + degraded + unhealthy;
  return <div className="grid grid-cols-3 gap-3 text-center"><div><strong className="block text-xl text-zinc-100">{healthy}</strong><span className="text-xs text-zinc-500">Healthy</span></div><div><strong className="block text-xl text-zinc-100">{degraded}</strong><span className="text-xs text-zinc-500">Degraded</span></div><div><strong className="block text-xl text-zinc-100">{unhealthy}</strong><span className="text-xs text-zinc-500">Unhealthy</span></div><p className="col-span-3 text-xs text-zinc-600">{total} monitored components</p></div>;
}
