"use client";
import Link from "next/link";
import { useEffect, useState } from "react";
import { Menu, X, Phone, ChevronDown, MessageCircle } from "lucide-react";
import { SITE, NAV_LINKS } from "@/lib/site";

function Logo() {
  return (
    <Link href="/" className="flex items-center gap-2.5" aria-label="BrickPoint home">
      <span className="grid h-10 w-10 place-items-center rounded-xl bg-gradient-to-br from-orange-500 to-orange-800 shadow-lg shadow-orange-900/40">
        <svg viewBox="0 0 24 24" className="h-6 w-6 text-white" fill="currentColor" aria-hidden>
          <rect x="2" y="4" width="9" height="4" rx="1" />
          <rect x="13" y="4" width="9" height="4" rx="1" />
          <rect x="7.5" y="10" width="9" height="4" rx="1" />
          <rect x="2" y="16" width="9" height="4" rx="1" />
          <rect x="13" y="16" width="9" height="4" rx="1" />
        </svg>
      </span>
      <span className="leading-none">
        <span className="font-display block text-xl font-900 font-black tracking-tight text-white">Brick<span className="text-orange-500">Point</span></span>
        <span className="block text-[10px] font-semibold uppercase tracking-[0.18em] text-white/60">Bricks & Materials</span>
      </span>
    </Link>
  );
}

