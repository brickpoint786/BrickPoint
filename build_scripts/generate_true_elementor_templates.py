import os
import json
import random

DEST = "/home/user/BrickPoint/wordpress/brickpoint/elementor-templates"
os.makedirs(DEST, exist_ok=True)

def gen_id():
    chars = "abcdef0123456789"
    return "".join(random.choice(chars) for _ in range(7))

def make_widget(widget_type, settings=None, custom_classes=""):
    s = settings.copy() if settings else {}
    if custom_classes:
        s["_css_classes"] = custom_classes
    return {
        "id": gen_id(),
        "elType": "widget",
        "widgetType": widget_type,
        "settings": s,
        "elements": []
    }

def make_column(widgets_or_inners, width=100, custom_classes="", is_inner=False):
    s = {"_column_size": width}
    if custom_classes:
        s["_css_classes"] = custom_classes
    return {
        "id": gen_id(),
        "elType": "column",
        "isInner": is_inner,
        "settings": s,
        "elements": widgets_or_inners
    }

def make_section(columns, custom_classes="", is_inner=False, bg_image=""):
    s = {"layout": "boxed"}
    if custom_classes:
        s["_css_classes"] = custom_classes
    if bg_image:
        s["background_background"] = "classic"
        s["background_image"] = {"url": bg_image, "id": ""}
        s["background_position"] = "center center"
        s["background_repeat"] = "no-repeat"
        s["background_size"] = "cover"
    return {
        "id": gen_id(),
        "elType": "section",
        "isInner": is_inner,
        "settings": s,
        "elements": columns
    }

def make_inner_section(columns, custom_classes=""):
    return make_section(columns, custom_classes=custom_classes, is_inner=True)

templates = {}

# =========================================================================
# 1. HOMEPAGE TEMPLATE (page-home.json) — 100% GRANULAR ELEMENTOR SECTIONS
# =========================================================================

# SECTION 1: HERO
hero_col_left = make_column([
    make_widget("heading", {
        "title": "Masha Allah • Fine Bricks • SS7",
        "header_size": "p",
        "align": "left",
    }, "bp-hero-badge"),
    make_widget("heading", {
        "title": "Building Strength.<br /><span class=\"text-orange\">Delivering Quality.</span><br />Shaping Tomorrow.",
        "header_size": "h1",
        "align": "left",
    }, "bp-hero-title font-display"),
    make_widget("text-editor", {
        "editor": "<p>Premium bricks and reliable construction materials for homes, commercial developments, and large-scale building projects.</p>",
    }, "bp-hero-sub"),
    make_inner_section([
        make_column([
            make_widget("button", {
                "text": "Explore Products →",
                "link": {"url": "/products", "is_external": False},
                "size": "md",
            }, "btn-brick")
        ], 33, is_inner=True),
        make_column([
            make_widget("button", {
                "text": "Request a Quote",
                "link": {"url": "/contact", "is_external": False},
                "size": "md",
            }, "btn-ghost")
        ], 33, is_inner=True),
        make_column([
            make_widget("button", {
                "text": "WhatsApp Us",
                "link": {"url": "https://api.whatsapp.com/send?phone=923152850818&text=Assalam-o-Alaikum%20BrickPoint%2C%20I%20need%20a%20quotation.", "is_external": True},
                "size": "md",
            }, "btn-whatsapp")
        ], 34, is_inner=True)
    ], "bp-hero-cta"),
    make_widget("text-editor", {
        "editor": "<div class=\"bp-hero-trust-row\"><span>🛡 Quality-focused supply</span><span>🚚 Reliable delivery</span><span>🏭 Multiple production locations</span></div>"
    })
], 55, "bp-hero-text")

hero_col_right = make_column([
    make_widget("video", {
        "video_type": "hosted",
        "hosted_url": {"url": "https://videos.pexels.com/video-files/35411576/15003649_3840_2160_24fps.mp4"},
        "show_controls": "yes",
    }, "hero-video-frame"),
    make_inner_section([
        make_column([
            make_widget("image", {
                "image": {"url": "/wp-content/themes/brickpoint/assets/images/red-stack.png"},
                "image_size": "thumbnail",
            }, "bp-ss7-thumb"),
        ], 30, is_inner=True),
        make_column([
            make_widget("heading", {
                "title": "★ Flagship",
                "header_size": "p",
            }, "bp-flagship-tag text-gold"),
            make_widget("heading", {
                "title": "SS7 Bricks",
                "header_size": "h3",
            }, "bp-ss7-title font-display"),
            make_widget("button", {
                "text": "View SS7 range →",
                "link": {"url": "/ss7-bricks", "is_external": False},
                "size": "xs",
            }, "bp-ss7-link")
        ], 70, is_inner=True)
    ], "ss7-brick ss7-brick-loop"),
    make_widget("html", {
        "html": "<div class=\"bp-units-pill\"><p class=\"bp-units-count\">3<span class=\"text-orange\">+</span></p><p class=\"bp-units-label\">Production units</p></div>"
    })
], 45, "bp-hero-media-wrap")

hero_marquee = make_inner_section([
    make_column([
        make_widget("html", {
            "html": "<div class=\"bp-marquee-bar\"><div class=\"marquee-track\"><div class=\"marquee-group\"><span><span class=\"bp-dot-orange\"></span>SS7 Bricks</span><span><span class=\"bp-dot-orange\"></span>Cement</span><span><span class=\"bp-dot-orange\"></span>Bajri / Crush</span><span><span class=\"bp-dot-orange\"></span>Sand / Rait</span><span><span class=\"bp-dot-orange\"></span>Steel</span><span><span class=\"bp-dot-orange\"></span>Pipes</span><span><span class=\"bp-dot-orange\"></span>Chemicals</span><span><span class=\"bp-dot-orange\"></span>Cables</span><span><span class=\"bp-dot-orange\"></span>Paints</span><span><span class=\"bp-dot-orange\"></span>Lights</span></div><div class=\"marquee-group\"><span><span class=\"bp-dot-orange\"></span>SS7 Bricks</span><span><span class=\"bp-dot-orange\"></span>Cement</span><span><span class=\"bp-dot-orange\"></span>Bajri / Crush</span><span><span class=\"bp-dot-orange\"></span>Sand / Rait</span><span><span class=\"bp-dot-orange\"></span>Steel</span><span><span class=\"bp-dot-orange\"></span>Pipes</span><span><span class=\"bp-dot-orange\"></span>Chemicals</span><span><span class=\"bp-dot-orange\"></span>Cables</span><span><span class=\"bp-dot-orange\"></span>Paints</span><span><span class=\"bp-dot-orange\"></span>Lights</span></div></div></div>"
        })
    ], 100, is_inner=True)
])

sec_hero = make_section([hero_col_left, hero_col_right], "bp-hero bp-dark", bg_image="/wp-content/themes/brickpoint/assets/images/brick-mason.png")
sec_hero["elements"].append(make_column([hero_marquee], 100))

