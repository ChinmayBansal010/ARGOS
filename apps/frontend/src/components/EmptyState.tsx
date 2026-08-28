type EmptyStateProps = { title: string; description: string };

export function EmptyState({ title, description }: EmptyStateProps) {
  return (
    <div className="rounded-2xl border border-dashed border-zinc-800 p-8 text-center">
      <h3 className="font-medium text-zinc-200">{title}</h3>
      <p className="mx-auto mt-2 max-w-md text-sm leading-6 text-zinc-500">{description}</p>
    </div>
  );
}
