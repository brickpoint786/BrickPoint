import os

DEST = "/home/user/BrickPoint/wordpress/brickpoint"
files = {}

# style.css
files["style.css"] = """/*
Theme Name: BrickPoint
Theme URI: https://brickpoint.pk/
Author: BrickPoint
Author URI: https://brickpoint.pk/
Description: Premium construction-materials and brick manufacturing WordPress theme for BrickPoint. Native Elementor Free and Elementor Pro Theme Builder support, one-click demo import, custom Product (bp_product), Video (bp_video), Project (bp_project), and Location (bp_location) post types with direct WhatsApp ordering. No WooCommerce required.
Version: 1.0.0
Requires at least: 6.0
Tested up to: 6.7
Requires PHP: 7.4
License: GNU General Public License v2 or later
License URI: http://www.gnu.org/licenses/gpl-2.0.html
Text Domain: brickpoint
Tags: construction, business, bricks, responsive, custom-colors, featured-images, threaded-comments, full-width-template
*/

:root {
  --bp-ink: #141210;
  --bp-charcoal: #1c1a17;
  --bp-coal: #24211d;
  --bp-brick: #c2410c;
  --bp-brick-deep: #9a3412;
  --bp-ember: #ea580c;
  --bp-sand: #f6f1ea;
  --bp-stone: #e9e1d5;
  --bp-gold: #d9a441;
  --bp-muted: #6b6560;
  --bp-radius: 18px;
  --bp-container: 1200px;
}
"""

# functions.php
files["functions.php"] = """<?php
/**
 * BrickPoint Theme Bootstrap
 *
 * @package BrickPoint
 * @version 1.0.0
 */

if ( ! defined( 'ABSPATH' ) ) {
  exit;
}

define( 'BRICKPOINT_VERSION', '1.0.0' );
define( 'BRICKPOINT_DIR', get_template_directory() );
define( 'BRICKPOINT_URI', get_template_directory_uri() );

// Core modules
require_once BRICKPOINT_DIR . '/inc/setup.php';
require_once BRICKPOINT_DIR . '/inc/enqueue.php';
require_once BRICKPOINT_DIR . '/inc/helpers.php';
require_once BRICKPOINT_DIR . '/inc/template-functions.php';
require_once BRICKPOINT_DIR . '/inc/post-types.php';
require_once BRICKPOINT_DIR . '/inc/taxonomies.php';
require_once BRICKPOINT_DIR . '/inc/meta-fields.php';
require_once BRICKPOINT_DIR . '/inc/whatsapp.php';
require_once BRICKPOINT_DIR . '/inc/customizer.php';
require_once BRICKPOINT_DIR . '/inc/admin-settings.php';
require_once BRICKPOINT_DIR . '/inc/elementor.php';
require_once BRICKPOINT_DIR . '/inc/elementor-widgets.php';
require_once BRICKPOINT_DIR . '/inc/demo-data.php';
require_once BRICKPOINT_DIR . '/inc/demo-importer.php';
require_once BRICKPOINT_DIR . '/inc/ajax-handlers.php';
"""

# header.php
files["header.php"] = """<?php
/**
 * The header template for BrickPoint
 *
 * @package BrickPoint
 */

if ( ! defined( 'ABSPATH' ) ) {
  exit;
}
?><!DOCTYPE html>
<html <?php language_attributes(); ?>>
<head>
  <meta charset="<?php bloginfo( 'charset' ); ?>">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="profile" href="https://gmpg.org/xfn/11">
  <?php wp_head(); ?>
</head>
<body <?php body_class(); ?>>
<?php wp_body_open(); ?>

<?php
// Elementor Pro Theme Builder: Header Location Check
if ( function_exists( 'elementor_theme_do_location' ) && elementor_theme_do_location( 'header' ) ) {
  return;
}
?>

<!-- Top Notification Bar -->
<div class="bp-topbar">
  <div class="bp-container bp-topbar-inner">
    <div class="bp-topbar-left">
      <span class="bp-topbar-phone">
        <svg class="bp-icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
        <a href="tel:<?php echo esc_attr( bp_option( 'bp_phone_display', '0315 2850818' ) ); ?>"><?php echo esc_html( bp_option( 'bp_phone_display', '0315 2850818' ) ); ?></a>
      </span>
      <span class="bp-topbar-units">Masha Allah Bricks Co. &bull; Fine Bricks Co. &bull; SS7 Bricks</span>
    </div>
    <div class="bp-topbar-right">
      <a href="<?php echo esc_url( home_url( '/locations' ) ); ?>"><?php esc_html_e( 'Our Bhattas', 'brickpoint' ); ?></a>
      <a href="<?php echo esc_url( home_url( '/videos' ) ); ?>"><?php esc_html_e( 'Videos', 'brickpoint' ); ?></a>
      <a href="<?php echo esc_url( home_url( '/about' ) ); ?>"><?php esc_html_e( 'About', 'brickpoint' ); ?></a>
      <a href="<?php echo esc_url( admin_url( 'themes.php?page=brickpoint-demo' ) ); ?>" class="bp-badge-pill"><?php esc_html_e( 'Theme Demo', 'brickpoint' ); ?></a>
    </div>
  </div>
</div>

<!-- Main Sticky Header -->
<header id="bpStickyHeader" class="bp-header sticky-header">
  <div class="bp-container bp-header-inner">
    <!-- Header Logo (Independently Customizable) -->
    <div class="bp-logo-wrap">
      <?php brickpoint_header_logo(); ?>
    </div>

    <!-- Main Navigation Menu -->
    <nav class="bp-nav" aria-label="<?php esc_attr_e( 'Main navigation', 'brickpoint' ); ?>">
      <?php
      if ( has_nav_menu( 'primary' ) ) {
        wp_nav_menu( array(
          'theme_location' => 'primary',
          'container'      => false,
          'menu_class'     => 'bp-menu',
          'fallback_cb'    => 'brickpoint_default_nav_menu',
        ) );
      } else {
        brickpoint_default_nav_menu();
      }
      ?>
    </nav>

    <!-- Header Action Buttons -->
    <div class="bp-header-cta">
      <a href="<?php echo esc_url( bp_whatsapp_url( 'Assalam-o-Alaikum BrickPoint, I need a quotation for construction materials.' ) ); ?>" target="_blank" rel="noopener" class="btn-whatsapp">
        <svg class="bp-icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/></svg>
        <span><?php esc_html_e( 'WhatsApp Us', 'brickpoint' ); ?></span>
      </a>
      <a href="<?php echo esc_url( home_url( '/contact' ) ); ?>" class="btn-brick">
        <span><?php esc_html_e( 'Request Quote', 'brickpoint' ); ?></span>
      </a>
    </div>

    <!-- Mobile Menu Toggle Button -->
    <button id="bpMenuToggle" class="bp-menu-toggle" aria-label="<?php esc_attr_e( 'Open menu', 'brickpoint' ); ?>" aria-expanded="false">
      <svg class="bp-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="4" x2="20" y1="12" y2="12"/><line x1="4" x2="20" y1="6" y2="6"/><line x1="4" x2="20" y1="18" y2="18"/></svg>
    </button>
  </div>
</header>

<!-- Mobile Navigation Drawer -->
<div id="bpMobileDrawer" class="bp-mobile-drawer" hidden>
  <div class="bp-mobile-overlay" id="bpMobileOverlay"></div>
  <div class="bp-mobile-panel">
    <div class="bp-mobile-header">
      <div class="bp-logo-wrap">
        <?php brickpoint_header_logo(); ?>
      </div>
      <button id="bpMenuClose" class="bp-mobile-close" aria-label="<?php esc_attr_e( 'Close menu', 'brickpoint' ); ?>">
        <svg class="bp-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" x2="6" y1="6" y2="18"/><line x1="6" x2="18" y1="6" y2="18"/></svg>
      </button>
    </div>

    <nav class="bp-mobile-nav" aria-label="<?php esc_attr_e( 'Mobile navigation', 'brickpoint' ); ?>">
      <?php
      if ( has_nav_menu( 'mobile' ) ) {
        wp_nav_menu( array(
          'theme_location' => 'mobile',
          'container'      => false,
          'menu_class'     => 'bp-mobile-menu-list',
          'fallback_cb'    => 'brickpoint_mobile_default_menu',
        ) );
      } else {
        brickpoint_mobile_default_menu();
      }
      ?>

      <div class="bp-mobile-quicklinks">
        <a href="<?php echo esc_url( home_url( '/for-contractors' ) ); ?>"><?php esc_html_e( 'For Contractors', 'brickpoint' ); ?></a>
        <a href="<?php echo esc_url( home_url( '/for-builders' ) ); ?>"><?php esc_html_e( 'For Builders', 'brickpoint' ); ?></a>
        <a href="<?php echo esc_url( home_url( '/for-companies' ) ); ?>"><?php esc_html_e( 'For Companies', 'brickpoint' ); ?></a>
        <a href="<?php echo esc_url( home_url( '/blog' ) ); ?>"><?php esc_html_e( 'Blog', 'brickpoint' ); ?></a>
      </div>
    </nav>

    <div class="bp-mobile-actions">
      <a href="<?php echo esc_url( bp_whatsapp_url( 'Assalam-o-Alaikum BrickPoint, I need a quotation for construction materials.' ) ); ?>" target="_blank" rel="noopener" class="btn-whatsapp btn-block">
        <svg class="bp-icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/></svg>
        <span>WhatsApp: <?php echo esc_html( bp_option( 'bp_phone_display', '0315 2850818' ) ); ?></span>
      </a>
      <a href="<?php echo esc_url( home_url( '/contact' ) ); ?>" class="btn-brick btn-block">
        <span><?php esc_html_e( 'Request a Quote', 'brickpoint' ); ?></span>
      </a>
    </div>
  </div>
</div>
"""