# SECTION 2: WHY BRICKPOINT (TRUST / INTRO)
sec_trust = make_section([
    make_column([
        make_widget("image", {
            "image": {"url": "/wp-content/themes/brickpoint/assets/images/kiln.png"},
            "image_size": "large",
        }, "bp-trust-media img-zoom"),
        make_inner_section([
            make_column([
                make_widget("heading", {"title": "Trusted Supply", "header_size": "h4"}, "bp-card-h-orange"),
                make_widget("text-editor", {"editor": "<p class=\"bp-card-sub\">Consistent quality for every order size</p>"}),
            ], 50, "bp-glass-card", is_inner=True),
            make_column([
                make_widget("heading", {"title": "Bulk Ready", "header_size": "h4"}, "bp-card-h-white"),
                make_widget("text-editor", {"editor": "<p class=\"bp-card-sub-dim\">Contractors & companies welcome</p>"}),
            ], 50, "bp-glass-card bp-glass-dark", is_inner=True)
        ], "bp-trust-cards-overlay")
    ], 50),
    make_column([
        make_widget("heading", {"title": "Why BrickPoint", "header_size": "p"}, "bp-eyebrow"),
        make_widget("heading", {"title": "A construction-materials partner you can build on", "header_size": "h2"}, "bp-heading-2 font-display"),
        make_widget("text-editor", {"editor": "<p class=\"bp-body-text\">BrickPoint brings together trusted brick manufacturing units and a complete construction-materials range — so contractors, builders and developers can source with confidence.</p>"}),
        make_widget("text-editor", {
            "editor": "<ul class=\"bp-check-list\"><li>✔ Quality-focused brick manufacturing at multiple bhatta locations</li><li>✔ Complete materials range — from cement and steel to finishes</li><li>✔ Project-based quotations with delivery coordination</li><li>✔ Direct WhatsApp ordering with fast response</li></ul>"
        }),
        make_inner_section([
            make_column([
                make_widget("button", {
                    "text": "About BrickPoint →",
                    "link": {"url": "/about", "is_external": False},
                    "size": "sm",
                }, "btn-dark")
            ], 50, is_inner=True),
            make_column([
                make_widget("button", {
                    "text": "Our Locations",
                    "link": {"url": "/locations", "is_external": False},
                    "size": "sm",
                }, "btn-ghost")
            ], 50, is_inner=True)
        ], "bp-action-row")
    ], 50, "bp-trust-content")
], "bp-section bp-trust-section")

# SECTION 3: PRODUCT CATEGORIES
sec_categories = make_section([
    make_column([
        make_widget("heading", {"title": "Product Categories", "header_size": "p", "align": "center"}, "bp-eyebrow"),
        make_widget("heading", {"title": "One supplier for your complete material list", "header_size": "h2", "align": "center"}, "bp-heading-2 bp-head-light font-display"),
        make_widget("text-editor", {"editor": "<p class=\"bp-body-text bp-head-light-dim\" style=\"text-align:center;\">From flagship SS7 bricks to cement, aggregates, steel, pipes, electricals and finishes.</p>"}),
        make_widget("bp_category_grid", {"count": 12, "columns": "4", "show_description": "yes", "show_arrow": "yes"}),
        make_widget("button", {
            "text": "View All Categories →",
            "link": {"url": "/categories", "is_external": False},
            "align": "center",
            "size": "md",
        }, "btn-ghost")
    ], 100)
], "bp-section bp-dark")

# SECTION 4: FLAGSHIP SS7 BRICKS
sec_ss7 = make_section([
    make_column([
        make_widget("heading", {"title": "Flagship Product", "header_size": "p"}, "bp-eyebrow"),
        make_widget("heading", {"title": "The Strength Behind Every Structure", "header_size": "h2"}, "bp-heading-2 font-display"),
        make_widget("text-editor", {"editor": "<p class=\"bp-body-text\">SS7 Bricks — our signature range engineered for strength, shape and lasting performance. Ask for specifications, availability and project pricing on WhatsApp.</p>"}),
        make_inner_section([
            make_column([
                make_widget("heading", {"title": "Size", "header_size": "p"}, "bp-spec-lbl"),
                make_widget("heading", {"title": "Standard chamber size", "header_size": "h4"}, "bp-spec-val")
            ], 50, "bp-spec-card", is_inner=True),
            make_column([
                make_widget("heading", {"title": "Type", "header_size": "p"}, "bp-spec-lbl"),
                make_widget("heading", {"title": "Burnt-clay SS7", "header_size": "h4"}, "bp-spec-val")
            ], 50, "bp-spec-card", is_inner=True)
        ]),
        make_inner_section([
            make_column([
                make_widget("heading", {"title": "Usage", "header_size": "p"}, "bp-spec-lbl"),
                make_widget("heading", {"title": "Homes • Commercial • Boundary", "header_size": "h4"}, "bp-spec-val")
            ], 50, "bp-spec-card", is_inner=True),
            make_column([
                make_widget("heading", {"title": "Availability", "header_size": "p"}, "bp-spec-lbl"),
                make_widget("heading", {"title": "Bulk & retail orders", "header_size": "h4"}, "bp-spec-val")
            ], 50, "bp-spec-card", is_inner=True)
        ]),
        make_inner_section([
            make_column([
                make_widget("button", {
                    "text": "Request SS7 Quote",
                    "link": {"url": "https://api.whatsapp.com/send?phone=923152850818&text=Assalam-o-Alaikum%20BrickPoint%2C%20I%20need%20a%20quotation%20for%20SS7%20Bricks.", "is_external": True},
                    "size": "md",
                }, "btn-whatsapp")
            ], 50, is_inner=True),
            make_column([
                make_widget("button", {
                    "text": "View SS7 Page →",
                    "link": {"url": "/ss7-bricks", "is_external": False},
                    "size": "md",
                }, "btn-dark")
            ], 50, is_inner=True)
        ], "bp-action-row")
    ], 50, "bp-ss7-content"),
    make_column([
        make_widget("image", {
            "image": {"url": "/wp-content/themes/brickpoint/assets/images/red-stack.png"},
            "image_size": "large",
        }, "bp-ss7-main-img img-zoom"),
        make_inner_section([
            make_column([make_widget("image", {"image": {"url": "/wp-content/themes/brickpoint/assets/images/stacked.png"}})], 33, is_inner=True),
            make_column([make_widget("image", {"image": {"url": "/wp-content/themes/brickpoint/assets/images/pile.png"}})], 33, is_inner=True),
            make_column([make_widget("image", {"image": {"url": "/wp-content/themes/brickpoint/assets/images/worker.png"}})], 34, is_inner=True),
        ], "bp-ss7-thumbs-row")
    ], 50, "bp-ss7-gallery-wrap")
], "bp-section bp-ss7-section")

# SECTION 5: FEATURED PRODUCTS
sec_featured_products = make_section([
    make_column([
        make_widget("heading", {"title": "Featured Products", "header_size": "p", "align": "center"}, "bp-eyebrow"),
        make_widget("heading", {"title": "Materials contractors ask for by name", "header_size": "h2", "align": "center"}, "bp-heading-2 font-display"),
        make_widget("text-editor", {"editor": "<p class=\"bp-body-text\" style=\"text-align:center;\">Live from the product catalogue — prices, units and WhatsApp ordering on every card.</p>"}),
        make_widget("bp_product_grid", {"count": 8, "columns": "4", "featured_only": "yes", "show_price": "yes", "show_whatsapp": "yes"}),
        make_widget("button", {
            "text": "Browse All Products →",
            "link": {"url": "/products", "is_external": False},
            "align": "center",
            "size": "md",
        }, "btn-brick")
    ], 100)
], "bp-section")

