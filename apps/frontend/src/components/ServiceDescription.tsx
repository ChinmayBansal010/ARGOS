type ServiceDescriptionProps = { name: string; description: string };

export function ServiceDescription({ name, description }: ServiceDescriptionProps) {
  return <div><h3 className="text-sm font-medium text-zinc-200">{name}</h3><p className="mt-1 text-sm leading-6 text-zinc-500">{description}</p></div>;
}
