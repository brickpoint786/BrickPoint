"use client";
import { useEffect, useRef } from "react";
import Link from "next/link";
import { MessageCircle, Play, MapPin, ArrowRight, BadgeCheck } from "lucide-react";
import { whatsappLink, productInquiryMessage } from "@/lib/site";

export function Reveal({ children, delay = 0, className = "" }: { children: React.ReactNode; delay?: 0 | 1 | 2 | 3; className?: string }) {
  const ref = useRef<HTMLDivElement>(null);
  useEffect(() => {
    const el = ref.current;
    if (!el) return;
    const io = new IntersectionObserver(
      (entries) => entries.forEach((e) => { if (e.isIntersecting) { el.classList.add("visible"); io.disconnect(); } }),
      { threshold: 0.12 }
    );
    io.observe(el);
    return () => io.disconnect();
  }, []);
  return <div ref={ref} className={`reveal ${delay ? `reveal-delay-${delay}` : ""} ${className}`}>{children}</div>;
}

export function SectionHead({ eyebrow, title, text, light = false, align = "center" }: { eyebrow: string; title: string; text?: string; light?: boolean; align?: "center" | "left" }) {
  return (
    <div className={`${align === "center" ? "mx-auto text-center" : "text-left"} max-w-2xl`}>
      <p className={`text-xs font-black uppercase tracking-[0.22em] ${light ? "text-orange-400" : "text-orange-700"}`}>{eyebrow}</p>
      <h2 className={`font-display mt-3 text-3xl font-black leading-tight md:text-4xl ${light ? "text-white" : "text-[#141210]"}`}>{title}</h2>
      {text && <p className={`mt-3 text-[15px] leading-relaxed ${light ? "text-white/70" : "text-[#6b6560]"}`}>{text}</p>}
    </div>
  );
}

export function WhatsAppButton({ label = "Order on WhatsApp", message, className = "", size = "md" }: { label?: string; message: string; className?: string; size?: "sm" | "md" | "lg" }) {
  const sizes = { sm: "px-3 py-2 text-xs", md: "px-5 py-3 text-sm", lg: "px-7 py-4 text-base" };
  return (
    <a href={whatsappLink(message)} target="_blank" rel="noopener" className={`btn-whatsapp inline-flex items-center justify-center gap-2 rounded-xl font-bold text-white ${sizes[size]} ${className}`}>
      <MessageCircle className="h-4 w-4" /> {label}
    </a>
  );
}

export function ProductCard({ p, categoryName }: { p: any; categoryName?: string }) {
  const msg = productInquiryMessage({ product: p.name, category: categoryName || "", price: p.price ? `${p.price} ${p.priceLabel || ""}`.trim() : null, unit: p.unit });
  return (
    <article className="card-hover group flex flex-col overflow-hidden rounded-2xl border border-black/5 bg-white">
      <Link href={`/products/${p.slug}`} className="img-zoom relative block aspect-[4/3] overflow-hidden bg-stone-200">
        {p.featuredImage ? (
          // eslint-disable-next-line @next/next/no-img-element
          <img src={p.featuredImage} alt={p.name} loading="lazy" className="h-full w-full object-cover" />
        ) : (
          <div className="grid h-full w-full place-items-center bg-gradient-to-br from-stone-300 to-stone-400 text-4xl">🧱</div>
        )}
        <div className="absolute left-3 top-3 flex flex-col gap-2">
          {p.badge && <span className="rounded-full bg-orange-600 px-3 py-1 text-[11px] font-black uppercase tracking-wider text-white">{p.badge}</span>}
          {p.availability && <span className={`rounded-full px-3 py-1 text-[11px] font-bold ${p.availability === "In Stock" ? "bg-emerald-600 text-white" : "bg-black/70 text-white"}`}>{p.availability}</span>}
        </div>
        {p.videoUrl && (
          <span className="absolute bottom-3 right-3 grid h-10 w-10 place-items-center rounded-full bg-black/70 text-white"><Play className="h-4 w-4" /></span>
        )}
      </Link>
      <div className="flex flex-1 flex-col p-5">
        {categoryName && <p className="text-[11px] font-black uppercase tracking-widest text-orange-700">{categoryName}</p>}
        <Link href={`/products/${p.slug}`} className="font-display mt-1 text-lg font-extrabold leading-snug hover:text-orange-700">{p.name}</Link>
        {p.shortDescription && <p className="line-clamp-2 mt-2 text-sm text-[#6b6560]">{p.shortDescription}</p>}
        <div className="mt-3 flex items-baseline gap-2">
          {p.price ? (
            <>
              <span className="font-display text-xl font-black text-[#141210]">{p.price}</span>
              {p.unit && <span className="text-xs font-semibold text-[#6b6560]">/ {p.unit}</span>}
            </>
          ) : (
            <span className="text-sm font-bold text-orange-700">Price on request</span>
          )}
        </div>
        {p.priceLabel && <p className="text-xs text-[#6b6560]">{p.priceLabel}</p>}
        <div className="mt-4 grid grid-cols-2 gap-2">
          <Link href={`/products/${p.slug}`} className="inline-flex items-center justify-center gap-1 rounded-xl border border-black/10 px-3 py-2.5 text-xs font-bold hover:border-orange-600 hover:text-orange-700">
            View Product
          </Link>
          <a href={whatsappLink(msg)} target="_blank" rel="noopener" className="btn-whatsapp inline-flex items-center justify-center gap-1 rounded-xl px-3 py-2.5 text-xs font-bold text-white">
            <MessageCircle className="h-3.5 w-3.5" /> WhatsApp
          </a>
        </div>
      </div>
    </article>
  );
}

