import Link from "next/link";
import { CheckCircle2, ArrowRight } from "lucide-react";
import { Reveal, SectionHead, WhatsAppButton } from "@/components/ui";
import { IMG } from "@/db/seed-data";

export const metadata = { title: "For Builders" };

export default function Page() {
  return (
    <div>
      <section className="relative overflow-hidden bg-[#141210] py-14 text-white md:py-20">
        {/* eslint-disable-next-line @next/next/no-img-element */}
        <img src={IMG.bricklayer} alt="" className="absolute inset-0 h-full w-full object-cover opacity-25" />
        <div className="absolute inset-0 bg-gradient-to-r from-[#141210] to-transparent" />
        <div className="relative bp-container">
          <p className="text-xs font-black uppercase tracking-[0.22em] text-orange-400">For Builders</p>
          <h1 className="font-display mt-2 max-w-2xl text-4xl font-black md:text-5xl">Consistent quality, house after house</h1>
          <p className="mt-4 max-w-xl text-white/70">Source complete material sets with consistent batches — from foundation to finishing.</p>
          <div className="mt-6 flex flex-wrap gap-3">
            <WhatsAppButton label="Discuss Your Build" message="Assalam-o-Alaikum BrickPoint,\n\nI am a builder and need materials for an upcoming house/building project.\n\nPlease guide me on sourcing.\n\nThank you." size="lg" />
            <Link href="/ss7-bricks" className="inline-flex items-center gap-2 rounded-xl border border-white/20 px-6 py-4 text-sm font-bold hover:bg-white/10">SS7 Bricks</Link>
          </div>
        </div>
      </section>
      <section className="py-14">
        <div className="bp-container">
          <Reveal><SectionHead eyebrow="Builder Benefits" title="Sourcing made simple" /></Reveal>
          <div className="mt-8 grid gap-4 md:grid-cols-2 lg:grid-cols-3">
            {[
              ["Multi-category sourcing", "One supplier for structure, services and finishes."],
              ["Consistent quality", "Sorted batches keep every house uniform."],
              ["Quantity planning", "Stage-wise estimates reduce waste and delays."],
              ["Bulk requirements", "House-builder rates on repeat orders."],
              ["Project planning support", "Material sequencing advice from our team."],
              ["Fast quotation", "WhatsApp your covered area + list for pricing."],
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
          <div className="mt-10 rounded-3xl bg-[#f6f1ea] p-8 text-center md:p-12">
            <h2 className="font-display text-2xl font-black">Planning your next build?</h2>
            <p className="mt-2 text-[#6b6560]">Get a complete material quotation before you break ground.</p>
            <div className="mt-6 flex flex-wrap justify-center gap-3">
              <Link href="/contact" className="btn-brick inline-flex items-center gap-2 rounded-xl px-6 py-4 text-sm font-bold text-white">Request Quotation <ArrowRight className="h-4 w-4" /></Link>
              <Link href="/construction-materials" className="inline-flex items-center gap-2 rounded-xl border px-6 py-4 text-sm font-bold hover:border-orange-600 hover:text-orange-700">Full Range</Link>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}
