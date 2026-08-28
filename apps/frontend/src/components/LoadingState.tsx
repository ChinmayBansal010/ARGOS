export function LoadingState() {
  return (
    <div role="status" aria-live="polite" className="flex items-center gap-3 rounded-xl border border-zinc-800 p-4 text-sm text-zinc-400">
      <span className="h-2 w-2 animate-pulse rounded-full bg-zinc-300" aria-hidden="true" />
      Loading service data...
    </div>
  );
}
