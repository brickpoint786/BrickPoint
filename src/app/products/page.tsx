import Link from "next/link";
import { db } from "@/db";
import { products, productCategories } from "@/db/schema";
import { desc } from "drizzle-orm";
import { Reveal, SectionHead, ProductCard } from "@/components/ui";

export const dynamic = "force-dynamic";
export const metadata = { title: "Products" };

export default async function ProductsPage({ searchParams }: { searchParams: Promise<{ category?: string; featured?: string }> }) {
  const sp = await searchParams;
  let cats: any[] = [];
  let prods: any[] = [];
  try {
    cats = await db.select().from(productCategories);
    prods = await db.select().from(products).orderBy(desc(products.featured), desc(products.id));
  } catch {}
  const catName = (id: number | null) => cats.find((c) => c.id === id)?.name || "";
  let filtered = prods;
  if (sp.category) {
    const c = cats.find((x) => x.slug === sp.category);
    if (c) filtered = filtered.filter((p: any) => p.categoryId === c.id);
  }
  if (sp.featured) filtered = filtered.filter((p: any) => p.featured);

  return (
    <div>
      <section className="bg-[#141210] py-14 text-white">
        <div className="bp-container">
          <p className="text-xs font-black uppercase tracking-[0.22em] text-orange-400">Catalogue</p>
          <h1 className="font-display mt-2 text-4xl font-black md:text-5xl">Products</h1>
          <p className="mt-3 max-w-2xl text-white/70">Every product with WhatsApp ordering — no cart, no checkout, just fast quotations.</p>
          <div className="mt-6 flex flex-wrap gap-2">
            <Link href="/products" className={`rounded-full px-4 py-2 text-xs font-bold ${!sp.category ? "bg-orange-600 text-white" : "bg-white/10 text-white/70 hover:bg-white/15"}`}>All</Link>
            <Link href="/products?featured=1" className={`rounded-full px-4 py-2 text-xs font-bold ${sp.featured ? "bg-orange-600 text-white" : "bg-white/10 text-white/70 hover:bg-white/15"}`}>Featured</Link>
            {cats.map((c) => (
              <Link key={c.id} href={`/products?category=${c.slug}`} className={`rounded-full px-4 py-2 text-xs font-bold ${sp.category === c.slug ? "bg-orange-600 text-white" : "bg-white/10 text-white/70 hover:bg-white/15"}`}>{c.name}</Link>
            ))}
          </div>
        </div>
      </section>
      <section className="py-12">
        <div className="bp-container">
          <p className="text-sm text-[#6b6560]">Showing <strong>{filtered.length}</strong> products {sp.category && <>in <strong>{cats.find((c) => c.slug === sp.category)?.name}</strong></>}</p>
          <div className="mt-6 grid gap-5 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
            {filtered.map((p: any, i: number) => (
              <Reveal key={p.id} delay={(i % 4) as 0 | 1 | 2 | 3}><ProductCard p={p} categoryName={catName(p.categoryId)} /></Reveal>
            ))}
          </div>
          {!filtered.length && (
            <div className="mt-10 rounded-2xl border border-dashed p-10 text-center text-sm text-[#6b6560]">
              No products found. <Link href="/products" className="font-bold text-orange-700">Clear filters</Link>
            </div>
          )}
        </div>
      </section>
    </div>
  );
}
