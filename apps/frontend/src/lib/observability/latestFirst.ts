export function latestFirst<T extends { timestamp: string | number | Date }>(items: T[]): T[] {
  return [...items].sort((a, b) => new Date(b.timestamp).getTime() - new Date(a.timestamp).getTime());
}
