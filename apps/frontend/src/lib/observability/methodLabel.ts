const METHODS = new Set(["GET", "POST", "PUT", "PATCH", "DELETE", "HEAD", "OPTIONS"]);

export function methodLabel(method: string): string {
  const normalized = method.trim().toUpperCase();
  return METHODS.has(normalized) ? normalized : "UNKNOWN";
}
