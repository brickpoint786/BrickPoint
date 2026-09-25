import Link from "next/link";
import { MapPin } from "lucide-react";
import { db } from "@/db";
import { projects } from "@/db/schema";
import { Reveal } from "@/components/ui";
import { IMG } from "@/db/seed-data";

export const dynamic = "force-dynamic";
export const metadata = { title: "Projects" };

const SOCIETIES = ["DHA Lahore", "Bahria Town Lahore", "Lake City Lahore", "Etihad Town Lahore", "Al-Kabir Town", "LDA City", "Paragon City", "Izmir Town", "Central Park Housing Scheme"];

export default async function ProjectsPage() {
  let items: any[] = [];
  try { items = await db.select().from(projects); } catch {}
  if (!items.length) {
    items = SOCIETIES.slice(0, 6).map((s, i) => ({
      id: i, title: `${s} — Construction Reference`, slug: s.toLowerCase().replace(/[^a-z]+/g, "-"),
      location: s, category: "Residential", featuredImage: [IMG.villa1, IMG.villa2, IMG.apt, IMG.villa3, IMG.site, IMG.brickMason][i % 6],
      description: "Illustrative construction reference.", status: "Illustrative construction reference",
    }));
  }
  return (
    <div>
      <section className="bg-[#141210] py-14 text-white">
        <div className="bp-container">
          <p className="text-xs font-black uppercase tracking-[0.22em] text-orange-400">References & Inspiration</p>
          <h1 className="font-display mt-2 text-4xl font-black md:text-5xl">Projects</h1>
          <p className="mt-3 max-w-2xl text-white/70">Construction references and project inspiration visuals from Lahore housing developments. Visuals are illustrative unless a project is verified by BrickPoint.</p>
          <div className="mt-5 flex flex-wrap gap-2">
            {SOCIETIES.map((s) => (
              <span key={s} className="inline-flex items-center gap-1 rounded-full bg-white/10 px-3 py-1.5 text-xs font-semibold text-white/80"><MapPin className="h-3 w-3 text-orange-400" /> {s}</span>
            ))}
          </div>
        </div>
      </section>
      <section className="py-12">
        <div className="bp-container">
          <div className="rounded-2xl border border-amber-300 bg-amber-50 p-4 text-xs text-amber-900">
            <strong>Content notice:</strong> Project visuals on this page are labelled <em>“Illustrative construction reference”</em> or <em>“Project inspiration visual”</em>. BrickPoint does not claim supply to any named society, developer or project unless verified by management.
          </div>
          <div className="mt-8 grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
            {items.map((pr: any, i: number) => (
              <Reveal key={pr.id} delay={(i % 3) as 0 | 1 | 2}>
                <article className="card-hover overflow-hidden rounded-3xl border bg-white">
                  <div className="img-zoom relative aspect-[16/10] overflow-hidden">
                    {/* eslint-disable-next-line @next/next/no-img-element */}
                    <img src={pr.featuredImage} alt={pr.title} loading="lazy" className="h-full w-full object-cover" />
                    <span className="absolute left-3 top-3 rounded-full bg-black/70 px-3 py-1 text-[11px] font-bold text-white">{pr.status || "Illustrative construction reference"}</span>
                  </div>
                  <div className="p-6">
                    <p className="text-[11px] font-black uppercase tracking-widest text-orange-700">{pr.location} {pr.category && `• ${pr.category}`}</p>
                    <h2 className="font-display mt-1 text-lg font-extrabold">{pr.title}</h2>
                    {pr.description && <p className="line-clamp-2 mt-2 text-sm text-[#6b6560]">{pr.description}</p>}
                    <div className="mt-4 flex gap-2">
                      <Link href="/contact" className="inline-flex flex-1 items-center justify-center rounded-xl bg-[#141210] px-3 py-2.5 text-xs font-bold text-white hover:bg-black">Build Like This — Get Quote</Link>
                      <Link href="/products" className="inline-flex items-center justify-center rounded-xl border px-3 py-2.5 text-xs font-bold hover:border-orange-600 hover:text-orange-700">Materials</Link>
                    </div>
                  </div>
                </article>
              </Reveal>
            ))}
          </div>
        </div>
      </section>
    </div>
  );
}
