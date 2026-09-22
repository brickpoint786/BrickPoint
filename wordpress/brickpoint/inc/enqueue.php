<?php
/**
 * Enqueue scripts and styles
 *
 * @package BrickPoint
 */

if ( ! defined( 'ABSPATH' ) ) {
  exit;
}

function brickpoint_scripts() {
  // Main compiled / minified theme stylesheet
  wp_enqueue_style( 'brickpoint-theme', BRICKPOINT_URI . '/assets/css/theme.css', array(), BRICKPOINT_VERSION );

  // WordPress style.css metadata
  wp_enqueue_style( 'brickpoint-style', get_stylesheet_uri(), array( 'brickpoint-theme' ), BRICKPOINT_VERSION );

  // Main interactive frontend script
  wp_enqueue_script( 'brickpoint-main', BRICKPOINT_URI . '/assets/js/main.js', array(), BRICKPOINT_VERSION, true );

  // Localize script with AJAX URL and settings
  wp_localize_script( 'brickpoint-main', 'bpThemeConfig', array(
    'ajaxUrl'  => admin_url( 'admin-ajax.php' ),
    'homeUrl'  => home_url( '/' ),
    'themeUri' => BRICKPOINT_URI,
    'waPhone'  => bp_option( 'bp_whatsapp_number', '923152850818' ),
  ) );

  if ( is_singular() && comments_open() && get_option( 'thread_comments' ) ) {
    wp_enqueue_script( 'comment-reply' );
  }
}
add_action( 'wp_enqueue_scripts', 'brickpoint_scripts' );

/**
 * Enqueue Admin Scripts & Styles (for Demo Importer)
 */
function brickpoint_admin_scripts( $hook ) {
  if ( strpos( $hook, 'brickpoint-demo' ) !== false || strpos( $hook, 'brickpoint-settings' ) !== false ) {
    wp_enqueue_style( 'brickpoint-admin-css', BRICKPOINT_URI . '/assets/css/theme.css', array(), BRICKPOINT_VERSION );
    wp_enqueue_script( 'brickpoint-admin-js', BRICKPOINT_URI . '/assets/js/admin.js', array( 'jquery' ), BRICKPOINT_VERSION, true );
    wp_localize_script( 'brickpoint-admin-js', 'bpAdminConfig', array(
      'ajaxUrl' => admin_url( 'admin-ajax.php' ),
      'nonce'   => wp_create_nonce( 'bp_demo_import_nonce' ),
    ) );
  }
}
add_action( 'admin_enqueue_scripts', 'brickpoint_admin_scripts' );