# SECTION 6: VIDEO SHOWCASE
sec_videos = make_section([
    make_column([
        make_widget("heading", {"title": "Inside BrickPoint", "header_size": "p"}, "bp-eyebrow"),
        make_widget("heading", {"title": "See the Strength Behind Every Brick", "header_size": "h2"}, "bp-heading-2 bp-head-light font-display"),
        make_widget("text-editor", {"editor": "<p class=\"bp-body-text bp-head-light-dim\">Manufacturing, bhattas, quality checks, materials and project references — on video.</p>"}),
        make_inner_section([
            make_column([
                make_widget("video", {
                    "video_type": "hosted",
                    "hosted_url": {"url": "https://videos.pexels.com/video-files/27758012/12218981_3840_2160_25fps.mp4"},
                    "show_controls": "yes",
                }, "bp-video-player hero-video-frame"),
                make_widget("heading", {"title": "★ Featured Facility Video", "header_size": "p"}, "bp-feat-badge")
            ], 65, is_inner=True),
            make_column([
                make_widget("video", {
                    "video_type": "hosted",
                    "hosted_url": {"url": "https://videos.pexels.com/video-files/11355903/11355903-uhd_3840_2160_25fps.mp4"},
                    "show_controls": "yes",
                }, "bp-video-player"),
                make_widget("heading", {"title": "From the Bhatta to Your Building", "header_size": "h4"}, "bp-video-sub-tag font-display"),
                make_widget("text-editor", {"editor": "<p class=\"bp-video-sub-desc\">Brick preparation, firing, stacking, loading and quality — the journey of every batch.</p>"}),
                make_widget("video", {
                    "video_type": "hosted",
                    "hosted_url": {"url": "https://videos.pexels.com/video-files/20731372/20731372-uhd_3840_2160_30fps.mp4"},
                    "show_controls": "yes",
                }, "bp-video-player"),
                make_widget("heading", {"title": "Materials That Become Landmarks", "header_size": "h4"}, "bp-video-sub-tag font-display"),
                make_widget("text-editor", {"editor": "<p class=\"bp-video-sub-desc\">Illustrative construction references from housing developments and building work.</p>"})
            ], 35, is_inner=True)
        ]),
        make_widget("bp_video_grid", {"count": 3, "columns": "3", "show_duration": "yes", "show_badge": "yes"}),
        make_widget("button", {
            "text": "View All Videos →",
            "link": {"url": "/videos", "is_external": False},
            "align": "center",
            "size": "md",
        }, "btn-ghost")
    ], 100)
], "bp-section bp-dark")

# SECTION 7: PROJECT REFERENCES
sec_projects = make_section([
    make_column([
        make_widget("heading", {"title": "Project References", "header_size": "p", "align": "center"}, "bp-eyebrow"),
        make_widget("heading", {"title": "Materials that become landmarks", "header_size": "h2", "align": "center"}, "bp-heading-2 font-display"),
        make_widget("text-editor", {"editor": "<p class=\"bp-body-text\" style=\"text-align:center;\">Illustrative construction references from Lahore housing societies and building work.</p>"}),
        make_widget("bp_project_grid", {"count": 3, "columns": "3", "show_location": "yes", "show_notice": "yes"}),
        make_widget("button", {
            "text": "Explore All Projects →",
            "link": {"url": "/projects", "is_external": False},
            "align": "center",
            "size": "md",
        }, "btn-ghost")
    ], 100)
], "bp-section")

# SECTION 8: WHO WE SERVE
sec_audiences = make_section([
    make_column([
        make_widget("heading", {"title": "Who We Serve", "header_size": "p", "align": "center"}, "bp-eyebrow"),
        make_widget("heading", {"title": "Built for the way you build", "header_size": "h2", "align": "center"}, "bp-heading-2 font-display"),
        make_widget("text-editor", {"editor": "<p class=\"bp-body-text\" style=\"text-align:center;\">Bulk supply, project quotations and coordinated materials — for every scale of builder.</p>"}),
        make_inner_section([
            make_column([
                make_widget("image", {"image": {"url": "/wp-content/themes/brickpoint/assets/images/site.png"}}, "bp-audience-media"),
                make_widget("heading", {"title": "For Contractors", "header_size": "h3"}, "font-display"),
                make_widget("text-editor", {"editor": "<p>Bulk material supply, project-based quotations and delivery coordination.</p>"}),
                make_widget("button", {"text": "Learn more →", "link": {"url": "/for-contractors"}, "size": "sm"}, "bp-audience-link")
            ], 33, "bp-audience-card card-hover", is_inner=True),
            make_column([
                make_widget("image", {"image": {"url": "/wp-content/themes/brickpoint/assets/images/bricklayer.png"}}, "bp-audience-media"),
                make_widget("heading", {"title": "For Builders", "header_size": "h3"}, "font-display"),
                make_widget("text-editor", {"editor": "<p>Consistent quality across every batch, with multi-category sourcing.</p>"}),
                make_widget("button", {"text": "Learn more →", "link": {"url": "/for-builders"}, "size": "sm"}, "bp-audience-link")
            ], 33, "bp-audience-card card-hover", is_inner=True),
            make_column([
                make_widget("image", {"image": {"url": "/wp-content/themes/brickpoint/assets/images/apt.png"}}, "bp-audience-media"),
                make_widget("heading", {"title": "For Construction Companies", "header_size": "h3"}, "font-display"),
                make_widget("text-editor", {"editor": "<p>Large-scale supply, documentation and dedicated contact.</p>"}),
                make_widget("button", {"text": "Learn more →", "link": {"url": "/for-companies"}, "size": "sm"}, "bp-audience-link")
            ], 34, "bp-audience-card card-hover", is_inner=True)
        ], "bp-grid cols-3")
    ], 100)
], "bp-section bp-sand-section")

# SECTION 9: CTA SECTION
sec_cta = make_section([
    make_column([
        make_widget("heading", {"title": "Get a fast quotation", "header_size": "p"}, "bp-eyebrow"),
        make_widget("heading", {"title": "Send your material list.<br />We handle the rest.", "header_size": "h2"}, "bp-heading-1 font-display"),
        make_widget("text-editor", {
            "editor": "<p class=\"bp-cta-meta\">📞 0315 2850818 • CEO: Syed Iftikhar Haider • Sales: Qasim Iqbal</p>"
        })
    ], 65, "bp-cta-text"),
    make_column([
        make_widget("button", {
            "text": "WhatsApp Your List",
            "link": {"url": "https://api.whatsapp.com/send?phone=923152850818&text=Assalam-o-Alaikum%20BrickPoint%2C%20Please%20share%20a%20quotation.", "is_external": True},
            "size": "lg",
        }, "btn-whatsapp btn-lg"),
        make_widget("button", {
            "text": "Request Quote Form",
            "link": {"url": "/contact", "is_external": False},
            "size": "lg",
        }, "btn-brick btn-lg")
    ], 35, "bp-cta-buttons")
], "bp-section bp-cta-section", bg_image="/wp-content/themes/brickpoint/assets/images/bricklayer.png")

templates["page-home.json"] = {
    "title": "Home",
    "type": "page",
    "version": "0.4",
    "content": [sec_hero, sec_trust, sec_categories, sec_ss7, sec_featured_products, sec_videos, sec_projects, sec_audiences, sec_cta]
}

# =========================================================================
# 2. ABOUT US PAGE (page-about.json)
# =========================================================================
about_hero = make_section([
    make_column([
        make_widget("heading", {"title": "Our Story", "header_size": "p"}, "bp-eyebrow"),
        make_widget("heading", {"title": "BrickPoint — strength you can build on", "header_size": "h1"}, "bp-heading-1 font-display"),
        make_widget("text-editor", {"editor": "<p class=\"bp-body-text bp-head-light-dim\">A construction-materials supplier bringing together trusted brick manufacturing units and a complete building-materials range for contractors, builders, developers and individual customers.</p>"}),
    ], 100)
], "bp-pagehead bp-dark", bg_image="/wp-content/themes/brickpoint/assets/images/bricklayer.png")