export default function Header() {
  const [open, setOpen] = useState(false);
  const [scrolled, setScrolled] = useState(false);
  const [drop, setDrop] = useState(false);

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 24);
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  useEffect(() => {
    document.body.style.overflow = open ? "hidden" : "";
    return () => { document.body.style.overflow = ""; };
  }, [open ]);

  return (
    <>
      <div className="hidden bg-[#141210] text-white/80 md:block">
        <div className="bp-container flex items-center justify-between py-2 text-xs">
          <p className="flex flex-wrap items-center gap-x-4 gap-y-1">
            <span className="inline-flex items-center gap-1.5"><Phone className="h-3.5 w-3.5 text-orange-500" /> {SITE.phoneDisplay}</span>
            <span className="hidden lg:inline text-white/50">Masha Allah Bricks Co. • Fine Bricks Co. • SS7 Bricks</span>
          </p>
          <div className="flex items-center gap-4">
            <Link href="/locations" className="hover:text-white">Our Bhattas</Link>
            <Link href="/videos" className="hover:text-white">Videos</Link>
            <Link href="/wordpress-theme" className="rounded-full bg-orange-600/20 px-3 py-1 font-semibold text-orange-300 hover:bg-orange-600/30">WP Theme</Link>
          </div>
        </div>
      </div>
      <header className={`sticky-header sticky top-0 z-50 bg-[#141210]/80 backdrop-blur ${scrolled ? "scrolled" : ""}`}>
        <div className="bp-container flex h-[72px] items-center justify-between gap-4">
          <Logo />
          <nav className="hidden items-center gap-1 lg:flex" aria-label="Main navigation">
            {NAV_LINKS.slice(0, 8).map((l) =>
              l.children ? (
                <div key={l.label} className="relative" onMouseEnter={() => setDrop(true)} onMouseLeave={() => setDrop(false)}>
                  <button className="flex items-center gap-1 rounded-lg px-3 py-2 text-sm font-semibold text-white/85 hover:bg-white/10 hover:text-white">
                    {l.label} <ChevronDown className="h-4 w-4" />
                  </button>
                  {drop && (
                    <div className="absolute left-0 top-full w-64 pt-2">
                      <div className="overflow-hidden rounded-2xl border border-white/10 bg-[#1c1a17] p-2 shadow-2xl">
                        {l.children.map((c) => (
                          <Link key={c.href + c.label} href={c.href} className="block rounded-xl px-4 py-2.5 text-sm text-white/80 hover:bg-orange-600 hover:text-white">
                            {c.label}
                          </Link>
                        ))}
                        <Link href="/for-contractors" className="block rounded-xl px-4 py-2.5 text-sm text-white/60 hover:bg-white/10 hover:text-white">For Contractors →</Link>
                      </div>
                    </div>
                  )}
                </div>
              ) : (
                <Link key={l.label} href={l.href} className="rounded-lg px-3 py-2 text-sm font-semibold text-white/85 hover:bg-white/10 hover:text-white">
                  {l.label}
                </Link>
              )
            )}
          </nav>
          <div className="hidden items-center gap-2 lg:flex">
            <a href={SITE.whatsapp} target="_blank" rel="noopener" className="btn-whatsapp inline-flex items-center gap-2 rounded-xl px-4 py-2.5 text-sm font-bold text-white">
              <MessageCircle className="h-4 w-4" /> WhatsApp Us
            </a>
            <Link href="/contact" className="btn-brick inline-flex items-center gap-2 rounded-xl px-4 py-2.5 text-sm font-bold text-white">
              Request Quote
            </Link>
          </div>
          <button onClick={() => setOpen(true)} className="grid h-11 w-11 place-items-center rounded-xl bg-white/10 text-white lg:hidden" aria-label="Open menu">
            <Menu className="h-5 w-5" />
          </button>
        </div>
      </header>

      {open && (
        <div className="fixed inset-0 z-[60] lg:hidden">
          <div className="absolute inset-0 bg-black/60" onClick={() => setOpen(false)} />
          <div className="absolute right-0 top-0 flex h-full w-[88%] max-w-sm flex-col bg-[#1c1a17] p-6 text-white shadow-2xl">
            <div className="flex items-center justify-between">
              <Logo />
              <button onClick={() => setOpen(false)} className="grid h-10 w-10 place-items-center rounded-xl bg-white/10" aria-label="Close menu">
                <X className="h-5 w-5" />
              </button>
            </div>
            <nav className="mt-6 flex-1 space-y-1 overflow-y-auto" aria-label="Mobile navigation">
              {NAV_LINKS.map((l) => (
                <div key={l.label}>
                  <Link href={l.href} onClick={() => setOpen(false)} className="block rounded-xl px-4 py-3 font-semibold text-white/90 hover:bg-white/10">
                    {l.label}
                  </Link>
                  {l.children?.map((c) => (
                    <Link key={c.label} href={c.href} onClick={() => setOpen(false)} className="ml-4 block rounded-lg px-4 py-2 text-sm text-white/60 hover:bg-white/10 hover:text-white">
                      — {c.label}
                    </Link>
                  ))}
                </div>
              ))}
              <div className="grid grid-cols-2 gap-2 pt-2">
                <Link href="/for-contractors" onClick={() => setOpen(false)} className="rounded-xl bg-white/5 px-4 py-3 text-sm font-semibold">For Contractors</Link>
                <Link href="/for-builders" onClick={() => setOpen(false)} className="rounded-xl bg-white/5 px-4 py-3 text-sm font-semibold">For Builders</Link>
                <Link href="/for-companies" onClick={() => setOpen(false)} className="rounded-xl bg-white/5 px-4 py-3 text-sm font-semibold">For Companies</Link>
                <Link href="/blog" onClick={() => setOpen(false)} className="rounded-xl bg-white/5 px-4 py-3 text-sm font-semibold">Blog</Link>
              </div>
            </nav>
            <div className="space-y-2 pt-4">
              <a href={SITE.whatsapp} target="_blank" rel="noopener" className="btn-whatsapp flex items-center justify-center gap-2 rounded-xl px-4 py-3 font-bold">
                <MessageCircle className="h-4 w-4" /> WhatsApp: {SITE.phoneDisplay}
              </a>
              <Link href="/contact" onClick={() => setOpen(false)} className="btn-brick flex items-center justify-center rounded-xl px-4 py-3 font-bold text-white">
                Request a Quote
              </Link>
            </div>
          </div>
        </div>
      )}
    </>
  );
}
