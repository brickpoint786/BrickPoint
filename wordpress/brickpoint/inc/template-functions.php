<?php
/**
 * Template Functions & Logo Handlers
 *
 * @package BrickPoint
 */

if ( ! defined( 'ABSPATH' ) ) {
  exit;
}

/**
 * Independent Header Logo renderer
 */
function brickpoint_header_logo() {
  $header_logo_id = get_theme_mod( 'bp_header_logo' );
  $header_logo_url = '';

  if ( $header_logo_id ) {
    $header_logo_url = wp_get_attachment_url( $header_logo_id );
  }

  if ( ! $header_logo_url ) {
    $custom_logo_id = get_theme_mod( 'custom_logo' );
    if ( $custom_logo_id ) {
      $header_logo_url = wp_get_attachment_url( $custom_logo_id );
    }
  }

  if ( ! $header_logo_url ) {
    $header_logo_url = BRICKPOINT_URI . '/assets/images/logo-header.png';
  }

  $h_desktop = get_theme_mod( 'bp_header_logo_height_desktop', 44 );
  $h_mobile  = get_theme_mod( 'bp_header_logo_height_mobile', 36 );
  ?>
  <a href="<?php echo esc_url( home_url( '/' ) ); ?>" class="bp-logo-link" rel="home">
    <img src="<?php echo esc_url( $header_logo_url ); ?>" alt="<?php bloginfo( 'name' ); ?>" class="bp-logo bp-header-logo-img" style="--bp-logo-h-desk: <?php echo intval( $h_desktop ); ?>px; --bp-logo-h-mob: <?php echo intval( $h_mobile ); ?>px;" />
  </a>
  <?php
}

/**
 * Independent Footer Logo renderer
 */
function brickpoint_footer_logo() {
  $footer_logo_id = get_theme_mod( 'bp_footer_logo' );
  $footer_logo_url = '';

  if ( $footer_logo_id ) {
    $footer_logo_url = wp_get_attachment_url( $footer_logo_id );
  }

  if ( ! $footer_logo_url ) {
    $footer_logo_url = BRICKPOINT_URI . '/assets/images/logo-footer.png';
  }

  if ( ! $footer_logo_url ) {
    $header_logo_id = get_theme_mod( 'bp_header_logo' );
    if ( $header_logo_id ) {
      $footer_logo_url = wp_get_attachment_url( $header_logo_id );
    }
  }

  $f_desktop = get_theme_mod( 'bp_footer_logo_height_desktop', 52 );
  $f_mobile  = get_theme_mod( 'bp_footer_logo_height_mobile', 42 );
  ?>
  <a href="<?php echo esc_url( home_url( '/' ) ); ?>" class="bp-footer-logo-link" rel="home">
    <img src="<?php echo esc_url( $footer_logo_url ); ?>" alt="<?php bloginfo( 'name' ); ?>" class="bp-footer-logo-img" style="--bp-flogo-h-desk: <?php echo intval( $f_desktop ); ?>px; --bp-flogo-h-mob: <?php echo intval( $f_mobile ); ?>px;" />
  </a>
  <?php
}

/**
 * Fallback Navigation Menus matching exact site layout
 */
function brickpoint_default_nav_menu() {
  ?>
  <ul class="bp-menu">
    <li><a href="<?php echo esc_url( home_url( '/' ) ); ?>"><?php esc_html_e( 'Home', 'brickpoint' ); ?></a></li>
    <li><a href="<?php echo esc_url( home_url( '/ss7-bricks' ) ); ?>" class="bp-highlight-menu-item"><?php esc_html_e( 'SS7 Bricks', 'brickpoint' ); ?></a></li>
    <li><a href="<?php echo esc_url( home_url( '/products' ) ); ?>"><?php esc_html_e( 'Products', 'brickpoint' ); ?></a></li>
    <li><a href="<?php echo esc_url( home_url( '/categories' ) ); ?>"><?php esc_html_e( 'Categories', 'brickpoint' ); ?></a></li>
    <li><a href="<?php echo esc_url( home_url( '/construction-materials' ) ); ?>"><?php esc_html_e( 'Materials', 'brickpoint' ); ?></a></li>
    <li><a href="<?php echo esc_url( home_url( '/videos' ) ); ?>"><?php esc_html_e( 'Videos', 'brickpoint' ); ?></a></li>
    <li><a href="<?php echo esc_url( home_url( '/projects' ) ); ?>"><?php esc_html_e( 'Projects', 'brickpoint' ); ?></a></li>
    <li><a href="<?php echo esc_url( home_url( '/about' ) ); ?>"><?php esc_html_e( 'About', 'brickpoint' ); ?></a></li>
    <li><a href="<?php echo esc_url( home_url( '/contact' ) ); ?>"><?php esc_html_e( 'Contact', 'brickpoint' ); ?></a></li>
  </ul>
  <?php
}

function brickpoint_mobile_default_menu() {
  ?>
  <ul class="bp-mobile-menu-list">
    <li><a href="<?php echo esc_url( home_url( '/' ) ); ?>"><?php esc_html_e( 'Home', 'brickpoint' ); ?></a></li>
    <li><a href="<?php echo esc_url( home_url( '/ss7-bricks' ) ); ?>"><?php esc_html_e( 'SS7 Bricks (Flagship)', 'brickpoint' ); ?></a></li>
    <li><a href="<?php echo esc_url( home_url( '/products' ) ); ?>"><?php esc_html_e( 'Products Catalogue', 'brickpoint' ); ?></a></li>
    <li><a href="<?php echo esc_url( home_url( '/categories' ) ); ?>"><?php esc_html_e( 'Product Categories', 'brickpoint' ); ?></a></li>
    <li><a href="<?php echo esc_url( home_url( '/construction-materials' ) ); ?>"><?php esc_html_e( 'Construction Materials', 'brickpoint' ); ?></a></li>
    <li><a href="<?php echo esc_url( home_url( '/videos' ) ); ?>"><?php esc_html_e( 'Inside BrickPoint (Videos)', 'brickpoint' ); ?></a></li>
    <li><a href="<?php echo esc_url( home_url( '/projects' ) ); ?>"><?php esc_html_e( 'Project References', 'brickpoint' ); ?></a></li>
    <li><a href="<?php echo esc_url( home_url( '/locations' ) ); ?>"><?php esc_html_e( 'Our Bhatta Locations', 'brickpoint' ); ?></a></li>
    <li><a href="<?php echo esc_url( home_url( '/about' ) ); ?>"><?php esc_html_e( 'About Us', 'brickpoint' ); ?></a></li>
    <li><a href="<?php echo esc_url( home_url( '/contact' ) ); ?>"><?php esc_html_e( 'Contact & Quotation', 'brickpoint' ); ?></a></li>
  </ul>
  <?php
}

/**
 * Custom Pagination Wrapper
 */
if ( ! function_exists( 'brickpoint_pagination' ) ) {
  function brickpoint_pagination() {
    the_posts_pagination( array(
      'mid_size'  => 2,
      'prev_text' => esc_html__( '&laquo; Previous', 'brickpoint' ),
      'next_text' => esc_html__( 'Next &raquo;', 'brickpoint' ),
    ) );
  }
}