about_brand_story = make_section([
    make_column([
        make_widget("video", {
            "video_type": "hosted",
            "hosted_url": {"url": "https://videos.pexels.com/video-files/11355903/11355903-uhd_3840_2160_25fps.mp4"},
            "show_controls": "yes",
        }, "hero-video-frame"),
        make_widget("text-editor", {"editor": "<p style=\"text-align:center;font-size:0.85rem;color:#6b6560;\">Company video — manufacturing and site work</p>"})
    ], 50),
    make_column([
        make_widget("heading", {"title": "Brand Story", "header_size": "p"}, "bp-eyebrow"),
        make_widget("heading", {"title": "From bhatta kilns to landmark buildings", "header_size": "h2"}, "bp-heading-2 font-display"),
        make_widget("text-editor", {"editor": "<p class=\"bp-body-text\">BrickPoint unites Masha Allah Bricks Company, Fine Bricks Company and the SS7 Bricks range with a full construction-materials catalogue — so every customer, from a single-home builder to a large developer, can source reliably from one supplier.</p>"}),
        make_inner_section([
            make_column([
                make_widget("heading", {"title": "🎯 Mission", "header_size": "h4"}, "font-display"),
                make_widget("text-editor", {"editor": "<p>Reliable, quality materials with honest quotations.</p>"})
            ], 33, "bp-box", is_inner=True),
            make_column([
                make_widget("heading", {"title": "👁 Vision", "header_size": "h4"}, "font-display"),
                make_widget("text-editor", {"editor": "<p>The trusted materials partner for every project scale.</p>"})
            ], 33, "bp-box", is_inner=True),
            make_column([
                make_widget("heading", {"title": "❤ Values", "header_size": "h4"}, "font-display"),
                make_widget("text-editor", {"editor": "<p>Quality, consistency and responsive service.</p>"})
            ], 34, "bp-box", is_inner=True),
        ])
    ], 50)
], "bp-section")

about_capabilities = make_section([
    make_column([
        make_widget("heading", {"title": "Capabilities", "header_size": "p", "align": "center"}, "bp-eyebrow"),
        make_widget("heading", {"title": "What We Supply", "header_size": "h2", "align": "center"}, "bp-heading-2 font-display"),
        make_inner_section([
            make_column([
                make_widget("heading", {"title": "🏭 Brick Manufacturing", "header_size": "h4"}, "font-display"),
                make_widget("text-editor", {"editor": "<p>Multiple bhatta locations producing burnt-clay and SS7 bricks.</p>"})
            ], 25, "bp-box bp-dark", is_inner=True),
            make_column([
                make_widget("heading", {"title": "🛡 Quality Commitment", "header_size": "h4"}, "font-display"),
                make_widget("text-editor", {"editor": "<p>Sorted batches, consistent firing and honest grading.</p>"})
            ], 25, "bp-box bp-dark", is_inner=True),
            make_column([
                make_widget("heading", {"title": "👥 All Customer Sizes", "header_size": "h4"}, "font-display"),
                make_widget("text-editor", {"editor": "<p>Individual home builders to contractors and companies.</p>"})
            ], 25, "bp-box bp-dark", is_inner=True),
            make_column([
                make_widget("heading", {"title": "🚚 Project Support", "header_size": "h4"}, "font-display"),
                make_widget("text-editor", {"editor": "<p>Stage-wise quotations and delivery coordination.</p>"})
            ], 25, "bp-box bp-dark", is_inner=True),
        ])
    ], 100)
], "bp-section bp-sand-section")

about_leadership = make_section([
    make_column([
        make_widget("heading", {"title": "Management", "header_size": "p", "align": "center"}, "bp-eyebrow"),
        make_widget("heading", {"title": "Leadership", "header_size": "h2", "align": "center"}, "bp-heading-2 font-display"),
        make_widget("text-editor", {"editor": "<p style=\"text-align:center;\">Direct access to decision-makers — no layers between you and your quotation.</p>"}),
        make_inner_section([
            make_column([
                make_widget("image", {"image": {"url": "/wp-content/themes/brickpoint/assets/images/worker.png"}}),
                make_widget("heading", {"title": "Syed Iftikhar Haider", "header_size": "h3", "align": "center"}, "font-display"),
                make_widget("heading", {"title": "Chief Executive Officer", "header_size": "p", "align": "center"}, "text-orange"),
                make_widget("text-editor", {"editor": "<p style=\"text-align:center;\">BrickPoint • 0315 2850818</p>"})
            ], 50, "bp-card p-6", is_inner=True),
            make_column([
                make_widget("image", {"image": {"url": "/wp-content/themes/brickpoint/assets/images/brick-mason.png"}}),
                make_widget("heading", {"title": "Qasim Iqbal", "header_size": "h3", "align": "center"}, "font-display"),
                make_widget("heading", {"title": "Sales Manager", "header_size": "p", "align": "center"}, "text-orange"),
                make_widget("text-editor", {"editor": "<p style=\"text-align:center;\">BrickPoint • 0315 2850818</p>"})
            ], 50, "bp-card p-6", is_inner=True),
        ]),
        make_inner_section([
            make_column([
                make_widget("button", {"text": "View Products →", "link": {"url": "/products"}, "size": "md"}, "btn-brick")
            ], 33, is_inner=True),
            make_column([
                make_widget("button", {"text": "Contact Us", "link": {"url": "/contact"}, "size": "md"}, "btn-ghost")
            ], 33, is_inner=True),
            make_column([
                make_widget("button", {"text": "Our Locations", "link": {"url": "/locations"}, "size": "md"}, "btn-ghost")
            ], 34, is_inner=True),
        ], "bp-center")
    ], 100)
], "bp-section")

templates["page-about.json"] = {
    "title": "About Us",
    "type": "page",
    "version": "0.4",
    "content": [about_hero, about_brand_story, about_capabilities, about_leadership]
}

# =========================================================================
# 3. CONTACT PAGE (page-contact.json)
# =========================================================================
contact_hero = make_section([
    make_column([
        make_widget("heading", {"title": "Get In Touch", "header_size": "p"}, "bp-eyebrow"),
        make_widget("heading", {"title": "Contact BrickPoint", "header_size": "h1"}, "bp-heading-1 font-display"),
        make_widget("text-editor", {"editor": "<p class=\"bp-body-text bp-head-light-dim\">Call, WhatsApp or send the quotation form — we respond fast on working hours.</p>"}),
    ], 100)
], "bp-pagehead bp-dark")

