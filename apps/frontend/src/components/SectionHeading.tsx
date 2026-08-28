type SectionHeadingProps = { eyebrow: string; title: string; description?: string };

export function SectionHeading({ eyebrow, title, description }: SectionHeadingProps) {
  return (
    <header>
      <p className="text-xs font-semibold uppercase tracking-[0.25em] text-zinc-500">{eyebrow}</p>
      <h2 className="mt-2 text-2xl font-semibold tracking-tight text-zinc-100">{title}</h2>
      {description ? <p className="mt-2 max-w-2xl text-sm leading-6 text-zinc-400">{description}</p> : null}
    </header>
  );
}