# footer.php
files["footer.php"] = """<?php
/**
 * The footer template for BrickPoint
 *
 * @package BrickPoint
 */

if ( ! defined( 'ABSPATH' ) ) {
  exit;
}

// Elementor Pro Theme Builder: Footer Location Check
if ( function_exists( 'elementor_theme_do_location' ) && elementor_theme_do_location( 'footer' ) ) {
  wp_footer();
  echo '</body></html>';
  return;
}
?>

<footer class="bp-footer">
  <div class="brick-lines absolute-bg"></div>
  <div class="bp-container bp-footer-grid">
    <!-- Col 1: About & Independent Footer Logo -->
    <div class="bp-footer-col">
      <div class="bp-footer-logo-wrap">
        <?php brickpoint_footer_logo(); ?>
      </div>
      <p class="bp-footer-desc">
        <?php echo esc_html( bp_option( 'bp_footer_desc', 'Premium bricks and reliable construction materials for homes, commercial developments, and large-scale building projects.' ) ); ?>
      </p>
      <div class="bp-footer-contact">
        <p class="bp-footer-contact-item">
          <svg class="bp-icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
          <a href="tel:<?php echo esc_attr( bp_option( 'bp_phone_display', '0315 2850818' ) ); ?>"><?php echo esc_html( bp_option( 'bp_phone_display', '0315 2850818' ) ); ?></a>
        </p>
        <p class="bp-footer-contact-item">
          <svg class="bp-icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg>
          <a href="mailto:<?php echo esc_attr( bp_option( 'bp_email', 'info@brickpoint.pk' ) ); ?>"><?php echo esc_html( bp_option( 'bp_email', 'info@brickpoint.pk' ) ); ?></a>
        </p>
        <p class="bp-footer-contact-item">
          <svg class="bp-icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></svg>
          <span><?php echo esc_html( bp_option( 'bp_address', 'Lahore, Punjab, Pakistan' ) ); ?></span>
        </p>
      </div>

      <!-- Social Links -->
      <div class="bp-social">
        <a href="<?php echo esc_url( bp_option( 'bp_social_facebook', 'https://www.facebook.com/brickpoint.pk/' ) ); ?>" target="_blank" rel="noopener" aria-label="Facebook">
          <svg class="bp-icon-sm" viewBox="0 0 24 24" fill="currentColor"><path d="M13.5 21v-7h2.4l.4-3h-2.8V9.1c0-.9.3-1.5 1.6-1.5h1.3V4.9c-.3 0-1.1-.1-2-.1-2 0-3.4 1.2-3.4 3.5V11H7.5v3H10v7h3.5Z"/></svg>
        </a>
        <a href="<?php echo esc_url( bp_option( 'bp_social_instagram', 'https://www.instagram.com/brickpoint.pk/' ) ); ?>" target="_blank" rel="noopener" aria-label="Instagram">
          <svg class="bp-icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.2" cy="6.8" r="1.2" fill="currentColor" stroke="none"/></svg>
        </a>
        <a href="<?php echo esc_url( bp_option( 'bp_social_twitter', 'https://x.com/BrickPointPK' ) ); ?>" target="_blank" rel="noopener" aria-label="X Twitter">
          <svg class="bp-icon-sm" viewBox="0 0 24 24" fill="currentColor"><path d="M17.7 3H21l-7.1 8.2L22.2 21h-6.6l-5.1-6.1L4.6 21H1.3l7.6-8.7L1.8 3h6.7l4.6 5.6L17.7 3Zm-1.2 16h1.8L7.1 4.9H5.2L16.5 19Z"/></svg>
        </a>
        <a href="<?php echo esc_url( bp_option( 'bp_social_tiktok', 'https://www.tiktok.com/@brickpoint.pk/' ) ); ?>" target="_blank" rel="noopener" aria-label="TikTok">
          <span style="font-weight:900;font-size:0.9rem;">T</span>
        </a>
      </div>
    </div>

    <!-- Col 2: Products & Company -->
    <div class="bp-footer-col">
      <h4 class="bp-footer-title"><?php esc_html_e( 'Products', 'brickpoint' ); ?></h4>
      <ul class="bp-footer-links">
        <li><a href="<?php echo esc_url( home_url( '/ss7-bricks' ) ); ?>"><?php esc_html_e( 'SS7 Bricks', 'brickpoint' ); ?></a></li>
        <li><a href="<?php echo esc_url( home_url( '/products' ) ); ?>"><?php esc_html_e( 'All Products', 'brickpoint' ); ?></a></li>
        <li><a href="<?php echo esc_url( home_url( '/categories' ) ); ?>"><?php esc_html_e( 'Product Categories', 'brickpoint' ); ?></a></li>
        <li><a href="<?php echo esc_url( home_url( '/construction-materials' ) ); ?>"><?php esc_html_e( 'Construction Materials', 'brickpoint' ); ?></a></li>
        <li><a href="<?php echo esc_url( home_url( '/videos' ) ); ?>"><?php esc_html_e( 'Product Videos', 'brickpoint' ); ?></a></li>
      </ul>

      <h4 class="bp-footer-title" style="margin-top:1.5rem;"><?php esc_html_e( 'Company', 'brickpoint' ); ?></h4>
      <ul class="bp-footer-links">
        <li><a href="<?php echo esc_url( home_url( '/about' ) ); ?>"><?php esc_html_e( 'About Us', 'brickpoint' ); ?></a></li>
        <li><a href="<?php echo esc_url( home_url( '/projects' ) ); ?>"><?php esc_html_e( 'Projects', 'brickpoint' ); ?></a></li>
        <li><a href="<?php echo esc_url( home_url( '/blog' ) ); ?>"><?php esc_html_e( 'Blog', 'brickpoint' ); ?></a></li>
        <li><a href="<?php echo esc_url( home_url( '/locations' ) ); ?>"><?php esc_html_e( 'Locations', 'brickpoint' ); ?></a></li>
      </ul>
    </div>

    <!-- Col 3: Who We Serve & Our Units -->
    <div class="bp-footer-col">
      <h4 class="bp-footer-title"><?php esc_html_e( 'Who We Serve', 'brickpoint' ); ?></h4>
      <ul class="bp-footer-links">
        <li><a href="<?php echo esc_url( home_url( '/for-contractors' ) ); ?>"><?php esc_html_e( 'For Contractors', 'brickpoint' ); ?></a></li>
        <li><a href="<?php echo esc_url( home_url( '/for-builders' ) ); ?>"><?php esc_html_e( 'For Builders', 'brickpoint' ); ?></a></li>
        <li><a href="<?php echo esc_url( home_url( '/for-companies' ) ); ?>"><?php esc_html_e( 'For Construction Companies', 'brickpoint' ); ?></a></li>
        <li><a href="<?php echo esc_url( home_url( '/contact' ) ); ?>"><?php esc_html_e( 'Request Quotation', 'brickpoint' ); ?></a></li>
      </ul>

      <h4 class="bp-footer-title" style="margin-top:1.5rem;"><?php esc_html_e( 'Our Units', 'brickpoint' ); ?></h4>
      <ul class="bp-footer-links bp-dim-links">
        <li>Masha Allah Bricks Company</li>
        <li>Fine Bricks Company</li>
        <li>SS7 Bricks</li>
        <li style="opacity:0.6;">CEO: <?php echo esc_html( bp_option( 'bp_ceo', 'Syed Iftikhar Haider' ) ); ?></li>
        <li style="opacity:0.6;">Sales: <?php echo esc_html( bp_option( 'bp_sales', 'Qasim Iqbal' ) ); ?></li>
      </ul>
    </div>

    <!-- Col 4: Quotation & WhatsApp -->
    <div class="bp-footer-col">
      <h4 class="bp-footer-title"><?php esc_html_e( 'Get a Quotation', 'brickpoint' ); ?></h4>
      <p class="bp-footer-desc">
        <?php esc_html_e( 'Send your material list on WhatsApp and get availability, delivery details, and final quotation.', 'brickpoint' ); ?>
      </p>
      <a href="<?php echo esc_url( bp_whatsapp_url( 'Assalam-o-Alaikum BrickPoint, I need a quotation for construction materials.' ) ); ?>" target="_blank" rel="noopener" class="btn-whatsapp btn-block" style="margin-top:1rem;">
        <svg class="bp-icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/></svg>
        <span><?php esc_html_e( 'Chat on WhatsApp', 'brickpoint' ); ?></span>
      </a>
      <a href="<?php echo esc_url( home_url( '/contact' ) ); ?>" class="btn-ghost btn-block" style="margin-top:0.5rem;color:#fff;border-color:rgba(255,255,255,0.2);">
        <span><?php esc_html_e( 'Contact Form', 'brickpoint' ); ?></span>
      </a>
      <a href="<?php echo esc_url( admin_url( 'themes.php?page=brickpoint-demo' ) ); ?>" class="btn-ghost btn-block" style="margin-top:0.5rem;color:#ea580c;border-color:rgba(234,88,12,0.4);background:rgba(234,88,12,0.08);">
        <span><?php esc_html_e( 'Demo Importer', 'brickpoint' ); ?></span>
      </a>
    </div>
  </div>

  <!-- Copyright Bar -->
  <div class="bp-footer-bottom">
    <div class="bp-container bp-footer-bottom-inner">
      <p>&copy; <?php echo esc_html( date( 'Y' ) ); ?> BrickPoint. <?php esc_html_e( 'All rights reserved.', 'brickpoint' ); ?></p>
      <div class="bp-footer-legal">
        <a href="<?php echo esc_url( home_url( '/privacy' ) ); ?>"><?php esc_html_e( 'Privacy Policy', 'brickpoint' ); ?></a>
        <a href="<?php echo esc_url( home_url( '/terms' ) ); ?>"><?php esc_html_e( 'Terms & Conditions', 'brickpoint' ); ?></a>
        <a href="<?php echo esc_url( home_url( '/locations' ) ); ?>"><?php esc_html_e( 'Locations', 'brickpoint' ); ?></a>
      </div>
    </div>
  </div>
</footer>

<!-- Floating WhatsApp Action -->
<a href="<?php echo esc_url( bp_whatsapp_url( 'Assalam-o-Alaikum BrickPoint, I need a quotation for construction materials.' ) ); ?>" target="_blank" rel="noopener" class="bp-float-wa" aria-label="<?php esc_attr_e( 'Chat on WhatsApp', 'brickpoint' ); ?>">
  <svg class="bp-icon-md" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/></svg>
  <span class="bp-ping-dot"></span>
</a>

<?php wp_footer(); ?>
</body>
</html>
"""

