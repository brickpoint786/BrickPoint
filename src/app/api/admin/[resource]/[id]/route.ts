import { NextResponse } from "next/server";
import { db } from "@/db";
import { products, productCategories, videos, videoCategories, projects, locations, posts, inquiries, settings } from "@/db/schema";
import { eq } from "drizzle-orm";

const MAP: Record<string, { table: any; pk: any }> = {
  products: { table: products, pk: products.id },
  product_categories: { table: productCategories, pk: productCategories.id },
  videos: { table: videos, pk: videos.id },
  video_categories: { table: videoCategories, pk: videoCategories.id },
  projects: { table: projects, pk: projects.id },
  locations: { table: locations, pk: locations.id },
  posts: { table: posts, pk: posts.id },
  inquiries: { table: inquiries, pk: inquiries.id },
};

export async function PUT(req: Request, { params }: { params: Promise<{ resource: string; id: string }> }) {
  const { resource, id } = await params;
  const entry = MAP[resource];
  if (!entry) return NextResponse.json({ ok: false, error: "Unknown resource" }, { status: 404 });
  try {
    const body = await req.json();
    if (body.id) delete body.id;
    if (body.createdAt) delete body.createdAt;
    if (body.publishedAt && typeof body.publishedAt === "string" && body.publishedAt) body.publishedAt = new Date(body.publishedAt);
    const rows = (await db.update(entry.table).set({ ...body, ...(resource === "products" ? { updatedAt: new Date() } : {}) }).where(eq(entry.pk, Number(id))).returning()) as any[];
    return NextResponse.json({ ok: true, row: rows[0] });
  } catch (e: any) {
    return NextResponse.json({ ok: false, error: e?.message }, { status: 500 });
  }
}

export async function DELETE(_: Request, { params }: { params: Promise<{ resource: string; id: string }> }) {
  const { resource, id } = await params;
  const entry = MAP[resource];
  if (!entry) return NextResponse.json({ ok: false, error: "Unknown resource" }, { status: 404 });
  try {
    await db.delete(entry.table).where(eq(entry.pk, Number(id)));
    return NextResponse.json({ ok: true });
  } catch (e: any) {
    return NextResponse.json({ ok: false, error: e?.message }, { status: 500 });
  }
}
