type BadgeProps = { children: React.ReactNode };

export function Badge({ children }: BadgeProps) {
  return <span className="inline-flex rounded-full border border-zinc-700 px-2 py-1 text-xs text-zinc-400">{children}</span>;
}
