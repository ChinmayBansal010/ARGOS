type RefreshButtonProps = { onRefresh: () => void; disabled?: boolean };

export function RefreshButton({ onRefresh, disabled = false }: RefreshButtonProps) {
  return (
    <button type="button" onClick={onRefresh} disabled={disabled} className="rounded-lg border border-zinc-700 px-3 py-2 text-sm text-zinc-300 transition hover:bg-zinc-900 disabled:cursor-not-allowed disabled:opacity-50">
      Refresh
    </button>
  );
}
