import Link from "next/link";
import { notFound } from "next/navigation";
import { db } from "@/db";
import { productCategories, products } from "@/db/schema";
import { eq } from "drizzle-orm";
import { ChevronRight, Play } from "lucide-react";
import { ProductCard, Reveal, WhatsAppButton } from "@/components/ui";
import { categoryInquiryMessage } from "@/lib/site";

export const dynamic = "force-dynamic";

export default async function CategoryDetail({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  let cat: any = null;
  let items: any[] = [];
  try {
    const [c] = await db.select().from(productCategories).where(eq(productCategories.slug, slug)).limit(1);
    if (!c) return notFound();
    cat = c;
    items = await db.select().from(products).where(eq(products.categoryId, c.id));
  } catch { return notFound(); }

  return (
    <div>
      <section className="relative overflow-hidden bg-[#141210] py-14 text-white">
        {cat.banner || cat.image ? (
          // eslint-disable-next-line @next/next/no-img-element
          <img src={cat.banner || cat.image} alt="" className="absolute inset-0 h-full w-full object-cover opacity-25" />
        ) : null}
        <div className="absolute inset-0 bg-gradient-to-r from-[#141210] to-transparent" />
        <div className="relative bp-container">
          <div className="flex items-center gap-2 text-xs text-white/60">
            <Link href="/" className="hover:text-white">Home</Link><ChevronRight className="h-3 w-3" />
            <Link href="/categories" className="hover:text-white">Categories</Link><ChevronRight className="h-3 w-3" />
            <span className="text-white">{cat.name}</span>
          </div>
          <h1 className="font-display mt-3 text-4xl font-black md:text-5xl">{cat.name}</h1>
          {cat.description && <p className="mt-3 max-w-2xl text-white/70">{cat.description}</p>}
          <div className="mt-6 flex flex-wrap gap-3">
            <WhatsAppButton label={`Get ${cat.name} Quote`} message={categoryInquiryMessage(cat.name)} />
            <Link href="/products" className="inline-flex items-center gap-2 rounded-xl border border-white/20 px-6 py-3 text-sm font-bold hover:bg-white/10">All Products</Link>
          </div>
        </div>
      </section>
      {cat.featuredVideo && (
        <section className="border-b bg-black py-8">
          <div className="bp-container max-w-3xl">
            <p className="mb-3 flex items-center gap-2 text-sm font-bold text-white"><Play className="h-4 w-4 text-orange-500" /> Featured {cat.name} Video</p>
            <video controls playsInline preload="metadata" poster={cat.image || undefined} className="aspect-video w-full rounded-2xl"><source src={cat.featuredVideo} type="video/mp4" /></video>
          </div>
        </section>
      )}
      <section className="py-12">
        <div className="bp-container">
          <p className="text-sm text-[#6b6560]"><strong>{items.length}</strong> products in {cat.name}</p>
          <div className="mt-6 grid gap-5 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
            {items.map((p: any, i: number) => (
              <Reveal key={p.id} delay={(i % 4) as 0 | 1 | 2 | 3}><ProductCard p={p} categoryName={cat.name} /></Reveal>
            ))}
          </div>
          {!items.length && (
            <div className="mt-8 rounded-2xl border border-dashed p-10 text-center text-sm text-[#6b6560]">
              Products in this category are being added. <a className="font-bold text-orange-700" target="_blank" rel="noopener" href={`https://wa.me/923152850818?text=${encodeURIComponent(categoryInquiryMessage(cat.name))}`}>Ask on WhatsApp →</a>
            </div>
          )}
        </div>
      </section>
    </div>
  );
}
