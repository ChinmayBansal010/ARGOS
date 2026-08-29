type ResponseCodeProps = { code: number };

export function ResponseCode({ code }: ResponseCodeProps) {
  return <span className="font-mono text-xs text-zinc-400" aria-label={`HTTP status ${code}`}>{code}</span>;
}
