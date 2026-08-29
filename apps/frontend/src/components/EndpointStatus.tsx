type EndpointStatusProps = { path: string; available: boolean };

export function EndpointStatus({ path, available }: EndpointStatusProps) {
  return <div className="flex items-center justify-between gap-4 rounded-lg border border-zinc-800 px-4 py-3"><code className="text-xs text-zinc-400">{path}</code><span className="text-xs text-zinc-500">{available ? "Available" : "Unavailable"}</span></div>;
}
