type UptimeValueProps = { value: number };

export function UptimeValue({ value }: UptimeValueProps) {
  const normalized = Math.max(0, Math.min(100, value));
  return <span className="font-mono text-sm text-zinc-200">{normalized.toFixed(2)}%</span>;
}
