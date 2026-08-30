export type HttpClass = "success" | "redirect" | "client-error" | "server-error" | "unknown";

export function httpClass(code: number): HttpClass {
  if (!Number.isFinite(code)) return "unknown";
  if (code >= 200 && code < 300) return "success";
  if (code >= 300 && code < 400) return "redirect";
  if (code >= 400 && code < 500) return "client-error";
  if (code >= 500 && code < 600) return "server-error";
  return "unknown";
}
