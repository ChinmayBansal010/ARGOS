type DurationValueProps = { milliseconds: number };

export function DurationValue({ milliseconds }: DurationValueProps) {
  const value = Math.max(0, milliseconds);
  if (value < 1000) return <span className="font-mono text-sm text-zinc-300">{Math.round(value)} ms</span>;
  return <span className="font-mono text-sm text-zinc-300">{(value / 1000).toFixed(2)} s</span>;
}