# front-page.php
files["front-page.php"] = """<?php
/**
 * The template for displaying the front page
 *
 * Checks if Elementor is used on this page; if so, outputs the Elementor content!
 * Otherwise, outputs the complete original 9-section BrickPoint homepage layout.
 *
 * @package BrickPoint
 */

if ( ! defined( 'ABSPATH' ) ) {
  exit;
}

get_header();

// Elementor Single/Page Location Check
if ( function_exists( 'elementor_theme_do_location' ) && elementor_theme_do_location( 'single' ) ) {
  get_footer();
  return;
}

// If current page is edited with Elementor, render the Elementor content directly!
if ( have_posts() ) {
  while ( have_posts() ) {
    the_post();
    if ( get_post_meta( get_the_ID(), '_elementor_edit_mode', true ) === 'builder' ) {
      the_content();
      get_footer();
      return;
    }
  }
}

/* ========================================================
 * NATIVE COMPLETE FALLBACK HOMEPAGE (SAME DESIGN & LAYOUT)
 * ======================================================== */
?>

<!-- 1. HERO SECTION -->
<?php get_template_part( 'template-parts/hero' ); ?>

<!-- 2. TRUST / INTRO SECTION ("Why BrickPoint") -->
<section class="bp-section bp-trust-section">
  <div class="bp-container bp-trust-grid">
    <div class="bp-trust-media img-zoom">
      <img src="<?php echo esc_url( bp_asset_image_url( 'kiln.png' ) ); ?>" alt="<?php esc_attr_e( 'Brick kiln production', 'brickpoint' ); ?>" loading="lazy" />
      <div class="bp-trust-cards-overlay">
        <div class="bp-glass-card">
          <p class="bp-card-h-orange"><?php esc_html_e( 'Trusted Supply', 'brickpoint' ); ?></p>
          <p class="bp-card-sub"><?php esc_html_e( 'Consistent quality for every order size', 'brickpoint' ); ?></p>
        </div>
        <div class="bp-glass-card bp-glass-dark">
          <p class="bp-card-h-white"><?php esc_html_e( 'Bulk Ready', 'brickpoint' ); ?></p>
          <p class="bp-card-sub-dim"><?php esc_html_e( 'Contractors & companies welcome', 'brickpoint' ); ?></p>
        </div>
      </div>
    </div>
    <div class="bp-trust-content">
      <div class="bp-section-head-left">
        <p class="bp-eyebrow"><?php esc_html_e( 'Why BrickPoint', 'brickpoint' ); ?></p>
        <h2 class="bp-heading-2"><?php esc_html_e( 'A construction-materials partner you can build on', 'brickpoint' ); ?></h2>
        <p class="bp-body-text"><?php esc_html_e( 'BrickPoint brings together trusted brick manufacturing units and a complete construction-materials range — so contractors, builders and developers can source with confidence.', 'brickpoint' ); ?></p>
      </div>
      <ul class="bp-check-list">
        <li>
          <svg class="bp-icon-check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M20 6 9 17l-5-5"/></svg>
          <span><?php esc_html_e( 'Quality-focused brick manufacturing at multiple bhatta locations', 'brickpoint' ); ?></span>
        </li>
        <li>
          <svg class="bp-icon-check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M20 6 9 17l-5-5"/></svg>
          <span><?php esc_html_e( 'Complete materials range — from cement and steel to finishes', 'brickpoint' ); ?></span>
        </li>
        <li>
          <svg class="bp-icon-check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M20 6 9 17l-5-5"/></svg>
          <span><?php esc_html_e( 'Project-based quotations with delivery coordination', 'brickpoint' ); ?></span>
        </li>
        <li>
          <svg class="bp-icon-check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M20 6 9 17l-5-5"/></svg>
          <span><?php esc_html_e( 'Direct WhatsApp ordering with fast response', 'brickpoint' ); ?></span>
        </li>
      </ul>
      <div class="bp-action-row">
        <a href="<?php echo esc_url( home_url( '/about' ) ); ?>" class="btn-dark"><?php esc_html_e( 'About BrickPoint →', 'brickpoint' ); ?></a>
        <a href="<?php echo esc_url( home_url( '/locations' ) ); ?>" class="btn-ghost"><?php esc_html_e( 'Our Locations', 'brickpoint' ); ?></a>
      </div>
    </div>
  </div>
</section>

<!-- 3. PRODUCT CATEGORIES SECTION -->
<section class="bp-section bp-dark">
  <div class="bp-container">
    <div class="bp-section-head bp-head-light">
      <p class="bp-eyebrow"><?php esc_html_e( 'Product Categories', 'brickpoint' ); ?></p>
      <h2 class="bp-heading-2"><?php esc_html_e( 'One supplier for your complete material list', 'brickpoint' ); ?></h2>
      <p class="bp-body-text"><?php esc_html_e( 'From flagship SS7 bricks to cement, aggregates, steel, pipes, electricals and finishes.', 'brickpoint' ); ?></p>
    </div>
    <div class="bp-grid cols-4 bp-mt">
      <?php
      $categories = get_terms( array(
        'taxonomy'   => 'bp_product_category',
        'hide_empty' => false,
        'number'     => 12,
        'orderby'    => 'meta_value_num',
        'meta_key'   => 'bp_cat_order',
        'order'      => 'ASC',
      ) );
      if ( empty( $categories ) || is_wp_error( $categories ) ) {
        $categories = get_terms( array( 'taxonomy' => 'bp_product_category', 'hide_empty' => false, 'number' => 12 ) );
      }
      if ( ! empty( $categories ) && ! is_wp_error( $categories ) ) :
        foreach ( $categories as $cat ) :
          $cat_img = get_term_meta( $cat->term_id, 'bp_cat_image', true );
          if ( ! $cat_img ) {
            $cat_img = bp_asset_image_url( 'stacked.png' );
          }
          $cat_link = ( $cat->slug === 'ss7-bricks' ) ? home_url( '/ss7-bricks' ) : get_term_link( $cat );
      ?>
        <a href="<?php echo esc_url( $cat_link ); ?>" class="bp-cat-card card-hover group">
          <div class="bp-cat-media img-zoom">
            <img src="<?php echo esc_url( $cat_img ); ?>" alt="<?php echo esc_attr( $cat->name ); ?>" loading="lazy" />
            <div class="bp-cat-grad"></div>
            <p class="bp-cat-name"><?php echo esc_html( $cat->name ); ?></p>
          </div>
          <div class="bp-cat-card-foot">
            <span class="bp-cat-desc"><?php echo esc_html( wp_trim_words( $cat->description, 7, '…' ) ); ?></span>
            <span class="bp-cat-arrow">
              <svg class="bp-icon-xs" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>
            </span>
          </div>
        </a>
      <?php endforeach; endif; ?>
    </div>
    <div class="bp-center bp-mt">
      <a href="<?php echo esc_url( home_url( '/categories' ) ); ?>" class="btn-ghost" style="color:#fff;border-color:rgba(255,255,255,0.25);">
        <span><?php esc_html_e( 'View All Categories →', 'brickpoint' ); ?></span>
      </a>
    </div>
  </div>
</section>

<!-- 4. FLAGSHIP SS7 BRICKS SECTION -->
<section class="bp-section bp-ss7-section">
  <div class="bp-container bp-ss7-grid">
    <div class="bp-ss7-content">
      <div class="bp-section-head-left">
        <p class="bp-eyebrow"><?php esc_html_e( 'Flagship Product', 'brickpoint' ); ?></p>
        <h2 class="bp-heading-2"><?php esc_html_e( 'The Strength Behind Every Structure', 'brickpoint' ); ?></h2>
        <p class="bp-body-text"><?php esc_html_e( 'SS7 Bricks — our signature range engineered for strength, shape and lasting performance. Ask for specifications, availability and project pricing on WhatsApp.', 'brickpoint' ); ?></p>
      </div>
      <div class="bp-specs-grid">
        <div class="bp-spec-card">
          <p class="bp-spec-lbl"><?php esc_html_e( 'Size', 'brickpoint' ); ?></p>
          <p class="bp-spec-val"><?php esc_html_e( 'Standard chamber size', 'brickpoint' ); ?></p>
        </div>
        <div class="bp-spec-card">
          <p class="bp-spec-lbl"><?php esc_html_e( 'Type', 'brickpoint' ); ?></p>
          <p class="bp-spec-val"><?php esc_html_e( 'Burnt-clay SS7', 'brickpoint' ); ?></p>
        </div>
        <div class="bp-spec-card">
          <p class="bp-spec-lbl"><?php esc_html_e( 'Usage', 'brickpoint' ); ?></p>
          <p class="bp-spec-val"><?php esc_html_e( 'Homes • Commercial • Boundary', 'brickpoint' ); ?></p>
        </div>
        <div class="bp-spec-card">
          <p class="bp-spec-lbl"><?php esc_html_e( 'Availability', 'brickpoint' ); ?></p>
          <p class="bp-spec-val"><?php esc_html_e( 'Bulk & retail orders', 'brickpoint' ); ?></p>
        </div>
      </div>
      <div class="bp-action-row">
        <a href="<?php echo esc_url( bp_whatsapp_url( bp_category_inquiry_message( 'SS7 Bricks' ) ) ); ?>" target="_blank" rel="noopener" class="btn-whatsapp">
          <svg class="bp-icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/></svg>
          <span><?php esc_html_e( 'Request SS7 Quote', 'brickpoint' ); ?></span>
        </a>
        <a href="<?php echo esc_url( home_url( '/ss7-bricks' ) ); ?>" class="btn-dark"><?php esc_html_e( 'View SS7 Page →', 'brickpoint' ); ?></a>
      </div>
    </div>
    <div class="bp-ss7-gallery-wrap">
      <div class="bp-ss7-main-img img-zoom">
        <img src="<?php echo esc_url( bp_asset_image_url( 'red-stack.png' ) ); ?>" alt="<?php esc_attr_e( 'SS7 Red Bricks Stacked', 'brickpoint' ); ?>" loading="lazy" />
      </div>
      <div class="bp-ss7-thumbs-row">
        <img src="<?php echo esc_url( bp_asset_image_url( 'stacked.png' ) ); ?>" alt="SS7 gallery" loading="lazy" />
        <img src="<?php echo esc_url( bp_asset_image_url( 'pile.png' ) ); ?>" alt="SS7 gallery" loading="lazy" />
        <img src="<?php echo esc_url( bp_asset_image_url( 'worker.png' ) ); ?>" alt="SS7 gallery" loading="lazy" />
      </div>
    </div>
  </div>
</section>

<!-- 5. FEATURED PRODUCTS SECTION -->
<section class="bp-section">
  <div class="bp-container">
    <div class="bp-section-head">
      <p class="bp-eyebrow"><?php esc_html_e( 'Featured Products', 'brickpoint' ); ?></p>
      <h2 class="bp-heading-2"><?php esc_html_e( 'Materials contractors ask for by name', 'brickpoint' ); ?></h2>
      <p class="bp-body-text"><?php esc_html_e( 'Live from the product catalogue — prices, units and WhatsApp ordering on every card.', 'brickpoint' ); ?></p>
    </div>
    <div class="bp-grid cols-4 bp-mt">
      <?php
      $pq = new WP_Query( array(
        'post_type'      => 'bp_product',
        'posts_per_page' => 8,
        'meta_key'       => '_bp_featured',
        'meta_value'     => '1',
      ) );
      if ( ! $pq->have_posts() ) {
        $pq = new WP_Query( array( 'post_type' => 'bp_product', 'posts_per_page' => 8 ) );
      }
      if ( $pq->have_posts() ) :
        while ( $pq->have_posts() ) : $pq->the_post();
          get_template_part( 'template-parts/product-card' );
        endwhile;
        wp_reset_postdata();
      else :
        for ( $i = 1; $i <= 4; $i++ ) : ?>
          <div class="bp-placeholder-card">
            <p><strong><?php esc_html_e( 'Products loading from catalogue…', 'brickpoint' ); ?></strong></p>
            <p class="bp-sub"><?php esc_html_e( 'Run Appearance → BrickPoint Demo to load demo products.', 'brickpoint' ); ?></p>
          </div>
      <?php endfor; endif; ?>
    </div>
    <div class="bp-center bp-mt">
      <a href="<?php echo esc_url( home_url( '/products' ) ); ?>" class="btn-brick">
        <span><?php esc_html_e( 'Browse All Products →', 'brickpoint' ); ?></span>
      </a>
    </div>
  </div>
</section>

<!-- 6. VIDEO SHOWCASE SECTION -->
<section class="bp-section bp-dark">
  <div class="bp-container">
    <div class="bp-video-header-row">
      <div class="bp-section-head-left">
        <p class="bp-eyebrow"><?php esc_html_e( 'Inside BrickPoint', 'brickpoint' ); ?></p>
        <h2 class="bp-heading-2 bp-head-light"><?php esc_html_e( 'See the Strength Behind Every Brick', 'brickpoint' ); ?></h2>
        <p class="bp-body-text bp-head-light-dim"><?php esc_html_e( 'Manufacturing, bhattas, quality checks, materials and project references — on video.', 'brickpoint' ); ?></p>
      </div>
      <a href="<?php echo esc_url( home_url( '/videos' ) ); ?>" class="btn-ghost" style="color:#fff;border-color:rgba(255,255,255,0.25);">
        <span><?php esc_html_e( 'View All Videos →', 'brickpoint' ); ?></span>
      </a>
    </div>
    <div class="bp-video-featured-grid bp-mt">
      <div class="bp-video-main hero-video-frame">
        <video controls playsinline preload="metadata" poster="<?php echo esc_url( bp_asset_image_url( 'drone-poster.png' ) ); ?>" class="bp-video-player">
          <source src="<?php echo esc_url( bp_option( 'bp_drone_video', 'https://videos.pexels.com/video-files/27758012/12218981_3840_2160_25fps.mp4' ) ); ?>" type="video/mp4" />
        </video>
        <span class="bp-feat-badge"><?php esc_html_e( 'Featured', 'brickpoint' ); ?></span>
      </div>
      <div class="bp-video-sub-col">
        <div class="bp-video-sub-card">
          <div class="bp-video-sub-thumb">
            <video playsinline muted loop autoplay preload="metadata" poster="<?php echo esc_url( bp_asset_image_url( 'site-poster.png' ) ); ?>">
              <source src="<?php echo esc_url( bp_option( 'bp_site_video', 'https://videos.pexels.com/video-files/11355903/11355903-uhd_3840_2160_25fps.mp4' ) ); ?>" type="video/mp4" />
            </video>
            <span class="bp-video-sub-tag"><?php esc_html_e( 'From the Bhatta to Your Building', 'brickpoint' ); ?></span>
          </div>
          <p class="bp-video-sub-desc"><?php esc_html_e( 'Brick preparation, firing, stacking, loading and quality — the journey of every batch.', 'brickpoint' ); ?></p>
        </div>
        <div class="bp-video-sub-card">
          <div class="bp-video-sub-thumb">
            <video playsinline muted loop autoplay preload="metadata" poster="<?php echo esc_url( bp_asset_image_url( 'aerial-poster.png' ) ); ?>">
              <source src="<?php echo esc_url( bp_option( 'bp_aerial_video', 'https://videos.pexels.com/video-files/20731372/20731372-uhd_3840_2160_30fps.mp4' ) ); ?>" type="video/mp4" />
            </video>
            <span class="bp-video-sub-tag"><?php esc_html_e( 'Materials That Become Landmarks', 'brickpoint' ); ?></span>
          </div>
          <p class="bp-video-sub-desc"><?php esc_html_e( 'Illustrative construction references from housing developments and building work.', 'brickpoint' ); ?></p>
        </div>
      </div>
    </div>
    <!-- 3 Recent Video Cards -->
    <div class="bp-grid cols-3 bp-mt">
      <?php
      $vq = new WP_Query( array( 'post_type' => 'bp_video', 'posts_per_page' => 3 ) );
      if ( $vq->have_posts() ) :
        while ( $vq->have_posts() ) : $vq->the_post();
          get_template_part( 'template-parts/video-card' );
        endwhile;
        wp_reset_postdata();
      endif;
      ?>
    </div>
  </div>
</section>

<!-- 7. PROJECT REFERENCES PREVIEW SECTION -->
<section class="bp-section">
  <div class="bp-container">
    <div class="bp-section-head">
      <p class="bp-eyebrow"><?php esc_html_e( 'Project References', 'brickpoint' ); ?></p>
      <h2 class="bp-heading-2"><?php esc_html_e( 'Materials that become landmarks', 'brickpoint' ); ?></h2>
      <p class="bp-body-text"><?php esc_html_e( 'Illustrative construction references from Lahore housing societies and building work.', 'brickpoint' ); ?></p>
    </div>
    <div class="bp-grid cols-3 bp-mt">
      <?php
      $proj_q = new WP_Query( array( 'post_type' => 'bp_project', 'posts_per_page' => 3 ) );
      if ( $proj_q->have_posts() ) :
        while ( $proj_q->have_posts() ) : $proj_q->the_post();
          get_template_part( 'template-parts/project-card' );
        endwhile;
        wp_reset_postdata();
      else :
        $default_projs = array(
          array( 'title' => 'DHA Lahore — Villa Reference', 'loc' => 'DHA Lahore', 'img' => bp_asset_image_url( 'villa1.png' ) ),
          array( 'title' => 'Bahria Town — Housing Reference', 'loc' => 'Bahria Town Lahore', 'img' => bp_asset_image_url( 'villa2.png' ) ),
          array( 'title' => 'Lake City — Development Reference', 'loc' => 'Lake City Lahore', 'img' => bp_asset_image_url( 'apt.png' ) ),
        );
        foreach ( $default_projs as $dp ) : ?>
          <a href="<?php echo esc_url( home_url( '/projects' ) ); ?>" class="bp-card card-hover group">
            <div class="bp-card-media img-zoom">
              <img src="<?php echo esc_url( $dp['img'] ); ?>" alt="<?php echo esc_attr( $dp['title'] ); ?>" loading="lazy" />
              <span class="bp-illus-badge"><?php esc_html_e( 'Illustrative construction reference', 'brickpoint' ); ?></span>
            </div>
            <div class="bp-card-body">
              <p class="bp-card-loc"><?php echo esc_html( $dp['loc'] ); ?></p>
              <h3><?php echo esc_html( $dp['title'] ); ?></h3>
            </div>
          </a>
      <?php endforeach; endif; ?>
    </div>
  </div>
</section>

<!-- 8. WHO WE SERVE SECTION -->
<section class="bp-section bp-sand-section">
  <div class="bp-container">
    <div class="bp-section-head">
      <p class="bp-eyebrow"><?php esc_html_e( 'Who We Serve', 'brickpoint' ); ?></p>
      <h2 class="bp-heading-2"><?php esc_html_e( 'Built for the way you build', 'brickpoint' ); ?></h2>
      <p class="bp-body-text"><?php esc_html_e( 'Bulk supply, project quotations and coordinated materials — for every scale of builder.', 'brickpoint' ); ?></p>
    </div>
    <div class="bp-grid cols-3 bp-mt">
      <!-- For Contractors -->
      <a href="<?php echo esc_url( home_url( '/for-contractors' ) ); ?>" class="bp-audience-card card-hover group">
        <div class="bp-audience-media img-zoom">
          <img src="<?php echo esc_url( bp_asset_image_url( 'site.png' ) ); ?>" alt="<?php esc_attr_e( 'For Contractors', 'brickpoint' ); ?>" loading="lazy" />
          <div class="bp-audience-overlay"></div>
        </div>
        <div class="bp-audience-body">
          <h3><?php esc_html_e( 'For Contractors', 'brickpoint' ); ?></h3>
          <p><?php esc_html_e( 'Bulk material supply, project-based quotations and delivery coordination.', 'brickpoint' ); ?></p>
          <span class="bp-audience-link"><?php esc_html_e( 'Learn more →', 'brickpoint' ); ?></span>
        </div>
      </a>
      <!-- For Builders -->
      <a href="<?php echo esc_url( home_url( '/for-builders' ) ); ?>" class="bp-audience-card card-hover group">
        <div class="bp-audience-media img-zoom">
          <img src="<?php echo esc_url( bp_asset_image_url( 'bricklayer.png' ) ); ?>" alt="<?php esc_attr_e( 'For Builders', 'brickpoint' ); ?>" loading="lazy" />
          <div class="bp-audience-overlay"></div>
        </div>
        <div class="bp-audience-body">
          <h3><?php esc_html_e( 'For Builders', 'brickpoint' ); ?></h3>
          <p><?php esc_html_e( 'Consistent quality across every batch, with multi-category sourcing.', 'brickpoint' ); ?></p>
          <span class="bp-audience-link"><?php esc_html_e( 'Learn more →', 'brickpoint' ); ?></span>
        </div>
      </a>
      <!-- For Construction Companies -->
      <a href="<?php echo esc_url( home_url( '/for-companies' ) ); ?>" class="bp-audience-card card-hover group">
        <div class="bp-audience-media img-zoom">
          <img src="<?php echo esc_url( bp_asset_image_url( 'apt.png' ) ); ?>" alt="<?php esc_attr_e( 'For Construction Companies', 'brickpoint' ); ?>" loading="lazy" />
          <div class="bp-audience-overlay"></div>
        </div>
        <div class="bp-audience-body">
          <h3><?php esc_html_e( 'For Construction Companies', 'brickpoint' ); ?></h3>
          <p><?php esc_html_e( 'Large-scale supply, documentation and dedicated contact.', 'brickpoint' ); ?></p>
          <span class="bp-audience-link"><?php esc_html_e( 'Learn more →', 'brickpoint' ); ?></span>
        </div>
      </a>
    </div>
  </div>
</section>

<!-- 9. CTA SECTION -->
<section class="bp-section bp-cta-section">
  <div class="bp-cta-bg-img">
    <img src="<?php echo esc_url( bp_asset_image_url( 'bricklayer.png' ) ); ?>" alt="" loading="lazy" />
    <div class="bp-cta-bg-grad"></div>
  </div>
  <div class="bp-container bp-cta-inner">
    <div class="bp-cta-text">
      <p class="bp-eyebrow"><?php esc_html_e( 'Get a fast quotation', 'brickpoint' ); ?></p>
      <h2 class="bp-heading-1"><?php esc_html_e( 'Send your material list.', 'brickpoint' ); ?><br /><?php esc_html_e( 'We handle the rest.', 'brickpoint' ); ?></h2>
      <p class="bp-cta-meta">
        <svg class="bp-icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
        <span><?php echo esc_html( bp_option( 'bp_phone_display', '0315 2850818' ) ); ?> &bull; CEO: <?php echo esc_html( bp_option( 'bp_ceo', 'Syed Iftikhar Haider' ) ); ?> &bull; Sales: <?php echo esc_html( bp_option( 'bp_sales', 'Qasim Iqbal' ) ); ?></span>
      </p>
    </div>
    <div class="bp-cta-buttons">
      <a href="<?php echo esc_url( bp_whatsapp_url( "Assalam-o-Alaikum BrickPoint,\\n\\nPlease share a quotation for my construction materials.\\n\\nThank you." ) ); ?>" target="_blank" rel="noopener" class="btn-whatsapp btn-lg">
        <svg class="bp-icon-md" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/></svg>
        <span><?php esc_html_e( 'WhatsApp Your List', 'brickpoint' ); ?></span>
      </a>
      <a href="<?php echo esc_url( home_url( '/contact' ) ); ?>" class="btn-brick btn-lg">
        <span><?php esc_html_e( 'Request Quote Form', 'brickpoint' ); ?></span>
      </a>
    </div>
  </div>
</section>

<?php
if ( have_posts() ) {
  while ( have_posts() ) {
    the_post();
    the_content();
  }
}

get_footer();
"""

