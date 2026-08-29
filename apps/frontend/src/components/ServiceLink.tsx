type ServiceLinkProps = { name: string; href: string };

export function ServiceLink({ name, href }: ServiceLinkProps) {
  return <a href={href} className="text-sm text-zinc-400 transition-colors hover:text-zinc-100">{name}</a>;
}
