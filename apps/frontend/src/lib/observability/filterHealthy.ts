export function filterHealthy<T extends { status: string }>(items: T[]): T[] {
  return items.filter(({ status }) => ["healthy", "ok", "up", "operational"].includes(status.toLowerCase()));
}
