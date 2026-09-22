import Link from "next/link";
import { CheckCircle2, ArrowRight } from "lucide-react";
import { Reveal, SectionHead, WhatsAppButton } from "@/components/ui";
import { IMG } from "@/db/seed-data";

export const metadata = { title: "For Contractors" };

export default function Page() {
  return (
    <div>
      <section className="relative overflow-hidden bg-[#141210] py-14 text-white md:py-20">
        {/* eslint-disable-next-line @next/next/no-img-element */}
        <img src={IMG.site} alt="" className="absolute inset-0 h-full w-full object-cover opacity-25" />
        <div className="absolute inset-0 bg-gradient-to-r from-[#141210] to-transparent" />
        <div className="relative bp-container">
          <p className="text-xs font-black uppercase tracking-[0.22em] text-orange-400">For Contractors</p>
          <h1 className="font-display mt-2 max-w-2xl text-4xl font-black md:text-5xl">Bulk supply that keeps your sites moving</h1>
          <p className="mt-4 max-w-xl text-white/70">Project-based quotations, reliable availability and delivery coordination across brick and material categories.</p>
          <div className="mt-6 flex flex-wrap gap-3">
            <WhatsAppButton label="Get Contractor Rates" message="Assalam-o-Alaikum BrickPoint,\n\nI am a contractor and need bulk rates for my project.\n\nPlease share your contractor pricing process.\n\nThank you." size="lg" />
            <Link href="/products" className="inline-flex items-center gap-2 rounded-xl border border-white/20 px-6 py-4 text-sm font-bold hover:bg-white/10">Browse Products</Link>
          </div>
        </div>
      </section>
      <section className="py-14">
        <div className="bp-container">
          <Reveal><SectionHead eyebrow="Contractor Benefits" title="Why contractors choose BrickPoint" /></Reveal>
          <div className="mt-8 grid gap-4 md:grid-cols-2 lg:grid-cols-3">
            {[
              ["Bulk material supply", "Trolley, thousand-brick and tonnage quantities with sorted batches."],
              ["Project-based quotations", "Send your BOQ or stage list — get one consolidated quote."],
              ["Delivery coordination", "Schedule deliveries stage-wise with site-location planning."],
              ["Reliable availability", "Multiple bhatta units back consistent brick supply."],
              ["Full category range", "Bricks, cement, aggregates, steel, pipes, electricals, finishes."],
              ["Direct WhatsApp line", "Fast answers on rates, stock and delivery slots."],
            ].map(([t, d], i) => (
              <Reveal key={t} delay={(i % 3) as 0 | 1 | 2}>
                <div className="h-full rounded-3xl border bg-white p-6">
                  <CheckCircle2 className="h-6 w-6 text-emerald-600" />
                  <h3 className="font-display mt-3 font-extrabold">{t}</h3>
                  <p className="mt-2 text-sm text-[#6b6560]">{d}</p>
                </div>
              </Reveal>
            ))}
          </div>
          <div className="mt-10 rounded-3xl bg-[#141210] p-8 text-center text-white md:p-12">
            <h2 className="font-display text-2xl font-black">Share your BOQ today</h2>
            <p className="mt-2 text-white/70">Attach your material list on WhatsApp for a project quotation.</p>
            <div className="mt-6 flex flex-wrap justify-center gap-3">
              <WhatsAppButton label="Send BOQ on WhatsApp" message="Assalam-o-Alaikum BrickPoint,\n\nI am sharing my project BOQ for quotation.\n\nThank you." size="lg" />
              <Link href="/contact" className="btn-brick inline-flex items-center gap-2 rounded-xl px-6 py-4 text-sm font-bold text-white">Use Quote Form <ArrowRight className="h-4 w-4" /></Link>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}
