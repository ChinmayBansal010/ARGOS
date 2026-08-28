type EndpointLinkProps = { href: string; label: string };

export function EndpointLink({ href, label }: EndpointLinkProps) {
  return <a href={href} className="font-mono text-xs text-zinc-400 underline decoration-zinc-700 underline-offset-4 hover:text-zinc-200">{label}</a>;
}
