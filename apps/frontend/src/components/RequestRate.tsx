type RequestRateProps = { requests: number; windowSeconds: number };

export function RequestRate({ requests, windowSeconds }: RequestRateProps) {
  const rate = windowSeconds > 0 ? requests / windowSeconds : 0;
  return <span className="font-mono text-sm text-zinc-300">{rate.toFixed(1)} req/s</span>;
}
