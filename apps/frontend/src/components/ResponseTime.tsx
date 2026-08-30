export function ResponseTime({ milliseconds }: { milliseconds: number }) {
  if (!Number.isFinite(milliseconds) || milliseconds < 0) return <span>--</span>;
  return <span>{milliseconds < 1000 ? `${Math.round(milliseconds)} ms` : `${(milliseconds / 1000).toFixed(2)} s`}</span>;
}
