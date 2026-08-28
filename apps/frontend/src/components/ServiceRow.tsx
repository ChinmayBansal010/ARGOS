type ServiceRowProps = { name: string; status: "healthy" | "degraded" | "unhealthy"; latencyMs: number };

export function ServiceRow({ name, status, latencyMs }: ServiceRowProps) {
  return (
    <div className="flex items-center justify-between border-b border-zinc-800 py-4 last:border-0">
      <div><p className="text-sm font-medium text-zinc-200">{name}</p><p className="text-xs text-zinc-500">{latencyMs.toFixed(1)} ms</p></div>
      <span className="text-xs capitalize text-zinc-400">{status}</span>
    </div>
  );
}
