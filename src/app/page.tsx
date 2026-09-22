import Link from "next/link";
import { ArrowRight, Play, ShieldCheck, Truck, Factory, Phone, MessageCircle, CheckCircle2, MapPin, Award, Boxes } from "lucide-react";
import { db } from "@/db";
import { products, productCategories, videos, projects } from "@/db/schema";
import { desc, eq } from "drizzle-orm";
import { SITE, whatsappLink, categoryInquiryMessage, productInquiryMessage } from "@/lib/site";
import { Reveal, SectionHead, ProductCard, VideoCard, WhatsAppButton } from "@/components/ui";
import { IMG, VID, PRODUCT_CATEGORIES_SEED } from "@/db/seed-data";

export const dynamic = "force-dynamic";
export const revalidate = 60;

async function getData() {
  try {
    const [cats, prods, vids, projs] = await Promise.all([
      db.select().from(productCategories).limit(24),
      db.select().from(products).orderBy(desc(products.featured), desc(products.id)).limit(8),
      db.select().from(videos).orderBy(desc(videos.featured), desc(videos.id)).limit(6),
      db.select().from(projects).limit(6),
    ]);
    return { cats, prods, vids, projs };
  } catch {
    return { cats: [], prods: [], vids: [], projs: [] };
  }
}

export default async function HomePage() {
  const { cats, prods, vids, projs } = await getData();
  const categories = cats.length ? cats : PRODUCT_CATEGORIES_SEED.map((c, i) => ({ id: i + 1, ...c, banner: null, featuredVideo: null, whatsappMessage: null, createdAt: null }));
  const catName = (id: number | null) => categories.find((c: any) => c.id === id)?.name || "";

  return (
    <>
      {/* ============ HERO ============ */}
      <section className="relative overflow-hidden bg-[#141210] text-white">
        <div className="absolute inset-0">
          {/* eslint-disable-next-line @next/next/no-img-element */}
          <img src={IMG.brickMason} alt="Bricklayers building a wall" className="h-full w-full object-cover opacity-30" />
          <div className="absolute inset-0 bg-gradient-to-r from-[#141210] via-[#141210]/85 to-[#141210]/40" />
          <div className="brick-lines absolute inset-0 opacity-40" />
        </div>
        <div className="relative bp-container grid items-center gap-10 py-16 md:py-24 lg:grid-cols-[1.05fr_.95fr]">
          <div>
            <Reveal>
              <p className="inline-flex items-center gap-2 rounded-full border border-orange-500/40 bg-orange-600/15 px-4 py-1.5 text-xs font-bold uppercase tracking-widest text-orange-300">
                <Factory className="h-3.5 w-3.5" /> Masha Allah • Fine Bricks • SS7
              </p>
            </Reveal>
            <Reveal delay={1}>
              <h1 className="font-display mt-5 text-4xl font-black leading-[1.05] md:text-6xl">
                Building Strength.<br />
                <span className="text-orange-500">Delivering Quality.</span><br />
                Shaping Tomorrow.
              </h1>
            </Reveal>
            <Reveal delay={2}>
              <p className="mt-5 max-w-xl text-base leading-relaxed text-white/75 md:text-lg">
                Premium bricks and reliable construction materials for homes, commercial developments, and large-scale building projects.
              </p>
            </Reveal>
            <Reveal delay={3}>
              <div className="mt-7 flex flex-wrap gap-3">
                <Link href="/products" className="btn-brick inline-flex items-center gap-2 rounded-xl px-6 py-3.5 text-sm font-bold text-white">
                  Explore Products <ArrowRight className="h-4 w-4" />
                </Link>
                <Link href="/contact" className="inline-flex items-center gap-2 rounded-xl border border-white/20 bg-white/5 px-6 py-3.5 text-sm font-bold hover:bg-white/10">
                  Request a Quote
                </Link>
                <a href={SITE.whatsapp} target="_blank" rel="noopener" className="btn-whatsapp inline-flex items-center gap-2 rounded-xl px-6 py-3.5 text-sm font-bold text-white">
                  <MessageCircle className="h-4 w-4" /> WhatsApp Us
                </a>
              </div>
            </Reveal>
            <Reveal delay={3}>
              <div className="mt-8 flex flex-wrap gap-x-8 gap-y-3 text-sm text-white/70">
                <span className="inline-flex items-center gap-2"><ShieldCheck className="h-4 w-4 text-emerald-400" /> Quality-focused supply</span>
                <span className="inline-flex items-center gap-2"><Truck className="h-4 w-4 text-emerald-400" /> Reliable delivery</span>
                <span className="inline-flex items-center gap-2"><Factory className="h-4 w-4 text-emerald-400" /> Multiple production locations</span>
              </div>
            </Reveal>
          </div>

          {/* Hero video + SS7 animation */}
          <div className="relative">
            <Reveal delay={2}>
              <div className="hero-video-frame relative overflow-hidden rounded-3xl border border-white/10">
                <video autoPlay muted loop playsInline preload="metadata" poster={VID.heroPoster} className="aspect-video w-full object-cover" aria-label="BrickPoint brick construction video">
                  <source src={VID.hero} type="video/mp4" />
                </video>
                <div className="absolute inset-0 bg-gradient-to-t from-black/60 via-transparent to-transparent" />
                <div className="absolute bottom-4 left-4 right-4 flex items-center justify-between">
                  <div>
                    <p className="text-[11px] font-black uppercase tracking-widest text-orange-300">SS7 Bricks • In Action</p>
                    <p className="font-display text-lg font-extrabold">See the strength behind every brick</p>
                  </div>
                  <Link href="/videos" className="grid h-12 w-12 shrink-0 place-items-center rounded-full bg-orange-600 shadow-xl hover:bg-orange-500" aria-label="Watch all videos">
                    <Play className="ml-0.5 h-5 w-5" />
                  </Link>
                </div>
              </div>
            </Reveal>
            {/* SS7 brick animation card */}
            <div className="absolute -bottom-8 -left-4 hidden md:block lg:-left-10">
              <div className="ss7-brick-loop rounded-2xl border border-white/10 bg-[#1c1a17]/95 p-4 shadow-2xl backdrop-blur">
                <div className="ss7-brick flex items-center gap-3">
                  {/* eslint-disable-next-line @next/next/no-img-element */}
                  <img src={IMG.redStack} alt="SS7 brick close-up" className="h-16 w-24 rounded-xl object-cover shadow-lg" style={{ aspectRatio: "3/2" }} />
                  <div>
                    <p className="flex items-center gap-1 text-[11px] font-black uppercase tracking-widest text-amber-400"><Award className="h-3 w-3" /> Flagship</p>
                    <p className="font-display font-black">SS7 Bricks</p>
                    <Link href="/ss7-bricks" className="text-xs font-bold text-orange-400 hover:text-orange-300">View SS7 range →</Link>
                  </div>
                </div>
              </div>
            </div>
            <div className="absolute -top-4 -right-2 hidden rounded-2xl border border-white/10 bg-white/10 px-4 py-3 backdrop-blur md:block">
              <p className="font-display text-2xl font-black text-white">3<span className="text-orange-500">+</span></p>
              <p className="text-[11px] font-semibold uppercase tracking-wider text-white/70">Production units</p>
            </div>
          </div>
        </div>
        {/* marquee */}
        <div className="relative border-t border-white/10 bg-black/30 py-3">
          <div className="overflow-hidden">
            <div className="marquee-track text-xs font-bold uppercase tracking-[0.2em] text-white/50">
              {[0, 1].map((k) => (
                <div key={k} className="flex shrink-0 gap-10 pr-10">
                  {["SS7 Bricks", "Cement", "Bajri / Crush", "Sand / Rait", "Steel", "Pipes", "Chemicals", "Cables", "Paints", "Lights"].map((t) => (
                    <span key={t} className="flex items-center gap-3"><span className="h-1.5 w-1.5 rounded-full bg-orange-500" />{t}</span>
                  ))}
                </div>
              ))}
            </div>
          </div>
        </div>
      </section>

      {/* ============ TRUST / INTRO ============ */}
      <section className="py-16 md:py-20">
        <div className="bp-container grid items-center gap-10 lg:grid-cols-2">
          <Reveal>
            <div className="img-zoom relative overflow-hidden rounded-3xl">
              {/* eslint-disable-next-line @next/next/no-img-element */}
              <img src={IMG.kiln} alt="Brick kiln production" className="aspect-[4/3] w-full object-cover" loading="lazy" />
              <div className="absolute bottom-4 left-4 right-4 flex gap-3">
                <div className="flex-1 rounded-2xl bg-white/95 p-4 shadow-xl backdrop-blur">
                  <p className="font-display text-xl font-black text-orange-700">Trusted Supply</p>
                  <p className="text-xs text-[#6b6560]">Consistent quality for every order size</p>
                </div>
                <div className="flex-1 rounded-2xl bg-[#141210]/95 p-4 text-white shadow-xl backdrop-blur">
                  <p className="font-display text-xl font-black">Bulk Ready</p>
                  <p className="text-xs text-white/60">Contractors & companies welcome</p>
                </div>
              </div>
            </div>
          </Reveal>
          <div>
            <Reveal><SectionHead align="left" eyebrow="Why BrickPoint" title="A construction-materials partner you can build on" text="BrickPoint brings together trusted brick manufacturing units and a complete construction-materials range — so contractors, builders and developers can source with confidence." /></Reveal>
            <Reveal delay={1}>
              <ul className="mt-6 space-y-3">
                {["Quality-focused brick manufacturing at multiple bhatta locations", "Complete materials range — from cement and steel to finishes", "Project-based quotations with delivery coordination", "Direct WhatsApp ordering with fast response"].map((t) => (
                  <li key={t} className="flex items-start gap-3 rounded-2xl border border-black/5 bg-white p-4 text-sm font-medium shadow-sm">
                    <CheckCircle2 className="mt-0.5 h-5 w-5 shrink-0 text-emerald-600" /> {t}
                  </li>
                ))}
              </ul>
            </Reveal>
            <Reveal delay={2}>
              <div className="mt-6 flex flex-wrap gap-3">
                <Link href="/about" className="inline-flex items-center gap-2 rounded-xl bg-[#141210] px-6 py-3 text-sm font-bold text-white hover:bg-black">About BrickPoint <ArrowRight className="h-4 w-4" /></Link>
                <Link href="/locations" className="inline-flex items-center gap-2 rounded-xl border border-black/10 bg-white px-6 py-3 text-sm font-bold hover:border-orange-600 hover:text-orange-700"><MapPin className="h-4 w-4" /> Our Locations</Link>
              </div>
            </Reveal>
          </div>
        </div>
      </section>

      {/* ============ CATEGORIES ============ */}
      <section className="bg-[#141210] py-16 text-white md:py-20">
        <div className="bp-container">
          <Reveal><SectionHead light eyebrow="Product Categories" title="One supplier for your complete material list" text="From flagship SS7 bricks to cement, aggregates, steel, pipes, electricals and finishes." /></Reveal>
          <div className="mt-10 grid grid-cols-2 gap-4 md:grid-cols-3 lg:grid-cols-4">
            {categories.slice(0, 12).map((c: any, i: number) => (
              <Reveal key={c.slug} delay={(i % 4) as 0 | 1 | 2 | 3}>
                <Link href={c.slug === "ss7-bricks" ? "/ss7-bricks" : `/categories/${c.slug}`} className="card-hover group block overflow-hidden rounded-2xl border border-white/10 bg-[#1c1a17]">
                  <div className="img-zoom relative aspect-[16/10] overflow-hidden">
                    {/* eslint-disable-next-line @next/next/no-img-element */}
                    <img src={c.image || IMG.stacked} alt={c.name} loading="lazy" className="h-full w-full object-cover" />
                    <div className="absolute inset-0 bg-gradient-to-t from-black/70 to-transparent" />
                    <p className="absolute bottom-3 left-4 font-display font-extrabold">{c.name}</p>
                  </div>
                  <div className="flex items-center justify-between p-4">
                    <span className="line-clamp-2 text-xs text-white/60">{c.description}</span>
                    <span className="grid h-9 w-9 shrink-0 place-items-center rounded-xl bg-orange-600 transition group-hover:bg-orange-500"><ArrowRight className="h-4 w-4" /></span>
                  </div>
                </Link>
              </Reveal>
            ))}
          </div>
          <Reveal>
            <div className="mt-8 text-center">
              <Link href="/categories" className="inline-flex items-center gap-2 rounded-xl border border-white/20 px-6 py-3 text-sm font-bold hover:bg-white/10">View All Categories <ArrowRight className="h-4 w-4" /></Link>
            </div>
          </Reveal>
        </div>
      </section>

      {/* ============ FEATURED SS7 ============ */}
      <section className="relative overflow-hidden py-16 md:py-24">
        <div className="absolute inset-0 bg-gradient-to-br from-orange-50 via-[#faf8f5] to-stone-200" />
        <div className="relative bp-container grid items-center gap-10 lg:grid-cols-2">
          <div>
            <Reveal><SectionHead align="left" eyebrow="Flagship Product" title="The Strength Behind Every Structure" text="SS7 Bricks — our signature range engineered for strength, shape and lasting performance. Ask for specifications, availability and project pricing on WhatsApp." /></Reveal>
            <Reveal delay={1}>
              <div className="mt-6 grid grid-cols-2 gap-3">
                {[["Size", "Standard chamber size (confirm on quote)"], ["Type", "Burnt-clay SS7"], ["Usage", "Homes • Commercial • Boundary"], ["Availability", "Bulk & retail orders"]].map(([k, v]) => (
                  <div key={k} className="rounded-2xl border border-black/5 bg-white p-4 shadow-sm">
                    <p className="text-[11px] font-black uppercase tracking-widest text-orange-700">{k}</p>
                    <p className="mt-1 text-sm font-semibold">{v}</p>
                  </div>
                ))}
              </div>
            </Reveal>
            <Reveal delay={2}>
              <div className="mt-6 flex flex-wrap gap-3">
                <WhatsAppButton label="Request SS7 Quote" message={categoryInquiryMessage("SS7 Bricks")} />
                <Link href="/ss7-bricks" className="inline-flex items-center gap-2 rounded-xl bg-[#141210] px-6 py-3 text-sm font-bold text-white hover:bg-black">View SS7 Page <ArrowRight className="h-4 w-4" /></Link>
              </div>
            </Reveal>
          </div>
          <Reveal delay={1}>
            <div className="relative">
              <div className="img-zoom overflow-hidden rounded-3xl shadow-2xl">
                {/* eslint-disable-next-line @next/next/no-img-element */}
                <img src={IMG.redStack} alt="SS7 red bricks stacked" className="aspect-[4/3] w-full object-cover" loading="lazy" />
              </div>
              <div className="absolute -bottom-6 left-4 right-4 grid grid-cols-3 gap-3">
                {[IMG.stacked, IMG.pile, IMG.worker].map((s) => (
                  // eslint-disable-next-line @next/next/no-img-element
                  <img key={s} src={s} alt="SS7 brick gallery" loading="lazy" className="aspect-video rounded-2xl border-4 border-white object-cover shadow-xl" />
                ))}
              </div>
            </div>
          </Reveal>
        </div>
      </section>

      {/* ============ FEATURED PRODUCTS ============ */}
      <section className="py-16 md:py-20">
        <div className="bp-container">
          <Reveal><SectionHead eyebrow="Featured Products" title="Materials contractors ask for by name" text="Live from the product catalogue — prices, units and WhatsApp ordering on every card." /></Reveal>
          <div className="mt-10 grid gap-5 sm:grid-cols-2 lg:grid-cols-4">
            {prods.length ? prods.map((p: any, i: number) => (
              <Reveal key={p.id} delay={(i % 4) as 0 | 1 | 2 | 3}><ProductCard p={p} categoryName={catName(p.categoryId)} /></Reveal>
            )) : (
              [1, 2, 3, 4].map((i) => (
                <div key={i} className="rounded-2xl border border-dashed border-black/15 bg-white/60 p-8 text-center text-sm text-[#6b6560]">
                  <Boxes className="mx-auto h-8 w-8 text-orange-600" />
                  <p className="mt-3 font-bold">Products loading from catalogue…</p>
                  <p className="mt-1">Visit /products to seed and browse.</p>
                </div>
              ))
            )}
          </div>
          <div className="mt-8 text-center">
            <Link href="/products" className="btn-brick inline-flex items-center gap-2 rounded-xl px-6 py-3 text-sm font-bold text-white">Browse All Products <ArrowRight className="h-4 w-4" /></Link>
          </div>
        </div>
      </section>

      {/* ============ VIDEO SECTIONS ============ */}
      <section className="bg-[#1c1a17] py-16 text-white md:py-20">
        <div className="bp-container">
          <div className="grid items-end justify-between gap-6 md:grid-cols-[1fr_auto]">
            <Reveal><SectionHead light align="left" eyebrow="Inside BrickPoint" title="See the Strength Behind Every Brick" text="Manufacturing, bhattas, quality checks, materials and project references — on video." /></Reveal>
            <Reveal delay={1}><Link href="/videos" className="inline-flex items-center gap-2 rounded-xl border border-white/20 px-6 py-3 text-sm font-bold hover:bg-white/10">View All Videos <ArrowRight className="h-4 w-4" /></Link></Reveal>
          </div>
          <div className="mt-10 grid gap-5 lg:grid-cols-3">
            <Reveal className="lg:col-span-2">
              <div className="hero-video-frame relative h-full min-h-[300px] overflow-hidden rounded-3xl">
                <video controls playsInline preload="metadata" poster={VID.dronePoster} className="h-full min-h-[300px] w-full object-cover">
                  <source src={VID.drone} type="video/mp4" />
                </video>
                <span className="absolute left-4 top-4 rounded-full bg-orange-600 px-3 py-1 text-[11px] font-black uppercase tracking-wider">Featured</span>
              </div>
            </Reveal>
            <div className="space-y-5">
              <Reveal delay={1}>
                <div className="overflow-hidden rounded-3xl border border-white/10 bg-[#141210]">
                  <div className="relative aspect-video">
                    <video playsInline muted loop autoPlay preload="metadata" poster={VID.sitePoster} className="h-full w-full object-cover">
                      <source src={VID.site} type="video/mp4" />
                    </video>
                    <span className="absolute bottom-3 left-3 rounded-lg bg-black/70 px-2 py-1 text-[11px] font-bold">From the Bhatta to Your Building</span>
                  </div>
                  <div className="p-4 text-sm text-white/70">Brick preparation, firing, stacking, loading and quality — the journey of every batch.</div>
                </div>
              </Reveal>
              <Reveal delay={2}>
                <div className="overflow-hidden rounded-3xl border border-white/10 bg-[#141210]">
                  <div className="relative aspect-video">
                    <video playsInline muted loop autoPlay preload="metadata" poster={VID.aerialPoster} className="h-full w-full object-cover">
                      <source src={VID.aerial} type="video/mp4" />
                    </video>
                    <span className="absolute bottom-3 left-3 rounded-lg bg-black/70 px-2 py-1 text-[11px] font-bold">Materials That Become Landmarks</span>
                  </div>
                  <div className="p-4 text-sm text-white/70">Illustrative construction references from housing developments and building work.</div>
                </div>
              </Reveal>
            </div>
          </div>
          {vids.length > 0 && (
            <div className="mt-8 grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
              {vids.slice(0, 3).map((v: any) => (
                <VideoCard key={v.id} v={v} categoryName="" />
              ))}
            </div>
          )}
        </div>
      </section>

      {/* ============ PROJECTS PREVIEW ============ */}
      <section className="py-16 md:py-20">
        <div className="bp-container">
          <Reveal><SectionHead eyebrow="Project References" title="Materials that become landmarks" text="Illustrative construction references from Lahore housing societies and building work." /></Reveal>
          <div className="mt-10 grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
            {(projs.length ? projs : [
              { title: "DHA Lahore — Villa Reference", location: "DHA Lahore", featuredImage: IMG.villa1, category: "Residential", slug: "dha-lahore" },
              { title: "Bahria Town — Housing Reference", location: "Bahria Town Lahore", featuredImage: IMG.villa2, category: "Residential", slug: "bahria-town" },
              { title: "Lake City — Development Reference", location: "Lake City Lahore", featuredImage: IMG.apt, category: "Development", slug: "lake-city" },
            ]).slice(0, 3).map((pr: any, i: number) => (
              <Reveal key={pr.slug || i} delay={(i % 3) as 0 | 1 | 2}>
                <Link href="/projects" className="card-hover group block overflow-hidden rounded-2xl border border-black/5 bg-white">
                  <div className="img-zoom relative aspect-[16/10] overflow-hidden">
                    {/* eslint-disable-next-line @next/next/no-img-element */}
                    <img src={pr.featuredImage} alt={pr.title} loading="lazy" className="h-full w-full object-cover" />
                    <span className="absolute left-3 top-3 rounded-full bg-black/70 px-3 py-1 text-[11px] font-bold text-white">Illustrative construction reference</span>
                  </div>
                  <div className="p-5">
                    <p className="text-[11px] font-black uppercase tracking-widest text-orange-700">{pr.location}</p>
                    <h3 className="font-display mt-1 font-extrabold group-hover:text-orange-700">{pr.title}</h3>
                  </div>
                </Link>
              </Reveal>
            ))}
          </div>
        </div>
      </section>

      {/* ============ AUDIENCES ============ */}
      <section className="bg-[#f6f1ea] py-16 md:py-20">
        <div className="bp-container">
          <Reveal><SectionHead eyebrow="Who We Serve" title="Built for the way you build" text="Bulk supply, project quotations and coordinated materials — for every scale of builder." /></Reveal>
          <div className="mt-10 grid gap-5 md:grid-cols-3">
            {[
              { t: "For Contractors", d: "Bulk material supply, project-based quotations and delivery coordination.", h: "/for-contractors", img: IMG.site },
              { t: "For Builders", d: "Consistent quality across every batch, with multi-category sourcing.", h: "/for-builders", img: IMG.bricklayer },
              { t: "For Construction Companies", d: "Large-scale supply, documentation and dedicated contact.", h: "/for-companies", img: IMG.apt },
            ].map((a, i) => (
              <Reveal key={a.t} delay={(i % 3) as 0 | 1 | 2}>
                <Link href={a.h} className="card-hover group block overflow-hidden rounded-3xl bg-[#141210] text-white">
                  <div className="img-zoom relative aspect-[16/9] overflow-hidden">
                    {/* eslint-disable-next-line @next/next/no-img-element */}
                    <img src={a.img} alt={a.t} loading="lazy" className="h-full w-full object-cover opacity-80" />
                    <div className="absolute inset-0 bg-gradient-to-t from-[#141210] to-transparent" />
                  </div>
                  <div className="p-6">
                    <h3 className="font-display text-xl font-black">{a.t}</h3>
                    <p className="mt-2 text-sm text-white/65">{a.d}</p>
                    <span className="mt-4 inline-flex items-center gap-2 text-sm font-bold text-orange-400">Learn more <ArrowRight className="h-4 w-4" /></span>
                  </div>
                </Link>
              </Reveal>
            ))}
          </div>
        </div>
      </section>

      {/* ============ CTA ============ */}
      <section className="relative overflow-hidden bg-[#141210] py-16 text-white md:py-20">
        <div className="absolute inset-0">
          {/* eslint-disable-next-line @next/next/no-img-element */}
          <img src={IMG.bricklayer} alt="" className="h-full w-full object-cover opacity-20" loading="lazy" />
          <div className="absolute inset-0 bg-gradient-to-r from-[#141210] to-transparent" />
        </div>
        <div className="relative bp-container grid items-center gap-8 lg:grid-cols-[1fr_auto]">
          <Reveal>
            <p className="text-xs font-black uppercase tracking-[0.22em] text-orange-400">Get a fast quotation</p>
            <h2 className="font-display mt-3 text-3xl font-black md:text-5xl">Send your material list.<br />We handle the rest.</h2>
            <p className="mt-4 flex items-center gap-2 text-white/70"><Phone className="h-4 w-4 text-orange-400" /> {SITE.phoneDisplay} • CEO: {SITE.ceo} • Sales: {SITE.salesManager}</p>
          </Reveal>
          <Reveal delay={1}>
            <div className="flex flex-col gap-3 sm:flex-row lg:flex-col">
              <a href={whatsappLink("Assalam-o-Alaikum BrickPoint,\n\nPlease share a quotation for my construction materials.\n\nThank you.")} target="_blank" rel="noopener" className="btn-whatsapp inline-flex items-center justify-center gap-2 rounded-xl px-8 py-4 font-bold text-white">
                <MessageCircle className="h-5 w-5" /> WhatsApp Your List
              </a>
              <Link href="/contact" className="btn-brick inline-flex items-center justify-center gap-2 rounded-xl px-8 py-4 font-bold text-white">Request Quote Form</Link>
            </div>
          </Reveal>
        </div>
      </section>
    </>
  );
}
