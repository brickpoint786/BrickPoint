import { NextResponse } from "next/server";
import fs from "node:fs";
import path from "node:path";

export const dynamic = "force-dynamic";

function walk(dir: string, base: string): { path: string; size: number }[] {
  const out: { path: string; size: number }[] = [];
  for (const f of fs.readdirSync(dir)) {
    const p = path.join(dir, f);
    const st = fs.statSync(p);
    if (st.isDirectory()) out.push(...walk(p, base));
    else out.push({ path: path.relative(base, p), size: st.size });
  }
  return out.sort((a, b) => a.path.localeCompare(b.path));
}

export async function GET() {
  const themeDir = path.join(process.cwd(), "wordpress", "brickpoint");
  if (!fs.existsSync(themeDir)) return NextResponse.json({ ok: false, error: "missing" }, { status: 404 });
  const files = walk(themeDir, themeDir);
  const total = files.reduce((n, f) => n + f.size, 0);
  return NextResponse.json({ ok: true, count: files.length, totalBytes: total, files });
}
