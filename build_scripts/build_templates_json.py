import os
import json

DEST = "/home/user/BrickPoint/wordpress/brickpoint/elementor-templates"
os.makedirs(DEST, exist_ok=True)

def create_elementor_tpl(title, tpl_type, elements):
    return {
        "title": title,
        "type": tpl_type,
        "version": "0.4",
        "content": elements
    }

def make_section(columns_data, custom_classes=""):
    return {
        "id": "sec_" + os.urandom(4).hex(),
        "elType": "section",
        "settings": {
            "layout": "boxed",
            "css_classes": custom_classes
        },
        "elements": columns_data,
        "isInner": False
    }

def make_column(widgets_data, width=100):
    return {
        "id": "col_" + os.urandom(4).hex(),
        "elType": "column",
        "settings": {
            "_column_size": width
        },
        "elements": widgets_data,
        "isInner": False
    }

def make_widget(widget_type, settings):
    return {
        "id": "wid_" + os.urandom(4).hex(),
        "elType": "widget",
        "widgetType": widget_type,
        "settings": settings
    }

templates = {}

# 1. header-default.json
templates["header-default.json"] = create_elementor_tpl("Header Default", "header", [
    make_section([
        make_column([
            make_widget("bp_header_logo_widget", {}),
            make_widget("heading", {"title": "BrickPoint Navigation", "header_size": "h4"}),
        ], 100)
    ], "bp-header")
])

# 2. footer-default.json
templates["footer-default.json"] = create_elementor_tpl("Footer Default", "footer", [
    make_section([
        make_column([
            make_widget("bp_footer_logo_widget", {}),
            make_widget("text-editor", {"editor": "<p>Premium bricks and reliable construction materials for homes, commercial developments, and large-scale building projects.</p>"}),
        ], 50),
        make_column([
            make_widget("bp_whatsapp_cta", {}),
        ], 50)
    ], "bp-footer")
])

# 3. single-product.json
templates["single-product.json"] = create_elementor_tpl("Single Product", "single-post", [
    make_section([
        make_column([
            make_widget("image", {"image": {"url": "/wp-content/themes/brickpoint/assets/images/red-stack.png"}}),
        ], 50),
        make_column([
            make_widget("heading", {"title": "SS7 Premium Red Bricks", "header_size": "h1"}),
            make_widget("text-editor", {"editor": "<p>High-density burnt clay bricks engineered for strength, uniform shape and durability.</p>"}),
            make_widget("bp_specs_table", {}),
            make_widget("button", {
                "text": "Order on WhatsApp",
                "link": {"url": "https://api.whatsapp.com/send?phone=923152850818"},
                "button_type": "success"
            }),
        ], 50)
    ])
])

# 4. archive-product.json
templates["archive-product.json"] = create_elementor_tpl("Products Archive", "archive", [
    make_section([
        make_column([
            make_widget("heading", {"title": "Products Catalogue", "header_size": "h1"}),
            make_widget("text-editor", {"editor": "<p>Every product with WhatsApp ordering — no cart, no checkout, just fast quotations.</p>"}),
            make_widget("bp_product_grid", {"count": 12, "columns": "4"}),
        ], 100)
    ])
])

# 5. single-video.json
templates["single-video.json"] = create_elementor_tpl("Single Video", "single-post", [
    make_section([
        make_column([
            make_widget("video", {"video_type": "hosted", "hosted_url": {"url": "https://videos.pexels.com/video-files/27758012/12218981_3840_2160_25fps.mp4"}}),
            make_widget("heading", {"title": "Inside BrickPoint Video", "header_size": "h1"}),
            make_widget("text-editor", {"editor": "<p>Continuous high-draft kiln chambers, automated brick handling, and quality checks.</p>"}),
        ], 100)
    ])
])

# 6. archive-video.json
templates["archive-video.json"] = create_elementor_tpl("Videos Archive", "archive", [
    make_section([
        make_column([
            make_widget("heading", {"title": "Inside BrickPoint (Videos)", "header_size": "h1"}),
            make_widget("bp_video_showcase", {}),
        ], 100)
    ])
])

# 7. single-project.json
templates["single-project.json"] = create_elementor_tpl("Single Project", "single-post", [
    make_section([
        make_column([
            make_widget("heading", {"title": "Project Reference", "header_size": "h1"}),
            make_widget("image", {"image": {"url": "/wp-content/themes/brickpoint/assets/images/villa1.png"}}),
            make_widget("text-editor", {"editor": "<p>Illustrative construction reference from premier housing societies.</p>"}),
        ], 100)
    ])
])

# 8. archive-project.json
templates["archive-project.json"] = create_elementor_tpl("Projects Archive", "archive", [
    make_section([
        make_column([
            make_widget("heading", {"title": "Project References & Landmarks", "header_size": "h1"}),
            make_widget("bp_projects_grid", {}),
        ], 100)
    ])
])

# 9. single-post.json
templates["single-post.json"] = create_elementor_tpl("Single Blog Post", "single-post", [
    make_section([
        make_column([
            make_widget("heading", {"title": "Blog Guide", "header_size": "h1"}),
            make_widget("text-editor", {"editor": "<p>Practical insights and field guidelines from BrickPoint masonry specialists.</p>"}),
        ], 100)
    ])
])

# 10. archive-post.json
templates["archive-post.json"] = create_elementor_tpl("Blog Archive", "archive", [
    make_section([
        make_column([
            make_widget("heading", {"title": "BrickPoint Knowledge & Guides", "header_size": "h1"}),
            make_widget("posts", {"posts_per_page": 6}),
        ], 100)
    ])
])

