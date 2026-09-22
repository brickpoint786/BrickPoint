import Link from "next/link";
import { Calendar, User } from "lucide-react";
import { db } from "@/db";
import { posts } from "@/db/schema";
import { desc } from "drizzle-orm";
import { Reveal } from "@/components/ui";

export const dynamic = "force-dynamic";
export const metadata = { title: "Blog" };

export default async function BlogPage({ searchParams }: { searchParams: Promise<{ q?: string; category?: string }> }) {
  const sp = await searchParams;
  let items: any[] = [];
  try { items = await db.select().from(posts).orderBy(desc(posts.publishedAt)); } catch {}
  if (sp.q) items = items.filter((p) => (p.title + p.excerpt + p.content).toLowerCase().includes(sp.q!.toLowerCase()));
  if (sp.category) items = items.filter((p) => p.category === sp.category);
  const cats = [...new Set(items.map((p: any) => p.category).filter(Boolean))];

  return (
    <div>
      <section className="bg-[#141210] py-14 text-white">
        <div className="bp-container">
          <p className="text-xs font-black uppercase tracking-[0.22em] text-orange-400">Guides & Updates</p>
          <h1 className="font-display mt-2 text-4xl font-black md:text-5xl">Blog</h1>
          <p className="mt-3 max-w-2xl text-white/70">Brick selection, material guides, planning tips and industry updates.</p>
          <form action="/blog" method="get" className="mt-6 flex max-w-md gap-2">
            <input name="q" defaultValue={sp.q || ""} placeholder="Search articles…" className="w-full rounded-xl border border-white/20 bg-white/10 px-4 py-2.5 text-sm text-white placeholder:text-white/40" />
            <button className="btn-brick rounded-xl px-5 py-2.5 text-sm font-bold text-white">Search</button>
          </form>
        </div>
      </section>
      <section className="py-12">
        <div className="bp-container">
          {!!cats.length && (
            <div className="flex flex-wrap gap-2">
              <Link href="/blog" className={`rounded-full px-4 py-1.5 text-xs font-bold ${!sp.category ? "bg-[#141210] text-white" : "border"}`}>All</Link>
              {cats.map((c: string) => (
                <Link key={c} href={`/blog?category=${encodeURIComponent(c)}`} className={`rounded-full px-4 py-1.5 text-xs font-bold ${sp.category === c ? "bg-[#141210] text-white" : "border"}`}>{c}</Link>
              ))}
            </div>
          )}
          <div className="mt-8 grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
            {items.map((p: any, i: number) => (
              <Reveal key={p.id} delay={(i % 3) as 0 | 1 | 2}>
                <Link href={`/blog/${p.slug}`} className="card-hover group block overflow-hidden rounded-3xl border bg-white">
                  <div className="img-zoom relative aspect-[16/9] overflow-hidden bg-stone-200">
                    {p.featuredImage ? (
                      // eslint-disable-next-line @next/next/no-img-element
                      <img src={p.featuredImage} alt={p.title} loading="lazy" className="h-full w-full object-cover" />
                    ) : null}
                    {p.category && <span className="absolute left-3 top-3 rounded-full bg-orange-600 px-3 py-1 text-[11px] font-black uppercase text-white">{p.category}</span>}
                  </div>
                  <div className="p-6">
                    <h2 className="font-display text-lg font-extrabold leading-snug group-hover:text-orange-700">{p.title}</h2>
                    {p.excerpt && <p className="line-clamp-2 mt-2 text-sm text-[#6b6560]">{p.excerpt}</p>}
                    <div className="mt-4 flex items-center gap-4 text-xs text-[#6b6560]">
                      <span className="inline-flex items-center gap-1"><User className="h-3.5 w-3.5" /> {p.author}</span>
                      {p.publishedAt && <span className="inline-flex items-center gap-1"><Calendar className="h-3.5 w-3.5" /> {new Date(p.publishedAt).toLocaleDateString()}</span>}
                    </div>
                  </div>
                </Link>
              </Reveal>
            ))}
          </div>
          {!items.length && <div className="mt-8 rounded-2xl border border-dashed p-10 text-center text-sm text-[#6b6560]">No articles found.</div>}
        </div>
      </section>
    </div>
  );
}
