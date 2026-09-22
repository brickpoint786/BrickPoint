export const SITE = {
  brand: "BrickPoint",
  tagline: "Premium Bricks & Construction Materials",
  phoneDisplay: "0315 2850818",
  phoneIntl: "923152850818",
  whatsapp: "https://wa.me/923152850818",
  email: "info@brickpoint.pk",
  address: "Lahore, Punjab, Pakistan",
  ceo: "Syed Iftikhar Haider",
  salesManager: "Qasim Iqbal",
  companies: ["Masha Allah Bricks Company", "Fine Bricks Company", "SS7 Bricks"],
  social: {
    facebook: "https://www.facebook.com/brickpoint.pk/",
    instagram: "https://www.instagram.com/brickpoint.pk/",
    twitter: "https://x.com/BrickPointPK",
    tiktok: "https://www.tiktok.com/@brickpoint.pk/",
  },
};

export function whatsappLink(message: string, phone = SITE.phoneIntl) {
  return `https://wa.me/${phone}?text=${encodeURIComponent(message)}`;
}

export function productInquiryMessage(opts: {
  product: string;
  category?: string | null;
  price?: string | null;
  unit?: string | null;
  quantity?: string;
  customerMessage?: string;
}) {
  const lines = [
    "Assalam-o-Alaikum BrickPoint,",
    "",
    "I am interested in the following product:",
    "",
    `Product: ${opts.product}`,
    `Category: ${opts.category || "-"}`,
    `Price: ${opts.price || "Please quote"}`,
    `Unit: ${opts.unit || "-"}`,
  ];
  if (opts.quantity) lines.push(`Quantity: ${opts.quantity}`);
  if (opts.customerMessage) lines.push(`Message: ${opts.customerMessage}`);
  lines.push("", "Please share availability, delivery details, and final quotation.", "", "Thank you.");
  return lines.join("\n");
}

export function categoryInquiryMessage(category: string) {
  return [
    "Assalam-o-Alaikum BrickPoint,",
    "",
    `I want a quotation for: ${category}`,
    "",
    "Please share price, availability and delivery details.",
    "",
    "Thank you.",
  ].join("\n");
}

export const NAV_LINKS = [
  { label: "Home", href: "/" },
  { label: "Products", href: "/products", children: [
    { label: "All Products", href: "/products" },
    { label: "Categories", href: "/categories" },
    { label: "SS7 Bricks", href: "/ss7-bricks" },
    { label: "Construction Materials", href: "/construction-materials" },
  ]},
  { label: "SS7 Bricks", href: "/ss7-bricks" },
  { label: "Projects", href: "/projects" },
  { label: "Videos", href: "/videos" },
  { label: "Locations", href: "/locations" },
  { label: "About", href: "/about" },
  { label: "Blog", href: "/blog" },
  { label: "Contact", href: "/contact" },
];
