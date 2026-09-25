import Link from "next/link";
import { notFound } from "next/navigation";
import { db } from "@/db";
import { posts } from "@/db/schema";
import { eq, ne } from "drizzle-orm";
import { ChevronRight, Calendar, User, Tag } from "lucide-react";

export const dynamic = "force-dynamic";

export default async function PostDetail({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  let p: any = null;
  let related: any[] = [];
  try {
    const [row] = await db.select().from(posts).where(eq(posts.slug, slug)).limit(1);
    if (!row) return notFound();
    p = row;
    related = await db.select().from(posts).where(ne(posts.id, p.id)).limit(3);
  } catch { return notFound(); }

  return (
    <div>
      <div className="border-b bg-white">
        <div className="bp-container flex items-center gap-2 py-4 text-xs text-[#6b6560]">
          <Link href="/" className="hover:text-orange-700">Home</Link><ChevronRight className="h-3 w-3" />
          <Link href="/blog" className="hover:text-orange-700">Blog</Link><ChevronRight className="h-3 w-3" />
          <span className="font-semibold text-[#141210]">{p.title}</span>
        </div>
      </div>
      <article className="bp-container max-w-3xl py-10">
        {p.category && <span className="rounded-full bg-orange-600 px-3 py-1 text-[11px] font-black uppercase text-white">{p.category}</span>}
        <h1 className="font-display mt-3 text-3xl font-black md:text-4xl">{p.title}</h1>
        <div className="mt-3 flex flex-wrap items-center gap-4 text-xs text-[#6b6560]">
          <span className="inline-flex items-center gap-1"><User className="h-3.5 w-3.5" /> {p.author}</span>
          {p.publishedAt && <span className="inline-flex items-center gap-1"><Calendar className="h-3.5 w-3.5" /> {new Date(p.publishedAt).toLocaleDateString()}</span>}
          {p.tags?.length > 0 && <span className="inline-flex items-center gap-1"><Tag className="h-3.5 w-3.5" /> {p.tags.join(", ")}</span>}
        </div>
        {p.featuredImage && (
          // eslint-disable-next-line @next/next/no-img-element
          <img src={p.featuredImage} alt={p.title} className="mt-6 aspect-[16/9] w-full rounded-3xl object-cover" />
        )}
        <div className="prose-bp mt-6 rounded-3xl border bg-white p-6 md:p-8">
          {p.excerpt && <p className="text-lg font-semibold text-[#141210]">{p.excerpt}</p>}
          <p>{p.content}</p>
        </div>
        <div className="mt-6 flex flex-wrap gap-3">
          <Link href="/blog" className="rounded-xl border px-5 py-2.5 text-sm font-bold hover:border-orange-600 hover:text-orange-700">← All Articles</Link>
          <Link href="/products" className="rounded-xl bg-[#141210] px-5 py-2.5 text-sm font-bold text-white hover:bg-black">Shop Materials</Link>
          <a href="https://wa.me/923152850818" target="_blank" rel="noopener" className="btn-whatsapp rounded-xl px-5 py-2.5 text-sm font-bold text-white">Ask on WhatsApp</a>
        </div>
      </article>
      {related.length > 0 && (
        <section className="border-t bg-white py-12">
          <div className="bp-container max-w-5xl">
            <h2 className="font-display text-2xl font-black">Related Articles</h2>
            <div className="mt-6 grid gap-5 sm:grid-cols-3">
              {related.map((r: any) => (
                <Link key={r.id} href={`/blog/${r.slug}`} className="card-hover overflow-hidden rounded-2xl border bg-white">
                  {r.featuredImage && (
                    // eslint-disable-next-line @next/next/no-img-element
                    <img src={r.featuredImage} alt={r.title} loading="lazy" className="aspect-[16/9] w-full object-cover" />
                  )}
                  <div className="p-4">
                    <h3 className="font-display text-sm font-extrabold">{r.title}</h3>
                  </div>
                </Link>
              ))}
            </div>
          </div>
        </section>
      )}
    </div>
  );
}
