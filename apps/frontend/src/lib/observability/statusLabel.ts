export function statusLabel(status: string | null | undefined): string {
  if (!status) return "Unknown";
  return status.trim().replace(/[-_]+/g, " ").replace(/\b\w/g, char => char.toUpperCase());
}
