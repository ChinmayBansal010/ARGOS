type KeyValueProps = { label: string; value: string };

export function KeyValue({ label, value }: KeyValueProps) {
  return <div className="flex items-center justify-between gap-6 py-2 text-sm"><span className="text-zinc-500">{label}</span><span className="truncate text-zinc-300">{value}</span></div>;
}