export function VideoCard({ v, categoryName }: { v: any; categoryName?: string }) {
  return (
    <Link href={`/videos/${v.slug}`} className="card-hover group overflow-hidden rounded-2xl border border-black/5 bg-white">
      <div className="img-zoom relative aspect-video overflow-hidden bg-black">
        {v.thumbnail ? (
          // eslint-disable-next-line @next/next/no-img-element
          <img src={v.thumbnail} alt={v.title} loading="lazy" className="h-full w-full object-cover opacity-90" />
        ) : (
          <div className="grid h-full w-full place-items-center bg-gradient-to-br from-stone-700 to-stone-900"><Play className="h-10 w-10 text-white/60" /></div>
        )}
        <div className="absolute inset-0 bg-gradient-to-t from-black/70 via-transparent to-transparent" />
        <span className="absolute inset-0 m-auto grid h-14 w-14 place-items-center rounded-full bg-orange-600 text-white shadow-xl transition group-hover:scale-110"><Play className="ml-0.5 h-6 w-6" /></span>
        {v.duration && <span className="absolute bottom-3 right-3 rounded-lg bg-black/80 px-2 py-1 text-[11px] font-bold text-white">{v.duration}</span>}
        {v.featured && <span className="absolute left-3 top-3 inline-flex items-center gap-1 rounded-full bg-amber-400 px-3 py-1 text-[11px] font-black text-black"><BadgeCheck className="h-3 w-3" /> Featured</span>}
      </div>
      <div className="p-5">
        {categoryName && <p className="text-[11px] font-black uppercase tracking-widest text-orange-700">{categoryName}</p>}
        <h3 className="font-display mt-1 font-extrabold leading-snug group-hover:text-orange-700">{v.title}</h3>
        {v.description && <p className="line-clamp-2 mt-2 text-sm text-[#6b6560]">{v.description}</p>}
      </div>
    </Link>
  );
}

export function LocationCard({ l }: { l: any }) {
  return (
    <article className="card-hover flex flex-col overflow-hidden rounded-2xl border border-black/5 bg-white">
      <div className="img-zoom relative aspect-[16/9] overflow-hidden bg-stone-200">
        {l.image ? (
          // eslint-disable-next-line @next/next/no-img-element
          <img src={l.image} alt={l.name} loading="lazy" className="h-full w-full object-cover" />
        ) : (
          <div className="grid h-full w-full place-items-center bg-gradient-to-br from-stone-300 to-stone-500"><MapPin className="h-10 w-10 text-white" /></div>
        )}
      </div>
      <div className="flex flex-1 flex-col p-5">
        <h3 className="font-display text-lg font-extrabold">{l.name}</h3>
        {l.address && <p className="mt-1 flex items-start gap-1.5 text-sm text-[#6b6560]"><MapPin className="mt-0.5 h-4 w-4 shrink-0 text-orange-600" /> {l.address}</p>}
        {l.description && <p className="line-clamp-3 mt-2 text-sm text-[#6b6560]">{l.description}</p>}
        <div className="mt-4 grid grid-cols-2 gap-2">
          {l.mapsUrl && (
            <a href={l.mapsUrl} target="_blank" rel="noopener" className="inline-flex items-center justify-center gap-1 rounded-xl bg-[#141210] px-3 py-2.5 text-xs font-bold text-white hover:bg-black">
              Google Maps <ArrowRight className="h-3.5 w-3.5" />
            </a>
          )}
          <Link href="/contact" className="inline-flex items-center justify-center rounded-xl border border-black/10 px-3 py-2.5 text-xs font-bold hover:border-orange-600 hover:text-orange-700">Contact</Link>
        </div>
      </div>
    </article>
  );
}

export function FloatingWhatsApp() {
  return (
    <a
      href="https://wa.me/923152850818?text=Assalam-o-Alaikum%20BrickPoint%2C%20I%20need%20a%20quotation%20for%20construction%20materials."
      target="_blank"
      rel="noopener"
      aria-label="Chat on WhatsApp"
      className="fixed bottom-5 right-5 z-50 grid h-14 w-14 place-items-center rounded-full bg-[#128c4b] text-white shadow-2xl transition hover:scale-105"
    >
      <MessageCircle className="h-6 w-6" />
      <span className="absolute -right-1 -top-1 h-4 w-4 animate-ping rounded-full bg-emerald-400 opacity-60" />
    </a>
  );
}
