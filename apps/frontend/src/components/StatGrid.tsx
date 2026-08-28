import type { ReactNode } from "react";

type StatGridProps = { children: ReactNode };

export function StatGrid({ children }: StatGridProps) {
  return <section className="grid gap-3 sm:grid-cols-2 lg:grid-cols-4" aria-label="Operational metrics">{children}</section>;
}
