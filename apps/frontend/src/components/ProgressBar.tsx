type ProgressBarProps = { value: number; label?: string };

export function ProgressBar({ value, label }: ProgressBarProps) {
  const safeValue = Math.min(100, Math.max(0, value));
  return <div aria-label={label} className="space-y-2"><div className="h-2 overflow-hidden rounded-full bg-zinc-800"><div className="h-full rounded-full bg-zinc-200" style={{ width: `${safeValue}%` }} /></div><span className="text-xs text-zinc-500">{safeValue}%</span></div>;
}
