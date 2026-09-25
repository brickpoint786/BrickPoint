import Link from "next/link";
import { CheckCircle2, ArrowRight } from "lucide-react";
import { Reveal, SectionHead, WhatsAppButton } from "@/components/ui";
import { IMG } from "@/db/seed-data";
import { SITE } from "@/lib/site";

export const metadata = { title: "For Construction Companies" };

export default function Page() {
  return (
    <div>
      <section className="relative overflow-hidden bg-[#141210] py-14 text-white md:py-20">
        {/* eslint-disable-next-line @next/next/no-img-element */}
        <img src={IMG.apt} alt="" className="absolute inset-0 h-full w-full object-cover opacity-25" />
        <div className="absolute inset-0 bg-gradient-to-r from-[#141210] to-transparent" />
        <div className="relative bp-container">
          <p className="text-xs font-black uppercase tracking-[0.22em] text-orange-400">For Construction Companies</p>
          <h1 className="font-display mt-2 max-w-2xl text-4xl font-black md:text-5xl">Large-scale supply, coordinated professionally</h1>
          <p className="mt-4 max-w-xl text-white/70">Multi-location coordination, documentation support and a dedicated contact for corporate accounts.</p>
          <div className="mt-6 flex flex-wrap gap-3">
            <WhatsAppButton label="Corporate Inquiry" message="Assalam-o-Alaikum BrickPoint,\n\nWe are a construction company interested in large-scale material supply.\n\nPlease share your corporate inquiry process.\n\nThank you." size="lg" />
            <Link href="/contact" className="inline-flex items-center gap-2 rounded-xl border border-white/20 px-6 py-4 text-sm font-bold hover:bg-white/10">Contact Form</Link>
          </div>
        </div>
      </section>
      <section className="py-14">
        <div className="bp-container">
          <Reveal><SectionHead eyebrow="Corporate Benefits" title="Built for scale" /></Reveal>
          <div className="mt-8 grid gap-4 md:grid-cols-2 lg:grid-cols-3">
            {[
              ["Large-scale supply", "High-volume brick and material orders with planning."],
              ["Material coordination", "Stage-wise scheduling across your sites."],
              ["Multiple locations", "Bhatta + office network for flexible fulfilment."],
              ["Product documentation", "Quotations, specs and delivery records on request."],
              ["Dedicated contact", `CEO ${SITE.ceo} • Sales ${SITE.salesManager} • ${SITE.phoneDisplay}`],
              ["Full-range sourcing", "Structure to finishes under one relationship."],
            ].map(([t, d], i) => (
              <Reveal key={t} delay={(i % 3) as 0 | 1 | 2}>
                <div className="h-full rounded-3xl bg-[#141210] p-6 text-white">
                  <CheckCircle2 className="h-6 w-6 text-emerald-400" />
                  <h3 className="font-display mt-3 font-extrabold">{t}</h3>
                  <p className="mt-2 text-sm text-white/65">{d}</p>
                </div>
              </Reveal>
            ))}
          </div>
          <div className="mt-10 rounded-3xl border p-8 text-center md:p-12">
            <h2 className="font-display text-2xl font-black">Start a corporate conversation</h2>
            <p className="mt-2 text-[#6b6560]">Share your company profile and upcoming requirement schedule.</p>
            <div className="mt-6 flex flex-wrap justify-center gap-3">
              <Link href="/contact" className="btn-brick inline-flex items-center gap-2 rounded-xl px-6 py-4 text-sm font-bold text-white">Corporate Inquiry Form <ArrowRight className="h-4 w-4" /></Link>
              <Link href="/projects" className="inline-flex items-center gap-2 rounded-xl border px-6 py-4 text-sm font-bold hover:border-orange-600 hover:text-orange-700">View References</Link>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}