contact_body = make_section([
    make_column([
        make_widget("heading", {"title": "Direct Contact", "header_size": "h3"}, "font-display"),
        make_widget("text-editor", {
            "editor": "<p>📞 <strong>Phone:</strong> 0315 2850818<br />✉ <strong>Email:</strong> info@brickpoint.pk<br />📍 <strong>Address:</strong> Lahore, Punjab, Pakistan<br />CEO: Syed Iftikhar Haider • Sales: Qasim Iqbal</p>"
        }),
        make_widget("button", {
            "text": "Chat on WhatsApp",
            "link": {"url": "https://api.whatsapp.com/send?phone=923152850818", "is_external": True},
            "size": "md",
        }, "btn-whatsapp btn-block"),
        make_widget("heading", {"title": "Office Map", "header_size": "h4"}, "font-display"),
        make_widget("button", {
            "text": "📍 Open Google Maps",
            "link": {"url": "https://maps.app.goo.gl/GACXw15YxyV4bK5t8", "is_external": True},
            "size": "sm",
        }, "btn-dark btn-block"),
        make_widget("button", {
            "text": "View All Bhatta Locations",
            "link": {"url": "/locations", "is_external": False},
            "size": "sm",
        }, "btn-ghost btn-block")
    ], 35, "bp-box bp-dark"),
    make_column([
        make_widget("heading", {"title": "Request a Quotation", "header_size": "h2"}, "font-display"),
        make_widget("text-editor", {"editor": "<p>Fill out the material quotation form below or send your BOQ on WhatsApp for instant response.</p>"}),
        make_widget("html", {
            "html": "<form action=\"https://api.whatsapp.com/send\" method=\"get\" target=\"_blank\"><input type=\"hidden\" name=\"phone\" value=\"923152850818\" /><div style=\"display:grid;grid-gap:15px;grid-template-columns:1fr 1fr;\"><div><label style=\"font-weight:700;font-size:0.85rem;\">Full Name *</label><input type=\"text\" name=\"name\" required placeholder=\"Your name\" style=\"width:100%;padding:10px;border-radius:10px;border:1px solid #ddd;\" /></div><div><label style=\"font-weight:700;font-size:0.85rem;\">Phone Number *</label><input type=\"text\" name=\"user_phone\" required placeholder=\"03xx xxxxxxx\" style=\"width:100%;padding:10px;border-radius:10px;border:1px solid #ddd;\" /></div><div><label style=\"font-weight:700;font-size:0.85rem;\">Email</label><input type=\"email\" name=\"email\" placeholder=\"you@email.com\" style=\"width:100%;padding:10px;border-radius:10px;border:1px solid #ddd;\" /></div><div><label style=\"font-weight:700;font-size:0.85rem;\">Material Required</label><select name=\"material\" style=\"width:100%;padding:10px;border-radius:10px;border:1px solid #ddd;\"><option>SS7 Bricks</option><option>First Class Bricks (Awwal)</option><option>Cement</option><option>Crush / Bajri</option><option>Sand / Rait</option><option>Steel</option><option>Pipes & Cables</option><option>Complete BOQ</option></select></div><div style=\"grid-column:1/-1;\"><label style=\"font-weight:700;font-size:0.85rem;\">Delivery Location</label><input type=\"text\" name=\"loc\" placeholder=\"e.g. DHA Phase 6, Lahore\" style=\"width:100%;padding:10px;border-radius:10px;border:1px solid #ddd;\" /></div><div style=\"grid-column:1/-1;\"><label style=\"font-weight:700;font-size:0.85rem;\">Message / Bill of Quantities</label><textarea name=\"text\" rows=\"4\" placeholder=\"Share your required quantities and timeline...\" style=\"width:100%;padding:10px;border-radius:10px;border:1px solid #ddd;\"></textarea></div><div style=\"grid-column:1/-1;\"><button type=\"submit\" class=\"btn-brick btn-lg\" style=\"width:100%;\">Submit Quotation Request →</button></div></div></form>"
        })
    ], 65, "bp-box")
], "bp-section")

templates["page-contact.json"] = {
    "title": "Contact Us",
    "type": "page",
    "version": "0.4",
    "content": [contact_hero, contact_body]
}

# =========================================================================
# 4. SS7 BRICKS PAGE (page-ss7-bricks.json)
# =========================================================================
ss7_hero = make_section([
    make_column([
        make_widget("heading", {"title": "★ Flagship Range", "header_size": "p"}, "bp-eyebrow"),
        make_widget("heading", {"title": "SS7 <span class=\"text-orange\">Bricks</span>", "header_size": "h1"}, "bp-heading-1 font-display"),
        make_widget("text-editor", {"editor": "<p class=\"bp-body-text bp-head-light-dim\">Our signature high-strength brick — consistent firing, sharp edges and dependable supply for homes, commercial work and boundary structures.</p>"}),
        make_inner_section([
            make_column([
                make_widget("button", {
                    "text": "Request SS7 Quotation",
                    "link": {"url": "https://api.whatsapp.com/send?phone=923152850818&text=Assalam-o-Alaikum%20BrickPoint%2C%20I%20need%20a%20quotation%20for%20SS7%20Bricks.", "is_external": True},
                    "size": "lg",
                }, "btn-whatsapp")
            ], 50, is_inner=True),
            make_column([
                make_widget("button", {
                    "text": "Browse All Products",
                    "link": {"url": "/products", "is_external": False},
                    "size": "lg",
                }, "btn-ghost")
            ], 50, is_inner=True)
        ], "bp-action-row")
    ], 50),
    make_column([
        make_widget("image", {
            "image": {"url": "/wp-content/themes/brickpoint/assets/images/red-stack.png"},
            "image_size": "large",
        }, "hero-video-frame ss7-brick-loop"),
    ], 50)
], "bp-hero bp-dark", bg_image="/wp-content/themes/brickpoint/assets/images/red-stack.png")

ss7_specs = make_section([
    make_column([
        make_widget("heading", {"title": "Editable Specifications", "header_size": "p", "align": "center"}, "bp-eyebrow"),
        make_widget("heading", {"title": "SS7 at a Glance", "header_size": "h2", "align": "center"}, "bp-heading-2 font-display"),
        make_widget("text-editor", {"editor": "<p style=\"text-align:center;\">Specification fields are editable from the product record — update size, colour, type, strength, usage, availability and delivery area any time.</p>"}),
        make_inner_section([
            make_column([
                make_widget("heading", {"title": "📏 Size", "header_size": "h4"}, "font-display"),
                make_widget("text-editor", {"editor": "<p>Standard chamber size (9\" x 4.5\" x 3\")</p>"})
            ], 25, "bp-box", is_inner=True),
            make_column([
                make_widget("heading", {"title": "🎨 Colour", "header_size": "h4"}, "font-display"),
                make_widget("text-editor", {"editor": "<p>Classic kiln-fired deep red with natural variation</p>"})
            ], 25, "bp-box", is_inner=True),
            make_column([
                make_widget("heading", {"title": "🧱 Type & Strength", "header_size": "h4"}, "font-display"),
                make_widget("text-editor", {"editor": "<p>Burnt-clay SS7 — high crushing strength grade (>2000 PSI)</p>"})
            ], 25, "bp-box", is_inner=True),
            make_column([
                make_widget("heading", {"title": "🚚 Usage & Delivery", "header_size": "h4"}, "font-display"),
                make_widget("text-editor", {"editor": "<p>Homes • Commercial • Boundary — delivery on schedule</p>"})
            ], 25, "bp-box", is_inner=True),
        ])
    ], 100)
], "bp-section")

templates["page-ss7-bricks.json"] = {
    "title": "SS7 Bricks",
    "type": "page",
    "version": "0.4",
    "content": [ss7_hero, ss7_specs, sec_featured_products, sec_cta]
}

# =========================================================================
# 5. FOR CONTRACTORS PAGE (page-for-contractors.json)
# =========================================================================
contractors_hero = make_section([
    make_column([
        make_widget("heading", {"title": "For Contractors", "header_size": "p"}, "bp-eyebrow"),
        make_widget("heading", {"title": "Bulk supply that keeps your sites moving", "header_size": "h1"}, "bp-heading-1 font-display"),
        make_widget("text-editor", {"editor": "<p class=\"bp-body-text bp-head-light-dim\">Project-based quotations, reliable availability and delivery coordination across brick and material categories.</p>"}),
        make_inner_section([
            make_column([
                make_widget("button", {
                    "text": "Get Contractor Rates",
                    "link": {"url": "https://api.whatsapp.com/send?phone=923152850818&text=Assalam-o-Alaikum%20BrickPoint%2C%20I%20am%20a%20contractor%20and%20need%20bulk%20rates.", "is_external": True},
                    "size": "lg",
                }, "btn-whatsapp")
            ], 50, is_inner=True),
            make_column([
                make_widget("button", {"text": "Browse Products", "link": {"url": "/products"}, "size": "lg"}, "btn-ghost")
            ], 50, is_inner=True)
        ], "bp-action-row")
    ], 100)
], "bp-pagehead bp-dark", bg_image="/wp-content/themes/brickpoint/assets/images/site.png")

