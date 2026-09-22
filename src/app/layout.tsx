import type { Metadata } from "next";
import type { ReactNode } from "react";
import "./globals.css";
import Header from "@/components/Header";
import Footer from "@/components/Footer";
import { FloatingWhatsApp } from "@/components/ui";

export const metadata: Metadata = {
  title: { default: "BrickPoint — Premium Bricks & Construction Materials", template: "%s | BrickPoint" },
  description: "Premium bricks and reliable construction materials for homes, commercial developments, and large-scale building projects. SS7 Bricks, cement, bajri, sand, steel & more.",
  openGraph: {
    title: "BrickPoint — Building Strength. Delivering Quality.",
    description: "Premium bricks & construction materials. WhatsApp ordering, bhatta locations, project references and videos.",
    type: "website",
  },
};

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en">
      <head>
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="anonymous" />
        <link href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700;800;900&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet" />
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{
            __html: JSON.stringify({
              "@context": "https://schema.org",
              "@type": "Organization",
              name: "BrickPoint",
              description: "Construction-materials supplier providing bricks and building materials.",
              telephone: "+92-315-2850818",
              sameAs: [
                "https://www.facebook.com/brickpoint.pk/",
                "https://www.instagram.com/brickpoint.pk/",
                "https://x.com/BrickPointPK",
                "https://www.tiktok.com/@brickpoint.pk/",
              ],
            }),
          }}
        />
      </head>
      <body className="bg-[#faf8f5] text-[#141210] antialiased">
        <Header />
        <main className="min-h-screen">{children}</main>
        <Footer />
        <FloatingWhatsApp />
      </body>
    </html>
  );
}
