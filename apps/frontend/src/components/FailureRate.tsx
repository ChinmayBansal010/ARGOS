type FailureRateProps = { failures: number; requests: number };

export function FailureRate({ failures, requests }: FailureRateProps) {
  const rate = requests > 0 ? (Math.max(0, failures) / requests) * 100 : 0;
  return <span className="font-mono text-sm text-zinc-300">{Math.min(100, rate).toFixed(2)}%</span>;
}
