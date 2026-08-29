type TelemetryStatusProps = { enabled: boolean; provider?: string };

export function TelemetryStatus({ enabled, provider }: TelemetryStatusProps) {
  return <div className="rounded-xl border border-zinc-800 p-4"><p className="text-xs uppercase tracking-[0.2em] text-zinc-500">Telemetry</p><p className="mt-2 text-sm text-zinc-200">{enabled ? provider ?? "Enabled" : "Disabled"}</p></div>;
}
