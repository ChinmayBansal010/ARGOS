type TimeValueProps = { timestamp: string };

export function TimeValue({ timestamp }: TimeValueProps) {
  const date = new Date(timestamp);
  const formatted = Number.isNaN(date.getTime()) ? "Unknown" : date.toLocaleString();
  return <time dateTime={timestamp} title={formatted} className="text-sm text-zinc-400">{formatted}</time>;
}
