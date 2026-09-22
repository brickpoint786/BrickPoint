import { NextResponse } from "next/server";
import { db } from "@/db";
import { productCategories, products, videoCategories, videos, projects, locations, posts, settings } from "@/db/schema";
import { PRODUCT_CATEGORIES_SEED, VIDEO_CATEGORIES_SEED, LOCATIONS_SEED, IMG, VID } from "@/db/seed-data";

export async function POST() {
  try {
    // Categories
    for (const c of PRODUCT_CATEGORIES_SEED) {
      await db.insert(productCategories).values(c).onConflictDoNothing();
    }
    for (const c of VIDEO_CATEGORIES_SEED) {
      await db.insert(videoCategories).values(c).onConflictDoNothing();
    }
    const cats = await db.select().from(productCategories);
    const catId = (slug: string) => cats.find((c) => c.slug === slug)?.id ?? null;
    const vcats = await db.select().from(videoCategories);
    const vcatId = (slug: string) => vcats.find((c) => c.slug === slug)?.id ?? null;

    // Products
    const seedProducts = [
      { name: "SS7 Premium Bricks", slug: "ss7-premium-bricks", categoryId: catId("ss7-bricks"), featuredImage: IMG.redStack, gallery: [IMG.stacked, IMG.pile, IMG.worker], shortDescription: "Flagship SS7 burnt-clay bricks — high strength, sharp edges, consistent firing.", fullDescription: "SS7 Premium Bricks are BrickPoint's flagship range. Manufactured at our trusted bhatta units with controlled firing for strength and dimensional consistency. Ideal for homes, commercial buildings and boundary walls. Contact us on WhatsApp for current pricing, availability and delivery scheduling.", price: "Rs. Contact for Rate", priceLabel: "Market-competitive bulk pricing", unit: "1000 bricks", availability: "In Stock", badge: "Best Seller", specifications: [{ label: "Type", value: "Burnt-clay SS7" }, { label: "Usage", value: "Residential, commercial, boundary walls" }, { label: "Availability", value: "Bulk & retail" }, { label: "Delivery Area", value: "Confirm on WhatsApp" }], features: ["High crushing strength", "Uniform size & sharp edges", "Consistent kiln firing", "Bulk order support"], sku: "BP-SS7-001", featured: true, videoUrl: VID.hero, videoType: "mp4", sortOrder: 1 },
      { name: "Awwal Burnt-Clay Bricks", slug: "awwal-bricks", categoryId: catId("bricks"), featuredImage: IMG.stacked, gallery: [IMG.pile, IMG.redStack], shortDescription: "Quality awwal-grade bricks for reliable masonry work.", fullDescription: "Awwal-grade burnt-clay bricks suitable for load-bearing and partition walls. Sorted for quality with dependable supply for projects of any size.", price: "Rs. Contact for Rate", priceLabel: "Grade-wise pricing available", unit: "1000 bricks", availability: "In Stock", badge: "Popular", specifications: [{ label: "Grade", value: "Awwal" }, { label: "Usage", value: "Walls, partitions, structures" }], features: ["Grade-sorted batches", "Reliable supply"], sku: "BP-BR-002", featured: true, sortOrder: 2 },
      { name: "Portland Cement (OPC)", slug: "portland-cement-opc", categoryId: catId("cement"), featuredImage: IMG.site, gallery: [], shortDescription: "Fresh stock cement for concrete, masonry and plaster.", fullDescription: "Quality Ordinary Portland Cement sourced fresh for strength and workability. Available for retail and bulk project supply.", price: "Rs. Contact for Rate", priceLabel: "Brand options on request", unit: "bag", availability: "In Stock", badge: "", specifications: [{ label: "Type", value: "OPC" }, { label: "Packing", value: "Standard bag" }], features: ["Fresh stock", "Bulk rates"], sku: "BP-CM-003", featured: true, sortOrder: 3 },
      { name: "Crush / Bajri (Graded)", slug: "crush-bajri-graded", categoryId: catId("bajri-crush"), featuredImage: IMG.pile, gallery: [], shortDescription: "Graded crush for foundations, concrete and road base.", fullDescription: "Machine-crushed graded bajri in multiple sizes for RCC, PCC and foundation work. Trolley and bulk supply available.", price: "Rs. Contact for Rate", priceLabel: "Per trolley / per brass options", unit: "trolley", availability: "In Stock", badge: "", specifications: [{ label: "Sizes", value: "Confirm on quote" }], features: ["Graded sizes", "Clean material"], sku: "BP-CR-004", featured: true, sortOrder: 4 },
      { name: "Clean Sand / Rait", slug: "clean-sand-rait", categoryId: catId("sand-rait"), featuredImage: IMG.align, gallery: [], shortDescription: "Clean sand for masonry, plaster and concrete mixes.", fullDescription: "Washed and screened sand suitable for all construction mixes. Consistent quality with bulk delivery options.", price: "Rs. Contact for Rate", priceLabel: "Trolley pricing", unit: "trolley", availability: "In Stock", badge: "", specifications: [{ label: "Type", value: "Construction sand" }], features: ["Screened", "Bulk supply"], sku: "BP-SD-005", featured: false, sortOrder: 5 },
      { name: "Deformed Steel Bars", slug: "deformed-steel-bars", categoryId: catId("steel"), featuredImage: IMG.site, gallery: [], shortDescription: "Structural reinforcement steel for RCC work.", fullDescription: "High-strength deformed bars for beams, columns, slabs and foundations. Cut-to-length coordination available for projects.", price: "Rs. Contact for Rate", priceLabel: "Per kg / per ton", unit: "kg", availability: "In Stock", badge: "", specifications: [{ label: "Grades", value: "Confirm on quote" }], features: ["Project quantities", "Reliable sourcing"], sku: "BP-ST-006", featured: true, sortOrder: 6 },
      { name: "Electric Conduit Pipe Pack", slug: "electric-conduit-pipe", categoryId: catId("electric-conduit-pipes"), featuredImage: IMG.cables, gallery: [], shortDescription: "Durable PVC conduit pipes for concealed wiring.", fullDescription: "Flame-retardant conduit pipes in standard diameters for residential and commercial electrical work.", price: "Rs. Contact for Rate", priceLabel: "Per bundle options", unit: "bundle", availability: "In Stock", badge: "", specifications: [], features: ["Multiple diameters"], sku: "BP-EL-007", featured: false, sortOrder: 7 },
      { name: "Plumbing Pipe & Fittings Set", slug: "plumbing-pipe-fittings", categoryId: catId("plumbing-pipes"), featuredImage: IMG.wall, gallery: [], shortDescription: "Pressure-rated pipes with complete fitting range.", fullDescription: "Complete plumbing range — pipes, elbows, tees, sockets and valves for water supply and drainage.", price: "Rs. Contact for Rate", priceLabel: "Complete range", unit: "set", availability: "In Stock", badge: "", specifications: [], features: ["Full fitting range"], sku: "BP-PL-008", featured: false, sortOrder: 8 },
      { name: "Waterproofing Chemical Kit", slug: "waterproofing-chemical-kit", categoryId: catId("construction-chemicals"), featuredImage: IMG.brickMason, gallery: [], shortDescription: "Waterproofing and bonding chemicals for lasting protection.", fullDescription: "Construction chemicals for waterproofing roofs, basements, tanks and bathrooms. Application guidance available.", price: "Rs. Contact for Rate", priceLabel: "Kit pricing", unit: "kit", availability: "In Stock", badge: "New", specifications: [], features: ["Roof & basement use"], sku: "BP-CH-009", featured: true, sortOrder: 9 },
      { name: "Insulation Membrane Roll", slug: "insulation-membrane-roll", categoryId: catId("insulation-membrane"), featuredImage: IMG.villa1, gallery: [], shortDescription: "Heat and water insulation membranes for roofs.", fullDescription: "Roof insulation and waterproofing membranes for energy efficiency and leak protection.", price: "Rs. Contact for Rate", priceLabel: "Per roll", unit: "roll", availability: "In Stock", badge: "", specifications: [], features: ["Roof application"], sku: "BP-IN-010", featured: false, sortOrder: 10 },
      { name: "Copper Wiring Cable Coil", slug: "copper-wiring-cable", categoryId: catId("cables-wires"), featuredImage: IMG.cables, gallery: [], shortDescription: "Pure copper cables for safe, lasting wiring.", fullDescription: "Quality copper conductor cables in standard gauges for house wiring and commercial circuits.", price: "Rs. Contact for Rate", priceLabel: "Per coil", unit: "coil", availability: "In Stock", badge: "", specifications: [], features: ["Multiple gauges"], sku: "BP-CB-011", featured: false, sortOrder: 11 },
      { name: "Weather-Shield Exterior Paint", slug: "weather-shield-paint", categoryId: catId("paints"), featuredImage: IMG.villa2, gallery: [], shortDescription: "Long-life exterior paint with weather protection.", fullDescription: "Premium exterior emulsion with UV and rain resistance. Shade cards available on request.", price: "Rs. Contact for Rate", priceLabel: "Per gallon", unit: "gallon", availability: "In Stock", badge: "", specifications: [], features: ["Shade options"], sku: "BP-PT-012", featured: false, sortOrder: 12 },
    ];
    for (const p of seedProducts) {
      await db.insert(products).values(p as any).onConflictDoNothing();
    }

    // Videos
    const seedVideos = [
      { title: "SS7 Bricks — Strength You Can See", slug: "ss7-strength", description: "A close look at SS7 brick quality, firing and finish.", categoryId: vcatId("ss7-bricks"), thumbnail: VID.heroPoster, sourceType: "mp4", videoUrl: VID.hero, duration: "0:14", featured: true, displayOrder: 1 },
      { title: "Inside Our Bhatta — Brick Making Process", slug: "bhatta-process", description: "From clay preparation to firing and stacking.", categoryId: vcatId("brick-manufacturing"), thumbnail: IMG.kiln, sourceType: "mp4", videoUrl: VID.site, duration: "0:16", featured: true, displayOrder: 2 },
      { title: "Bricks in Action — Site Work", slug: "site-work", description: "Masonry work and material handling on site.", categoryId: vcatId("construction-projects"), thumbnail: VID.sitePoster, sourceType: "mp4", videoUrl: VID.site, duration: "0:16", featured: false, displayOrder: 3 },
      { title: "Aerial View — Developments We Supply", slug: "aerial-developments", description: "Illustrative aerial construction reference.", categoryId: vcatId("construction-projects"), thumbnail: VID.aerialPoster, sourceType: "mp4", videoUrl: VID.aerial, duration: "0:14", featured: true, displayOrder: 4 },
      { title: "Brick Quality Check", slug: "brick-quality-check", description: "How we check strength, shape and sound of bricks.", categoryId: vcatId("brick-quality"), thumbnail: IMG.stacked, sourceType: "youtube", videoUrl: "https://www.youtube.com/embed/dQw4w9WgXcQ", duration: "2:30", featured: false, displayOrder: 5 },
      { title: "BrickPoint Brand Story", slug: "brand-story", description: "Who we are and how we support builders.", categoryId: vcatId("company-brand"), thumbnail: IMG.bricklayer, sourceType: "mp4", videoUrl: VID.drone, duration: "1:20", featured: true, displayOrder: 6 },
    ];
    for (const v of seedVideos) {
      await db.insert(videos).values(v as any).onConflictDoNothing();
    }

    // Projects (illustrative)
    const seedProjects = [
      { title: "DHA Lahore — Villa Construction Reference", slug: "dha-lahore-villa", category: "Residential", location: "DHA Lahore", description: "Illustrative construction reference showing villa-scale masonry and finishing work typical of DHA Lahore developments.", featuredImage: IMG.villa1, status: "Illustrative construction reference", featured: true, illustrative: true, sortOrder: 1 },
      { title: "Bahria Town — Housing Reference", slug: "bahria-town-housing", category: "Residential", location: "Bahria Town Lahore", description: "Illustrative construction reference for housing-scale brickwork and material usage.", featuredImage: IMG.villa2, status: "Illustrative construction reference", featured: true, illustrative: true, sortOrder: 2 },
      { title: "Lake City — Development Reference", slug: "lake-city-dev", category: "Development", location: "Lake City Lahore", description: "Illustrative construction reference for large development blocks and apartment construction.", featuredImage: IMG.apt, status: "Illustrative construction reference", featured: true, illustrative: true, sortOrder: 3 },
      { title: "Etihad Town — Block Reference", slug: "etihad-town-block", category: "Residential", location: "Etihad Town Lahore", description: "Illustrative construction reference for block development and boundary structures.", featuredImage: IMG.villa3, status: "Illustrative construction reference", featured: false, illustrative: true, sortOrder: 4 },
      { title: "Al-Kabir Town — Commercial Reference", slug: "alkabir-commercial", category: "Commercial", location: "Al-Kabir Town", description: "Illustrative construction reference for commercial masonry and finishing.", featuredImage: IMG.site, status: "Illustrative construction reference", featured: false, illustrative: true, sortOrder: 5 },
      { title: "Paragon City — Villa Reference", slug: "paragon-city-villa", category: "Residential", location: "Paragon City", description: "Illustrative construction reference showing premium villa construction stages.", featuredImage: IMG.brickMason, status: "Illustrative construction reference", featured: false, illustrative: true, sortOrder: 6 },
    ];
    for (const p of seedProjects) {
      await db.insert(projects).values(p as any).onConflictDoNothing();
    }

    for (const l of LOCATIONS_SEED) {
      await db.insert(locations).values(l as any).onConflictDoNothing();
    }

    const seedPosts = [
      { title: "How to Choose the Right Bricks for Your House", slug: "choose-right-bricks", excerpt: "Awwal vs SS7, strength checks, and what to ask your supplier before ordering.", content: "Choosing bricks is the most important material decision for your house. In this guide we cover brick grades, simple field tests (shape, sound, water absorption), and the questions to ask your supplier — including firing consistency, batch sorting and delivery planning. For project pricing, share your covered area and wall schedule on WhatsApp and we will estimate quantities.", featuredImage: IMG.stacked, category: "Brick Selection", tags: ["bricks", "guide"], author: "BrickPoint Team" },
      { title: "Cement, Sand and Crush: Correct Ratios Explained", slug: "cement-sand-crush-ratios", excerpt: "Simple ratios for PCC, RCC and masonry mortar — and mistakes to avoid.", content: "Correct mix ratios decide the strength of your structure. We explain standard PCC (1:4:8), RCC (1:2:4) and mortar (1:4 / 1:6) mixes, water-cement discipline, curing time, and the common mistakes that weaken concrete. Always confirm structural mixes with your engineer.", featuredImage: IMG.site, category: "Material Guides", tags: ["cement", "concrete"], author: "BrickPoint Team" },
      { title: "Brick Manufacturing: From Bhatta to Building", slug: "brick-manufacturing-bhatta", excerpt: "Clay preparation, moulding, drying, firing and quality sorting.", content: "Every brick passes through clay preparation, moulding, sun drying, kiln firing and sorting. Consistent firing temperature and proper stacking decide final strength and colour. This article walks through each stage so buyers understand what quality firing looks like.", featuredImage: IMG.kiln, category: "Manufacturing", tags: ["bhatta", "quality"], author: "BrickPoint Team" },
      { title: "Material Planning Checklist for a 5-Marla House", slug: "5-marla-checklist", excerpt: "Bricks, cement, steel, sand and crush — how to plan stage-wise.", content: "A stage-wise material plan prevents over-ordering and site delays. We share a practical checklist for foundation, grey structure, masonry, plaster and finishing stages — with tips on storage, wastage allowance and delivery scheduling around Lahore.", featuredImage: IMG.bricklayer, category: "Planning", tags: ["planning", "estimate"], author: "BrickPoint Team" },
    ];
    for (const p of seedPosts) {
      await db.insert(posts).values(p as any).onConflictDoNothing();
    }

    const seedSettings = [
      ["phone", "0315 2850818"],
      ["whatsapp", "923152850818"],
      ["email", "info@brickpoint.pk"],
      ["hero_video", VID.hero],
      ["hero_poster", VID.heroPoster],
      ["facebook", "https://www.facebook.com/brickpoint.pk/"],
      ["instagram", "https://www.instagram.com/brickpoint.pk/"],
      ["twitter", "https://x.com/BrickPointPK"],
      ["tiktok", "https://www.tiktok.com/@brickpoint.pk/"],
    ];
    for (const [key, value] of seedSettings) {
      await db.insert(settings).values({ key, value }).onConflictDoNothing();
    }

    return NextResponse.json({ ok: true, message: "Seeded BrickPoint catalogue" });
  } catch (e: any) {
    return NextResponse.json({ ok: false, error: e?.message || "seed failed" }, { status: 500 });
  }
}

export async function GET() {
  return POST();
}
