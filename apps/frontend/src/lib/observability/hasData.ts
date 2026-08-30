export function hasData<T>(items: T[] | null | undefined): boolean {
  return Array.isArray(items) && items.length > 0;
}