contractors_benefits = make_section([
    make_column([
        make_widget("heading", {"title": "Contractor Benefits", "header_size": "p", "align": "center"}, "bp-eyebrow"),
        make_widget("heading", {"title": "Why Contractors Choose BrickPoint", "header_size": "h2", "align": "center"}, "bp-heading-2 font-display"),
        make_inner_section([
            make_column([
                make_widget("heading", {"title": "✔ Bulk material supply", "header_size": "h4"}, "font-display"),
                make_widget("text-editor", {"editor": "<p>Trolley, thousand-brick and tonnage quantities with sorted batches.</p>"})
            ], 33, "bp-box", is_inner=True),
            make_column([
                make_widget("heading", {"title": "✔ Project-based quotations", "header_size": "h4"}, "font-display"),
                make_widget("text-editor", {"editor": "<p>Send your BOQ or stage list — get one consolidated quote.</p>"})
            ], 33, "bp-box", is_inner=True),
            make_column([
                make_widget("heading", {"title": "✔ Delivery coordination", "header_size": "h4"}, "font-display"),
                make_widget("text-editor", {"editor": "<p>Schedule deliveries stage-wise with site-location planning.</p>"})
            ], 34, "bp-box", is_inner=True),
        ]),
        make_inner_section([
            make_column([
                make_widget("heading", {"title": "✔ Reliable availability", "header_size": "h4"}, "font-display"),
                make_widget("text-editor", {"editor": "<p>Multiple bhatta units back consistent brick supply.</p>"})
            ], 33, "bp-box", is_inner=True),
            make_column([
                make_widget("heading", {"title": "✔ Full category range", "header_size": "h4"}, "font-display"),
                make_widget("text-editor", {"editor": "<p>Bricks, cement, aggregates, steel, pipes, electricals, finishes.</p>"})
            ], 33, "bp-box", is_inner=True),
            make_column([
                make_widget("heading", {"title": "✔ Direct WhatsApp line", "header_size": "h4"}, "font-display"),
                make_widget("text-editor", {"editor": "<p>Fast answers on rates, stock and delivery slots.</p>"})
            ], 34, "bp-box", is_inner=True),
        ])
    ], 100)
], "bp-section")

templates["page-for-contractors.json"] = {
    "title": "For Contractors",
    "type": "page",
    "version": "0.4",
    "content": [contractors_hero, contractors_benefits, sec_cta]
}

# =========================================================================
# 6. FOR BUILDERS PAGE (page-for-builders.json)
# =========================================================================
builders_hero = make_section([
    make_column([
        make_widget("heading", {"title": "For Builders", "header_size": "p"}, "bp-eyebrow"),
        make_widget("heading", {"title": "Consistent quality, house after house", "header_size": "h1"}, "bp-heading-1 font-display"),
        make_widget("text-editor", {"editor": "<p class=\"bp-body-text bp-head-light-dim\">Source complete material sets with consistent batches — from foundation to finishing.</p>"}),
        make_inner_section([
            make_column([
                make_widget("button", {
                    "text": "Discuss Your Build",
                    "link": {"url": "https://api.whatsapp.com/send?phone=923152850818&text=Assalam-o-Alaikum%20BrickPoint%2C%20I%20am%20a%20builder.", "is_external": True},
                    "size": "lg",
                }, "btn-whatsapp")
            ], 50, is_inner=True),
            make_column([
                make_widget("button", {"text": "SS7 Bricks Range", "link": {"url": "/ss7-bricks"}, "size": "lg"}, "btn-ghost")
            ], 50, is_inner=True)
        ], "bp-action-row")
    ], 100)
], "bp-pagehead bp-dark", bg_image="/wp-content/themes/brickpoint/assets/images/bricklayer.png")

templates["page-for-builders.json"] = {
    "title": "For Builders",
    "type": "page",
    "version": "0.4",
    "content": [builders_hero, contractors_benefits, sec_cta]
}

# =========================================================================
# 7. FOR CONSTRUCTION COMPANIES (page-for-companies.json)
# =========================================================================
companies_hero = make_section([
    make_column([
        make_widget("heading", {"title": "For Construction Companies", "header_size": "p"}, "bp-eyebrow"),
        make_widget("heading", {"title": "Large-scale supply, coordinated professionally", "header_size": "h1"}, "bp-heading-1 font-display"),
        make_widget("text-editor", {"editor": "<p class=\"bp-body-text bp-head-light-dim\">Multi-location coordination, documentation support and a dedicated contact for corporate accounts.</p>"}),
        make_inner_section([
            make_column([
                make_widget("button", {
                    "text": "Corporate Inquiry",
                    "link": {"url": "https://api.whatsapp.com/send?phone=923152850818&text=Assalam-o-Alaikum%20BrickPoint%2C%20Corporate%20Inquiry.", "is_external": True},
                    "size": "lg",
                }, "btn-whatsapp")
            ], 50, is_inner=True),
            make_column([
                make_widget("button", {"text": "Contact Form", "link": {"url": "/contact"}, "size": "lg"}, "btn-ghost")
            ], 50, is_inner=True)
        ], "bp-action-row")
    ], 100)
], "bp-pagehead bp-dark", bg_image="/wp-content/themes/brickpoint/assets/images/apt.png")

templates["page-for-companies.json"] = {
    "title": "For Construction Companies",
    "type": "page",
    "version": "0.4",
    "content": [companies_hero, contractors_benefits, sec_cta]
}

# =========================================================================
# 8. CONSTRUCTION MATERIALS (page-materials.json)
# =========================================================================
materials_hero = make_section([
    make_column([
        make_widget("heading", {"title": "Complete Range", "header_size": "p"}, "bp-eyebrow"),
        make_widget("heading", {"title": "Construction Materials", "header_size": "h1"}, "bp-heading-1 font-display"),
        make_widget("text-editor", {"editor": "<p class=\"bp-body-text bp-head-light-dim\">Cement to finishes — one quotation, coordinated supply, WhatsApp-fast response.</p>"}),
    ], 100)
], "bp-pagehead bp-dark")

templates["page-materials.json"] = {
    "title": "Construction Materials",
    "type": "page",
    "version": "0.4",
    "content": [materials_hero, sec_categories, sec_featured_products, sec_cta]
}

# =========================================================================
# 9. PRIVACY & TERMS
# =========================================================================
templates["page-privacy.json"] = {
    "title": "Privacy Policy",
    "type": "page",
    "version": "0.4",
    "content": [
        make_section([
            make_column([
                make_widget("heading", {"title": "Privacy Policy", "header_size": "h1"}, "font-display"),
                make_widget("text-editor", {
                    "editor": "<p>BrickPoint Pakistan respects your privacy. Information submitted through our contact forms or WhatsApp messaging is used exclusively to facilitate material quotes, arrange logistics, and coordinate order delivery. We do not sell or share personal customer information with external third parties.</p>"
                })
            ], 100)
        ], "bp-section bp-container")
    ]
}

templates["page-terms.json"] = {
    "title": "Terms & Conditions",
    "type": "page",
    "version": "0.4",
    "content": [
        make_section([
            make_column([
                make_widget("heading", {"title": "Terms & Conditions", "header_size": "h1"}, "font-display"),
                make_widget("text-editor", {
                    "editor": "<p>All brick and construction material quotations provided by BrickPoint are subject to site access, unloading feasibility, and prevailing market rates for raw ingredients. Quoted rates remain valid for the period specified on formal quotation slips.</p>"
                })
            ], 100)
        ], "bp-section bp-container")
    ]
}

