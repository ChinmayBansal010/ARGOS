export function filterFailures<T extends { status: string }>(items: T[]): T[] {
  return items.filter(({ status }) => ["critical", "failed", "error", "down"].includes(status.toLowerCase()));
}
