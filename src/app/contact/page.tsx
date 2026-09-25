"use client";
import { useState } from "react";
import { Phone, Mail, MapPin, MessageCircle, Send, CheckCircle2 } from "lucide-react";
import { SITE } from "@/lib/site";

export default function ContactPage() {
  const [form, setForm] = useState({ name: "", phone: "", email: "", company: "", material: "", quantity: "", location: "", message: "" });
  const [status, setStatus] = useState<"idle" | "sending" | "done" | "error">("idle");
  const set = (k: string) => (e: any) => setForm((f) => ({ ...f, [k]: e.target.value }));

  async function submit(e: React.FormEvent) {
    e.preventDefault();
    setStatus("sending");
    try {
      const res = await fetch("/api/contact", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(form) });
      const j = await res.json();
      setStatus(j.ok ? "done" : "error");
    } catch { setStatus("error"); }
  }

  const input = "w-full rounded-xl border border-black/10 bg-white px-4 py-3 text-sm";

  return (
    <div>
      <section className="bg-[#141210] py-14 text-white">
        <div className="bp-container">
          <p className="text-xs font-black uppercase tracking-[0.22em] text-orange-400">Get In Touch</p>
          <h1 className="font-display mt-2 text-4xl font-black md:text-5xl">Contact BrickPoint</h1>
          <p className="mt-3 max-w-2xl text-white/70">Call, WhatsApp or send the quotation form — we respond fast on working hours.</p>
        </div>
      </section>
      <section className="py-12">
        <div className="bp-container grid gap-8 lg:grid-cols-[380px_1fr]">
          <div className="space-y-4">
            <div className="rounded-3xl bg-[#141210] p-6 text-white">
              <h2 className="font-display text-lg font-black">Direct Contact</h2>
              <div className="mt-4 space-y-3 text-sm">
                <p className="flex items-center gap-2"><Phone className="h-4 w-4 text-orange-400" /> {SITE.phoneDisplay}</p>
                <p className="flex items-center gap-2"><Mail className="h-4 w-4 text-orange-400" /> {SITE.email}</p>
                <p className="flex items-start gap-2"><MapPin className="mt-0.5 h-4 w-4 shrink-0 text-orange-400" /> {SITE.address}</p>
                <p className="text-white/60">CEO: {SITE.ceo}<br />Sales Manager: {SITE.salesManager}</p>
              </div>
              <a href={SITE.whatsapp} target="_blank" rel="noopener" className="btn-whatsapp mt-5 flex items-center justify-center gap-2 rounded-xl px-4 py-3 text-sm font-bold text-white"><MessageCircle className="h-4 w-4" /> Chat on WhatsApp</a>
              <div className="mt-3 grid grid-cols-2 gap-2 text-center text-xs font-bold">
                <a href={SITE.social.facebook} target="_blank" rel="noopener" className="rounded-xl bg-white/10 py-2.5 hover:bg-white/15">Facebook</a>
                <a href={SITE.social.instagram} target="_blank" rel="noopener" className="rounded-xl bg-white/10 py-2.5 hover:bg-white/15">Instagram</a>
                <a href={SITE.social.twitter} target="_blank" rel="noopener" className="rounded-xl bg-white/10 py-2.5 hover:bg-white/15">X / Twitter</a>
                <a href={SITE.social.tiktok} target="_blank" rel="noopener" className="rounded-xl bg-white/10 py-2.5 hover:bg-white/15">TikTok</a>
              </div>
            </div>
            <div className="rounded-3xl border bg-white p-6">
              <h3 className="font-display font-extrabold">Office Map</h3>
              <p className="mt-1 text-xs text-[#6b6560]">Open the verified office location in Google Maps.</p>
              <a href="https://maps.app.goo.gl/GACXw15YxyV4bK5t8?g_st=awb" target="_blank" rel="noopener" className="mt-3 flex items-center justify-center gap-2 rounded-xl bg-[#141210] px-4 py-3 text-sm font-bold text-white hover:bg-black"><MapPin className="h-4 w-4" /> Open Google Maps</a>
              <a href="/locations" className="mt-2 flex items-center justify-center rounded-xl border px-4 py-3 text-sm font-bold hover:border-orange-600 hover:text-orange-700">All Locations</a>
            </div>
          </div>
          <div className="rounded-3xl border bg-white p-6 md:p-8">
            <h2 className="font-display text-2xl font-black">Request a Quotation</h2>
            <p className="mt-1 text-sm text-[#6b6560]">Fields: name, phone, email, company, required material, quantity, location, message.</p>
            {status === "done" ? (
              <div className="mt-6 rounded-2xl border border-emerald-200 bg-emerald-50 p-8 text-center">
                <CheckCircle2 className="mx-auto h-10 w-10 text-emerald-600" />
                <h3 className="font-display mt-3 text-xl font-black">Inquiry received!</h3>
                <p className="mt-2 text-sm text-emerald-900">Thank you — our sales team will contact you shortly. For an instant response, message us on WhatsApp.</p>
                <a href={SITE.whatsapp} target="_blank" rel="noopener" className="btn-whatsapp mt-4 inline-flex items-center gap-2 rounded-xl px-6 py-3 text-sm font-bold text-white"><MessageCircle className="h-4 w-4" /> Continue on WhatsApp</a>
              </div>
            ) : (
              <form onSubmit={submit} className="mt-6 grid gap-4 sm:grid-cols-2">
                <div><label className="mb-1 block text-xs font-bold">Full Name *</label><input required value={form.name} onChange={set("name")} className={input} placeholder="Your name" /></div>
                <div><label className="mb-1 block text-xs font-bold">Phone *</label><input required value={form.phone} onChange={set("phone")} className={input} placeholder="03xx xxxxxxx" /></div>
                <div><label className="mb-1 block text-xs font-bold">Email</label><input type="email" value={form.email} onChange={set("email")} className={input} placeholder="you@email.com" /></div>
                <div><label className="mb-1 block text-xs font-bold">Company</label><input value={form.company} onChange={set("company")} className={input} placeholder="Company / contractor name" /></div>
                <div><label className="mb-1 block text-xs font-bold">Required Material</label>
                  <select value={form.material} onChange={set("material")} className={input}>
                    <option value="">Select material…</option>
                    {["SS7 Bricks", "Bricks", "Cement", "Bajri / Crush", "Sand / Rait", "Steel", "Pipes", "Chemicals", "Insulation", "Cables", "Paints", "Lights", "Switches", "Multiple / Full List"].map((m) => (<option key={m}>{m}</option>))}
                  </select>
                </div>
                <div><label className="mb-1 block text-xs font-bold">Quantity</label><input value={form.quantity} onChange={set("quantity")} className={input} placeholder="e.g. 50,000 bricks / 200 bags" /></div>
                <div className="sm:col-span-2"><label className="mb-1 block text-xs font-bold">Site / Delivery Location</label><input value={form.location} onChange={set("location")} className={input} placeholder="e.g. DHA Phase 6, Lahore" /></div>
                <div className="sm:col-span-2"><label className="mb-1 block text-xs font-bold">Message</label><textarea value={form.message} onChange={set("message")} rows={4} className={input} placeholder="Share your full material list, sizes and timeline…" /></div>
                <div className="sm:col-span-2">
                  <button disabled={status === "sending"} className="btn-brick inline-flex w-full items-center justify-center gap-2 rounded-xl px-6 py-4 font-bold text-white disabled:opacity-60">
                    <Send className="h-4 w-4" /> {status === "sending" ? "Sending…" : "Send Quotation Request"}
                  </button>
                  {status === "error" && <p className="mt-2 text-center text-sm font-semibold text-red-600">Something went wrong. Please try WhatsApp instead.</p>}
                </div>
              </form>
            )}
          </div>
        </div>
      </section>
    </div>
  );
}