# =========================================================================
# 10. HEADER DEFAULT (header-default.json) — THEME BUILDER HEADER
# =========================================================================
header_topbar = make_section([
    make_column([
        make_widget("text-editor", {
            "editor": "<span style=\"color:#fff;font-weight:700;\">📞 0315 2850818</span> &nbsp;•&nbsp; <span style=\"color:#a8a29e;\">Masha Allah Bricks Co. • Fine Bricks Co. • SS7 Bricks</span>"
        })
    ], 60),
    make_column([
        make_widget("text-editor", {
            "editor": "<div style=\"text-align:right;\"><a href=\"/locations\" style=\"color:#e5e5e5;margin-right:15px;\">Our Bhattas</a><a href=\"/videos\" style=\"color:#e5e5e5;margin-right:15px;\">Videos</a><a href=\"/about\" style=\"color:#e5e5e5;\">About Us</a></div>"
        })
    ], 40)
], "bp-topbar")

header_main = make_section([
    make_column([
        make_widget("bp_header_logo_widget", {
            "desktop_height": 44,
            "mobile_height": 36,
        })
    ], 25, "bp-logo-wrap"),
    make_column([
        make_widget("html", {
            "html": "<nav class=\"bp-nav\"><ul class=\"bp-menu\"><li><a href=\"/\">Home</a></li><li><a href=\"/ss7-bricks\" class=\"bp-highlight-menu-item\">SS7 Bricks</a></li><li><a href=\"/products\">Products</a></li><li><a href=\"/categories\">Categories</a></li><li><a href=\"/construction-materials\">Materials</a></li><li><a href=\"/videos\">Videos</a></li><li><a href=\"/projects\">Projects</a></li><li><a href=\"/about\">About</a></li><li><a href=\"/contact\">Contact</a></li></ul></nav>"
        })
    ], 50),
    make_column([
        make_inner_section([
            make_column([
                make_widget("button", {
                    "text": "WhatsApp Us",
                    "link": {"url": "https://api.whatsapp.com/send?phone=923152850818", "is_external": True},
                    "size": "sm",
                }, "btn-whatsapp")
            ], 50, is_inner=True),
            make_column([
                make_widget("button", {
                    "text": "Request Quote",
                    "link": {"url": "/contact", "is_external": False},
                    "size": "sm",
                }, "btn-brick")
            ], 50, is_inner=True)
        ], "bp-header-cta")
    ], 25)
], "bp-header sticky-header")

templates["header-default.json"] = {
    "title": "Header Default",
    "type": "header",
    "version": "0.4",
    "content": [header_topbar, header_main]
}

# =========================================================================
# 11. FOOTER DEFAULT (footer-default.json) — THEME BUILDER FOOTER
# =========================================================================
footer_main = make_section([
    # Col 1: Logo & About
    make_column([
        make_widget("bp_footer_logo_widget", {
            "desktop_height": 52,
            "mobile_height": 42,
        }),
        make_widget("text-editor", {
            "editor": "<p class=\"bp-footer-desc\">Premium bricks and reliable construction materials for homes, commercial developments, and large-scale building projects.</p><p>📞 0315 2850818<br />✉ info@brickpoint.pk<br />📍 Lahore, Punjab, Pakistan</p>"
        }),
        make_widget("html", {
            "html": "<div class=\"bp-social\"><a href=\"https://facebook.com/brickpoint.pk/\" target=\"_blank\">f</a><a href=\"https://instagram.com/brickpoint.pk/\" target=\"_blank\">in</a><a href=\"https://x.com/BrickPointPK\" target=\"_blank\">x</a><a href=\"https://tiktok.com/@brickpoint.pk/\" target=\"_blank\">t</a></div>"
        })
    ], 30, "bp-footer-col"),
    # Col 2: Products & Company
    make_column([
        make_widget("heading", {"title": "Products", "header_size": "h4"}, "bp-footer-title"),
        make_widget("text-editor", {
            "editor": "<ul class=\"bp-footer-links\"><li><a href=\"/ss7-bricks\">SS7 Bricks</a></li><li><a href=\"/products\">All Products</a></li><li><a href=\"/categories\">Product Categories</a></li><li><a href=\"/construction-materials\">Construction Materials</a></li><li><a href=\"/videos\">Product Videos</a></li></ul>"
        }),
        make_widget("heading", {"title": "Company", "header_size": "h4"}, "bp-footer-title"),
        make_widget("text-editor", {
            "editor": "<ul class=\"bp-footer-links\"><li><a href=\"/about\">About Us</a></li><li><a href=\"/projects\">Projects</a></li><li><a href=\"/blog\">Blog</a></li><li><a href=\"/locations\">Locations</a></li></ul>"
        })
    ], 22, "bp-footer-col"),
    # Col 3: Who We Serve & Units
    make_column([
        make_widget("heading", {"title": "Who We Serve", "header_size": "h4"}, "bp-footer-title"),
        make_widget("text-editor", {
            "editor": "<ul class=\"bp-footer-links\"><li><a href=\"/for-contractors\">For Contractors</a></li><li><a href=\"/for-builders\">For Builders</a></li><li><a href=\"/for-companies\">For Construction Companies</a></li><li><a href=\"/contact\">Request Quotation</a></li></ul>"
        }),
        make_widget("heading", {"title": "Our Units", "header_size": "h4"}, "bp-footer-title"),
        make_widget("text-editor", {
            "editor": "<ul class=\"bp-footer-links bp-dim-links\"><li>Masha Allah Bricks Company</li><li>Fine Bricks Company</li><li>SS7 Bricks</li><li>CEO: Syed Iftikhar Haider</li><li>Sales: Qasim Iqbal</li></ul>"
        })
    ], 22, "bp-footer-col"),
    # Col 4: Quotation & WhatsApp
    make_column([
        make_widget("heading", {"title": "Get a Quotation", "header_size": "h4"}, "bp-footer-title"),
        make_widget("text-editor", {
            "editor": "<p class=\"bp-footer-desc\">Send your material list on WhatsApp and get availability, delivery details, and final quotation.</p>"
        }),
        make_widget("button", {
            "text": "Chat on WhatsApp",
            "link": {"url": "https://api.whatsapp.com/send?phone=923152850818&text=Assalam-o-Alaikum%20BrickPoint%2C%20I%20need%20a%20quotation.", "is_external": True},
            "size": "md",
        }, "btn-whatsapp btn-block"),
        make_widget("button", {
            "text": "Contact Form",
            "link": {"url": "/contact", "is_external": False},
            "size": "sm",
        }, "btn-ghost btn-block")
    ], 26, "bp-footer-col"),
], "bp-footer bp-dark")

footer_bottom = make_section([
    make_column([
        make_widget("text-editor", {
            "editor": "<div class=\"bp-footer-bottom-inner\"><p>© 2026 BrickPoint. All rights reserved.</p><div class=\"bp-footer-legal\"><a href=\"/privacy\">Privacy Policy</a> &bull; <a href=\"/terms\">Terms & Conditions</a> &bull; <a href=\"/locations\">Locations</a></div></div>"
        })
    ], 100)
], "bp-footer-bottom")

templates["footer-default.json"] = {
    "title": "Footer Default",
    "type": "footer",
    "version": "0.4",
    "content": [footer_main, footer_bottom]
}

# =========================================================================
# 12. DYNAMIC CPT TEMPLATES (Theme Builder Single & Archive)
# =========================================================================

