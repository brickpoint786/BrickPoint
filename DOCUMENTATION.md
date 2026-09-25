# BrickPoint WordPress Theme Technical Documentation

This document provides complete technical specifications, architecture details, and developer guides for the **BrickPoint** WordPress theme.

---

## Table of Contents

1. [Architecture Overview](#1-architecture-overview)
2. [Custom Post Types & Taxonomies](#2-custom-post-types--taxonomies)
3. [Meta Fields & Data Storage](#3-meta-fields--data-storage)
4. [No-WooCommerce WhatsApp Ordering Engine](#4-no-woocommerce-whatsapp-ordering-engine)
5. [Elementor Free & Elementor Pro Theme Builder Integration](#5-elementor-free--elementor-pro-theme-builder-integration)
6. [The 13 Custom Elementor Widgets](#6-the-13-custom-elementor-widgets)
7. [The 24 Bundled Elementor Templates](#7-the-24-bundled-elementor-templates)
8. [The 17 Complete Site Pages](#8-the-17-complete-site-pages)
9. [The 12 Construction Products Catalogue](#9-the-12-construction-products-catalogue)
10. [Independent Header & Footer Logos](#10-independent-header--footer-logos)
11. [One-Click Demo Importer & Offline Media](#11-one-click-demo-importer--offline-media)
12. [Theme Customizer & Options](#12-theme-customizer--options)

---

## 1. Architecture Overview

BrickPoint is built as a hybrid WordPress theme that achieves 100% visual and functional parity with the Next.js React frontend:
- **Pure Native Fallback:** If Elementor is inactive, the theme renders native PHP templates (`front-page.php`, `single-bp_product.php`, etc.) using high-performance semantic markup, CSS variables, and modern flexbox/grid layouts.
- **Full Elementor Native Integration:** If a page or single template is edited with Elementor, `the_content()` outputs native Elementor container and widget markup without any wrappers or restrictions.
- **Theme Builder Locations:** Native registration for Elementor Pro Theme Builder locations (`header`, `footer`, `single`, `archive`) ensures that users who own Elementor Pro can override headers, footers, and archive layouts seamlessly via the Elementor Theme Builder UI.

---

## 2. Custom Post Types & Taxonomies

| Post Type / Taxonomy | Slug / Rewrite | Public | Description |
| :--- | :--- | :--- | :--- |
| **`bp_product`** | `product/` (archive: `products`) | Yes | Construction materials & bricks catalogue. No cart or checkout. |
| **`bp_video`** | `video/` (archive: `videos`) | Yes | Production plant, bhatta operations, and site videos. |
| **`bp_project`** | `project/` (archive: `projects`) | Yes | Housing society construction references & landmarks. |
| **`bp_location`** | `location/` (archive: `locations`) | Yes | Brick kiln manufacturing units and corporate offices. |
| **`bp_product_category`** | `product-category/` | Yes | Hierarchical category taxonomy for products. |
| **`bp_video_category`** | `video-category/` | Yes | Hierarchical category taxonomy for video library. |

---

## 3. Meta Fields & Data Storage

All custom post types use standard WordPress post meta (`wp_postmeta`) with clean sanitization hooks:

### Product Meta (`bp_product`)
- `_bp_price`: Listed rate string (e.g. `Rs 14,000`, `Rs 1,450`, `Rs 255,000`).
- `_bp_price_label`: Pricing subtext (e.g. `per 1,000 bricks`, `per 50 kg bag`, `per metric ton`).
- `_bp_unit`: Unit indicator (e.g. `1000 Bricks`, `Bag`, `CFT`, `Ton`, `Coil`).
- `_bp_availability`: Stock status (`In Stock`, `Made to Order`).
- `_bp_badge`: Promoted card badge (e.g. `Flagship Product`, `Certified Grade`).
- `_bp_featured`: Flag for homepage and featured query (`1` or `0`).
- `_bp_sku`: Inventory / item reference code.
- `_bp_short`: Short summary shown on archive cards.
- `_bp_gallery`: Multi-line image URLs for the product image gallery.
- `_bp_specs`: Multi-line key-value specifications (`Label: Value`).
- `_bp_features`: Multi-line checklist items.
- `_bp_video`: Direct MP4 video preview URL.
- `_bp_brochure`: Technical PDF datasheet download URL.
- `_bp_whatsapp`: Custom WhatsApp message override text.

### Video Meta (`bp_video`)
- `_bpv_source`: Video source type (`mp4`, `youtube`, `vimeo`).
- `_bpv_url`: Embed or hosted video URL.
- `_bpv_file`: Direct file fallback URL.
- `_bpv_duration`: Video length string (e.g. `1:45`, `2:10`).
- `_bpv_featured`: Featured flag (`1` or `0`).

### Project Meta (`bp_project`)
- `_bpp_category`: Project sector (`Residential`, `Commercial`, `Community`).
- `_bpp_location`: Project society or area (e.g. `DHA Lahore`, `Bahria Town`).
- `_bpp_status`: Notice label (default: `Illustrative construction reference`).

### Location Meta (`bp_location`)
- `_bpl_address`: Physical address of kiln or office.
- `_bpl_phone`: Specific telephone contact.
- `_bpl_hours`: Working operating hours.
- `_bpl_maps_url`: Direct Google Maps link for GPS navigation.
- `_bpl_video`: Virtual tour MP4 video URL.

---

## 4. No-WooCommerce WhatsApp Ordering Engine

BrickPoint deliberately avoids WooCommerce to ensure zero e-commerce friction. In the Pakistani construction sector, contractors, builders, and home owners require negotiated bulk pricing, transport coordination, and immediate responses.

### Functions:
1. `bp_whatsapp_clean_phone($phone)`: Strips spaces, dashes, and plus signs to output a clean international number (e.g. `923152850818`).
2. `bp_whatsapp_url($message, $phone)`: Constructs an HTTPS URL targeting `https://api.whatsapp.com/send?phone=...&text=...`.
3. `bp_product_inquiry_message($args)`: Generates a structured inquiry containing product title, category, rate, unit, and request for delivery terms.
4. `bp_category_inquiry_message($category_name)`: Prepares a category-wide rate inquiry.

---

## 5. Elementor Free & Elementor Pro Theme Builder Integration

### Free Elementor Support:
- Any page can be opened in the Elementor visual editor.
- The theme sets `body` width, container margins, and CSS custom properties so that standard Elementor widgets (Headings, Text, Images, Buttons, Icons, Accordions) look identical to native theme components.

### Elementor Pro Theme Builder:
- Locations registered via `elementor/theme/register_locations`:
  - `header`
  - `footer`
  - `single`
  - `archive`
- If a user builds a template in Theme Builder and assigns conditions (e.g. *Entire Site*, *Products*, *Single Post*), the theme automatically yields execution to `elementor_theme_do_location()`. If no Theme Builder template is active, the theme renders the pixel-perfect PHP template.

---

## 6. The 13 Custom Elementor Widgets

All widgets are located in `inc/elementor-widgets.php` and registered in the `BrickPoint Theme Elements` category:

1. **`bp_hero`**: Full hero section with video loop frame, SS7 3D floating brick card, action buttons, trust points, and animated marquee ticker.
2. **`bp_ss7_showcase`**: Flagship SS7 burnt-clay brick showcase, 4-point specifications grid, image gallery, and direct WhatsApp quote button.
3. **`bp_product_grid`**: Live catalog grid with query controls (count, columns: 2/3/4), pricing, badges, and WhatsApp ordering buttons.
4. **`bp_category_grid`**: 12 Category cards with background image overlays, descriptions, and arrow links.
5. **`bp_video_showcase`**: Video showcase featuring large primary video player, two sub-feature preview cards, and 3-column video cards.
6. **`bp_projects_grid`**: Project reference showcase with society tags and illustrative notices.
7. **`bp_locations_grid`**: Bhatta kiln units and corporate coordination hub with addresses, maps links, and telephone numbers.
8. **`bp_whatsapp_cta`**: Full-width high-converting call-to-action banner with background image, contact manager metadata, and one-tap WhatsApp button.
9. **`bp_audience_cards`**: "Who We Serve" cards for Contractors, Builders, and Construction Companies.
10. **`bp_stats_bar`**: 4-column trust counters (Production Units, Material Categories, Quality Fired, 24/7 Support).
11. **`bp_specs_table`**: Technical material properties table with field testing standards.
12. **`bp_header_logo_widget`**: Independent Header Logo widget with responsive sizing controls.
13. **`bp_footer_logo_widget`**: Independent Footer Logo widget with responsive sizing controls.

---

## 7. The 24 Bundled Elementor Templates

Located in `elementor-templates/` and automatically imported into the WordPress `elementor_library`:

| Template Filename | Type | Purpose |
| :--- | :--- | :--- |
| `header-default.json` | `header` | Theme Builder default header |
| `footer-default.json` | `footer` | Theme Builder default footer |
| `single-product.json` | `single-post` | Single product layout with specs table & WhatsApp CTA |
| `archive-product.json` | `archive` | Product catalog archive template |
| `single-video.json` | `single-post` | Single video detail & related videos template |
| `archive-video.json` | `archive` | Video library archive template |
| `single-project.json` | `single-post` | Single project reference template |
| `archive-project.json` | `archive` | Projects & societies archive template |
| `single-post.json` | `single-post` | Single blog article layout |
| `archive-post.json` | `archive` | Blog index archive layout |
| `page-home.json` | `page` | 8-section homepage layout |
| `page-about.json` | `page` | About Us company page |
| `page-ss7-bricks.json` | `page` | SS7 Bricks flagship page |
| `page-materials.json` | `page` | Complete materials range page |
| `page-for-contractors.json` | `page` | Commercial contractors service page |
| `page-for-builders.json` | `page` | Residential builders service page |
| `page-for-companies.json` | `page` | Corporate developers service page |
| `page-contact.json` | `page` | Contact & quotation request page |
| `section-hero.json` | `section` | Modular Hero section |
| `section-categories.json` | `section` | Modular Categories section |
| `section-ss7-showcase.json` | `section` | Modular SS7 Showcase section |
| `section-featured-products.json` | `section` | Modular Featured Products section |
| `section-video-showcase.json` | `section` | Modular Video Showcase section |
| `section-cta-banner.json` | `section` | Modular WhatsApp CTA section |

---

## 8. The 17 Complete Site Pages

Created by the demo importer with complete, non-placeholder content:

1. **Home (`/`)**: 9 complete sections (Hero, Trust Intro, Categories, SS7 Showcase, Featured Products, Video Showcase, Project References, Who We Serve, Quotation CTA).
2. **About Us (`/about`)**: Company background, bhatta units, leadership (CEO Syed Iftikhar Haider, Sales Qasim Iqbal), and quality mission.
3. **SS7 Bricks (`/ss7-bricks`)**: Technical engineering specifications, kiln firing parameters, bell sound ring tests, and project pricing.
4. **Construction Materials (`/construction-materials`)**: Single-source supply breakdown for cement, aggregates, sand, steel, pipes, and cables.
5. **For Contractors (`/for-contractors`)**: Staged site drop-offs, bulk volume pricing, crane offloading, and unified GST invoices.
6. **For Builders (`/for-builders`)**: Consistent batch quality, zero mortar wastage, and residential society supply.
7. **For Construction Companies (`/for-companies`)**: High-capacity reserve kilns, compliance documentation, and corporate accounts.
8. **Products (`/products`)**: Live products archive with category filter pills and direct WhatsApp ordering.
9. **Categories (`/categories`)**: 12 Material categories grid.
10. **Videos (`/videos`)**: Video library featuring bhatta drone tours, brick selection, and project references.
11. **Projects (`/projects`)**: Construction references from DHA Lahore, Bahria Town, Lake City, LDA City, and Etihad Town.
12. **Locations (`/locations`)**: 3 Bhatta kiln units and Lahore central office with addresses, phone numbers, and Google Maps links.
13. **Blog (`/blog`)**: Practical field guides, material estimation checklists, and masonry advice.
14. **Contact (`/contact`)**: Quotation request form, direct telephone lines, and office location.
15. **Privacy Policy (`/privacy`)**: Customer data privacy declaration.
16. **Terms & Conditions (`/terms`)**: Quotation validity, delivery logistics, and offloading guidelines.
17. **Sample Page (`/sample-page`)**: Standard WordPress sample page.

---

## 9. The 12 Construction Products Catalogue

| Product Title | Category | Price | Unit | SKU |
| :--- | :--- | :--- | :--- | :--- |
| **SS7 Premium Red Bricks** | SS7 Bricks | Rs 14,000 | 1000 Bricks | `BP-SS7-01` |
| **First Class Red Bricks (Awwal)** | First Class Bricks (Awwal) | Rs 13,000 | 1000 Bricks | `BP-AWW-02` |
| **Second Class Bricks (Doyam)** | Second Class Bricks (Doyam) | Rs 10,500 | 1000 Bricks | `BP-DOY-03` |
| **Falcon / Maple Leaf Portland Cement** | Cement | Rs 1,450 | 50 kg Bag | `BP-CEM-04` |
| **Margalla Crushed Stone (1/2")** | Crush / Aggregates (Bajri) | Rs 115 | CFT | `BP-CRU-05` |
| **Chenab River Sand (Rait)** | Sand (Rait) | Rs 58 | CFT | `BP-SND-06` |
| **Grade 60 Deformed Steel Rebar** | Deformed Steel Bars (Sarya) | Rs 255,000 | Ton | `BP-STL-07` |
| **UPVC Sewerage Pipes (4")** | Pipes & Fittings | Rs 2,850 | 13 ft Length | `BP-PIP-08` |
| **Pakistan Cables 7/.029 Copper** | Cables & Electrical | Rs 18,200 | 90m Coil | `BP-ELE-09` |
| **SBR Waterproofing Chemical (20L)** | Construction Chemicals | Rs 9,500 | 20 Litre Can | `BP-CHM-10` |
| **WeatherCoat Exterior Shield Paint** | Paints & Finishes | Rs 16,800 | 16 Litre Drum | `BP-PNT-11` |
| **12W Architectural LED SMD Light** | LED Lights & Fixtures | Rs 650 | Piece | `BP-LGT-12` |

---

## 10. Independent Header & Footer Logos

Under **Appearance → Customize → BrickPoint Theme Options**:

- **Header Logo Controls:**
  - `bp_header_logo`: Media upload for top header and mobile drawer.
  - `bp_header_logo_height_desktop`: Numeric height control in pixels (default: `44px`).
  - `bp_header_logo_height_mobile`: Numeric height control in pixels (default: `36px`).
- **Footer Logo Controls:**
  - `bp_footer_logo`: Media upload for dark footer (supports inverted / white logo versions).
  - `bp_footer_logo_height_desktop`: Numeric height control in pixels (default: `52px`).
  - `bp_footer_logo_height_mobile`: Numeric height control in pixels (default: `42px`).

---

## 11. One-Click Demo Importer & Offline Media

The demo importer operates under **Appearance → BrickPoint Demo**:
1. **Zero External Requests:** All 23 PNG image assets and 15 SVG icons reside directly in the theme package (`assets/images/` and `assets/icons/`).
2. **Media Library Side-Loading:** The importer copies bundled images into `wp-content/uploads/` and registers them using `wp_insert_attachment()`, generating full responsive thumbnail sizes and attaching them as featured images to products, videos, projects, and locations.
3. **Idempotency:** Existing items are looked up by `slug` before creation. Re-running the importer updates metadata without creating duplicate entries.
4. **Automated Setup:** Sets **Front page displays** to **A static page** (`Home`) and **Posts page** to `Blog`, creates the primary menu, and binds it to the `primary`, `mobile`, and `footer` locations.

---

## 12. Theme Customizer & Options

Managed via **Appearance → Customize** or **Appearance → Theme Settings**:
- `bp_phone_display`: Display phone number (default: `0315 2850818`).
- `bp_whatsapp_number`: Clean numeric WhatsApp number with country code (default: `923152850818`).
- `bp_email`: Official contact email (default: `info@brickpoint.pk`).
- `bp_address`: Corporate office address (default: `Lahore, Punjab, Pakistan`).
- `bp_ceo`: Executive contact (default: `Syed Iftikhar Haider`).
- `bp_sales`: Sales & logistics manager (default: `Qasim Iqbal`).
- `bp_social_facebook`: Facebook Page URL.
- `bp_social_instagram`: Instagram Profile URL.
- `bp_social_twitter`: X / Twitter Profile URL.
- `bp_social_tiktok`: TikTok Profile URL.
