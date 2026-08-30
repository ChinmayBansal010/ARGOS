export function HttpStatusBadge({ code }: { code: number }) {
  const tone = code >= 500 ? "error" : code >= 400 ? "warning" : code >= 200 && code < 300 ? "success" : "neutral";
  return <span className={`http-status http-${tone}`}>{code}</span>;
}