# Single Product
templates["single-product.json"] = {
    "title": "Single Product Template",
    "type": "single-post",
    "version": "0.4",
    "content": [
        make_section([
            make_column([
                make_widget("image", {
                    "image": {"url": "/wp-content/themes/brickpoint/assets/images/red-stack.png"},
                    "image_size": "large",
                }, "bp-product-hero-media img-zoom"),
            ], 50),
            make_column([
                make_widget("heading", {"title": "Product Title", "header_size": "h1"}, "font-display"),
                make_widget("heading", {"title": "Price on Request", "header_size": "h3"}, "bp-price-main text-orange"),
                make_widget("text-editor", {"editor": "<p>High-grade construction material manufactured and tested according to Pakistani building standards.</p>"}),
                make_widget("button", {
                    "text": "Order on WhatsApp",
                    "link": {"url": "https://api.whatsapp.com/send?phone=923152850818", "is_external": True},
                    "size": "lg",
                }, "btn-whatsapp btn-block"),
                make_widget("button", {
                    "text": "Call for Rate",
                    "link": {"url": "tel:03152850818", "is_external": False},
                    "size": "md",
                }, "btn-ghost btn-block")
            ], 50)
        ], "bp-section bp-product-layout"),
        sec_cta
    ]
}

# Archive Product
templates["archive-product.json"] = {
    "title": "Products Archive Template",
    "type": "archive",
    "version": "0.4",
    "content": [
        make_section([
            make_column([
                make_widget("heading", {"title": "Catalogue", "header_size": "p", "align": "center"}, "bp-eyebrow"),
                make_widget("heading", {"title": "All Products", "header_size": "h1", "align": "center"}, "bp-heading-1 font-display"),
                make_widget("text-editor", {"editor": "<p style=\"text-align:center;\">Every product with WhatsApp ordering — no cart, no checkout, just fast quotations.</p>"}),
                make_widget("bp_product_grid", {"count": 12, "columns": "4", "show_price": "yes", "show_whatsapp": "yes"})
            ], 100)
        ], "bp-section")
    ]
}

# Single Video
templates["single-video.json"] = {
    "title": "Single Video Template",
    "type": "single-post",
    "version": "0.4",
    "content": [
        make_section([
            make_column([
                make_widget("video", {
                    "video_type": "hosted",
                    "hosted_url": {"url": "https://videos.pexels.com/video-files/27758012/12218981_3840_2160_25fps.mp4"},
                    "show_controls": "yes",
                }, "hero-video-frame"),
                make_widget("heading", {"title": "Inside BrickPoint Video", "header_size": "h1"}, "font-display bp-mt"),
                make_widget("text-editor", {"editor": "<p>Walkthrough of our brick manufacturing plant, clay mixing pits, and continuous coal-firing chambers.</p>"}),
                make_widget("button", {"text": "← Back to Videos", "link": {"url": "/videos"}}, "btn-ghost")
            ], 100)
        ], "bp-section bp-narrow")
    ]
}

# Archive Video
templates["archive-video.json"] = {
    "title": "Videos Archive Template",
    "type": "archive",
    "version": "0.4",
    "content": [
        make_section([
            make_column([
                make_widget("heading", {"title": "Video Library", "header_size": "p", "align": "center"}, "bp-eyebrow"),
                make_widget("heading", {"title": "Inside BrickPoint", "header_size": "h1", "align": "center"}, "bp-heading-1 font-display"),
                make_widget("bp_video_grid", {"count": 6, "columns": "3", "show_duration": "yes", "show_badge": "yes"})
            ], 100)
        ], "bp-section")
    ]
}

# Single Project
templates["single-project.json"] = {
    "title": "Single Project Template",
    "type": "single-post",
    "version": "0.4",
    "content": [
        make_section([
            make_column([
                make_widget("heading", {"title": "Project Reference", "header_size": "p"}, "bp-eyebrow"),
                make_widget("heading", {"title": "DHA Lahore Villa Reference", "header_size": "h1"}, "font-display"),
                make_widget("image", {"image": {"url": "/wp-content/themes/brickpoint/assets/images/villa1.png"}}, "bp-post-hero-img img-zoom"),
                make_widget("text-editor", {
                    "editor": "<div class=\"bp-notice-box\"><strong>Content notice:</strong> Illustrative construction reference. BrickPoint does not claim supply to any named society unless verified.</div><p>High-end structural masonry combining exposed SS7 red bricks with reinforced concrete.</p>"
                }),
                make_widget("button", {
                    "text": "Inquire on WhatsApp",
                    "link": {"url": "https://api.whatsapp.com/send?phone=923152850818", "is_external": True},
                }, "btn-whatsapp")
            ], 100)
        ], "bp-section bp-narrow")
    ]
}

# Archive Project
templates["archive-project.json"] = {
    "title": "Projects Archive Template",
    "type": "archive",
    "version": "0.4",
    "content": [
        make_section([
            make_column([
                make_widget("heading", {"title": "References & Inspiration", "header_size": "p", "align": "center"}, "bp-eyebrow"),
                make_widget("heading", {"title": "Projects", "header_size": "h1", "align": "center"}, "bp-heading-1 font-display"),
                make_widget("bp_project_grid", {"count": 6, "columns": "3", "show_location": "yes", "show_notice": "yes"})
            ], 100)
        ], "bp-section")
    ]
}

# Single Post
templates["single-post.json"] = {
    "title": "Single Blog Post Template",
    "type": "single-post",
    "version": "0.4",
    "content": [
        make_section([
            make_column([
                make_widget("heading", {"title": "Guides & Updates", "header_size": "p"}, "bp-eyebrow"),
                make_widget("heading", {"title": "Article Title", "header_size": "h1"}, "font-display"),
                make_widget("image", {"image": {"url": "/wp-content/themes/brickpoint/assets/images/brick-mason.png"}}, "bp-post-hero-img"),
                make_widget("text-editor", {"editor": "<p>Practical insights and field guidelines from BrickPoint masonry specialists.</p>"}),
                make_widget("button", {"text": "← Back to Blog", "link": {"url": "/blog"}}, "btn-ghost")
            ], 100)
        ], "bp-section bp-narrow")
    ]
}

# Archive Post
templates["archive-post.json"] = {
    "title": "Blog Archive Template",
    "type": "archive",
    "version": "0.4",
    "content": [
        make_section([
            make_column([
                make_widget("heading", {"title": "Guides & Updates", "header_size": "p", "align": "center"}, "bp-eyebrow"),
                make_widget("heading", {"title": "Blog", "header_size": "h1", "align": "center"}, "bp-heading-1 font-display"),
                make_widget("bp_blog_grid", {"count": 6, "columns": "3", "show_date": "yes", "show_author": "yes"})
            ], 100)
        ], "bp-section")
    ]
}

# Modular Sections
templates["section-hero.json"] = {"title": "Modular Hero Section", "type": "section", "version": "0.4", "content": [sec_hero]}
templates["section-categories.json"] = {"title": "Modular Categories Section", "type": "section", "version": "0.4", "content": [sec_categories]}
templates["section-ss7-showcase.json"] = {"title": "Modular SS7 Showcase Section", "type": "section", "version": "0.4", "content": [sec_ss7]}
templates["section-featured-products.json"] = {"title": "Modular Featured Products Section", "type": "section", "version": "0.4", "content": [sec_featured_products]}
templates["section-video-showcase.json"] = {"title": "Modular Video Showcase Section", "type": "section", "version": "0.4", "content": [sec_videos]}
templates["section-cta-banner.json"] = {"title": "Modular WhatsApp CTA Banner Section", "type": "section", "version": "0.4", "content": [sec_cta]}

# Write all templates to disk
for filename, tpl_data in templates.items():
    filepath = os.path.join(DEST, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(tpl_data, f, indent=2)

print(f"Generated {len(templates)} true Elementor templates in {DEST}")