# page.php
files["page.php"] = """<?php
/**
 * The template for displaying all pages
 *
 * @package BrickPoint
 */

if ( ! defined( 'ABSPATH' ) ) {
  exit;
}

get_header();

// Elementor Pro single location check
if ( function_exists( 'elementor_theme_do_location' ) && elementor_theme_do_location( 'single' ) ) {
  get_footer();
  return;
}
?>

<main id="primary" class="site-main">
  <?php
  while ( have_posts() ) : the_post();
    // If page is built with Elementor, output content directly full width!
    if ( get_post_meta( get_the_ID(), '_elementor_edit_mode', true ) === 'builder' ) {
      the_content();
    } else {
      ?>
      <div class="bp-pagehead">
        <div class="bp-container">
          <p class="bp-eyebrow"><?php esc_html_e( 'BrickPoint', 'brickpoint' ); ?></p>
          <h1 class="bp-heading-1"><?php the_title(); ?></h1>
        </div>
      </div>
      <div class="bp-section">
        <div class="bp-container bp-prose-wrap">
          <div class="prose-bp">
            <?php the_content(); ?>
          </div>
        </div>
      </div>
      <?php
    }
  endwhile;
  ?>
</main>

<?php
get_footer();
"""

# single.php
files["single.php"] = """<?php
/**
 * The template for displaying single blog posts
 *
 * @package BrickPoint
 */

if ( ! defined( 'ABSPATH' ) ) {
  exit;
}

get_header();

if ( function_exists( 'elementor_theme_do_location' ) && elementor_theme_do_location( 'single' ) ) {
  get_footer();
  return;
}
?>

<div class="bp-crumbs-bar">
  <div class="bp-container bp-crumbs">
    <a href="<?php echo esc_url( home_url( '/' ) ); ?>"><?php esc_html_e( 'Home', 'brickpoint' ); ?></a> &gt;
    <a href="<?php echo esc_url( home_url( '/blog' ) ); ?>"><?php esc_html_e( 'Blog', 'brickpoint' ); ?></a> &gt;
    <span><?php the_title(); ?></span>
  </div>
</div>

<article id="post-<?php the_ID(); ?>" <?php post_class( 'bp-container bp-single-post-wrap bp-section' ); ?>>
  <?php
  $cats = get_the_category();
  if ( ! empty( $cats ) ) : ?>
    <span class="bp-badge" style="position:static;display:inline-block;margin-bottom:0.8rem;"><?php echo esc_html( $cats[0]->name ); ?></span>
  <?php endif; ?>

  <h1 class="bp-heading-1"><?php the_title(); ?></h1>

  <div class="bp-post-meta-row">
    <span class="bp-meta-item">
      <svg class="bp-icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
      <?php the_author(); ?>
    </span>
    <span class="bp-meta-item">
      <svg class="bp-icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect width="18" height="18" x="3" y="4" rx="2" ry="2"/><line x1="16" x2="16" y1="2" y2="6"/><line x1="8" x2="8" y1="2" y2="6"/><line x1="3" x2="21" y1="10" y2="10"/></svg>
      <?php echo esc_html( get_the_date() ); ?>
    </span>
    <?php
    $tags = get_the_tags();
    if ( ! empty( $tags ) ) : ?>
      <span class="bp-meta-item">
        <svg class="bp-icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2H2v10l9.29 9.29c.94.94 2.48.94 3.42 0l6.58-6.58c.94-.94.94-2.48 0-3.42L12 2Z"/><path d="M7 7h.01"/></svg>
        <?php the_tags( '', ', ' ); ?>
      </span>
    <?php endif; ?>
  </div>

  <?php if ( has_post_thumbnail() ) : ?>
    <div class="bp-post-hero-img img-zoom">
      <?php the_post_thumbnail( 'large', array( 'class' => 'bp-featured-img' ) ); ?>
    </div>
  <?php endif; ?>

  <div class="bp-post-content-box prose-bp">
    <?php if ( has_excerpt() ) : ?>
      <p class="bp-post-lead"><?php echo esc_html( get_the_excerpt() ); ?></p>
    <?php endif; ?>
    <?php the_content(); ?>
  </div>

  <div class="bp-post-cta-row">
    <a href="<?php echo esc_url( home_url( '/blog' ) ); ?>" class="btn-ghost"><?php esc_html_e( '← All Articles', 'brickpoint' ); ?></a>
    <a href="<?php echo esc_url( home_url( '/products' ) ); ?>" class="btn-dark"><?php esc_html_e( 'Shop Materials', 'brickpoint' ); ?></a>
    <a href="<?php echo esc_url( bp_whatsapp_url( 'Assalam-o-Alaikum BrickPoint, I have an inquiry.' ) ); ?>" target="_blank" rel="noopener" class="btn-whatsapp">
      <span><?php esc_html_e( 'Ask on WhatsApp', 'brickpoint' ); ?></span>
    </a>
  </div>
</article>

<?php
// Related posts
$orig_cats = wp_get_post_categories( get_the_ID() );
if ( ! empty( $orig_cats ) ) {
  $rel_q = new WP_Query( array(
    'category__in'   => $orig_cats,
    'post__not_in'   => array( get_the_ID() ),
    'posts_per_page' => 3,
  ) );
  if ( $rel_q->have_posts() ) : ?>
    <section class="bp-section bp-related-section">
      <div class="bp-container">
        <h2 class="bp-heading-2"><?php esc_html_e( 'Related Articles', 'brickpoint' ); ?></h2>
        <div class="bp-grid cols-3 bp-mt">
          <?php while ( $rel_q->have_posts() ) : $rel_q->the_post(); ?>
            <a href="<?php the_permalink(); ?>" class="bp-card card-hover group">
              <?php if ( has_post_thumbnail() ) : ?>
                <div class="bp-card-media img-zoom">
                  <?php the_post_thumbnail( 'bp-card' ); ?>
                </div>
              <?php endif; ?>
              <div class="bp-card-body">
                <h3><?php the_title(); ?></h3>
              </div>
            </a>
          <?php endwhile; wp_reset_postdata(); ?>
        </div>
      </div>
    </section>
  <?php endif;
}

get_footer();
"""

# archive.php & home.php
files["archive.php"] = """<?php
/**
 * The archive template for blog posts
 *
 * @package BrickPoint
 */

if ( ! defined( 'ABSPATH' ) ) {
  exit;
}

get_header();

if ( function_exists( 'elementor_theme_do_location' ) && elementor_theme_do_location( 'archive' ) ) {
  get_footer();
  return;
}
?>

<div class="bp-pagehead">
  <div class="bp-container">
    <p class="bp-eyebrow"><?php esc_html_e( 'Guides & Updates', 'brickpoint' ); ?></p>
    <h1 class="bp-heading-1"><?php the_archive_title(); ?></h1>
    <p class="bp-pagehead-desc"><?php the_archive_description(); ?></p>
  </div>
</div>

<section class="bp-section">
  <div class="bp-container">
    <div class="bp-grid cols-3">
      <?php
      if ( have_posts() ) :
        while ( have_posts() ) : the_post();
          get_template_part( 'template-parts/content' );
        endwhile;
      else : ?>
        <p><?php esc_html_e( 'No posts found.', 'brickpoint' ); ?></p>
      <?php endif; ?>
    </div>
    <div class="bp-pagination bp-mt">
      <?php the_posts_pagination(); ?>
    </div>
  </div>
</section>

<?php
get_footer();
"""

files["home.php"] = """<?php
/**
 * Blog index template
 *
 * @package BrickPoint
 */

if ( ! defined( 'ABSPATH' ) ) {
  exit;
}

get_header();

if ( function_exists( 'elementor_theme_do_location' ) && elementor_theme_do_location( 'archive' ) ) {
  get_footer();
  return;
}
?>

<div class="bp-pagehead">
  <div class="bp-container">
    <p class="bp-eyebrow"><?php esc_html_e( 'Guides & Updates', 'brickpoint' ); ?></p>
    <h1 class="bp-heading-1"><?php esc_html_e( 'Blog', 'brickpoint' ); ?></h1>
    <p class="bp-pagehead-desc"><?php esc_html_e( 'Brick selection, material guides, planning tips and industry updates.', 'brickpoint' ); ?></p>
    <form action="<?php echo esc_url( home_url( '/blog' ) ); ?>" method="get" class="bp-search-form bp-mt">
      <input type="search" name="s" placeholder="<?php esc_attr_e( 'Search articles…', 'brickpoint' ); ?>" value="<?php echo esc_attr( get_search_query() ); ?>" class="bp-input" />
      <button type="submit" class="btn-brick"><?php esc_html_e( 'Search', 'brickpoint' ); ?></button>
    </form>
  </div>
</div>

<section class="bp-section">
  <div class="bp-container">
    <?php
    $categories = get_categories();
    if ( ! empty( $categories ) ) : ?>
      <div class="bp-filters">
        <a href="<?php echo esc_url( home_url( '/blog' ) ); ?>" class="bp-filter-pill active"><?php esc_html_e( 'All', 'brickpoint' ); ?></a>
        <?php foreach ( $categories as $c ) : ?>
          <a href="<?php echo esc_url( get_category_link( $c->term_id ) ); ?>" class="bp-filter-pill"><?php echo esc_html( $c->name ); ?></a>
        <?php endforeach; ?>
      </div>
    <?php endif; ?>

    <div class="bp-grid cols-3 bp-mt">
      <?php
      if ( have_posts() ) :
        while ( have_posts() ) : the_post();
          get_template_part( 'template-parts/content' );
        endwhile;
      else : ?>
        <p><?php esc_html_e( 'No posts found.', 'brickpoint' ); ?></p>
      <?php endif; ?>
    </div>

    <div class="bp-pagination bp-mt">
      <?php the_posts_pagination(); ?>
    </div>
  </div>
</section>

<?php
get_footer();
"""

