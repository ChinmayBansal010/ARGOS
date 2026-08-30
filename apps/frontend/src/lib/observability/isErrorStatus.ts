export function isErrorStatus(code: number): boolean {
  return Number.isFinite(code) && code >= 400;
}
