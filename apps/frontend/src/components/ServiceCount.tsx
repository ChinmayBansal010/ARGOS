type ServiceCountProps = { healthy: number; total: number };

export function ServiceCount({ healthy, total }: ServiceCountProps) {
  const safeHealthy = Math.max(0, Math.min(healthy, total));
  return <p className="text-sm text-zinc-400"><span className="font-medium text-zinc-200">{safeHealthy}</span> of {Math.max(0, total)} services healthy</p>;
}