# single-bp_product.php
files["single-bp_product.php"] = """<?php
/**
 * Single Product template (No WooCommerce, Direct WhatsApp Ordering)
 *
 * @package BrickPoint
 */

if ( ! defined( 'ABSPATH' ) ) {
  exit;
}

get_header();

if ( function_exists( 'elementor_theme_do_location' ) && elementor_theme_do_location( 'single' ) ) {
  get_footer();
  return;
}

the_post();
$id = get_the_ID();
$price = bp_meta( $id, '_bp_price', '' );
$price_label = bp_meta( $id, '_bp_price_label', '' );
$unit = bp_meta( $id, '_bp_unit', '' );
$avail = bp_meta( $id, '_bp_availability', 'In Stock' );
$badge = bp_meta( $id, '_bp_badge', '' );
$sku = bp_meta( $id, '_bp_sku', '' );
$short = bp_meta( $id, '_bp_short', '' );
$gallery_raw = bp_meta( $id, '_bp_gallery', '' );
$specs_raw = bp_meta( $id, '_bp_specs', '' );
$features_raw = bp_meta( $id, '_bp_features', '' );
$video_url = bp_meta( $id, '_bp_video', '' );
$brochure_url = bp_meta( $id, '_bp_brochure', '' );
$wa_override = bp_meta( $id, '_bp_whatsapp', '' );

$terms = get_the_terms( $id, 'bp_product_category' );
$cat_name = ( $terms && ! is_wp_error( $terms ) ) ? $terms[0]->name : '';
$cat_link = ( $terms && ! is_wp_error( $terms ) ) ? get_term_link( $terms[0] ) : '';

$inquiry_text = $wa_override ? $wa_override : bp_product_inquiry_message( array(
  'product'  => get_the_title(),
  'category' => $cat_name,
  'price'    => trim( $price . ' ' . $price_label ),
  'unit'     => $unit,
) );
?>

<div class="bp-crumbs-bar">
  <div class="bp-container bp-crumbs">
    <a href="<?php echo esc_url( home_url( '/' ) ); ?>"><?php esc_html_e( 'Home', 'brickpoint' ); ?></a> &gt;
    <a href="<?php echo esc_url( home_url( '/products' ) ); ?>"><?php esc_html_e( 'Products', 'brickpoint' ); ?></a> &gt;
    <?php if ( $cat_name ) : ?>
      <a href="<?php echo esc_url( $cat_link ); ?>"><?php echo esc_html( $cat_name ); ?></a> &gt;
    <?php endif; ?>
    <span><?php the_title(); ?></span>
  </div>
</div>

<article id="product-<?php echo esc_attr( $id ); ?>" class="bp-section">
  <div class="bp-container bp-product-layout">
    <!-- Left Column: Media & Gallery -->
    <div class="bp-product-media-col">
      <div class="bp-product-hero-media img-zoom">
        <?php if ( has_post_thumbnail() ) : ?>
          <?php the_post_thumbnail( 'large', array( 'id' => 'bpMainProductImg', 'class' => 'bp-product-img' ) ); ?>
        <?php else : ?>
          <img id="bpMainProductImg" src="<?php echo esc_url( bp_asset_image_url( 'stacked.png' ) ); ?>" alt="<?php the_title_attribute(); ?>" class="bp-product-img" />
        <?php endif; ?>
        <?php if ( $badge ) : ?><span class="bp-badge"><?php echo esc_html( $badge ); ?></span><?php endif; ?>
      </div>

      <?php
      $gallery = array_filter( array_map( 'trim', explode( "\\n", $gallery_raw ) ) );
      if ( ! empty( $gallery ) ) : ?>
        <div class="bp-thumbs bp-mt">
          <?php if ( has_post_thumbnail() ) : ?>
            <img src="<?php echo esc_url( get_the_post_thumbnail_url( $id, 'thumbnail' ) ); ?>" alt="thumb" class="bp-thumb active" onclick="document.getElementById('bpMainProductImg').src='<?php echo esc_url( get_the_post_thumbnail_url( $id, 'large' ) ); ?>'" />
          <?php endif; ?>
          <?php foreach ( $gallery as $img_url ) : ?>
            <img src="<?php echo esc_url( $img_url ); ?>" alt="gallery thumb" class="bp-thumb" onclick="document.getElementById('bpMainProductImg').src='<?php echo esc_url( $img_url ); ?>'" />
          <?php endforeach; ?>
        </div>
      <?php endif; ?>

      <?php if ( $video_url ) : ?>
        <div class="bp-box bp-mt">
          <h4><?php esc_html_e( 'Product Video', 'brickpoint' ); ?></h4>
          <video controls playsinline preload="metadata" class="bp-video-player bp-mt">
            <source src="<?php echo esc_url( $video_url ); ?>" type="video/mp4" />
          </video>
        </div>
      <?php endif; ?>
    </div>

    <!-- Right Column: Product Details & WhatsApp Ordering -->
    <div class="bp-product-info-col">
      <?php if ( $cat_name ) : ?>
        <p class="bp-eyebrow"><a href="<?php echo esc_url( $cat_link ); ?>" style="color:inherit;text-decoration:none;"><?php echo esc_html( $cat_name ); ?></a></p>
      <?php endif; ?>

      <h1 class="bp-heading-1"><?php the_title(); ?></h1>

      <div class="bp-product-price-box bp-mt">
        <?php if ( $price ) : ?>
          <span class="bp-price-main"><?php echo esc_html( $price ); ?></span>
          <?php if ( $unit ) : ?><span class="bp-unit-tag">/ <?php echo esc_html( $unit ); ?></span><?php endif; ?>
        <?php else : ?>
          <span class="bp-price-main"><?php esc_html_e( 'Price on request', 'brickpoint' ); ?></span>
        <?php endif; ?>
        <?php if ( $price_label ) : ?>
          <p class="bp-price-lbl"><?php echo esc_html( $price_label ); ?></p>
        <?php endif; ?>
      </div>

      <?php if ( $avail ) : ?>
        <p class="bp-avail-tag"><span class="bp-dot"></span> <?php echo esc_html( $avail ); ?></p>
      <?php endif; ?>

      <?php if ( $sku ) : ?>
        <p class="bp-sku-tag">SKU: <strong><?php echo esc_html( $sku ); ?></strong></p>
      <?php endif; ?>

      <?php if ( $short ) : ?>
        <div class="bp-short-desc bp-mt">
          <p><?php echo esc_html( $short ); ?></p>
        </div>
      <?php endif; ?>

      <!-- Ordering Buttons: WhatsApp & Phone -->
      <div class="bp-product-cta bp-mt">
        <a href="<?php echo esc_url( bp_whatsapp_url( $inquiry_text ) ); ?>" target="_blank" rel="noopener" class="btn-whatsapp btn-lg btn-block">
          <svg class="bp-icon-md" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/></svg>
          <span><?php esc_html_e( 'Order on WhatsApp', 'brickpoint' ); ?></span>
        </a>
        <a href="tel:<?php echo esc_attr( bp_option( 'bp_phone_display', '0315 2850818' ) ); ?>" class="btn-ghost btn-lg btn-block">
          <svg class="bp-icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
          <span><?php esc_html_e( 'Call for Rate', 'brickpoint' ); ?></span>
        </a>
      </div>

      <!-- Specifications Table -->
      <?php
      $specs = array_filter( array_map( 'trim', explode( "\\n", $specs_raw ) ) );
      if ( ! empty( $specs ) ) : ?>
        <div class="bp-box bp-mt">
          <h3><?php esc_html_e( 'Product Specifications', 'brickpoint' ); ?></h3>
          <dl class="bp-specs-dl">
            <?php foreach ( $specs as $line ) :
              $parts = explode( ':', $line, 2 );
              if ( count( $parts ) === 2 ) : ?>
                <div class="bp-spec-row">
                  <dt><?php echo esc_html( trim( $parts[0] ) ); ?></dt>
                  <dd><?php echo esc_html( trim( $parts[1] ) ); ?></dd>
                </div>
            <?php endif; endforeach; ?>
          </dl>
        </div>
      <?php endif; ?>

      <!-- Features Checklist -->
      <?php
      $features = array_filter( array_map( 'trim', explode( "\\n", $features_raw ) ) );
      if ( ! empty( $features ) ) : ?>
        <div class="bp-box bp-mt">
          <h3><?php esc_html_e( 'Key Features', 'brickpoint' ); ?></h3>
          <ul class="bp-check-list bp-mt">
            <?php foreach ( $features as $feat ) : ?>
              <li>
                <svg class="bp-icon-check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M20 6 9 17l-5-5"/></svg>
                <span><?php echo esc_html( $feat ); ?></span>
              </li>
            <?php endforeach; ?>
          </ul>
        </div>
      <?php endif; ?>

      <?php if ( $brochure_url ) : ?>
        <p class="bp-mt">
          <a href="<?php echo esc_url( $brochure_url ); ?>" target="_blank" rel="noopener" class="btn-ghost">
            <span><?php esc_html_e( '📄 Download Brochure / Specs PDF', 'brickpoint' ); ?></span>
          </a>
        </p>
      <?php endif; ?>
    </div>
  </div>

  <!-- Full Description Tab/Box -->
  <div class="bp-container bp-mt">
    <div class="bp-box prose-bp">
      <h2><?php esc_html_e( 'Product Description', 'brickpoint' ); ?></h2>
      <?php the_content(); ?>
    </div>
  </div>

  <!-- Related Products Section -->
  <?php
  if ( $terms && ! is_wp_error( $terms ) ) {
    $rel_p = new WP_Query( array(
      'post_type'      => 'bp_product',
      'posts_per_page' => 4,
      'post__not_in'   => array( $id ),
      'tax_query'      => array(
        array(
          'taxonomy' => 'bp_product_category',
          'field'    => 'term_id',
          'terms'    => $terms[0]->term_id,
        ),
      ),
    ) );
    if ( $rel_p->have_posts() ) : ?>
      <div class="bp-container bp-mt" style="padding-top:2rem;">
        <h2 class="bp-heading-2"><?php esc_html_e( 'Related Products', 'brickpoint' ); ?></h2>
        <div class="bp-grid cols-4 bp-mt">
          <?php while ( $rel_p->have_posts() ) : $rel_p->the_post();
            get_template_part( 'template-parts/product-card' );
          endwhile; wp_reset_postdata(); ?>
        </div>
      </div>
    <?php endif;
  }
  ?>
</article>

<?php
get_footer();
"""

# archive-bp_product.php
files["archive-bp_product.php"] = """<?php
/**
 * Product Archive Template
 *
 * @package BrickPoint
 */

if ( ! defined( 'ABSPATH' ) ) {
  exit;
}

get_header();

if ( function_exists( 'elementor_theme_do_location' ) && elementor_theme_do_location( 'archive' ) ) {
  get_footer();
  return;
}
?>

<div class="bp-pagehead">
  <div class="bp-container">
    <p class="bp-eyebrow"><?php esc_html_e( 'Catalogue', 'brickpoint' ); ?></p>
    <h1 class="bp-heading-1"><?php esc_html_e( 'Products', 'brickpoint' ); ?></h1>
    <p class="bp-pagehead-desc"><?php esc_html_e( 'Every product with WhatsApp ordering — no cart, no checkout, just fast quotations.', 'brickpoint' ); ?></p>
    <div class="bp-filters bp-mt">
      <a href="<?php echo esc_url( get_post_type_archive_link( 'bp_product' ) ); ?>" class="bp-filter-pill active"><?php esc_html_e( 'All', 'brickpoint' ); ?></a>
      <?php
      $cats = get_terms( array( 'taxonomy' => 'bp_product_category', 'hide_empty' => false ) );
      if ( ! empty( $cats ) && ! is_wp_error( $cats ) ) :
        foreach ( $cats as $c ) : ?>
          <a href="<?php echo esc_url( get_term_link( $c ) ); ?>" class="bp-filter-pill"><?php echo esc_html( $c->name ); ?></a>
      <?php endforeach; endif; ?>
    </div>
  </div>
</div>

<section class="bp-section">
  <div class="bp-container">
    <div class="bp-grid cols-4">
      <?php
      if ( have_posts() ) :
        while ( have_posts() ) : the_post();
          get_template_part( 'template-parts/product-card' );
        endwhile;
      else : ?>
        <p class="bp-center" style="grid-column:1/-1;"><?php esc_html_e( 'No products found. Please import demo data from Appearance → BrickPoint Demo.', 'brickpoint' ); ?></p>
      <?php endif; ?>
    </div>
    <div class="bp-pagination bp-mt">
      <?php the_posts_pagination(); ?>
    </div>
  </div>
</section>

<?php
get_footer();
"""

# taxonomy-bp_product_category.php
files["taxonomy-bp_product_category.php"] = """<?php
/**
 * Product Category Taxonomy Template
 *
 * @package BrickPoint
 */

if ( ! defined( 'ABSPATH' ) ) {
  exit;
}

get_header();

if ( function_exists( 'elementor_theme_do_location' ) && elementor_theme_do_location( 'archive' ) ) {
  get_footer();
  return;
}

$term = get_queried_object();
$banner = get_term_meta( $term->term_id, 'bp_cat_banner', true );
if ( ! $banner ) {
  $banner = get_term_meta( $term->term_id, 'bp_cat_image', true );
}
$cat_video = get_term_meta( $term->term_id, 'bp_cat_video', true );
?>

<div class="bp-pagehead" <?php if ( $banner ) : ?>style="background-image:linear-gradient(rgba(20,18,16,0.85), rgba(20,18,16,0.95)), url('<?php echo esc_url( $banner ); ?>'); background-size:cover; background-position:center;"<?php endif; ?>>
  <div class="bp-container">
    <div class="bp-crumbs" style="color:rgba(255,255,255,0.7);">
      <a href="<?php echo esc_url( home_url( '/' ) ); ?>" style="color:inherit;"><?php esc_html_e( 'Home', 'brickpoint' ); ?></a> &gt;
      <a href="<?php echo esc_url( home_url( '/categories' ) ); ?>" style="color:inherit;"><?php esc_html_e( 'Categories', 'brickpoint' ); ?></a> &gt;
      <span><?php echo esc_html( $term->name ); ?></span>
    </div>
    <h1 class="bp-heading-1 bp-mt"><?php echo esc_html( $term->name ); ?></h1>
    <?php if ( $term->description ) : ?>
      <p class="bp-pagehead-desc"><?php echo esc_html( $term->description ); ?></p>
    <?php endif; ?>
    <div class="bp-action-row bp-mt">
      <a href="<?php echo esc_url( bp_whatsapp_url( bp_category_inquiry_message( $term->name ) ) ); ?>" target="_blank" rel="noopener" class="btn-whatsapp">
        <svg class="bp-icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/></svg>
        <span><?php printf( esc_html__( 'Get %s Quote', 'brickpoint' ), esc_html( $term->name ) ); ?></span>
      </a>
      <a href="<?php echo esc_url( home_url( '/products' ) ); ?>" class="btn-ghost" style="color:#fff;border-color:rgba(255,255,255,0.3);">
        <span><?php esc_html_e( 'All Products', 'brickpoint' ); ?></span>
      </a>
    </div>
  </div>
</div>

<?php if ( $cat_video ) : ?>
  <section class="bp-section bp-dark" style="padding:2rem 0;">
    <div class="bp-container bp-narrow">
      <p class="bp-eyebrow" style="margin-bottom:0.8rem;"><?php printf( esc_html__( 'Featured %s Video', 'brickpoint' ), esc_html( $term->name ) ); ?></p>
      <video controls playsinline preload="metadata" class="bp-video-player">
        <source src="<?php echo esc_url( $cat_video ); ?>" type="video/mp4" />
      </video>
    </div>
  </section>
<?php endif; ?>

<section class="bp-section">
  <div class="bp-container">
    <div class="bp-grid cols-4">
      <?php
      if ( have_posts() ) :
        while ( have_posts() ) : the_post();
          get_template_part( 'template-parts/product-card' );
        endwhile;
      else : ?>
        <p class="bp-center" style="grid-column:1/-1;">
          <?php printf( esc_html__( 'No products in %s yet. Ask for rates on WhatsApp.', 'brickpoint' ), esc_html( $term->name ) ); ?>
        </p>
      <?php endif; ?>
    </div>
    <div class="bp-pagination bp-mt">
      <?php the_posts_pagination(); ?>
    </div>
  </div>
</section>

<?php
get_footer();
"""

# single-bp_video.php
files["single-bp_video.php"] = """<?php
/**
 * Single Video Template
 *
 * @package BrickPoint
 */

if ( ! defined( 'ABSPATH' ) ) {
  exit;
}

get_header();

if ( function_exists( 'elementor_theme_do_location' ) && elementor_theme_do_location( 'single' ) ) {
  get_footer();
  return;
}

the_post();
$id = get_the_ID();
$source = bp_meta( $id, '_bpv_source', 'mp4' );
$url = bp_meta( $id, '_bpv_url', '' );
$file = bp_meta( $id, '_bpv_file', '' );
$dur = bp_meta( $id, '_bpv_duration', '' );
$feat = bp_meta( $id, '_bpv_featured', '0' );

$is_embed = ( $source === 'youtube' || $source === 'vimeo' || strpos( $url, 'embed' ) !== false );
?>

<div class="bp-dark" style="padding:1.5rem 0 3rem 0;">
  <div class="bp-container">
    <div class="bp-crumbs" style="color:rgba(255,255,255,0.6);margin-bottom:1.5rem;">
      <a href="<?php echo esc_url( home_url( '/' ) ); ?>" style="color:inherit;"><?php esc_html_e( 'Home', 'brickpoint' ); ?></a> &gt;
      <a href="<?php echo esc_url( home_url( '/videos' ) ); ?>" style="color:inherit;"><?php esc_html_e( 'Videos', 'brickpoint' ); ?></a> &gt;
      <span><?php the_title(); ?></span>
    </div>

    <!-- Video Embed / Player -->
    <div class="bp-video-stage hero-video-frame">
      <?php if ( $is_embed ) : ?>
        <iframe src="<?php echo esc_url( $url ); ?>" title="<?php the_title_attribute(); ?>" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen class="bp-video-embed"></iframe>
      <?php else : ?>
        <video controls playsinline preload="metadata" poster="<?php echo esc_url( get_the_post_thumbnail_url( $id, 'large' ) ); ?>" class="bp-video-player">
          <source src="<?php echo esc_url( $file ? $file : $url ); ?>" type="video/mp4" />
        </video>
      <?php endif; ?>
    </div>

    <div class="bp-video-meta-box bp-mt">
      <?php
      $cats = get_the_terms( $id, 'bp_video_category' );
      if ( ! empty( $cats ) && ! is_wp_error( $cats ) ) : ?>
        <p class="bp-eyebrow"><?php echo esc_html( $cats[0]->name ); ?></p>
      <?php endif; ?>
      <h1 class="bp-heading-1 bp-head-light"><?php the_title(); ?></h1>
      <div class="bp-video-specs bp-mt">
        <?php if ( $dur ) : ?>
          <span class="bp-meta-pill">⏱ <?php echo esc_html( $dur ); ?></span>
        <?php endif; ?>
        <span class="bp-meta-pill">📅 <?php echo esc_html( get_the_date() ); ?></span>
        <?php if ( $feat === '1' ) : ?>
          <span class="bp-badge" style="position:static;"><?php esc_html_e( 'Featured', 'brickpoint' ); ?></span>
        <?php endif; ?>
      </div>
      <div class="bp-video-desc prose-bp bp-mt" style="color:rgba(255,255,255,0.8);">
        <?php the_content(); ?>
      </div>
      <div class="bp-action-row bp-mt">
        <a href="<?php echo esc_url( home_url( '/videos' ) ); ?>" class="btn-ghost" style="color:#fff;border-color:rgba(255,255,255,0.3);"><?php esc_html_e( '← All Videos', 'brickpoint' ); ?></a>
        <a href="<?php echo esc_url( home_url( '/products' ) ); ?>" class="btn-brick"><?php esc_html_e( 'Related Products', 'brickpoint' ); ?></a>
        <a href="<?php echo esc_url( bp_whatsapp_url( 'Assalam-o-Alaikum BrickPoint, I saw your video: ' . get_the_title() ) ); ?>" target="_blank" rel="noopener" class="btn-whatsapp">
          <span><?php esc_html_e( 'WhatsApp Us', 'brickpoint' ); ?></span>
        </a>
      </div>
    </div>

    <!-- More Videos -->
    <?php
    $more = new WP_Query( array(
      'post_type'      => 'bp_video',
      'posts_per_page' => 3,
      'post__not_in'   => array( $id ),
    ) );
    if ( $more->have_posts() ) : ?>
      <div class="bp-mt" style="padding-top:3rem;">
        <h2 class="bp-heading-2 bp-head-light"><?php esc_html_e( 'More Videos', 'brickpoint' ); ?></h2>
        <div class="bp-grid cols-3 bp-mt">
          <?php while ( $more->have_posts() ) : $more->the_post();
            get_template_part( 'template-parts/video-card' );
          endwhile; wp_reset_postdata(); ?>
        </div>
      </div>
    <?php endif; ?>
  </div>
</div>

<?php
get_footer();
"""

