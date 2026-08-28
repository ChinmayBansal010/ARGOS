type ErrorStateProps = { message: string; onRetry?: () => void };

export function ErrorState({ message, onRetry }: ErrorStateProps) {
  return (
    <div role="alert" className="rounded-xl border border-zinc-800 p-5">
      <p className="text-sm text-zinc-300">{message}</p>
      {onRetry ? <button type="button" onClick={onRetry} className="mt-3 text-sm underline underline-offset-4">Retry</button> : null}
    </div>
  );
}
