export type Trend = "up" | "down" | "flat";

export function trend(current: number, previous: number, tolerance = 0.01): Trend {
  const delta = current - previous;
  if (Math.abs(delta) <= tolerance) return "flat";
  return delta > 0 ? "up" : "down";
}
