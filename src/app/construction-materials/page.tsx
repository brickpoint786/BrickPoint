import Link from "next/link";
import { ArrowRight } from "lucide-react";
import { db } from "@/db";
import { productCategories, products } from "@/db/schema";
import { Reveal, SectionHead, ProductCard } from "@/components/ui";

export const dynamic = "force-dynamic";
export const metadata = { title: "Construction Materials" };

const GROUPS: Record<string, string[]> = {
  "Structure & Masonry": ["bricks", "ss7-bricks", "cement", "bajri-crush", "sand-rait", "steel"],
  "Pipes & Services": ["electric-conduit-pipes", "plumbing-pipes", "cables-wires", "switches-sockets"],
  "Protection & Finish": ["construction-chemicals", "insulation-membrane", "paints", "lights", "other-materials"],
};

export default async function MaterialsPage() {
  let cats: any[] = [];
  let prods: any[] = [];
  try {
    cats = await db.select().from(productCategories);
    prods = await db.select().from(products);
  } catch {}
  const bySlug = (s: string) => cats.find((c) => c.slug === s);
  const inCat = (slug: string) => { const c = bySlug(slug); return c ? prods.filter((p) => p.categoryId === c.id).slice(0, 4) : []; };

  return (
    <div>
      <section className="bg-[#141210] py-14 text-white">
        <div className="bp-container">
          <p className="text-xs font-black uppercase tracking-[0.22em] text-orange-400">Complete Range</p>
          <h1 className="font-display mt-2 text-4xl font-black md:text-5xl">Construction Materials</h1>
          <p className="mt-3 max-w-2xl text-white/70">Cement to finishes — one quotation, coordinated supply, WhatsApp-fast response.</p>
        </div>
      </section>
      {Object.entries(GROUPS).map(([group, slugs]) => (
        <section key={group} className="border-b py-12 last:border-0">
          <div className="bp-container">
            <div className="flex flex-wrap items-end justify-between gap-4">
              <div>
                <h2 className="font-display text-2xl font-black md:text-3xl">{group}</h2>
                <div className="mt-3 flex flex-wrap gap-2">
                  {slugs.map((s) => bySlug(s) && (
                    <Link key={s} href={`/categories/${s}`} className="rounded-full border px-4 py-1.5 text-xs font-bold hover:border-orange-600 hover:text-orange-700">{bySlug(s).name}</Link>
                  ))}
                </div>
              </div>
              <Link href="/categories" className="inline-flex items-center gap-1 text-sm font-bold text-orange-700">All categories <ArrowRight className="h-4 w-4" /></Link>
            </div>
            <div className="mt-6 grid gap-5 sm:grid-cols-2 lg:grid-cols-4">
              {slugs.flatMap((s) => inCat(s).map((p: any) => ({ ...p, _cat: bySlug(s)?.name }))).slice(0, 4).map((p: any) => (
                <ProductCard key={p.id} p={p} categoryName={p._cat} />
              ))}
            </div>
          </div>
        </section>
      ))}
      <section className="py-12">
        <div className="bp-container">
          <Reveal><SectionHead eyebrow="Bulk Orders" title="One list. One quotation. Coordinated delivery." text="Send your BOQ or material list on WhatsApp and get a consolidated project quotation." /></Reveal>
          <div className="mt-6 text-center">
            <Link href="/contact" className="btn-brick inline-flex items-center gap-2 rounded-xl px-8 py-4 font-bold text-white">Request Project Quotation <ArrowRight className="h-4 w-4" /></Link>
          </div>
        </div>
      </section>
    </div>
  );
}
