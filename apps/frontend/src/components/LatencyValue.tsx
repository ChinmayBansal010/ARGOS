type LatencyValueProps = { milliseconds: number };

export function LatencyValue({ milliseconds }: LatencyValueProps) {
  const value = milliseconds >= 1000 ? `${(milliseconds / 1000).toFixed(2)} s` : `${milliseconds.toFixed(1)} ms`;
  return <span className="font-mono text-sm text-zinc-300" title={`${milliseconds.toFixed(2)} milliseconds`}>{value}</span>;
}