# archive-bp_video.php & taxonomy-bp_video_category.php
files["archive-bp_video.php"] = """<?php
/**
 * Video Library Archive
 *
 * @package BrickPoint
 */

if ( ! defined( 'ABSPATH' ) ) {
  exit;
}

get_header();

if ( function_exists( 'elementor_theme_do_location' ) && elementor_theme_do_location( 'archive' ) ) {
  get_footer();
  return;
}
?>

<div class="bp-pagehead">
  <div class="bp-container">
    <p class="bp-eyebrow"><?php esc_html_e( 'Video Library', 'brickpoint' ); ?></p>
    <h1 class="bp-heading-1"><?php esc_html_e( 'Inside BrickPoint', 'brickpoint' ); ?></h1>
    <p class="bp-pagehead-desc"><?php esc_html_e( 'Explore our products, production process, construction materials, projects, and company updates through video.', 'brickpoint' ); ?></p>
    <div class="bp-filters bp-mt">
      <a href="<?php echo esc_url( get_post_type_archive_link( 'bp_video' ) ); ?>" class="bp-filter-pill active"><?php esc_html_e( 'All Videos', 'brickpoint' ); ?></a>
      <?php
      $vcats = get_terms( array( 'taxonomy' => 'bp_video_category', 'hide_empty' => false ) );
      if ( ! empty( $vcats ) && ! is_wp_error( $vcats ) ) :
        foreach ( $vcats as $vc ) : ?>
          <a href="<?php echo esc_url( get_term_link( $vc ) ); ?>" class="bp-filter-pill"><?php echo esc_html( $vc->name ); ?></a>
      <?php endforeach; endif; ?>
    </div>
  </div>
</div>

<section class="bp-section">
  <div class="bp-container">
    <div class="bp-grid cols-3">
      <?php
      if ( have_posts() ) :
        while ( have_posts() ) : the_post();
          get_template_part( 'template-parts/video-card' );
        endwhile;
      else : ?>
        <p class="bp-center" style="grid-column:1/-1;"><?php esc_html_e( 'No videos found.', 'brickpoint' ); ?></p>
      <?php endif; ?>
    </div>
    <div class="bp-pagination bp-mt">
      <?php the_posts_pagination(); ?>
    </div>
  </div>
</section>

<?php
get_footer();
"""

files["taxonomy-bp_video_category.php"] = """<?php
/**
 * Video Category Taxonomy Template
 *
 * @package BrickPoint
 */

if ( ! defined( 'ABSPATH' ) ) {
  exit;
}

get_header();

if ( function_exists( 'elementor_theme_do_location' ) && elementor_theme_do_location( 'archive' ) ) {
  get_footer();
  return;
}

$term = get_queried_object();
?>

<div class="bp-pagehead">
  <div class="bp-container">
    <div class="bp-crumbs" style="color:rgba(255,255,255,0.7);">
      <a href="<?php echo esc_url( home_url( '/' ) ); ?>" style="color:inherit;"><?php esc_html_e( 'Home', 'brickpoint' ); ?></a> &gt;
      <a href="<?php echo esc_url( home_url( '/videos' ) ); ?>" style="color:inherit;"><?php esc_html_e( 'Videos', 'brickpoint' ); ?></a> &gt;
      <span><?php echo esc_html( $term->name ); ?></span>
    </div>
    <h1 class="bp-heading-1 bp-mt"><?php echo esc_html( $term->name ); ?></h1>
    <?php if ( $term->description ) : ?>
      <p class="bp-pagehead-desc"><?php echo esc_html( $term->description ); ?></p>
    <?php endif; ?>
  </div>
</div>

<section class="bp-section">
  <div class="bp-container">
    <div class="bp-grid cols-3">
      <?php
      if ( have_posts() ) :
        while ( have_posts() ) : the_post();
          get_template_part( 'template-parts/video-card' );
        endwhile;
      else : ?>
        <p class="bp-center" style="grid-column:1/-1;"><?php esc_html_e( 'No videos in this category yet.', 'brickpoint' ); ?></p>
      <?php endif; ?>
    </div>
    <div class="bp-pagination bp-mt">
      <?php the_posts_pagination(); ?>
    </div>
  </div>
</section>

<?php
get_footer();
"""

# single-bp_project.php & archive-bp_project.php
files["single-bp_project.php"] = """<?php
/**
 * Single Project Template
 *
 * @package BrickPoint
 */

if ( ! defined( 'ABSPATH' ) ) {
  exit;
}

get_header();

if ( function_exists( 'elementor_theme_do_location' ) && elementor_theme_do_location( 'single' ) ) {
  get_footer();
  return;
}

the_post();
$id = get_the_ID();
$cat = bp_meta( $id, '_bpp_category', 'Residential' );
$loc = bp_meta( $id, '_bpp_location', 'Lahore' );
$status = bp_meta( $id, '_bpp_status', 'Illustrative construction reference' );
?>

<div class="bp-crumbs-bar">
  <div class="bp-container bp-crumbs">
    <a href="<?php echo esc_url( home_url( '/' ) ); ?>"><?php esc_html_e( 'Home', 'brickpoint' ); ?></a> &gt;
    <a href="<?php echo esc_url( home_url( '/projects' ) ); ?>"><?php esc_html_e( 'Projects', 'brickpoint' ); ?></a> &gt;
    <span><?php the_title(); ?></span>
  </div>
</div>

<article id="project-<?php echo esc_attr( $id ); ?>" class="bp-section">
  <div class="bp-container bp-narrow">
    <div class="bp-notice-box">
      <strong><?php esc_html_e( 'Content notice:', 'brickpoint' ); ?></strong>
      <em>“<?php echo esc_html( $status ); ?>”</em>. <?php esc_html_e( 'BrickPoint does not claim supply to any named society or developer unless verified by management.', 'brickpoint' ); ?>
    </div>

    <div class="bp-mt">
      <p class="bp-eyebrow"><?php echo esc_html( $loc ); ?> &bull; <?php echo esc_html( $cat ); ?></p>
      <h1 class="bp-heading-1"><?php the_title(); ?></h1>
    </div>

    <?php if ( has_post_thumbnail() ) : ?>
      <div class="bp-post-hero-img img-zoom bp-mt">
        <?php the_post_thumbnail( 'large', array( 'class' => 'bp-featured-img' ) ); ?>
      </div>
    <?php endif; ?>

    <div class="bp-box prose-bp bp-mt">
      <?php the_content(); ?>
    </div>

    <div class="bp-action-row bp-mt">
      <a href="<?php echo esc_url( home_url( '/projects' ) ); ?>" class="btn-ghost"><?php esc_html_e( '← All Projects', 'brickpoint' ); ?></a>
      <a href="<?php echo esc_url( bp_whatsapp_url( 'Assalam-o-Alaikum BrickPoint, I need materials like the ones in project: ' . get_the_title() ) ); ?>" target="_blank" rel="noopener" class="btn-whatsapp">
        <svg class="bp-icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/></svg>
        <span><?php esc_html_e( 'Inquire on WhatsApp', 'brickpoint' ); ?></span>
      </a>
      <a href="<?php echo esc_url( home_url( '/contact' ) ); ?>" class="btn-brick"><?php esc_html_e( 'Request Quotation', 'brickpoint' ); ?></a>
    </div>
  </div>
</article>

<?php
get_footer();
"""

files["archive-bp_project.php"] = """<?php
/**
 * Projects Archive Template
 *
 * @package BrickPoint
 */

if ( ! defined( 'ABSPATH' ) ) {
  exit;
}

get_header();

if ( function_exists( 'elementor_theme_do_location' ) && elementor_theme_do_location( 'archive' ) ) {
  get_footer();
  return;
}

$societies = array( 'DHA Lahore', 'Bahria Town Lahore', 'Lake City Lahore', 'Etihad Town Lahore', 'Al-Kabir Town', 'LDA City', 'Paragon City', 'Izmir Town' );
?>

<div class="bp-pagehead">
  <div class="bp-container">
    <p class="bp-eyebrow"><?php esc_html_e( 'References & Inspiration', 'brickpoint' ); ?></p>
    <h1 class="bp-heading-1"><?php esc_html_e( 'Projects', 'brickpoint' ); ?></h1>
    <p class="bp-pagehead-desc"><?php esc_html_e( 'Construction references and project inspiration visuals from Lahore housing developments. Visuals are illustrative unless a project is verified by BrickPoint.', 'brickpoint' ); ?></p>
    <div class="bp-societies-row bp-mt">
      <?php foreach ( $societies as $s ) : ?>
        <span class="bp-soc-pill">
          <svg class="bp-icon-xs" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/></svg>
          <?php echo esc_html( $s ); ?>
        </span>
      <?php endforeach; ?>
    </div>
  </div>
</div>

<section class="bp-section">
  <div class="bp-container">
    <div class="bp-notice-box">
      <strong><?php esc_html_e( 'Content notice:', 'brickpoint' ); ?></strong>
      <?php esc_html_e( 'Project visuals on this page are labelled “Illustrative construction reference” or “Project inspiration visual”. BrickPoint does not claim supply to any named society, developer or project unless verified by management.', 'brickpoint' ); ?>
    </div>

    <div class="bp-grid cols-3 bp-mt">
      <?php
      if ( have_posts() ) :
        while ( have_posts() ) : the_post();
          get_template_part( 'template-parts/project-card' );
        endwhile;
      else : ?>
        <p class="bp-center" style="grid-column:1/-1;"><?php esc_html_e( 'No project references loaded.', 'brickpoint' ); ?></p>
      <?php endif; ?>
    </div>

    <div class="bp-pagination bp-mt">
      <?php the_posts_pagination(); ?>
    </div>
  </div>
</section>

<?php
get_footer();
"""

# single-bp_location.php & archive-bp_location.php
files["single-bp_location.php"] = """<?php
/**
 * Single Location Template
 *
 * @package BrickPoint
 */

if ( ! defined( 'ABSPATH' ) ) {
  exit;
}

get_header();

the_post();
$id = get_the_ID();
$addr = bp_meta( $id, '_bpl_address', '' );
$phone = bp_meta( $id, '_bpl_phone', bp_option( 'bp_phone_display', '0315 2850818' ) );
$hours = bp_meta( $id, '_bpl_hours', 'Mon – Sat: 8:00 AM – 6:00 PM' );
$maps = bp_meta( $id, '_bpl_maps_url', '' );
$video = bp_meta( $id, '_bpl_video', '' );
?>

<div class="bp-crumbs-bar">
  <div class="bp-container bp-crumbs">
    <a href="<?php echo esc_url( home_url( '/' ) ); ?>"><?php esc_html_e( 'Home', 'brickpoint' ); ?></a> &gt;
    <a href="<?php echo esc_url( home_url( '/locations' ) ); ?>"><?php esc_html_e( 'Locations', 'brickpoint' ); ?></a> &gt;
    <span><?php the_title(); ?></span>
  </div>
</div>

<article id="location-<?php echo esc_attr( $id ); ?>" class="bp-section">
  <div class="bp-container bp-narrow">
    <h1 class="bp-heading-1"><?php the_title(); ?></h1>

    <?php if ( has_post_thumbnail() ) : ?>
      <div class="bp-post-hero-img img-zoom bp-mt">
        <?php the_post_thumbnail( 'large', array( 'class' => 'bp-featured-img' ) ); ?>
      </div>
    <?php endif; ?>

    <div class="bp-box bp-mt">
      <p class="bp-loc-meta-item">
        <svg class="bp-icon-sm text-orange" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/></svg>
        <strong>Address:</strong> <?php echo esc_html( $addr ); ?>
      </p>
      <p class="bp-loc-meta-item bp-mt">
        <svg class="bp-icon-sm text-orange" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
        <strong>Phone:</strong> <a href="tel:<?php echo esc_attr( $phone ); ?>"><?php echo esc_html( $phone ); ?></a>
      </p>
      <p class="bp-loc-meta-item bp-mt">
        <svg class="bp-icon-sm text-orange" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
        <strong>Hours:</strong> <?php echo esc_html( $hours ); ?>
      </p>
    </div>

    <div class="bp-box prose-bp bp-mt">
      <?php the_content(); ?>
    </div>

    <?php if ( $video ) : ?>
      <div class="bp-box bp-mt">
        <h3><?php esc_html_e( 'Facility Video', 'brickpoint' ); ?></h3>
        <video controls playsinline preload="metadata" class="bp-video-player bp-mt">
          <source src="<?php echo esc_url( $video ); ?>" type="video/mp4" />
        </video>
      </div>
    <?php endif; ?>

    <div class="bp-action-row bp-mt">
      <?php if ( $maps ) : ?>
        <a href="<?php echo esc_url( $maps ); ?>" target="_blank" rel="noopener" class="btn-dark">
          <span><?php esc_html_e( '📍 Open in Google Maps', 'brickpoint' ); ?></span>
        </a>
      <?php endif; ?>
      <a href="<?php echo esc_url( bp_whatsapp_url( 'Assalam-o-Alaikum BrickPoint, I am interested in visiting: ' . get_the_title() ) ); ?>" target="_blank" rel="noopener" class="btn-whatsapp">
        <span><?php esc_html_e( 'WhatsApp Inquiry', 'brickpoint' ); ?></span>
      </a>
      <a href="<?php echo esc_url( home_url( '/locations' ) ); ?>" class="btn-ghost"><?php esc_html_e( 'All Locations', 'brickpoint' ); ?></a>
    </div>
  </div>
</article>

<?php
get_footer();
"""

