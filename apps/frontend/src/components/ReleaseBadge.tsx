type ReleaseBadgeProps = { version: string; channel?: string };

export function ReleaseBadge({ version, channel = "stable" }: ReleaseBadgeProps) {
  return <span className="inline-flex items-center gap-2 rounded-full border border-zinc-700 px-2.5 py-1 text-xs text-zinc-400"><span>{version}</span><span className="text-zinc-600">{channel}</span></span>;
}
