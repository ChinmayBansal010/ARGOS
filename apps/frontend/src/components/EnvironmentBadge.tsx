type EnvironmentBadgeProps = { environment: string };

export function EnvironmentBadge({ environment }: EnvironmentBadgeProps) {
  return <span className="rounded-md border border-zinc-700 px-2 py-1 text-xs font-medium uppercase tracking-wide text-zinc-400">{environment}</span>;
}
