import Link from "next/link";
import { Download, CheckCircle2, FolderTree, Puzzle, MessageCircle, ShieldCheck, FileCode2 } from "lucide-react";
import { Reveal } from "@/components/ui";

export const dynamic = "force-dynamic";
export const metadata = { title: "WordPress Theme — Download & Docs" };

async function getFiles() {
  try {
    const fs = await import("node:fs");
    const path = await import("node:path");
    const dir = path.join(process.cwd(), "wordpress", "brickpoint");
    const walk = (d: string, base: string): string[] => {
      let out: string[] = [];
      for (const f of fs.readdirSync(d)) {
        const p = path.join(d, f);
        if (fs.statSync(p).isDirectory()) out = out.concat(walk(p, base));
        else out.push(path.relative(base, p));
      }
      return out;
    };
    return walk(dir, dir).sort();
  } catch { return []; }
}

export default async function ThemePage() {
  const files = await getFiles();
  const groups: Record<string, string[]> = {};
  for (const f of files) {
    const top = f.includes("/") ? f.split("/")[0] + "/" : "(root)";
    (groups[top] = groups[top] || []).push(f);
  }

  return (
    <div>
      <section className="bg-[#141210] py-14 text-white">
        <div className="bp-container grid items-center gap-8 lg:grid-cols-[1fr_auto]">
          <div>
            <p className="text-xs font-black uppercase tracking-[0.22em] text-orange-400">Installable WordPress Theme • v1.0.0</p>
            <h1 className="font-display mt-2 text-4xl font-black md:text-5xl">BrickPoint for WordPress</h1>
            <p className="mt-3 max-w-2xl text-white/70">A real, installable custom theme — <strong className="text-white">{files.length} files</strong> with Products (bp_product), Videos (bp_video), Projects, Locations, WhatsApp inquiries, Customizer settings and 9 Elementor widgets. No WooCommerce.</p>
            <div className="mt-6 flex flex-wrap gap-3">
              <a href="/api/theme-download" className="btn-brick inline-flex items-center gap-2 rounded-xl px-7 py-4 font-bold text-white"><Download className="h-5 w-5" /> Download brickpoint.zip</a>
              <Link href="/admin" className="inline-flex items-center gap-2 rounded-xl border border-white/20 px-6 py-4 text-sm font-bold hover:bg-white/10">Try Live Content Manager</Link>
            </div>
          </div>
          <div className="grid grid-cols-2 gap-3">
            {[["48", "PHP templates"], ["9", "Elementor widgets"], ["4", "Post types"], ["0", "WooCommerce"]].map(([n, l]) => (
              <div key={l} className="rounded-2xl border border-white/10 bg-white/5 p-5 text-center">
                <p className="font-display text-3xl font-black text-orange-400">{n}</p>
                <p className="text-xs font-semibold text-white/60">{l}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      <section className="py-12">
        <div className="bp-container grid gap-8 lg:grid-cols-[1fr_380px]">
          <div>
            <Reveal>
              <h2 className="font-display text-2xl font-black">Installation steps</h2>
              <ol className="mt-4 space-y-3">
                {[
                  ["1. Download", "Click “Download brickpoint.zip” above. The ZIP contains the /brickpoint/ theme folder."],
                  ["2. Upload", "In WordPress go to Appearance → Themes → Add New → Upload Theme, choose brickpoint.zip and click Install Now."],
                  ["3. Activate", "Click Activate. Default Product Categories (15) and Video Categories (15) are created automatically."],
                  ["4. Menus", "Go to Appearance → Menus and assign menus to Primary, Footer and Mobile locations."],
                  ["5. Customize", "Go to Appearance → Customize → BrickPoint to set phone, WhatsApp number, email, social links, hero video, colors and footer text."],
                  ["6. Elementor (optional)", "Install free Elementor to edit pages with drag & drop. Elementor Pro unlocks Theme Builder header/footer/single-product/single-video templates."],
                  ["7. Add content", "Use Products, Videos, Projects and Locations in the admin sidebar. Every product auto-generates a WhatsApp inquiry message."],
                  ["8. Pages", "Create Home, About, Products, SS7 Bricks, Videos, Locations, Contact etc. as normal Pages and build them with Elementor + BrickPoint widgets."],
                ].map(([t, d]) => (
                  <li key={t} className="flex gap-3 rounded-2xl border bg-white p-4 text-sm">
                    <CheckCircle2 className="mt-0.5 h-5 w-5 shrink-0 text-emerald-600" />
                    <span><strong>{t} — </strong>{d}</span>
                  </li>
                ))}
              </ol>
            </Reveal>

            <Reveal>
              <h2 className="font-display mt-10 text-2xl font-black">What is included</h2>
              <div className="mt-4 grid gap-4 sm:grid-cols-2">
                {[
                  [FileCode2, "Custom post types", "bp_product + bp_product_category, bp_video + bp_video_category, bp_project, bp_location — all with meta boxes, no page-builder lock-in."],
                  [MessageCircle, "WhatsApp system", "Prefilled product/category inquiry messages with dynamic name, category, price and unit. Number editable in Customizer."],
                  [Puzzle, "9 Elementor widgets", "Product Grid, Product Categories, Product Price, WhatsApp Button, Video Grid, Video Card, Project Grid, Location Cards, Social Links."],
                  [ShieldCheck, "Secure & fast", "Nonces, sanitization, escaping, proper enqueueing, lazy thumbnails, thumbnail-first video, reduced-motion support."],
                ].map(([Icon, t, d]: any) => (
                  <div key={t} className="rounded-2xl border bg-white p-5">
                    <Icon className="h-6 w-6 text-orange-600" />
                    <h3 className="font-display mt-2 font-extrabold">{t}</h3>
                    <p className="mt-1 text-sm text-[#6b6560]">{d}</p>
                  </div>
                ))}
              </div>
            </Reveal>

            <Reveal>
              <div className="mt-8 rounded-2xl border border-amber-300 bg-amber-50 p-5 text-sm text-amber-900">
                <strong>Theme Builder note:</strong> header/footer/single/archive template overrides via Elementor require <em>Elementor Pro</em>. The theme works fully without it — all PHP templates (single-bp_product, archive-bp_video, taxonomies, 404, search…) render natively.
              </div>
            </Reveal>
          </div>

          <div>
            <div className="sticky top-24 rounded-3xl border bg-white p-5">
              <h3 className="font-display flex items-center gap-2 font-extrabold"><FolderTree className="h-5 w-5 text-orange-600" /> Theme file tree ({files.length})</h3>
              <div className="mt-4 max-h-[560px] space-y-3 overflow-y-auto pr-1 text-xs">
                {Object.entries(groups).map(([g, list]) => (
                  <div key={g}>
                    <p className="font-black uppercase tracking-wider text-orange-700">{g}</p>
                    <ul className="mt-1 space-y-0.5 font-mono text-[11px] text-stone-600">
                      {list.map((f) => (<li key={f} className="truncate">📄 {f}</li>))}
                    </ul>
                  </div>
                ))}
              </div>
              <a href="/api/theme-download" className="btn-brick mt-4 flex items-center justify-center gap-2 rounded-xl px-4 py-3 text-sm font-bold text-white"><Download className="h-4 w-4" /> Download ZIP</a>
              <p className="mt-2 text-center text-[11px] text-stone-500">brickpoint.zip • built from /wordpress/brickpoint</p>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}