# 11. page-home.json
templates["page-home.json"] = create_elementor_tpl("Homepage Template", "page", [
    make_section([make_column([make_widget("bp_hero", {})], 100)]),
    make_section([make_column([make_widget("bp_category_grid", {})], 100)]),
    make_section([make_column([make_widget("bp_ss7_showcase", {})], 100)]),
    make_section([make_column([make_widget("bp_product_grid", {"count": 8, "columns": "4"})], 100)]),
    make_section([make_column([make_widget("bp_video_showcase", {})], 100)]),
    make_section([make_column([make_widget("bp_projects_grid", {})], 100)]),
    make_section([make_column([make_widget("bp_audience_cards", {})], 100)]),
    make_section([make_column([make_widget("bp_whatsapp_cta", {})], 100)])
])

# 12. page-about.json
templates["page-about.json"] = create_elementor_tpl("About Us Page", "page", [
    make_section([
        make_column([
            make_widget("heading", {"title": "A Construction Materials Partner You Can Build On", "header_size": "h1"}),
            make_widget("text-editor", {"editor": "<p>BrickPoint brings together trusted brick manufacturing units and a complete construction-materials range — so contractors, builders and developers can source with confidence.</p>"}),
            make_widget("bp_stats_bar", {}),
            make_widget("bp_locations_grid", {}),
        ], 100)
    ])
])

# 13. page-ss7-bricks.json
templates["page-ss7-bricks.json"] = create_elementor_tpl("SS7 Bricks Page", "page", [
    make_section([
        make_column([
            make_widget("bp_ss7_showcase", {}),
            make_widget("bp_specs_table", {}),
            make_widget("bp_whatsapp_cta", {}),
        ], 100)
    ])
])

# 14. page-materials.json
templates["page-materials.json"] = create_elementor_tpl("Construction Materials Page", "page", [
    make_section([
        make_column([
            make_widget("heading", {"title": "Complete Construction Materials Range", "header_size": "h1"}),
            make_widget("bp_category_grid", {}),
            make_widget("bp_product_grid", {"count": 12, "columns": "4"}),
        ], 100)
    ])
])

# 15. page-for-contractors.json
templates["page-for-contractors.json"] = create_elementor_tpl("For Contractors Page", "page", [
    make_section([
        make_column([
            make_widget("heading", {"title": "Built for Commercial Contractors", "header_size": "h1"}),
            make_widget("text-editor", {"editor": "<p>Bulk material supply, project-based quotations, lab test certificates, and scheduled site drop-offs.</p>"}),
            make_widget("bp_whatsapp_cta", {}),
        ], 100)
    ])
])

# 16. page-for-builders.json
templates["page-for-builders.json"] = create_elementor_tpl("For Builders Page", "page", [
    make_section([
        make_column([
            make_widget("heading", {"title": "Dependable Quality for Residential Builders", "header_size": "h1"}),
            make_widget("text-editor", {"editor": "<p>Consistent quality across every batch with multi-category sourcing for housing societies in Lahore.</p>"}),
            make_widget("bp_whatsapp_cta", {}),
        ], 100)
    ])
])

# 17. page-for-companies.json
templates["page-for-companies.json"] = create_elementor_tpl("For Construction Companies Page", "page", [
    make_section([
        make_column([
            make_widget("heading", {"title": "Large-Scale Supply for Developers & Companies", "header_size": "h1"}),
            make_widget("text-editor", {"editor": "<p>High capacity production reserves, documentation compliance, and dedicated procurement account manager.</p>"}),
            make_widget("bp_whatsapp_cta", {}),
        ], 100)
    ])
])

# 18. page-contact.json
templates["page-contact.json"] = create_elementor_tpl("Contact Page", "page", [
    make_section([
        make_column([
            make_widget("heading", {"title": "Contact & Quotation Request", "header_size": "h1"}),
            make_widget("text-editor", {"editor": "<p>Send your bill of quantities on WhatsApp or call our sales line directly.</p>"}),
            make_widget("bp_whatsapp_cta", {}),
        ], 100)
    ])
])

# 19. section-hero.json
templates["section-hero.json"] = create_elementor_tpl("Hero Section", "section", [
    make_section([make_column([make_widget("bp_hero", {})], 100)])
])

# 20. section-categories.json
templates["section-categories.json"] = create_elementor_tpl("Categories Section", "section", [
    make_section([make_column([make_widget("bp_category_grid", {})], 100)])
])

# 21. section-ss7-showcase.json
templates["section-ss7-showcase.json"] = create_elementor_tpl("SS7 Showcase Section", "section", [
    make_section([make_column([make_widget("bp_ss7_showcase", {})], 100)])
])

# 22. section-featured-products.json
templates["section-featured-products.json"] = create_elementor_tpl("Featured Products Section", "section", [
    make_section([make_column([make_widget("bp_product_grid", {"count": 8, "columns": "4"})], 100)])
])

# 23. section-video-showcase.json
templates["section-video-showcase.json"] = create_elementor_tpl("Video Showcase Section", "section", [
    make_section([make_column([make_widget("bp_video_showcase", {})], 100)])
])

# 24. section-cta-banner.json
templates["section-cta-banner.json"] = create_elementor_tpl("WhatsApp CTA Banner Section", "section", [
    make_section([make_column([make_widget("bp_whatsapp_cta", {})], 100)])
])

for filename, data in templates.items():
    filepath = os.path.join(DEST, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

print(f"Generated {len(templates)} Elementor JSON templates in {DEST}")
