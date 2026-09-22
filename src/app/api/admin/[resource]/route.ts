import { NextResponse } from "next/server";
import { db } from "@/db";
import { products, productCategories, videos, videoCategories, projects, locations, posts, inquiries, settings } from "@/db/schema";
import { desc } from "drizzle-orm";

const MAP: Record<string, any> = {
  products, product_categories: productCategories, videos, video_categories: videoCategories,
  projects, locations, posts, inquiries, settings,
};

export async function GET(_: Request, { params }: { params: Promise<{ resource: string }> }) {
  const { resource } = await params;
  const table = MAP[resource];
  if (!table) return NextResponse.json({ ok: false, error: "Unknown resource" }, { status: 404 });
  try {
    const rows = await db.select().from(table).limit(200);
    return NextResponse.json({ ok: true, rows });
  } catch (e: any) {
    return NextResponse.json({ ok: false, error: e?.message }, { status: 500 });
  }
}

export async function POST(req: Request, { params }: { params: Promise<{ resource: string }> }) {
  const { resource } = await params;
  const table = MAP[resource];
  if (!table) return NextResponse.json({ ok: false, error: "Unknown resource" }, { status: 404 });
  try {
    const body = await req.json();
    if (body.id) delete body.id;
    if (body.createdAt) delete body.createdAt;
    if (body.updatedAt) delete body.updatedAt;
    if (body.publishedAt && typeof body.publishedAt === "string" && body.publishedAt) body.publishedAt = new Date(body.publishedAt);
    const rows = (await db.insert(table).values(body).returning()) as any[];
    return NextResponse.json({ ok: true, row: rows[0] });
  } catch (e: any) {
    return NextResponse.json({ ok: false, error: e?.message }, { status: 500 });
  }
}
