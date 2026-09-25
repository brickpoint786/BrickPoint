import Link from "next/link";
import { ArrowRight, Factory, ShieldCheck, Users, Target, Eye, Heart } from "lucide-react";
import { Reveal, SectionHead } from "@/components/ui";
import { SITE } from "@/lib/site";
import { IMG, VID } from "@/db/seed-data";

export const metadata = { title: "About Us" };

export default function AboutPage() {
  return (
    <div>
      <section className="relative overflow-hidden bg-[#141210] py-14 text-white md:py-20">
        {/* eslint-disable-next-line @next/next/no-img-element */}
        <img src={IMG.bricklayer} alt="" className="absolute inset-0 h-full w-full object-cover opacity-20" />
        <div className="absolute inset-0 bg-gradient-to-r from-[#141210] to-transparent" />
        <div className="relative bp-container">
          <p className="text-xs font-black uppercase tracking-[0.22em] text-orange-400">Our Story</p>
          <h1 className="font-display mt-2 max-w-2xl text-4xl font-black md:text-5xl">BrickPoint — strength you can build on</h1>
          <p className="mt-4 max-w-2xl text-white/70">A construction-materials supplier bringing together trusted brick manufacturing units and a complete building-materials range for contractors, builders, developers and individual customers.</p>
        </div>
      </section>

      <section className="py-14">
        <div className="bp-container grid items-center gap-10 lg:grid-cols-2">
          <Reveal>
            <div className="hero-video-frame overflow-hidden rounded-3xl">
              <video controls playsInline preload="metadata" poster={VID.sitePoster} className="aspect-video w-full"><source src={VID.site} type="video/mp4" /></video>
            </div>
            <p className="mt-3 text-center text-xs text-[#6b6560]">Company video — manufacturing and site work (replaceable from theme settings)</p>
          </Reveal>
          <div>
            <Reveal><SectionHead align="left" eyebrow="Brand Story" title="From bhatta kilns to landmark buildings" text="BrickPoint unites Masha Allah Bricks Company, Fine Bricks Company and the SS7 Bricks range with a full construction-materials catalogue — so every customer, from a single-home builder to a large developer, can source reliably from one supplier." /></Reveal>
            <div className="mt-6 grid gap-3 sm:grid-cols-3">
              {[
                { icon: Target, t: "Mission", d: "Reliable, quality materials with honest quotations." },
                { icon: Eye, t: "Vision", d: "The trusted materials partner for every project scale." },
                { icon: Heart, t: "Values", d: "Quality, consistency and responsive service." },
              ].map((v, i) => (
                <Reveal key={v.t} delay={(i % 3) as 0 | 1 | 2}>
                  <div className="h-full rounded-2xl border bg-white p-5 shadow-sm">
                    <v.icon className="h-6 w-6 text-orange-600" />
                    <h3 className="font-display mt-2 font-extrabold">{v.t}</h3>
                    <p className="mt-1 text-xs text-[#6b6560]">{v.d}</p>
                  </div>
                </Reveal>
              ))}
            </div>
          </div>
        </div>
      </section>

      <section className="bg-[#f6f1ea] py-14">
        <div className="bp-container">
          <Reveal><SectionHead eyebrow="Capabilities" title="What we supply" /></Reveal>
          <div className="mt-8 grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
            {[
              { icon: Factory, t: "Brick Manufacturing", d: "Multiple bhatta locations producing burnt-clay and SS7 bricks." },
              { icon: ShieldCheck, t: "Quality Commitment", d: "Sorted batches, consistent firing and honest grading." },
              { icon: Users, t: "All Customer Sizes", d: "Individual home builders to contractors and companies." },
              { icon: Target, t: "Project Support", d: "Stage-wise quotations and delivery coordination." },
            ].map((c, i) => (
              <Reveal key={c.t} delay={(i % 4) as 0 | 1 | 2 | 3}>
                <div className="h-full rounded-3xl bg-[#141210] p-6 text-white">
                  <c.icon className="h-7 w-7 text-orange-400" />
                  <h3 className="font-display mt-3 font-extrabold">{c.t}</h3>
                  <p className="mt-2 text-sm text-white/65">{c.d}</p>
                </div>
              </Reveal>
            ))}
          </div>
        </div>
      </section>

      <section className="py-14">
        <div className="bp-container">
          <Reveal><SectionHead eyebrow="Management" title="Leadership" text="Direct access to decision-makers — no layers between you and your quotation." /></Reveal>
          <div className="mx-auto mt-8 grid max-w-3xl gap-5 sm:grid-cols-2">
            {[
              { name: SITE.ceo, role: "Chief Executive Officer", img: IMG.worker },
              { name: SITE.salesManager, role: "Sales Manager", img: IMG.brickMason },
            ].map((m, i) => (
              <Reveal key={m.name} delay={i as 0 | 1}>
                <div className="card-hover overflow-hidden rounded-3xl border bg-white text-center">
                  {/* eslint-disable-next-line @next/next/no-img-element */}
                  <img src={m.img} alt={m.name} loading="lazy" className="aspect-[16/9] w-full object-cover" />
                  <div className="p-6">
                    <h3 className="font-display text-xl font-black">{m.name}</h3>
                    <p className="text-sm font-semibold text-orange-700">{m.role}</p>
                    <p className="mt-2 text-xs text-[#6b6560]">BrickPoint • {SITE.phoneDisplay}</p>
                  </div>
                </div>
              </Reveal>
            ))}
          </div>
          <div className="mt-10 flex flex-wrap justify-center gap-3">
            <Link href="/products" className="btn-brick inline-flex items-center gap-2 rounded-xl px-6 py-3 text-sm font-bold text-white">View Products <ArrowRight className="h-4 w-4" /></Link>
            <Link href="/contact" className="inline-flex items-center gap-2 rounded-xl border px-6 py-3 text-sm font-bold hover:border-orange-600 hover:text-orange-700">Contact Us</Link>
            <Link href="/locations" className="inline-flex items-center gap-2 rounded-xl border px-6 py-3 text-sm font-bold hover:border-orange-600 hover:text-orange-700">Our Locations</Link>
          </div>
        </div>
      </section>
    </div>
  );
}
