type HealthScoreProps = { score: number };

export function HealthScore({ score }: HealthScoreProps) {
  const normalized = Math.min(100, Math.max(0, Math.round(score)));
  return <div className="rounded-xl border border-zinc-800 bg-zinc-900/40 p-5"><p className="text-sm text-zinc-500">Health score</p><p className="mt-2 text-3xl font-semibold text-zinc-100">{normalized}<span className="text-base text-zinc-500">/100</span></p></div>;
}
