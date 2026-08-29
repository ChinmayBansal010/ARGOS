type RegionValueProps = { region: string; zone?: string };

export function RegionValue({ region, zone }: RegionValueProps) {
  return <div><span className="text-sm text-zinc-200">{region}</span>{zone ? <span className="ml-2 text-xs text-zinc-500">{zone}</span> : null}</div>;
}
