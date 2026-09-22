import { NextResponse } from "next/server";
import { db } from "@/db";
import { inquiries } from "@/db/schema";

export async function POST(req: Request) {
  try {
    const body = await req.json();
    const { name, phone, email, company, material, quantity, location, message, productId } = body;
    if (!name || !phone) {
      return NextResponse.json({ ok: false, error: "Name and phone are required." }, { status: 400 });
    }
    await db.insert(inquiries).values({
      name: String(name).slice(0, 160),
      phone: String(phone).slice(0, 40),
      email: email ? String(email).slice(0, 160) : null,
      company: company ? String(company).slice(0, 160) : null,
      material: material ? String(material).slice(0, 160) : null,
      quantity: quantity ? String(quantity).slice(0, 120) : null,
      location: location ? String(location).slice(0, 160) : null,
      message: message ? String(message).slice(0, 2000) : null,
      productId: productId ? Number(productId) : null,
    } as any);
    return NextResponse.json({ ok: true, message: "Inquiry received. We will contact you shortly." });
  } catch (e: any) {
    return NextResponse.json({ ok: false, error: e?.message || "Failed" }, { status: 500 });
  }
}
