import Link from "next/link";
import { Phone, Mail, MapPin, MessageCircle } from "lucide-react";
import { SITE } from "@/lib/site";

const socialIcon = "h-4 w-4";
function FacebookIcon() { return (<svg viewBox="0 0 24 24" className={socialIcon} fill="currentColor"><path d="M13.5 21v-7h2.4l.4-3h-2.8V9.1c0-.9.3-1.5 1.6-1.5h1.3V4.9c-.3 0-1.1-.1-2-.1-2 0-3.4 1.2-3.4 3.5V11H7.5v3H10v7h3.5Z"/></svg>); }
function InstagramIcon() { return (<svg viewBox="0 0 24 24" className={socialIcon} fill="none" stroke="currentColor" strokeWidth="2"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.2" cy="6.8" r="1.2" fill="currentColor" stroke="none"/></svg>); }
function XIcon() { return (<svg viewBox="0 0 24 24" className={socialIcon} fill="currentColor"><path d="M17.7 3H21l-7.1 8.2L22.2 21h-6.6l-5.1-6.1L4.6 21H1.3l7.6-8.7L1.8 3h6.7l4.6 5.6L17.7 3Zm-1.2 16h1.8L7.1 4.9H5.2L16.5 19Z"/></svg>); }

export default function Footer() {
  return (
    <footer className="relative overflow-hidden bg-[#141210] text-white">
      <div className="brick-lines absolute inset-0 opacity-60" />
      <div className="relative bp-container grid gap-10 py-14 md:grid-cols-2 lg:grid-cols-4">
        <div>
          <div className="flex items-center gap-2.5">
            <span className="grid h-10 w-10 place-items-center rounded-xl bg-gradient-to-br from-orange-500 to-orange-800">
              <svg viewBox="0 0 24 24" className="h-6 w-6 text-white" fill="currentColor"><rect x="2" y="4" width="9" height="4" rx="1" /><rect x="13" y="4" width="9" height="4" rx="1" /><rect x="7.5" y="10" width="9" height="4" rx="1" /><rect x="2" y="16" width="9" height="4" rx="1" /><rect x="13" y="16" width="9" height="4" rx="1" /></svg>
            </span>
            <span className="font-display text-xl font-black">Brick<span className="text-orange-500">Point</span></span>
          </div>
          <p className="mt-4 text-sm leading-relaxed text-white/65">
            Premium bricks and reliable construction materials for homes, commercial developments, and large-scale building projects.
          </p>
          <div className="mt-4 space-y-2 text-sm text-white/75">
            <p className="flex items-center gap-2"><Phone className="h-4 w-4 text-orange-500" /> {SITE.phoneDisplay}</p>
            <p className="flex items-center gap-2"><Mail className="h-4 w-4 text-orange-500" /> {SITE.email}</p>
            <p className="flex items-center gap-2"><MapPin className="h-4 w-4 text-orange-500" /> {SITE.address}</p>
          </div>
          <div className="mt-4 flex gap-2">
            <a href={SITE.social.facebook} target="_blank" rel="noopener" aria-label="Facebook" className="grid h-10 w-10 place-items-center rounded-xl bg-white/10 hover:bg-orange-600"><FacebookIcon /></a>
            <a href={SITE.social.instagram} target="_blank" rel="noopener" aria-label="Instagram" className="grid h-10 w-10 place-items-center rounded-xl bg-white/10 hover:bg-orange-600"><InstagramIcon /></a>
            <a href={SITE.social.twitter} target="_blank" rel="noopener" aria-label="X Twitter" className="grid h-10 w-10 place-items-center rounded-xl bg-white/10 hover:bg-orange-600"><XIcon /></a>
            <a href={SITE.social.tiktok} target="_blank" rel="noopener" aria-label="TikTok" className="grid h-10 w-10 place-items-center rounded-xl bg-white/10 text-sm font-black hover:bg-orange-600">T</a>
          </div>
        </div>
        <div>
          <h4 className="text-sm font-bold uppercase tracking-widest text-orange-400">Products</h4>
          <ul className="mt-4 space-y-2.5 text-sm text-white/70">
            <li><Link href="/ss7-bricks" className="hover:text-white">SS7 Bricks</Link></li>
            <li><Link href="/products" className="hover:text-white">All Products</Link></li>
            <li><Link href="/categories" className="hover:text-white">Product Categories</Link></li>
            <li><Link href="/construction-materials" className="hover:text-white">Construction Materials</Link></li>
            <li><Link href="/videos" className="hover:text-white">Product Videos</Link></li>
          </ul>
          <h4 className="mt-6 text-sm font-bold uppercase tracking-widest text-orange-400">Company</h4>
          <ul className="mt-4 space-y-2.5 text-sm text-white/70">
            <li><Link href="/about" className="hover:text-white">About Us</Link></li>
            <li><Link href="/projects" className="hover:text-white">Projects</Link></li>
            <li><Link href="/blog" className="hover:text-white">Blog</Link></li>
            <li><Link href="/locations" className="hover:text-white">Locations</Link></li>
          </ul>
        </div>
        <div>
          <h4 className="text-sm font-bold uppercase tracking-widest text-orange-400">Who We Serve</h4>
          <ul className="mt-4 space-y-2.5 text-sm text-white/70">
            <li><Link href="/for-contractors" className="hover:text-white">For Contractors</Link></li>
            <li><Link href="/for-builders" className="hover:text-white">For Builders</Link></li>
            <li><Link href="/for-companies" className="hover:text-white">For Construction Companies</Link></li>
            <li><Link href="/contact" className="hover:text-white">Request Quotation</Link></li>
          </ul>
          <h4 className="mt-6 text-sm font-bold uppercase tracking-widest text-orange-400">Our Units</h4>
          <ul className="mt-4 space-y-2.5 text-sm text-white/70">
            {SITE.companies.map((c) => (<li key={c}>{c}</li>))}
            <li className="text-white/50">CEO: {SITE.ceo}</li>
          </ul>
        </div>
        <div>
          <h4 className="text-sm font-bold uppercase tracking-widest text-orange-400">Get a Quotation</h4>
          <p className="mt-4 text-sm text-white/65">Send your material list on WhatsApp and get availability, delivery details and final quotation.</p>
          <a href={SITE.whatsapp} target="_blank" rel="noopener" className="btn-whatsapp mt-4 flex items-center justify-center gap-2 rounded-xl px-4 py-3 text-sm font-bold text-white">
            <MessageCircle className="h-5 w-5" /> Chat on WhatsApp
          </a>
          <Link href="/contact" className="mt-2 flex items-center justify-center rounded-xl bg-white/10 px-4 py-3 text-sm font-bold hover:bg-white/15">Contact Form</Link>
          <Link href="/wordpress-theme" className="mt-2 flex items-center justify-center rounded-xl border border-orange-500/40 bg-orange-600/10 px-4 py-3 text-sm font-bold text-orange-300 hover:bg-orange-600/20">Download WP Theme</Link>
        </div>
      </div>
      <div className="relative border-t border-white/10">
        <div className="bp-container flex flex-col items-center justify-between gap-3 py-5 text-xs text-white/50 md:flex-row">
          <p>© {new Date().getFullYear()} BrickPoint. All rights reserved.</p>
          <div className="flex gap-5">
            <Link href="/privacy" className="hover:text-white">Privacy Policy</Link>
            <Link href="/terms" className="hover:text-white">Terms & Conditions</Link>
            <Link href="/wordpress-theme" className="hover:text-white">Theme Docs</Link>
          </div>
        </div>
      </div>
    </footer>
  );
}
