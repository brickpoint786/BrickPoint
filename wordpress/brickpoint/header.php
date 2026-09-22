<?php
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
