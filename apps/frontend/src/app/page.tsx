import Image from "next/image";

const capabilities = [
  "API health and service observability",
  "Configurable telemetry and tracing",
  "AI-ready backend services",
];

export default function Home() {
  return (
    <main className="min-h-screen bg-zinc-950 px-6 py-16 text-zinc-100">
      <div className="mx-auto flex max-w-5xl flex-col gap-16">
        <header className="flex items-center justify-between">
          <div className="flex items-center gap-3">
            <Image src="/next.svg" alt="ARGOS" width={72} height={18} className="invert" priority />
            <span className="text-sm font-medium tracking-[0.25em] text-zinc-400">ARGOS</span>
          </div>
          <a className="rounded-full border border-zinc-700 px-4 py-2 text-sm hover:bg-zinc-900" href="/docs">
            API Docs
          </a>
        </header>

        <section className="max-w-3xl">
          <p className="mb-4 text-sm font-semibold uppercase tracking-[0.3em] text-zinc-400">AI operations platform</p>
          <h1 className="text-5xl font-semibold tracking-tight sm:text-7xl">Observe, operate, and evolve your AI services.</h1>
          <p className="mt-6 max-w-2xl text-lg leading-8 text-zinc-400">
            ARGOS brings service health, telemetry, and AI infrastructure together behind a focused developer experience.
          </p>
        </section>

        <section className="grid gap-4 sm:grid-cols-3" aria-label="ARGOS capabilities">
          {capabilities.map((capability) => (
            <article key={capability} className="rounded-2xl border border-zinc-800 bg-zinc-900/60 p-6">
              <div className="mb-5 h-2 w-2 rounded-full bg-zinc-100" aria-hidden="true" />
              <p className="leading-7 text-zinc-300">{capability}</p>
            </article>
          ))}
        </section>

        <footer className="border-t border-zinc-800 pt-6 text-sm text-zinc-500">
          Built for reliable development, deployment, and observability.
        </footer>
      </div>
    </main>
  );
}
