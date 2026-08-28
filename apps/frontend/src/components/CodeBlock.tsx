type CodeBlockProps = { code: string; language?: string };

export function CodeBlock({ code, language = "text" }: CodeBlockProps) {
  return (
    <pre aria-label={`${language} code`} className="overflow-x-auto rounded-xl border border-zinc-800 bg-zinc-950 p-4 text-sm leading-6 text-zinc-300">
      <code>{code}</code>
    </pre>
  );
}