files["archive-bp_location.php"] = """<?php
/**
 * Locations Archive Template (Our Bhattas & Office)
 *
 * @package BrickPoint
 */

if ( ! defined( 'ABSPATH' ) ) {
  exit;
}

get_header();
?>

<div class="bp-pagehead">
  <div class="bp-container">
    <p class="bp-eyebrow"><?php esc_html_e( 'Bhattas & Office', 'brickpoint' ); ?></p>
    <h1 class="bp-heading-1"><?php esc_html_e( 'Our Locations', 'brickpoint' ); ?></h1>
    <p class="bp-pagehead-desc"><?php esc_html_e( 'Three production units plus head office — tap any card for real Google Maps directions.', 'brickpoint' ); ?></p>
  </div>
</div>

<section class="bp-section">
  <div class="bp-container">
    <div class="bp-grid cols-2">
      <?php
      if ( have_posts() ) :
        $unit_num = 1;
        while ( have_posts() ) : the_post();
          $id = get_the_ID();
          $addr = bp_meta( $id, '_bpl_address', '' );
          $phone = bp_meta( $id, '_bpl_phone', bp_option( 'bp_phone_display', '0315 2850818' ) );
          $hours = bp_meta( $id, '_bpl_hours', 'Mon – Sat: 8:00 AM – 6:00 PM' );
          $maps = bp_meta( $id, '_bpl_maps_url', '' );
          $video = bp_meta( $id, '_bpl_video', '' );
      ?>
        <article class="bp-card card-hover group bp-loc-full-card">
          <div class="bp-card-media img-zoom">
            <?php if ( has_post_thumbnail() ) : ?>
              <?php the_post_thumbnail( 'large' ); ?>
            <?php else : ?>
              <img src="<?php echo esc_url( bp_asset_image_url( 'kiln.png' ) ); ?>" alt="<?php the_title_attribute(); ?>" />
            <?php endif; ?>
            <span class="bp-badge"><?php printf( esc_html__( 'Unit %d', 'brickpoint' ), $unit_num ); ?></span>
          </div>
          <div class="bp-card-body">
            <h3><?php the_title(); ?></h3>
            <?php if ( $addr ) : ?>
              <p class="bp-loc-item">
                <svg class="bp-icon-sm text-orange" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/></svg>
                <span><?php echo esc_html( $addr ); ?></span>
              </p>
            <?php endif; ?>
            <p class="bp-loc-desc"><?php echo esc_html( get_the_excerpt() ); ?></p>
            <div class="bp-loc-meta-tags">
              <?php if ( $phone ) : ?><span>📞 <?php echo esc_html( $phone ); ?></span><?php endif; ?>
              <?php if ( $hours ) : ?><span>⏱ <?php echo esc_html( $hours ); ?></span><?php endif; ?>
            </div>
            <?php if ( $video ) : ?>
              <video controls playsinline preload="metadata" class="bp-video-player bp-mt">
                <source src="<?php echo esc_url( $video ); ?>" type="video/mp4" />
              </video>
            <?php endif; ?>
            <div class="bp-card-cta bp-mt">
              <?php if ( $maps ) : ?>
                <a href="<?php echo esc_url( $maps ); ?>" target="_blank" rel="noopener" class="btn-dark btn-sm"><?php esc_html_e( '📍 Directions', 'brickpoint' ); ?></a>
              <?php endif; ?>
              <a href="<?php echo esc_url( bp_whatsapp_url( 'Assalam-o-Alaikum BrickPoint, I want to visit ' . get_the_title() ) ); ?>" target="_blank" rel="noopener" class="btn-whatsapp btn-sm"><?php esc_html_e( 'WhatsApp', 'brickpoint' ); ?></a>
              <a href="<?php echo esc_url( home_url( '/contact' ) ); ?>" class="btn-ghost btn-sm"><?php esc_html_e( 'Contact', 'brickpoint' ); ?></a>
            </div>
          </div>
        </article>
      <?php $unit_num++; endwhile; endif; ?>
    </div>
  </div>
</section>

<?php
get_footer();
"""

# search.php & 404.php & rtl.css & readme.txt
files["search.php"] = """<?php
/**
 * The template for displaying search results
 *
 * @package BrickPoint
 */

if ( ! defined( 'ABSPATH' ) ) {
  exit;
}

get_header();
?>

<div class="bp-pagehead">
  <div class="bp-container">
    <p class="bp-eyebrow"><?php esc_html_e( 'Search Results', 'brickpoint' ); ?></p>
    <h1 class="bp-heading-1"><?php printf( esc_html__( 'Results for: %s', 'brickpoint' ), '<span>' . get_search_query() . '</span>' ); ?></h1>
  </div>
</div>

<section class="bp-section">
  <div class="bp-container">
    <div class="bp-grid cols-3">
      <?php
      if ( have_posts() ) :
        while ( have_posts() ) : the_post();
          get_template_part( 'template-parts/content' );
        endwhile;
      else : ?>
        <p class="bp-center" style="grid-column:1/-1;"><?php esc_html_e( 'No results matched your query. Try a different search term.', 'brickpoint' ); ?></p>
      <?php endif; ?>
    </div>
    <div class="bp-pagination bp-mt">
      <?php the_posts_pagination(); ?>
    </div>
  </div>
</section>

<?php
get_footer();
"""

files["404.php"] = """<?php
/**
 * The template for displaying 404 pages (Not Found)
 *
 * @package BrickPoint
 */

if ( ! defined( 'ABSPATH' ) ) {
  exit;
}

get_header();
?>

<div class="bp-section bp-center" style="padding:6rem 0;">
  <div class="bp-container bp-narrow">
    <p class="bp-eyebrow"><?php esc_html_e( '404 Error', 'brickpoint' ); ?></p>
    <h1 class="bp-heading-1 bp-mt"><?php esc_html_e( 'Page Not Found', 'brickpoint' ); ?></h1>
    <p class="bp-body-text bp-mt"><?php esc_html_e( 'The page you are looking for does not exist or has been moved.', 'brickpoint' ); ?></p>
    <div class="bp-action-row bp-mt" style="justify-content:center;">
      <a href="<?php echo esc_url( home_url( '/' ) ); ?>" class="btn-brick"><?php esc_html_e( 'Back to Home', 'brickpoint' ); ?></a>
      <a href="<?php echo esc_url( home_url( '/products' ) ); ?>" class="btn-dark"><?php esc_html_e( 'Browse Products', 'brickpoint' ); ?></a>
      <a href="<?php echo esc_url( home_url( '/contact' ) ); ?>" class="btn-ghost"><?php esc_html_e( 'Contact Us', 'brickpoint' ); ?></a>
    </div>
  </div>
</div>

<?php
get_footer();
"""

files["rtl.css"] = """/* RTL Styles */
body { direction: rtl; unicode-bidi: embed; }
.bp-topbar-inner, .bp-header-inner, .bp-footer-bottom-inner { flex-direction: row-reverse; }
.bp-specs-dl dt { text-align: right; }
.bp-float-wa { right: auto; left: 1.25rem; }
"""

files["readme.txt"] = """=== BrickPoint ===
Contributors: BrickPoint
Requires at least: 6.0
Tested up to: 6.7
Requires PHP: 7.4
License: GPLv2 or later

== Description ==
BrickPoint is a premium construction-materials and brick manufacturing WordPress theme.
Designed with native Elementor Free and Elementor Pro Theme Builder support, one-click demo import, custom Product (bp_product), Video (bp_video), Project (bp_project), and Location (bp_location) post types with direct WhatsApp ordering. No WooCommerce required.

== Features ==
* Native Elementor Free and Pro support
* Elementor Pro Theme Builder locations (Header, Footer, Single Product, Product Archive, Single Video, Video Archive, Single Project, Project Archive, Single Blog, Blog Archive)
* One-Click Demo Importer with 17 complete pages and 24 Elementor templates
* Direct WhatsApp ordering on all products and categories
* Independent Header Logo and Footer Logo controls with responsive sizing
* 13 custom Elementor widgets
* Offline media bundling for reliable demo imports
"""

# Template parts
files["template-parts/hero.php"] = """<?php
/**
 * Hero template part
 *
 * @package BrickPoint
 */

if ( ! defined( 'ABSPATH' ) ) {
  exit;
}

$hero_img = bp_asset_image_url( 'brick-mason.png' );
$hero_video = bp_option( 'bp_hero_video', 'https://videos.pexels.com/video-files/35411576/15003649_3840_2160_24fps.mp4' );
$hero_poster = bp_asset_image_url( 'hero-poster.png' );
?>
<section class="bp-hero relative">
  <div class="bp-hero-bg">
    <img src="<?php echo esc_url( $hero_img ); ?>" alt="<?php esc_attr_e( 'Bricklayers building a wall', 'brickpoint' ); ?>" class="bp-hero-bg-img" />
    <div class="bp-hero-overlay"></div>
    <div class="brick-lines absolute-bg"></div>
  </div>

  <div class="bp-container bp-hero-grid relative">
    <!-- Left Hero Column -->
    <div class="bp-hero-text">
      <p class="bp-hero-badge">
        <svg class="bp-icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 20a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8l-7 5V8l-7 5V4a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2Z"/></svg>
        <span>Masha Allah &bull; Fine Bricks &bull; SS7</span>
      </p>

      <h1 class="bp-hero-title">
        Building Strength.<br />
        <span class="text-orange">Delivering Quality.</span><br />
        Shaping Tomorrow.
      </h1>

      <p class="bp-hero-sub">
        Premium bricks and reliable construction materials for homes, commercial developments, and large-scale building projects.
      </p>

      <div class="bp-hero-cta">
        <a href="<?php echo esc_url( home_url( '/products' ) ); ?>" class="btn-brick">
          <span><?php esc_html_e( 'Explore Products', 'brickpoint' ); ?></span>
          <svg class="bp-icon-xs" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>
        </a>
        <a href="<?php echo esc_url( home_url( '/contact' ) ); ?>" class="btn-ghost" style="color:#fff;border-color:rgba(255,255,255,0.25);">
          <span><?php esc_html_e( 'Request a Quote', 'brickpoint' ); ?></span>
        </a>
        <a href="<?php echo esc_url( bp_whatsapp_url( 'Assalam-o-Alaikum BrickPoint, I need a quotation for construction materials.' ) ); ?>" target="_blank" rel="noopener" class="btn-whatsapp">
          <svg class="bp-icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/></svg>
          <span><?php esc_html_e( 'WhatsApp Us', 'brickpoint' ); ?></span>
        </a>
      </div>

      <div class="bp-hero-trust-row">
        <span><svg class="bp-icon-sm text-green" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/></svg> Quality-focused supply</span>
        <span><svg class="bp-icon-sm text-green" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 18V6a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2v11a1 1 0 0 0 1 1h2"/><path d="M15 18H9"/><path d="M19 18h2a1 1 0 0 0 1-1v-3.65a1 1 0 0 0-.22-.624l-3.48-4.35A1 1 0 0 0 17.52 8H14"/><circle cx="17" cy="18.5" r="2.5"/><circle cx="7" cy="18.5" r="2.5"/></svg> Reliable delivery</span>
        <span><svg class="bp-icon-sm text-green" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 20a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8l-7 5V8l-7 5V4a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2Z"/></svg> Multiple production locations</span>
      </div>
    </div>

    <!-- Right Hero Column: Video Frame + SS7 Animated Floating Card -->
    <div class="bp-hero-media-wrap relative">
      <div class="hero-video-frame relative">
        <video autoplay muted loop playsinline preload="metadata" poster="<?php echo esc_url( $hero_poster ); ?>" class="bp-hero-video-el" aria-label="BrickPoint brick construction video">
          <source src="<?php echo esc_url( $hero_video ); ?>" type="video/mp4" />
        </video>
        <div class="bp-hero-video-overlay">
          <div>
            <p class="bp-video-eyebrow">SS7 Bricks &bull; In Action</p>
            <p class="bp-video-caption">See the strength behind every brick</p>
          </div>
          <a href="<?php echo esc_url( home_url( '/videos' ) ); ?>" class="bp-play-circle" aria-label="Watch all videos">
            <svg class="bp-icon-sm" viewBox="0 0 24 24" fill="currentColor"><polygon points="6 3 20 12 6 21 6 3"/></svg>
          </a>
        </div>
      </div>

      <!-- SS7 3D Floating Brick Card -->
      <div class="bp-ss7-float-badge ss7-brick-loop">
        <div class="ss7-brick">
          <img src="<?php echo esc_url( bp_asset_image_url( 'red-stack.png' ) ); ?>" alt="SS7 brick close up" class="bp-ss7-thumb" />
          <div>
            <p class="bp-flagship-tag">
              <svg class="bp-icon-xs text-gold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="8" r="6"/><path d="m15.477 12.89 1.515 8.526a.5.5 0 0 1-.722.522l-4.27-2.247-4.27 2.247a.5.5 0 0 1-.722-.522l1.515-8.526"/></svg> Flagship
            </p>
            <p class="bp-ss7-title">SS7 Bricks</p>
            <a href="<?php echo esc_url( home_url( '/ss7-bricks' ) ); ?>" class="bp-ss7-link">View SS7 range &rarr;</a>
          </div>
        </div>
      </div>

      <!-- Production Units Pill -->
      <div class="bp-units-pill">
        <p class="bp-units-count">3<span class="text-orange">+</span></p>
        <p class="bp-units-label">Production units</p>
      </div>
    </div>
  </div>

  <!-- Marquee Bar -->
  <div class="bp-marquee-bar">
    <div class="marquee-track">
      <div class="marquee-group">
        <span><span class="bp-dot-orange"></span>SS7 Bricks</span>
        <span><span class="bp-dot-orange"></span>Cement</span>
        <span><span class="bp-dot-orange"></span>Bajri / Crush</span>
        <span><span class="bp-dot-orange"></span>Sand / Rait</span>
        <span><span class="bp-dot-orange"></span>Steel</span>
        <span><span class="bp-dot-orange"></span>Pipes</span>
        <span><span class="bp-dot-orange"></span>Chemicals</span>
        <span><span class="bp-dot-orange"></span>Cables</span>
        <span><span class="bp-dot-orange"></span>Paints</span>
        <span><span class="bp-dot-orange"></span>Lights</span>
      </div>
      <div class="marquee-group">
        <span><span class="bp-dot-orange"></span>SS7 Bricks</span>
        <span><span class="bp-dot-orange"></span>Cement</span>
        <span><span class="bp-dot-orange"></span>Bajri / Crush</span>
        <span><span class="bp-dot-orange"></span>Sand / Rait</span>
        <span><span class="bp-dot-orange"></span>Steel</span>
        <span><span class="bp-dot-orange"></span>Pipes</span>
        <span><span class="bp-dot-orange"></span>Chemicals</span>
        <span><span class="bp-dot-orange"></span>Cables</span>
        <span><span class="bp-dot-orange"></span>Paints</span>
        <span><span class="bp-dot-orange"></span>Lights</span>
      </div>
    </div>
  </div>
</section>
"""

