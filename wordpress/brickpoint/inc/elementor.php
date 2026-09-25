<?php
/**
 * Elementor Free & Elementor Pro Theme Builder Integration
 *
 * @package BrickPoint
 */

if ( ! defined( 'ABSPATH' ) ) {
  exit;
}

/**
 * Register Elementor Pro Theme Builder locations:
 * - Header
 * - Footer
 * - Single (Product, Video, Project, Page, Post)
 * - Archive (Product Archive, Video Archive, Project Archive, Category Archive, Blog Archive)
 */
function brickpoint_register_elementor_locations( $elementor_theme_manager ) {
  $elementor_theme_manager->register_location( 'header' );
  $elementor_theme_manager->register_location( 'footer' );
  $elementor_theme_manager->register_location( 'single' );
  $elementor_theme_manager->register_location( 'archive' );
}
add_action( 'elementor/theme/register_locations', 'brickpoint_register_elementor_locations' );

/**
 * Add custom BrickPoint category to Elementor Free & Pro panel
 */
function brickpoint_add_elementor_widget_categories( $elements_manager ) {
  $elements_manager->add_category(
    'brickpoint-elements',
    array(
      'title' => esc_html__( 'BrickPoint Theme Elements', 'brickpoint' ),
      'icon'  => 'fa fa-cube',
    )
  );
}
add_action( 'elementor/elements/categories_registered', 'brickpoint_add_elementor_widget_categories' );

/**
 * Ensure Elementor supports our Custom Post Types by default
 */
function brickpoint_enable_cpt_elementor_support() {
  $cpts = get_option( 'elementor_cpt_support', array( 'page', 'post' ) );
  $wanted = array( 'bp_product', 'bp_video', 'bp_project', 'bp_location' );
  $updated = false;

  foreach ( $wanted as $cpt ) {
    if ( ! in_array( $cpt, $cpts, true ) ) {
      $cpts[] = $cpt;
      $updated = true;
    }
  }

  if ( $updated ) {
    update_option( 'elementor_cpt_support', $cpts );
  }
}
add_action( 'after_switch_theme', 'brickpoint_enable_cpt_elementor_support' );
