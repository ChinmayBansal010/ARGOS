type WorkflowStepProps = { number: number; title: string; description: string };

export function WorkflowStep({ number, title, description }: WorkflowStepProps) {
  return <article className="flex gap-4"><span className="flex h-8 w-8 shrink-0 items-center justify-center rounded-full border border-zinc-700 text-xs text-zinc-400">{number}</span><div><h3 className="text-sm font-medium text-zinc-200">{title}</h3><p className="mt-1 text-sm leading-6 text-zinc-500">{description}</p></div></article>;
}