files["template-parts/product-card.php"] = """<?php
/**
 * Product Card template part
 *
 * @package BrickPoint
 */

if ( ! defined( 'ABSPATH' ) ) {
  exit;
}

$id = get_the_ID();
$price = bp_meta( $id, '_bp_price', '' );
$price_label = bp_meta( $id, '_bp_price_label', '' );
$unit = bp_meta( $id, '_bp_unit', '' );
$avail = bp_meta( $id, '_bp_availability', 'In Stock' );
$badge = bp_meta( $id, '_bp_badge', '' );
$short = bp_meta( $id, '_bp_short', '' );
$video = bp_meta( $id, '_bp_video', '' );

$terms = get_the_terms( $id, 'bp_product_category' );
$cat_name = ( $terms && ! is_wp_error( $terms ) ) ? $terms[0]->name : '';

$inquiry_text = bp_product_inquiry_message( array(
  'product'  => get_the_title(),
  'category' => $cat_name,
  'price'    => trim( $price . ' ' . $price_label ),
  'unit'     => $unit,
) );
?>
<article class="bp-card card-hover group flex-col">
  <a href="<?php the_permalink(); ?>" class="bp-card-media img-zoom">
    <?php if ( has_post_thumbnail() ) : ?>
      <?php the_post_thumbnail( 'bp-card' ); ?>
    <?php else : ?>
      <img src="<?php echo esc_url( bp_asset_image_url( 'stacked.png' ) ); ?>" alt="<?php the_title_attribute(); ?>" />
    <?php endif; ?>

    <div class="bp-card-badges-top">
      <?php if ( $badge ) : ?>
        <span class="bp-badge"><?php echo esc_html( $badge ); ?></span>
      <?php endif; ?>
      <?php if ( $avail ) : ?>
        <span class="bp-avail <?php echo ( $avail === 'In Stock' ) ? 'in-stock' : ''; ?>"><?php echo esc_html( $avail ); ?></span>
      <?php endif; ?>
    </div>

    <?php if ( $video ) : ?>
      <span class="bp-card-video-play">
        <svg class="bp-icon-xs" viewBox="0 0 24 24" fill="currentColor"><polygon points="6 3 20 12 6 21 6 3"/></svg>
      </span>
    <?php endif; ?>
  </a>

  <div class="bp-card-body flex-1">
    <?php if ( $cat_name ) : ?>
      <p class="bp-card-cat-name"><?php echo esc_html( $cat_name ); ?></p>
    <?php endif; ?>

    <h3 class="bp-card-title">
      <a href="<?php the_permalink(); ?>"><?php the_title(); ?></a>
    </h3>

    <?php if ( $short ) : ?>
      <p class="bp-card-excerpt line-clamp-2"><?php echo esc_html( $short ); ?></p>
    <?php endif; ?>

    <div class="bp-card-pricing bp-mt">
      <?php if ( $price ) : ?>
        <span class="bp-price"><?php echo esc_html( $price ); ?></span>
        <?php if ( $unit ) : ?><span class="bp-unit">/ <?php echo esc_html( $unit ); ?></span><?php endif; ?>
      <?php else : ?>
        <span class="bp-price-ask"><?php esc_html_e( 'Price on request', 'brickpoint' ); ?></span>
      <?php endif; ?>
    </div>
    <?php if ( $price_label ) : ?>
      <p class="bp-price-sub"><?php echo esc_html( $price_label ); ?></p>
    <?php endif; ?>

    <div class="bp-card-cta bp-mt">
      <a href="<?php the_permalink(); ?>" class="btn-ghost btn-sm">
        <span><?php esc_html_e( 'View Product', 'brickpoint' ); ?></span>
      </a>
      <a href="<?php echo esc_url( bp_whatsapp_url( $inquiry_text ) ); ?>" target="_blank" rel="noopener" class="btn-whatsapp btn-sm">
        <svg class="bp-icon-xs" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/></svg>
        <span><?php esc_html_e( 'WhatsApp', 'brickpoint' ); ?></span>
      </a>
    </div>
  </div>
</article>
"""

files["template-parts/video-card.php"] = """<?php
/**
 * Video Card template part
 *
 * @package BrickPoint
 */

if ( ! defined( 'ABSPATH' ) ) {
  exit;
}

$id = get_the_ID();
$dur = bp_meta( $id, '_bpv_duration', '' );
$feat = bp_meta( $id, '_bpv_featured', '0' );

$terms = get_the_terms( $id, 'bp_video_category' );
$cat_name = ( $terms && ! is_wp_error( $terms ) ) ? $terms[0]->name : '';
?>
<a href="<?php the_permalink(); ?>" class="bp-card card-hover group bp-video-card">
  <div class="bp-card-media img-zoom bp-video-thumb">
    <?php if ( has_post_thumbnail() ) : ?>
      <?php the_post_thumbnail( 'bp-card' ); ?>
    <?php else : ?>
      <img src="<?php echo esc_url( bp_asset_image_url( 'drone-poster.png' ) ); ?>" alt="<?php the_title_attribute(); ?>" />
    <?php endif; ?>
    <div class="bp-video-thumb-overlay"></div>
    <span class="bp-play-btn">
      <svg class="bp-icon-sm" viewBox="0 0 24 24" fill="currentColor"><polygon points="6 3 20 12 6 21 6 3"/></svg>
    </span>
    <?php if ( $dur ) : ?>
      <span class="bp-duration"><?php echo esc_html( $dur ); ?></span>
    <?php endif; ?>
    <?php if ( $feat === '1' ) : ?>
      <span class="bp-feat"><?php esc_html_e( 'Featured', 'brickpoint' ); ?></span>
    <?php endif; ?>
  </div>
  <div class="bp-card-body">
    <?php if ( $cat_name ) : ?>
      <p class="bp-card-cat-name"><?php echo esc_html( $cat_name ); ?></p>
    <?php endif; ?>
    <h3 class="bp-card-title"><?php the_title(); ?></h3>
    <p class="bp-card-excerpt line-clamp-2"><?php echo esc_html( get_the_excerpt() ); ?></p>
  </div>
</a>
"""

files["template-parts/project-card.php"] = """<?php
/**
 * Project Card template part
 *
 * @package BrickPoint
 */

if ( ! defined( 'ABSPATH' ) ) {
  exit;
}

$id = get_the_ID();
$loc = bp_meta( $id, '_bpp_location', 'Lahore' );
$status = bp_meta( $id, '_bpp_status', 'Illustrative construction reference' );
?>
<a href="<?php echo esc_url( home_url( '/projects' ) ); ?>" class="bp-card card-hover group">
  <div class="bp-card-media img-zoom">
    <?php if ( has_post_thumbnail() ) : ?>
      <?php the_post_thumbnail( 'bp-card' ); ?>
    <?php else : ?>
      <img src="<?php echo esc_url( bp_asset_image_url( 'villa1.png' ) ); ?>" alt="<?php the_title_attribute(); ?>" />
    <?php endif; ?>
    <span class="bp-illus-badge"><?php echo esc_html( $status ); ?></span>
  </div>
  <div class="bp-card-body">
    <p class="bp-card-loc"><?php echo esc_html( $loc ); ?></p>
    <h3 class="bp-card-title"><?php the_title(); ?></h3>
  </div>
</a>
"""

files["template-parts/location-card.php"] = """<?php
/**
 * Location Card template part
 *
 * @package BrickPoint
 */

if ( ! defined( 'ABSPATH' ) ) {
  exit;
}

$id = get_the_ID();
$addr = bp_meta( $id, '_bpl_address', '' );
$maps = bp_meta( $id, '_bpl_maps_url', '' );
?>
<article class="bp-card card-hover group flex-col">
  <div class="bp-card-media img-zoom">
    <?php if ( has_post_thumbnail() ) : ?>
      <?php the_post_thumbnail( 'bp-card' ); ?>
    <?php else : ?>
      <img src="<?php echo esc_url( bp_asset_image_url( 'kiln.png' ) ); ?>" alt="<?php the_title_attribute(); ?>" />
    <?php endif; ?>
  </div>
  <div class="bp-card-body flex-1">
    <h3 class="bp-card-title"><?php the_title(); ?></h3>
    <?php if ( $addr ) : ?>
      <p class="bp-loc-item">
        <svg class="bp-icon-xs text-orange" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/></svg>
        <span><?php echo esc_html( $addr ); ?></span>
      </p>
    <?php endif; ?>
    <p class="bp-card-excerpt line-clamp-3"><?php echo esc_html( get_the_excerpt() ); ?></p>
    <div class="bp-card-cta bp-mt">
      <?php if ( $maps ) : ?>
        <a href="<?php echo esc_url( $maps ); ?>" target="_blank" rel="noopener" class="btn-dark btn-sm"><?php esc_html_e( 'Google Maps →', 'brickpoint' ); ?></a>
      <?php endif; ?>
      <a href="<?php echo esc_url( home_url( '/contact' ) ); ?>" class="btn-ghost btn-sm"><?php esc_html_e( 'Contact', 'brickpoint' ); ?></a>
    </div>
  </div>
</article>
"""

files["template-parts/social-links.php"] = """<?php
/**
 * Social Links template part
 *
 * @package BrickPoint
 */

if ( ! defined( 'ABSPATH' ) ) {
  exit;
}
?>
<div class="bp-social">
  <a href="<?php echo esc_url( bp_option( 'bp_social_facebook', 'https://www.facebook.com/brickpoint.pk/' ) ); ?>" target="_blank" rel="noopener" aria-label="Facebook">
    <svg class="bp-icon-sm" viewBox="0 0 24 24" fill="currentColor"><path d="M13.5 21v-7h2.4l.4-3h-2.8V9.1c0-.9.3-1.5 1.6-1.5h1.3V4.9c-.3 0-1.1-.1-2-.1-2 0-3.4 1.2-3.4 3.5V11H7.5v3H10v7h3.5Z"/></svg>
  </a>
  <a href="<?php echo esc_url( bp_option( 'bp_social_instagram', 'https://www.instagram.com/brickpoint.pk/' ) ); ?>" target="_blank" rel="noopener" aria-label="Instagram">
    <svg class="bp-icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.2" cy="6.8" r="1.2" fill="currentColor" stroke="none"/></svg>
  </a>
  <a href="<?php echo esc_url( bp_option( 'bp_social_twitter', 'https://x.com/BrickPointPK' ) ); ?>" target="_blank" rel="noopener" aria-label="X Twitter">
    <svg class="bp-icon-sm" viewBox="0 0 24 24" fill="currentColor"><path d="M17.7 3H21l-7.1 8.2L22.2 21h-6.6l-5.1-6.1L4.6 21H1.3l7.6-8.7L1.8 3h6.7l4.6 5.6L17.7 3Zm-1.2 16h1.8L7.1 4.9H5.2L16.5 19Z"/></svg>
  </a>
  <a href="<?php echo esc_url( bp_option( 'bp_social_tiktok', 'https://www.tiktok.com/@brickpoint.pk/' ) ); ?>" target="_blank" rel="noopener" aria-label="TikTok">
    <span style="font-weight:900;font-size:0.9rem;">T</span>
  </a>
</div>
"""

files["template-parts/content.php"] = """<?php
/**
 * Standard Post Card template part
 *
 * @package BrickPoint
 */

if ( ! defined( 'ABSPATH' ) ) {
  exit;
}
?>
<article id="post-<?php the_ID(); ?>" <?php post_class( 'bp-card card-hover group flex-col' ); ?>>
  <?php if ( has_post_thumbnail() ) : ?>
    <a href="<?php the_permalink(); ?>" class="bp-card-media img-zoom">
      <?php the_post_thumbnail( 'bp-card' ); ?>
    </a>
  <?php endif; ?>
  <div class="bp-card-body flex-1">
    <div class="bp-post-meta-line">
      <span><?php echo esc_html( get_the_date() ); ?></span> &bull;
      <span><?php the_author(); ?></span>
    </div>
    <h3 class="bp-card-title"><a href="<?php the_permalink(); ?>"><?php the_title(); ?></a></h3>
    <p class="bp-card-excerpt line-clamp-2"><?php echo esc_html( get_the_excerpt() ); ?></p>
    <a href="<?php the_permalink(); ?>" class="bp-readmore-link bp-mt"><?php esc_html_e( 'Read Article →', 'brickpoint' ); ?></a>
  </div>
</article>
"""

files["languages/brickpoint.pot"] = """msgid ""
msgstr ""
"Project-Id-Version: BrickPoint 1.0.0\\n"
"Report-Msgid-Bugs-To: \\n"
"Last-Translator: \\n"
"Language-Team: \\n"
"MIME-Version: 1.0\\n"
"Content-Type: text/plain; charset=UTF-8\\n"
"Content-Transfer-Encoding: 8bit\\n"
"POT-Creation-Date: 2026-09-22T08:00:00+00:00\\n"

msgid "Building Strength. Delivering Quality. Shaping Tomorrow."
msgstr ""
msgid "Products"
msgstr ""
msgid "Videos"
msgstr ""
msgid "Projects"
msgstr ""
msgid "Locations"
msgstr ""
msgid "Order on WhatsApp"
msgstr ""
"""

# Write all core php files
for rel_path, content in files.items():
    full_path = os.path.join(DEST, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")

print(f"Wrote {len(files)} core PHP template files successfully.")

