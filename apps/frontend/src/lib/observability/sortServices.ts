export type ServiceStatus = { name: string; status: string; latency?: number };

export function sortServices(services: ServiceStatus[]): ServiceStatus[] {
  return [...services].sort((a, b) => a.name.localeCompare(b.name));
}
