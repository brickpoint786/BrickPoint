import Link from "next/link";
import { db } from "@/db";
import { videos, videoCategories } from "@/db/schema";
import { desc } from "drizzle-orm";
import { Reveal, VideoCard } from "@/components/ui";

export const dynamic = "force-dynamic";
export const metadata = { title: "Videos — Inside BrickPoint" };

export default async function VideosPage({ searchParams }: { searchParams: Promise<{ category?: string; featured?: string }> }) {
  const sp = await searchParams;
  let vids: any[] = [];
  let cats: any[] = [];
  try {
    cats = await db.select().from(videoCategories);
    vids = await db.select().from(videos).orderBy(desc(videos.featured), desc(videos.displayOrder));
  } catch {}
  const catName = (id: number | null) => cats.find((c) => c.id === id)?.name || "";
  let filtered = vids;
  if (sp.category) {
    const c = cats.find((x) => x.slug === sp.category);
    if (c) filtered = filtered.filter((v: any) => v.categoryId === c.id);
  }
  if (sp.featured) filtered = filtered.filter((v: any) => v.featured);

  return (
    <div>
      <section className="bg-[#141210] py-14 text-white">
        <div className="bp-container">
          <p className="text-xs font-black uppercase tracking-[0.22em] text-orange-400">Video Library</p>
          <h1 className="font-display mt-2 text-4xl font-black md:text-5xl">Inside BrickPoint</h1>
          <p className="mt-3 max-w-2xl text-white/70">Explore our products, production process, construction materials, projects, and company updates through video.</p>
          <div className="mt-6 flex flex-wrap gap-2">
            <Link href="/videos" className={`rounded-full px-4 py-2 text-xs font-bold ${!sp.category && !sp.featured ? "bg-orange-600" : "bg-white/10 text-white/70"}`}>All Videos</Link>
            <Link href="/videos?featured=1" className={`rounded-full px-4 py-2 text-xs font-bold ${sp.featured ? "bg-orange-600" : "bg-white/10 text-white/70"}`}>Featured</Link>
            {cats.map((c) => (
              <Link key={c.id} href={`/videos?category=${c.slug}`} className={`rounded-full px-4 py-2 text-xs font-bold ${sp.category === c.slug ? "bg-orange-600" : "bg-white/10 text-white/70"}`}>{c.name}</Link>
            ))}
          </div>
        </div>
      </section>
      <section className="py-12">
        <div className="bp-container">
          <p className="text-sm text-[#6b6560]">Showing <strong>{filtered.length}</strong> videos</p>
          <div className="mt-6 grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
            {filtered.map((v: any, i: number) => (
              <Reveal key={v.id} delay={(i % 3) as 0 | 1 | 2}><VideoCard v={v} categoryName={catName(v.categoryId)} /></Reveal>
            ))}
          </div>
          {!filtered.length && <div className="mt-8 rounded-2xl border border-dashed p-10 text-center text-sm text-[#6b6560]">No videos in this filter yet.</div>}
        </div>
      </section>
    </div>
  );
}
