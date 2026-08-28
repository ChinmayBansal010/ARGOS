import type { ReactNode } from "react";

type PanelProps = { children: ReactNode; className?: string };

export function Panel({ children, className = "" }: PanelProps) {
  return <section className={`rounded-2xl border border-zinc-800 bg-zinc-900/40 p-6 ${className}`}>{children}</section>;
}
