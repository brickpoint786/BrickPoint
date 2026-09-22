import Link from "next/link";
import { Award, CheckCircle2, Play, ArrowRight, Ruler, Palette, Layers, Truck } from "lucide-react";
import { db } from "@/db";
import { products, productCategories, videos } from "@/db/schema";
import { eq } from "drizzle-orm";
import { Reveal, SectionHead, ProductCard, WhatsAppButton } from "@/components/ui";
import { IMG, VID } from "@/db/seed-data";
import { categoryInquiryMessage } from "@/lib/site";

export const dynamic = "force-dynamic";
export const metadata = { title: "SS7 Bricks" };

export default async function SS7Page() {
  let items: any[] = [];
  let vids: any[] = [];
  try {
    const [cat] = await db.select().from(productCategories).where(eq(productCategories.slug, "ss7-bricks")).limit(1);
    if (cat) items = await db.select().from(products).where(eq(products.categoryId, cat.id));
    vids = await db.select().from(videos).limit(3);
  } catch {}

  return (
    <div>
      <section className="relative overflow-hidden bg-[#141210] py-16 text-white md:py-24">
        {/* eslint-disable-next-line @next/next/no-img-element */}
        <img src={IMG.redStack} alt="SS7 bricks" className="absolute inset-0 h-full w-full object-cover opacity-25" />
        <div className="absolute inset-0 bg-gradient-to-r from-[#141210] via-[#141210]/90 to-[#141210]/50" />
        <div className="relative bp-container grid items-center gap-10 lg:grid-cols-2">
          <div>
            <Reveal>
              <p className="inline-flex items-center gap-2 rounded-full border border-amber-400/40 bg-amber-400/10 px-4 py-1.5 text-xs font-black uppercase tracking-widest text-amber-300"><Award className="h-3.5 w-3.5" /> Flagship Range</p>
              <h1 className="font-display mt-4 text-4xl font-black md:text-6xl">SS7 <span className="text-orange-500">Bricks</span></h1>
              <p className="mt-4 max-w-xl text-white/75">Our signature high-strength brick — consistent firing, sharp edges and dependable supply for homes, commercial work and boundary structures.</p>
              <div className="mt-7 flex flex-wrap gap-3">
                <WhatsAppButton label="Request SS7 Quotation" message={categoryInquiryMessage("SS7 Bricks")} size="lg" />
                <Link href="/products" className="inline-flex items-center gap-2 rounded-xl border border-white/20 px-6 py-4 text-sm font-bold hover:bg-white/10">Browse Products</Link>
              </div>
            </Reveal>
          </div>
          <Reveal delay={1}>
            <div className="ss7-brick-loop relative mx-auto w-fit">
              <div className="ss7-brick overflow-hidden rounded-3xl border border-white/15 shadow-2xl">
                {/* eslint-disable-next-line @next/next/no-img-element */}
                <img src={IMG.redStack} alt="SS7 brick close-up, premium red bricks" className="aspect-[4/3] w-full max-w-lg object-cover" style={{ aspectRatio: "4/3" }} />
              </div>
              <div className="absolute -bottom-5 left-1/2 grid w-[92%] -translate-x-1/2 grid-cols-3 gap-2">
                {["High Strength", "Sharp Edges", "Even Firing"].map((t) => (
                  <div key={t} className="rounded-xl bg-orange-600 px-2 py-2 text-center text-[11px] font-black uppercase tracking-wide text-white shadow-xl">{t}</div>
                ))}
              </div>
            </div>
          </Reveal>
        </div>
      </section>

      <section className="py-14">
        <div className="bp-container">
          <Reveal><SectionHead eyebrow="Editable Specifications" title="SS7 at a glance" text="Specification fields are editable from the product record — update size, colour, type, strength, usage, availability and delivery area any time." /></Reveal>
          <div className="mt-8 grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
            {[
              { icon: Ruler, k: "Size", v: "Standard chamber size — confirm current batch on quote" },
              { icon: Palette, k: "Colour", v: "Classic kiln-fired red with natural variation" },
              { icon: Layers, k: "Type & Strength", v: "Burnt-clay SS7 — high crushing strength grade" },
              { icon: Truck, k: "Usage & Delivery", v: "Homes • Commercial • Boundary — delivery on schedule" },
            ].map((s, i) => (
              <Reveal key={s.k} delay={(i % 4) as 0 | 1 | 2 | 3}>
                <div className="h-full rounded-3xl border bg-white p-6 shadow-sm">
                  <s.icon className="h-7 w-7 text-orange-600" />
                  <h3 className="font-display mt-3 font-extrabold">{s.k}</h3>
                  <p className="mt-2 text-sm text-[#6b6560]">{s.v}</p>
                </div>
              </Reveal>
            ))}
          </div>
          <Reveal>
            <div className="mt-6 rounded-2xl border border-amber-300 bg-amber-50 p-5 text-sm text-amber-900">
              <strong>Quality highlights:</strong> uniform size & sharp edges • consistent kiln firing • sorted batches • bulk order support. For lab-tested strength figures of the current batch, message us on WhatsApp.
            </div>
          </Reveal>
        </div>
      </section>

      <section className="bg-[#1c1a17] py-14 text-white">
        <div className="bp-container grid items-center gap-8 lg:grid-cols-2">
          <Reveal>
            <p className="text-xs font-black uppercase tracking-[0.22em] text-orange-400">Product Video</p>
            <h2 className="font-display mt-2 text-3xl font-black">Watch SS7 bricks up close</h2>
            <ul className="mt-5 space-y-2.5 text-sm text-white/75">
              {["Manufacturing walkthrough", "Quality & firing checks", "Usage on real sites"].map((t) => (
                <li key={t} className="flex items-center gap-2"><CheckCircle2 className="h-4 w-4 text-emerald-400" /> {t}</li>
              ))}
            </ul>
            <Link href="/videos" className="mt-6 inline-flex items-center gap-2 rounded-xl border border-white/20 px-6 py-3 text-sm font-bold hover:bg-white/10"><Play className="h-4 w-4" /> All Videos</Link>
          </Reveal>
          <Reveal delay={1}>
            <div className="hero-video-frame overflow-hidden rounded-3xl">
              <video controls playsInline preload="metadata" poster={VID.heroPoster} className="aspect-video w-full"><source src={VID.hero} type="video/mp4" /></video>
            </div>
          </Reveal>
        </div>
      </section>

      {items.length > 0 && (
        <section className="py-14">
          <div className="bp-container">
            <div className="flex items-end justify-between">
              <h2 className="font-display text-2xl font-black md:text-3xl">SS7 Products</h2>
              <Link href="/products?category=ss7-bricks" className="inline-flex items-center gap-1 text-sm font-bold text-orange-700">View all <ArrowRight className="h-4 w-4" /></Link>
            </div>
            <div className="mt-6 grid gap-5 sm:grid-cols-2 lg:grid-cols-4">
              {items.map((p: any) => (<ProductCard key={p.id} p={p} categoryName="SS7 Bricks" />))}
            </div>
          </div>
        </section>
      )}

      <section className="bg-[#f6f1ea] py-14">
        <div className="bp-container grid gap-4 rounded-3xl bg-[#141210] p-8 text-white md:grid-cols-[1fr_auto] md:items-center md:p-12">
          <div>
            <h2 className="font-display text-2xl font-black md:text-3xl">Need SS7 for your project?</h2>
            <p className="mt-2 text-white/70">Share quantity + site location for availability, delivery details and final quotation.</p>
          </div>
          <div className="flex flex-wrap gap-3">
            <WhatsAppButton label="WhatsApp SS7 Inquiry" message={categoryInquiryMessage("SS7 Bricks")} size="lg" />
            <Link href="/contact" className="btn-brick inline-flex items-center rounded-xl px-6 py-4 text-sm font-bold text-white">Request Quote Form</Link>
          </div>
        </div>
      </section>
    </div>
  );
}
