import Link from "next/link";
import { ArrowRight, MessageCircle } from "lucide-react";
import { db } from "@/db";
import { productCategories, products } from "@/db/schema";
import { Reveal } from "@/components/ui";
import { whatsappLink, categoryInquiryMessage } from "@/lib/site";

export const dynamic = "force-dynamic";
export const metadata = { title: "Product Categories" };

export default async function CategoriesPage() {
  let cats: any[] = [];
  let prods: any[] = [];
  try {
    cats = await db.select().from(productCategories);
    prods = await db.select().from(products);
  } catch {}
  const count = (id: number) => prods.filter((p) => p.categoryId === id).length;
  return (
    <div>
      <section className="bg-[#141210] py-14 text-white">
        <div className="bp-container">
          <p className="text-xs font-black uppercase tracking-[0.22em] text-orange-400">Browse by category</p>
          <h1 className="font-display mt-2 text-4xl font-black md:text-5xl">Product Categories</h1>
          <p className="mt-3 max-w-2xl text-white/70">Fifteen editable categories — from SS7 bricks to finishing materials.</p>
        </div>
      </section>
      <section className="py-12">
        <div className="bp-container grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
          {cats.map((c: any, i: number) => (
            <Reveal key={c.id} delay={(i % 3) as 0 | 1 | 2}>
              <article className="card-hover overflow-hidden rounded-3xl border bg-white">
                <Link href={`/categories/${c.slug}`} className="img-zoom relative block aspect-[16/9] overflow-hidden bg-stone-200">
                  {c.image ? (
                    // eslint-disable-next-line @next/next/no-img-element
                    <img src={c.image} alt={c.name} loading="lazy" className="h-full w-full object-cover" />
                  ) : <div className="grid h-full place-items-center text-4xl">🧱</div>}
                  <span className="absolute left-4 top-4 rounded-full bg-black/70 px-3 py-1 text-[11px] font-bold text-white">{count(c.id)} products</span>
                </Link>
                <div className="p-6">
                  <Link href={`/categories/${c.slug}`} className="font-display text-xl font-black hover:text-orange-700">{c.name}</Link>
                  {c.description && <p className="line-clamp-2 mt-2 text-sm text-[#6b6560]">{c.description}</p>}
                  <div className="mt-4 grid grid-cols-2 gap-2">
                    <Link href={`/categories/${c.slug}`} className="inline-flex items-center justify-center gap-1 rounded-xl bg-[#141210] px-3 py-2.5 text-xs font-bold text-white hover:bg-black">Explore <ArrowRight className="h-3.5 w-3.5" /></Link>
                    <a href={whatsappLink(categoryInquiryMessage(c.name))} target="_blank" rel="noopener" className="btn-whatsapp inline-flex items-center justify-center gap-1 rounded-xl px-3 py-2.5 text-xs font-bold text-white"><MessageCircle className="h-3.5 w-3.5" /> Quote</a>
                  </div>
                </div>
              </article>
            </Reveal>
          ))}
        </div>
      </section>
    </div>
  );
}
