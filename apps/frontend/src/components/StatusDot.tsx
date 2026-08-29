type StatusDotProps = { active?: boolean };

export function StatusDot({ active = true }: StatusDotProps) {
  return <span className={`inline-block h-2 w-2 rounded-full ${active ? "bg-zinc-100" : "bg-zinc-600"}`} aria-hidden="true" />;
}
