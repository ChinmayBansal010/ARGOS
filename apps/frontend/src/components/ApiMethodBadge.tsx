type ApiMethodBadgeProps = { method: "GET" | "POST" | "PUT" | "PATCH" | "DELETE" };

export function ApiMethodBadge({ method }: ApiMethodBadgeProps) {
  return <span className="inline-flex min-w-14 justify-center rounded border border-zinc-700 px-2 py-1 font-mono text-xs text-zinc-300">{method}</span>;
}
