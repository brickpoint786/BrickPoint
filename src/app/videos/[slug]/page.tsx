import Link from "next/link";
import { notFound } from "next/navigation";
import { db } from "@/db";
import { videos, videoCategories } from "@/db/schema";
import { eq, ne } from "drizzle-orm";
import { ChevronRight, Calendar, Clock } from "lucide-react";
import { VideoCard } from "@/components/ui";

export const dynamic = "force-dynamic";

export default async function VideoDetail({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  let v: any = null;
  let cat: any = null;
  let more: any[] = [];
  let catMap: Record<number, string> = {};
  try {
    const [row] = await db.select().from(videos).where(eq(videos.slug, slug)).limit(1);
    if (!row) return notFound();
    v = row;
    const cats = await db.select().from(videoCategories);
    cats.forEach((c) => (catMap[c.id] = c.name));
    if (v.categoryId) cat = cats.find((c) => c.id === v.categoryId) || null;
    more = await db.select().from(videos).where(ne(videos.id, v.id)).limit(3);
  } catch { return notFound(); }

  const isEmbed = v.sourceType === "youtube" || v.sourceType === "vimeo" || (v.videoUrl && v.videoUrl.includes("embed"));

  return (
    <div className="bg-[#0f0e0c] text-white">
      <div className="bp-container flex items-center gap-2 py-5 text-xs text-white/60">
        <Link href="/" className="hover:text-white">Home</Link><ChevronRight className="h-3 w-3" />
        <Link href="/videos" className="hover:text-white">Videos</Link><ChevronRight className="h-3 w-3" />
        <span className="text-white">{v.title}</span>
      </div>
      <section className="bp-container pb-10">
        <div className="overflow-hidden rounded-3xl border border-white/10 bg-black">
          {isEmbed ? (
            <iframe src={v.videoUrl} title={v.title} className="aspect-video w-full" loading="lazy" allow="accelerometer; autoplay; encrypted-media; picture-in-picture" allowFullScreen />
          ) : (
            <video controls playsInline preload="metadata" poster={v.thumbnail || undefined} className="aspect-video w-full">
              <source src={v.fileUrl || v.videoUrl} type="video/mp4" />
              {v.captionsUrl && <track kind="captions" src={v.captionsUrl} label="Captions" />}
            </video>
          )}
        </div>
        <div className="mt-6 max-w-3xl">
          {cat && <p className="text-xs font-black uppercase tracking-[0.22em] text-orange-400">{cat.name}</p>}
          <h1 className="font-display mt-2 text-3xl font-black md:text-4xl">{v.title}</h1>
          <div className="mt-3 flex flex-wrap gap-4 text-xs text-white/60">
            {v.duration && <span className="inline-flex items-center gap-1"><Clock className="h-3.5 w-3.5" /> {v.duration}</span>}
            {v.publishedAt && <span className="inline-flex items-center gap-1"><Calendar className="h-3.5 w-3.5" /> {new Date(v.publishedAt).toLocaleDateString()}</span>}
            {v.featured && <span className="rounded-full bg-amber-400 px-3 py-0.5 font-black text-black">Featured</span>}
          </div>
          {v.description && <p className="mt-4 text-white/75">{v.description}</p>}
          <div className="mt-6 flex flex-wrap gap-3">
            <Link href="/videos" className="rounded-xl border border-white/20 px-5 py-2.5 text-sm font-bold hover:bg-white/10">← All Videos</Link>
            <Link href="/products" className="rounded-xl bg-orange-600 px-5 py-2.5 text-sm font-bold hover:bg-orange-500">Related Products</Link>
          </div>
        </div>
        {more.length > 0 && (
          <div className="mt-10">
            <h2 className="font-display text-xl font-black">More Videos</h2>
            <div className="mt-5 grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
              {more.map((m: any) => (<VideoCard key={m.id} v={m} categoryName={catMap[m.categoryId]} />))}
            </div>
          </div>
        )}
      </section>
    </div>
  );
}
