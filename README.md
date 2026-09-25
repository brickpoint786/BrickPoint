# BrickPoint — True Elementor-Native WordPress Theme (v2)

[![Version](https://img.shields.io/badge/version-2.0.0-orange.svg)](https://brickpoint.pk/)
[![WordPress](https://img.shields.io/badge/WordPress-6.0%2B-blue.svg)](https://wordpress.org/)
[![PHP](https://img.shields.io/badge/PHP-7.4%2B-purple.svg)](https://php.net/)
[![Elementor](https://img.shields.io/badge/Elementor-Free%20%26%20Pro-red.svg)](https://elementor.com/)
[![License](https://img.shields.io/badge/License-GPLv2%2B-green.svg)](http://www.gnu.org/licenses/gpl-2.0.html)

> **BrickPoint** is a high-performance, 100% Elementor-native WordPress theme faithfully converted from the original BrickPoint website. Every section on the Homepage, About, SS7 Bricks, Services, Contact, Header, and Footer is constructed using **real, granular Elementor elements** (Headings, Text Editors, Buttons, Containers/Columns, Images, and Videos) that can be visually edited, duplicated, deleted, or reordered directly in the Elementor visual panel.

---

## Deliverables & Quick Links

- **Final Installable Theme Package (v2):** [`brickpoint-wordpress-elementor-final-v2.zip`](./brickpoint-wordpress-elementor-final-v2.zip) (578 KB, single-level theme archive containing `brickpoint/`)
- **Theme Source Directory:** [`wordpress/brickpoint/`](./wordpress/brickpoint/)
- **Comprehensive Technical Documentation:** [`DOCUMENTATION.md`](./DOCUMENTATION.md)
- **GitHub Pull Request:** [PR #1 on branch `arena/01a0c866-brickpoint`](https://github.com/brickpoint786/BrickPoint/pull/1)

---

## What Makes Version 2 Truly Elementor-Native?

### 1. Zero Monolithic Black-Box Widgets
- **Previous limitation:** Early implementations placed entire sections inside a single PHP-rendered custom widget or PHP template, rendering text and buttons inaccessible in the Elementor visual canvas.
- **V2 Solution:** All visual sections are constructed using **native Elementor widgets** (`heading`, `text-editor`, `button`, `image`, `video`, `html`). When opening **Home → Edit with Elementor**, the user sees the real sections, columns, headings, and buttons in the Navigator and can click and edit any piece of content directly.

### 2. Custom Widgets are Strictly Dynamic Query Tools
In strict adherence to professional WordPress/Elementor standards, custom widgets are reserved exclusively for genuine dynamic database queries:
1. `bp_product_grid` — Dynamic Product Query with controls for count, columns (2, 3, 4), category filter, featured switch, price display, and WhatsApp order button.
2. `bp_category_grid` — Dynamic Category Cards with column and description toggles.
3. `bp_video_grid` — Dynamic Video Library Grid with duration and badge controls.
4. `bp_project_grid` — Dynamic Project References Grid with location and notice controls.
5. `bp_location_grid` — Dynamic Bhatta Kiln Locations Grid with phone, hours, and map links.
6. `bp_blog_grid` — Dynamic Blog Guides Grid.
7. `bp_header_logo_widget` — Independent Header Logo with responsive desktop/mobile height sliders.
8. `bp_footer_logo_widget` — Independent Footer Logo with responsive desktop/mobile height sliders.

### 3. Full 9-Section Homepage Structure in Elementor
1. **Hero Section:**
   - Badge ("Masha Allah • Fine Bricks • SS7")
   - Main Heading ("Building Strength.")
   - Highlight Heading ("Delivering Quality.")
   - Subline Heading ("Shaping Tomorrow.")
   - Subtitle paragraph ("Premium bricks and reliable construction materials...")
   - 3 Action Buttons: "Explore Products →", "Request a Quote", "WhatsApp Us"
   - Trust row: Quality-focused supply • Reliable delivery • Multiple production locations
   - Video player with poster frame
   - SS7 3D Card with thumbnail, "★ Flagship" tag, and "View SS7 range →" button
   - "3+ Production Units" badge
   - Animated marquee ticker of all 10 material types
2. **Why BrickPoint (Trust & Intro):**
   - Media column: Kiln production image + "Trusted Supply" and "Bulk Ready" glass overlay cards
   - Content column: Eyebrow, Heading, Description paragraph, 4-point check checklist, 2 Action buttons ("About BrickPoint →", "Our Locations")
3. **Product Categories Grid:**
   - Eyebrow, Heading, Subheading
   - 12 category cards with hover zoom and description teasers
   - "View All Categories →" button
4. **Flagship SS7 Bricks Showcase:**
   - Eyebrow, Heading, Description
   - 4-part Specifications Grid (Size, Type, Usage, Availability)
   - 2 Action buttons ("Request SS7 Quote", "View SS7 Page →")
   - Media column: Main SS7 Red Bricks image + 3 gallery thumbnails
5. **Featured Products:**
   - Eyebrow, Heading, Subheading
   - Dynamic Product Grid with real pricing and WhatsApp order buttons
   - "Browse All Products →" button
6. **Inside BrickPoint Video Showcase:**
   - Eyebrow, Heading, Description, "View All Videos →" button
   - Main Video player ("Featured" badge)
   - 2 Sub-video cards ("From the Bhatta to Your Building", "Materials That Become Landmarks")
   - 3-column Video Grid
7. **Project References:**
   - Eyebrow, Heading, Description
   - 3 Project cards (DHA Lahore, Bahria Town, Lake City)
   - "Explore All Projects →" button
8. **Who We Serve (Audience Cards):**
   - Eyebrow, Heading, Description
   - 3 Audience cards: For Contractors, For Builders, For Construction Companies
9. **Quotation CTA Banner:**
   - Dark textured background + overlay
   - Eyebrow, Heading ("Send your material list. We handle the rest.")
   - Telephone line, CEO, and Sales manager contact line
   - "WhatsApp Your List" button + "Request Quote Form" button

### 4. Complete Elementor Pro Theme Builder Templates
- **Header Default (`header-default.json`):** Top bar with phone, units, and quicklinks; main header with independent header logo, full navigation menu, WhatsApp button, and Request Quote button.
- **Footer Default (`footer-default.json`):** 4-column layout with independent footer logo, company bio, direct contacts, social media links, product link lists, company units, quotation text, WhatsApp button, and bottom copyright/legal bar.
- **Single Product (`single-product.json`):** Product image, pricing, specifications, features, WhatsApp ordering button, and quote request.
- **Archive Product (`archive-product.json`):** Product catalog archive template.
- **Single Video & Archive Video:** Video player, metadata, and playlist.
- **Single Project & Archive Project:** Reference photos, society badges, and content notices.
- **Single Post & Archive Post:** Blog layout.

### 5. Automated Demo Importer with True Elementor Injection
Located in **Appearance → BrickPoint Demo**:
- Injects authentic `_elementor_data` JSON onto all created WordPress pages (`Home`, `About`, `SS7 Bricks`, `Construction Materials`, `For Contractors`, `For Builders`, `For Companies`, `Contact`, `Privacy`, `Terms`).
- Sets `_elementor_edit_mode = 'builder'`, `_elementor_template_type = 'wp-page'`, and `_elementor_version = '3.20.0'`.
- Imports all 26 templates into the WordPress `elementor_library` and registers Theme Builder conditions (`include/general` for header/footer).
- Side-loads 23 bundled offline images into the Media Library without external requests.
- Assigns Navigation Menus and sets the static Front Page to `Home` and Posts Page to `Blog`.

---

## Installation & Setup Guide

1. In WordPress Admin, navigate to **Appearance → Themes → Add New → Upload Theme**.
2. Select [`brickpoint-wordpress-elementor-final-v2.zip`](./brickpoint-wordpress-elementor-final-v2.zip) and click **Install Now**, then **Activate**.
3. Install and activate the **Elementor** plugin (Free or Pro).
4. Go to **Appearance → BrickPoint Demo** and click **Start Full Demo Import**.
5. Go to **Pages → Home → Edit with Elementor** — every section, heading, text, button, image, and column will be ready to visually edit!

---

## Contact & Credits

- **Enterprise:** BrickPoint Pakistan
- **Units:** Masha Allah Bricks Co. • Fine Bricks Co. • SS7 Bricks
- **CEO:** Syed Iftikhar Haider
- **Sales & Logistics:** Qasim Iqbal
- **Phone / WhatsApp:** +92 315 2850818
- **Email:** info@brickpoint.pk
- **Location:** Lahore, Punjab, Pakistan
- **Repository:** [https://github.com/brickpoint786/BrickPoint](https://github.com/brickpoint786/BrickPoint)
