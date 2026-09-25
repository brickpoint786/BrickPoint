import Link from "next/link";
import { notFound } from "next/navigation";
import { db } from "@/db";
import { products, productCategories } from "@/db/schema";
import { eq, ne, and } from "drizzle-orm";
import { MessageCircle, Phone, ChevronRight, CheckCircle2, Share2, FileText, Play } from "lucide-react";
import { SITE, whatsappLink, productInquiryMessage } from "@/lib/site";
import { ProductCard, Reveal } from "@/components/ui";

export const dynamic = "force-dynamic";

export async function generateMetadata({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  try {
    const [p] = await db.select().from(products).where(eq(products.slug, slug)).limit(1);
    return { title: p ? p.name : "Product" };
  } catch { return { title: "Product" }; }
}

export default async function ProductDetail({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  let p: any = null;
  let cat: any = null;
  let related: any[] = [];
  try {
    const [row] = await db.select().from(products).where(eq(products.slug, slug)).limit(1);
    if (!row) return notFound();
    p = row;
    if (p.categoryId) {
      const [c] = await db.select().from(productCategories).where(eq(productCategories.id, p.categoryId)).limit(1);
      cat = c || null;
      related = await db.select().from(products).where(and(eq(products.categoryId, p.categoryId), ne(products.id, p.id))).limit(4);
    }
    if (!related.length) related = await db.select().from(products).where(ne(products.id, p.id)).limit(4);
  } catch { return notFound(); }

  const msg = productInquiryMessage({ product: p.name, category: cat?.name, price: p.price ? `${p.price} ${p.priceLabel || ""}`.trim() : null, unit: p.unit });
  const gallery: string[] = [p.featuredImage, ...(p.gallery || [])].filter(Boolean);

  return (
    <div>
      <div className="border-b bg-white">
        <div className="bp-container flex items-center gap-2 py-4 text-xs text-[#6b6560]">
          <Link href="/" className="hover:text-orange-700">Home</Link><ChevronRight className="h-3 w-3" />
          <Link href="/products" className="hover:text-orange-700">Products</Link><ChevronRight className="h-3 w-3" />
          {cat && (<><Link href={`/products?category=${cat.slug}`} className="hover:text-orange-700">{cat.name}</Link><ChevronRight className="h-3 w-3" /></>)}
          <span className="font-semibold text-[#141210]">{p.name}</span>
        </div>
      </div>
      <section className="py-10">
        <div className="bp-container grid gap-10 lg:grid-cols-2">
          <div>
            <Reveal>
              <div className="overflow-hidden rounded-3xl border bg-white shadow-sm">
                {gallery[0] ? (
                  // eslint-disable-next-line @next/next/no-img-element
                  <img src={gallery[0]} alt={p.name} className="aspect-[4/3] w-full object-cover" />
                ) : <div className="grid aspect-[4/3] place-items-center bg-stone-200 text-5xl">🧱</div>}
              </div>
            </Reveal>
            {gallery.length > 1 && (
              <div className="mt-4 grid grid-cols-4 gap-3">
                {gallery.slice(1, 5).map((g, i) => (
                  // eslint-disable-next-line @next/next/no-img-element
                  <img key={i} src={g} alt={`${p.name} ${i + 2}`} loading="lazy" className="aspect-square rounded-2xl border object-cover" />
                ))}
              </div>
            )}
            {p.videoUrl && (
              <div className="mt-4 overflow-hidden rounded-3xl border bg-black">
                <div className="flex items-center gap-2 bg-[#141210] px-5 py-3 text-sm font-bold text-white"><Play className="h-4 w-4 text-orange-500" /> Product Video</div>
                {p.videoType === "youtube" || p.videoType === "vimeo" ? (
                  <iframe src={p.videoUrl} title={`${p.name} video`} className="aspect-video w-full" loading="lazy" allow="accelerometer; autoplay; encrypted-media; picture-in-picture" allowFullScreen />
                ) : (
                  <video controls playsInline preload="metadata" poster={p.featuredImage || undefined} className="aspect-video w-full"><source src={p.videoUrl} type="video/mp4" /></video>
                )}
              </div>
            )}
          </div>
          <div>
            {cat && <p className="text-xs font-black uppercase tracking-[0.22em] text-orange-700">{cat.name}</p>}
            <h1 className="font-display mt-2 text-3xl font-black md:text-4xl">{p.name}</h1>
            {p.shortDescription && <p className="mt-3 text-[#3d3833]">{p.shortDescription}</p>}
            <div className="mt-5 flex flex-wrap items-center gap-3">
              {p.price ? (
                <p className="font-display text-3xl font-black">{p.price} {p.unit && <span className="text-base font-semibold text-[#6b6560]">/ {p.unit}</span>}</p>
              ) : <p className="font-display text-2xl font-black text-orange-700">Price on request</p>}
              {p.availability && <span className={`rounded-full px-3 py-1 text-xs font-bold ${p.availability === "In Stock" ? "bg-emerald-100 text-emerald-800" : "bg-stone-200 text-stone-700"}`}>{p.availability}</span>}
              {p.badge && <span className="rounded-full bg-orange-600 px-3 py-1 text-xs font-black uppercase text-white">{p.badge}</span>}
            </div>
            {p.priceLabel && <p className="mt-1 text-sm text-[#6b6560]">{p.priceLabel}</p>}
            {p.sku && <p className="mt-2 text-xs text-[#6b6560]">SKU / Ref: <strong>{p.sku}</strong></p>}
            <div className="mt-6 grid gap-2 sm:grid-cols-3">
              <a href={whatsappLink(msg)} target="_blank" rel="noopener" className="btn-whatsapp inline-flex items-center justify-center gap-2 rounded-xl px-4 py-3.5 text-sm font-bold text-white"><MessageCircle className="h-4 w-4" /> WhatsApp Inquiry</a>
              <a href={`tel:${SITE.phoneIntl}`} className="inline-flex items-center justify-center gap-2 rounded-xl bg-[#141210] px-4 py-3.5 text-sm font-bold text-white hover:bg-black"><Phone className="h-4 w-4" /> {SITE.phoneDisplay}</a>
              <Link href={`/contact?product=${p.slug}`} className="btn-brick inline-flex items-center justify-center gap-2 rounded-xl px-4 py-3.5 text-sm font-bold text-white"><FileText className="h-4 w-4" /> Request Quote</Link>
            </div>
            {p.features?.length > 0 && (
              <div className="mt-6 rounded-2xl border bg-white p-5">
                <h3 className="font-display font-extrabold">Key Features</h3>
                <ul className="mt-3 space-y-2">
                  {p.features.map((f: string) => (
                    <li key={f} className="flex items-start gap-2 text-sm"><CheckCircle2 className="mt-0.5 h-4 w-4 shrink-0 text-emerald-600" /> {f}</li>
                  ))}
                </ul>
              </div>
            )}
            {p.specifications?.length > 0 && (
              <div className="mt-4 overflow-hidden rounded-2xl border bg-white">
                <h3 className="font-display bg-[#141210] px-5 py-3 text-sm font-extrabold text-white">Specifications</h3>
                <dl>
                  {p.specifications.map((s: any) => (
                    <div key={s.label} className="grid grid-cols-[140px_1fr] gap-2 border-b px-5 py-3 text-sm last:border-0">
                      <dt className="font-bold text-[#6b6560]">{s.label}</dt><dd className="font-medium">{s.value}</dd>
                    </div>
                  ))}
                </dl>
              </div>
            )}
            {p.fullDescription && (
              <div className="prose-bp mt-6 rounded-2xl border bg-white p-6">
                <h3 className="font-display mb-2 font-extrabold">Product Description</h3>
                <p>{p.fullDescription}</p>
              </div>
            )}
            <div className="mt-4 flex items-center gap-2 text-xs text-[#6b6560]">
              <Share2 className="h-4 w-4" /> Share:
              <a className="font-bold hover:text-orange-700" target="_blank" rel="noopener" href={`https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(`/products/${p.slug}`)}`}>Facebook</a>•
              <a className="font-bold hover:text-orange-700" target="_blank" rel="noopener" href={`https://wa.me/?text=${encodeURIComponent(p.name)}`}>WhatsApp</a>•
              <a className="font-bold hover:text-orange-700" target="_blank" rel="noopener" href={`https://x.com/intent/tweet?text=${encodeURIComponent(p.name)}`}>X</a>
            </div>
          </div>
        </div>
      </section>
      {related.length > 0 && (
        <section className="border-t bg-white py-12">
          <div className="bp-container">
            <h2 className="font-display text-2xl font-black">Related Products</h2>
            <div className="mt-6 grid gap-5 sm:grid-cols-2 lg:grid-cols-4">
              {related.map((r: any) => (<ProductCard key={r.id} p={r} categoryName={cat?.name} />))}
            </div>
          </div>
        </section>
      )}
    </div>
  );
}
