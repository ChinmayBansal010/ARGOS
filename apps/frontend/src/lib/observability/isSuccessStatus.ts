export function isSuccessStatus(code: number): boolean {
  return Number.isFinite(code) && code >= 200 && code < 300;
}
