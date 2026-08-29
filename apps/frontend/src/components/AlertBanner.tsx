type AlertBannerProps = { title: string; message: string };

export function AlertBanner({ title, message }: AlertBannerProps) {
  return <aside role="status" className="rounded-xl border border-zinc-800 bg-zinc-900/60 p-4"><p className="text-sm font-medium text-zinc-200">{title}</p><p className="mt-1 text-sm text-zinc-500">{message}</p></aside>;
}
