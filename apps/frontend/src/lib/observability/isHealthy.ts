export function isHealthy(status: string | null | undefined): boolean {
  if (!status) return false;
  return ["healthy", "ok", "operational", "up"].includes(status.trim().toLowerCase());
}
