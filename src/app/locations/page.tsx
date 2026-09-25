import { MapPin, Phone, Clock, MessageCircle, Navigation } from "lucide-react";
import { db } from "@/db";
import { locations } from "@/db/schema";
import { Reveal } from "@/components/ui";
import { SITE } from "@/lib/site";
import { LOCATIONS_SEED } from "@/db/seed-data";

export const dynamic = "force-dynamic";
export const metadata = { title: "Locations" };

export default async function LocationsPage() {
  let items: any[] = [];
  try { items = await db.select().from(locations); } catch {}
  if (!items.length) items = LOCATIONS_SEED as any[];

  return (
    <div>
      <section className="bg-[#141210] py-14 text-white">
        <div className="bp-container">
          <p className="text-xs font-black uppercase tracking-[0.22em] text-orange-400">Bhattas & Office</p>
          <h1 className="font-display mt-2 text-4xl font-black md:text-5xl">Our Locations</h1>
          <p className="mt-3 max-w-2xl text-white/70">Three production units plus head office — tap any card for real Google Maps directions.</p>
        </div>
      </section>
      <section className="py-12">
        <div className="bp-container grid gap-6 md:grid-cols-2">
          {items.map((l: any, i: number) => (
            <Reveal key={l.slug || l.id} delay={(i % 2) as 0 | 1}>
              <article className="card-hover overflow-hidden rounded-3xl border bg-white">
                <div className="img-zoom relative aspect-[16/8] overflow-hidden">
                  {l.image ? (
                    // eslint-disable-next-line @next/next/no-img-element
                    <img src={l.image} alt={l.name} loading="lazy" className="h-full w-full object-cover" />
                  ) : <div className="grid h-full place-items-center bg-stone-300"><MapPin className="h-10 w-10 text-white" /></div>}
                  <span className="absolute left-4 top-4 rounded-full bg-orange-600 px-3 py-1 text-[11px] font-black uppercase text-white">Unit {i + 1}</span>
                </div>
                <div className="p-6 md:p-8">
                  <h2 className="font-display text-xl font-black md:text-2xl">{l.name}</h2>
                  {l.address && <p className="mt-2 flex items-start gap-2 text-sm text-[#6b6560]"><MapPin className="mt-0.5 h-4 w-4 shrink-0 text-orange-600" /> {l.address}</p>}
                  {l.description && <p className="mt-3 text-sm leading-relaxed text-[#3d3833]">{l.description}</p>}
                  <div className="mt-4 flex flex-wrap gap-x-6 gap-y-2 text-sm text-[#3d3833]">
                    {l.phone && <span className="inline-flex items-center gap-1.5"><Phone className="h-4 w-4 text-orange-600" /> {l.phone}</span>}
                    {l.hours && <span className="inline-flex items-center gap-1.5"><Clock className="h-4 w-4 text-orange-600" /> {l.hours}</span>}
                  </div>
                  {l.videoUrl && (
                    <video controls playsInline preload="metadata" poster={l.image || undefined} className="mt-4 aspect-video w-full rounded-2xl bg-black"><source src={l.videoUrl} type="video/mp4" /></video>
                  )}
                  <div className="mt-5 grid grid-cols-3 gap-2">
                    {l.mapsUrl && (
                      <a href={l.mapsUrl} target="_blank" rel="noopener" className="inline-flex items-center justify-center gap-1 rounded-xl bg-[#141210] px-3 py-3 text-xs font-bold text-white hover:bg-black"><Navigation className="h-3.5 w-3.5" /> Directions</a>
                    )}
                    <a href={SITE.whatsapp} target="_blank" rel="noopener" className="btn-whatsapp inline-flex items-center justify-center gap-1 rounded-xl px-3 py-3 text-xs font-bold text-white"><MessageCircle className="h-3.5 w-3.5" /> WhatsApp</a>
                    {l.phone && <a href={`tel:${l.phone.replace(/\s/g, "")}`} className="inline-flex items-center justify-center gap-1 rounded-xl border px-3 py-3 text-xs font-bold hover:border-orange-600 hover:text-orange-700"><Phone className="h-3.5 w-3.5" /> Call</a>}
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
