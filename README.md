# BrickPoint — Premium Construction Materials & Brick Manufacturing WordPress Theme

[![Version](https://img.shields.io/badge/version-1.0.0-orange.svg)](https://brickpoint.pk/)
[![WordPress](https://img.shields.io/badge/WordPress-6.0%2B-blue.svg)](https://wordpress.org/)
[![PHP](https://img.shields.io/badge/PHP-7.4%2B-purple.svg)](https://php.net/)
[![Elementor](https://img.shields.io/badge/Elementor-Free%20%26%20Pro-red.svg)](https://elementor.com/)
[![License](https://img.shields.io/badge/License-GPLv2%2B-green.svg)](http://www.gnu.org/licenses/gpl-2.0.html)

> **BrickPoint** is a high-performance, production-ready WordPress theme built for brick manufacturers, building suppliers, and construction material enterprises. Engineered with native **Elementor Free** and **Elementor Pro Theme Builder** support, a built-in **One-Click Demo Importer** with bundled offline media, and direct **WhatsApp Ordering** on all products without WooCommerce overhead.

---

## Deliverables & Quick Links

- **Installable Theme Zip:** [`brickpoint-wordpress-elementor-final.zip`](./brickpoint-wordpress-elementor-final.zip) (0.54 MB, clean single-level archive containing `brickpoint/`)
- **Theme Source Directory:** [`wordpress/brickpoint/`](./wordpress/brickpoint/)
- **Comprehensive Documentation:** [`DOCUMENTATION.md`](./DOCUMENTATION.md)

---

## Key Features

### 1. Pixel-Perfect Visual Fidelity
Matches the modern industrial aesthetic of BrickPoint:
- **Brand Colors:** Terracotta Brick (`#c2410c`), Deep Ember (`#ea580c`), Dark Charcoal Ink (`#141210`), Sand Stone (`#f6f1ea`), Warm Gold (`#d9a441`).
- **Typography & Responsive Design:** High-contrast headings, fluid typography, mobile touch navigation drawer, and smooth animations.
- **Dynamic 3D SS7 Floating Card & Video Showcase:** CSS animations, video embed/player frames, and infinite marquee tickers.

### 2. Dual Elementor Architecture (Free & Pro Theme Builder)
- **Elementor Free Support:** All sections, headers, cards, grids, and CTA banners are fully editable using Elementor's native drag-and-drop editor.
- **Elementor Pro Theme Builder Ready:** Native integration with Elementor Pro locations:
  - `header`
  - `footer`
  - `single` (Products, Videos, Projects, Posts, Pages)
  - `archive` (Product Catalogue, Video Library, Project References, Categories, Blog)
- **13 Custom Elementor Widgets:** Registered under the dedicated category `BrickPoint Theme Elements`:
  1. `BrickPoint_Hero_Widget` (Hero Section with video and floating 3D badge)
  2. `BrickPoint_SS7_Showcase_Widget` (Flagship SS7 brick showcase & technical specs)
  3. `BrickPoint_Product_Grid_Widget` (Product grid with live prices and WhatsApp ordering)
  4. `BrickPoint_Category_Grid_Widget` (12 Category cards with background media)
  5. `BrickPoint_Video_Showcase_Widget` (Production video player & playlist)
  6. `BrickPoint_Projects_Grid_Widget` (Construction reference cards)
  7. `BrickPoint_Locations_Grid_Widget` (Bhatta kiln units with Google Maps directions)
  8. `BrickPoint_WhatsApp_CTA_Widget` (Pre-formatted quotation inquiry banner)
  9. `BrickPoint_Audience_Cards_Widget` (Who We Serve: Contractors, Builders, Companies)
  10. `BrickPoint_Stats_Bar_Widget` (Trust stats and volume counters)
  11. `BrickPoint_Specifications_Table_Widget` (Technical material properties table)
  12. `BrickPoint_Header_Logo_Widget` (Header logo with desktop/mobile responsive height controls)
  13. `BrickPoint_Footer_Logo_Widget` (Footer logo with desktop/mobile responsive height controls)
- **24 Bundled Elementor JSON Templates:** Located in `elementor-templates/`, automatically imported during demo setup.

### 3. Custom Post Types & Meta Fields (Zero WooCommerce)
No complicated e-commerce bloat, shopping carts, or payment gateway configurations. BrickPoint is built specifically for construction-materials procurement:
- **`bp_product` (Products):**
  - Fields: Price, Price Label, Unit (e.g. `1000 Bricks`, `Bag`, `Ton`), Availability (`In Stock`), Badge, SKU, Short Summary, Gallery Images, Technical Specifications (key-value), Key Features, Video URL, Brochure PDF URL, Custom WhatsApp Message Override.
- **`bp_video` (Videos):**
  - Fields: Video Source (`mp4`, `youtube`, `vimeo`), Video URL, Direct File URL, Duration, Featured flag.
- **`bp_project` (Projects):**
  - Fields: Category (`Residential`, `Commercial`), Location (`DHA Lahore`, `Bahria Town`, etc.), Status Label (`Illustrative construction reference`).
- **`bp_location` (Locations):**
  - Fields: Address, Phone Number, Operating Hours, Google Maps Direction Link, Facility Video URL.
- **Custom Taxonomies:**
  - `bp_product_category` (with custom image, banner, and sort order)
  - `bp_video_category`

### 4. Direct WhatsApp Ordering & Inquiry System
- Instant WhatsApp Web / WhatsApp App click-to-chat links with URL-encoded, pre-formatted messages:
  - Product inquiries automatically include product title, category, listed price, and unit.
  - Category inquiries include the specific material category name.
  - Floating WhatsApp action button with pulsating live indicator.
- Configurable WhatsApp phone numbers with international country code formatting.

### 5. Independent Header & Footer Logos
- Independent customizer controls under **Appearance → Customize → BrickPoint Theme Options**:
  - Independent Header Logo upload & separate Desktop / Mobile height sliders.
  - Independent Footer Logo upload & separate Desktop / Mobile height sliders (supports dark-mode / inverted variations).

### 6. One-Click Demo Importer (`Appearance → BrickPoint Demo`)
- Imports 17 complete production pages:
  `Home`, `About Us`, `SS7 Bricks`, `Construction Materials`, `For Contractors`, `For Builders`, `For Construction Companies`, `All Products`, `Product Categories`, `Inside BrickPoint Videos`, `Project References`, `Our Bhattas & Locations`, `Blog`, `Contact & Quotation`, `Privacy Policy`, `Terms & Conditions`, `Sample Page`.
- Bundles 23 offline PNG images and 15 SVG icons — **zero external network requests** required for a complete, visually stunning demo setup.
- Idempotent update/skip logic prevents duplicate pages or posts on re-runs.
- Automatically assigns Navigation Menus (`Primary`, `Mobile`, `Footer`) and sets Static Front Page (`Home`) and Posts Page (`Blog`).

---

## Installation & Setup Guide

### Method A: Install via WordPress Admin
1. Go to **WordPress Admin → Appearance → Themes → Add New → Upload Theme**.
2. Choose [`brickpoint-wordpress-elementor-final.zip`](./brickpoint-wordpress-elementor-final.zip) and click **Install Now**.
3. Click **Activate**.
4. (Optional but recommended) Install and activate **Elementor** (Free or Pro) from the WordPress Plugin Directory.
5. Navigate to **Appearance → BrickPoint Demo** and click **Start Full Demo Import**.
6. The importer will automatically populate all 17 pages, 12 products, 12 categories, 6 videos, 6 projects, 4 bhattas, 4 blog guides, menus, and 24 Elementor templates.

### Method B: Install via FTP / Manual Unzip
1. Extract the contents of `brickpoint-wordpress-elementor-final.zip` into `wp-content/themes/`.
2. Ensure the resulting path is `wp-content/themes/brickpoint/style.css`.
3. In WordPress Admin, go to **Appearance → Themes** and activate **BrickPoint**.

---

## Theme Structure

```text
brickpoint/
├── 404.php                              # 404 Not Found template
├── archive-bp_location.php              # Locations / Bhattas archive
├── archive-bp_product.php               # Products catalogue archive
├── archive-bp_project.php               # Projects & references archive
├── archive-bp_video.php                 # Video library archive
├── archive.php                          # Blog archive template
├── footer.php                           # Site footer (Theme Builder compatible)
├── front-page.php                       # 9-section homepage template
├── functions.php                        # Main theme bootstrap
├── header.php                           # Sticky header & navigation
├── home.php                             # Blog index template
├── index.php                            # Default fallback template
├── page.php                             # Default page template
├── readme.txt                           # Theme description and tags
├── rtl.css                              # Right-to-left layout support
├── screenshot.png                       # Theme preview screenshot (800x600)
├── search.php                           # Search results template
├── single-bp_location.php               # Single bhatta location template
├── single-bp_product.php                # Single product with WhatsApp order
├── single-bp_project.php                # Single project reference template
├── single-bp_video.php                  # Single video player template
├── single.php                           # Single blog article template
├── style.css                            # Theme metadata & CSS variables
├── taxonomy-bp_product_category.php     # Category product listing
├── taxonomy-bp_video_category.php       # Video category listing
├── assets/
│   ├── css/
│   │   ├── main.css                     # Primary styles
│   │   ├── theme.css                    # Consolidated theme CSS
│   │   ├── animations.css               # Keyframes & transitions
│   │   └── responsive.css               # Media query overrides
│   ├── icons/                           # 15 Custom SVG icons
│   ├── images/                          # 23 Bundled offline media assets
│   └── js/
│       ├── main.js                      # Sticky header, drawer, gallery
│       └── admin.js                     # One-click demo AJAX handler
├── elementor-templates/                 # 24 Elementor JSON templates
│   ├── header-default.json
│   ├── footer-default.json
│   ├── single-product.json
│   ├── archive-product.json
│   ├── page-home.json
│   └── ... (19 additional templates)
├── inc/
│   ├── admin-settings.php               # Theme settings page
│   ├── admin.php                        # Admin columns & notices
│   ├── ajax-handlers.php                # Demo importer AJAX endpoints
│   ├── customizer.php                   # Independent header/footer logos & settings
│   ├── demo-data.php                    # 17 pages, 12 products, bhatta data
│   ├── demo-importer.php                # Import logic & media library side-loader
│   ├── elementor.php                    # Elementor Free & Pro integration
│   ├── elementor-widgets.php            # 13 Custom Elementor widgets
│   ├── enqueue.php                      # CSS/JS enqueuing
│   ├── helpers.php                      # Theme helper functions
│   ├── meta-fields.php                  # Meta boxes for all CPTs
│   ├── post-types.php                   # bp_product, bp_video, bp_project, bp_location
│   ├── project-functions.php            # Project reference helpers
│   ├── setup.php                        # Theme features, thumbnail sizes, menus
│   ├── taxonomies.php                   # bp_product_category, bp_video_category
│   ├── template-functions.php           # Logos, menus, breadcrumbs
│   ├── video-functions.php              # Video embed helpers
│   └── whatsapp.php                     # WhatsApp inquiry builders
└── template-parts/
    ├── content.php                      # Blog card
    ├── hero.php                         # 9-section hero banner
    ├── location-card.php                # Bhatta unit card
    ├── product-card.php                 # Product catalogue card
    ├── project-card.php                 # Project reference card
    ├── social-links.php                 # Social media icons
    └── video-card.php                   # Video player card
```

---

## Contact & Credits

- **Enterprise:** BrickPoint Pakistan
- **Manufacturing Units:** Masha Allah Bricks Co. &bull; Fine Bricks Co. &bull; SS7 Bricks
- **CEO:** Syed Iftikhar Haider
- **Sales & Logistics:** Qasim Iqbal
- **Phone / WhatsApp:** +92 315 2850818
- **Email:** info@brickpoint.pk
- **Location:** Lahore, Punjab, Pakistan
- **Repository:** [https://github.com/brickpoint786/BrickPoint](https://github.com/brickpoint786/BrickPoint)
