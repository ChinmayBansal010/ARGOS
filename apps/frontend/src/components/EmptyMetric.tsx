type EmptyMetricProps = { label: string };

export function EmptyMetric({ label }: EmptyMetricProps) {
  return <div className="rounded-xl border border-dashed border-zinc-800 p-5"><p className="text-sm text-zinc-500">{label}</p><p className="mt-2 text-sm text-zinc-600">No data available</p></div>;
}
