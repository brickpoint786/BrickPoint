<?php
/**
 * Theme setup functions
 *
 * @package BrickPoint
 */

if ( ! defined( 'ABSPATH' ) ) {
  exit;
}

if ( ! function_exists( 'brickpoint_setup' ) ) :
  function brickpoint_setup() {
    // Make theme available for translation
    load_theme_textdomain( 'brickpoint', BRICKPOINT_DIR . '/languages' );

    // Add default posts and comments RSS feed links to head
    add_theme_support( 'automatic-feed-links' );

    // Let WordPress manage document title
    add_theme_support( 'title-tag' );

    // Enable support for Post Thumbnails on posts and pages
    add_theme_support( 'post-thumbnails' );
    set_post_thumbnail_size( 800, 500, true );
    add_image_size( 'bp-card', 600, 400, true );
    add_image_size( 'bp-square', 400, 400, true );
    add_image_size( 'bp-hero', 1920, 1080, true );

    // Register Navigation Menus
    register_nav_menus( array(
      'primary' => esc_html__( 'Primary Navigation Menu', 'brickpoint' ),
      'mobile'  => esc_html__( 'Mobile Navigation Menu', 'brickpoint' ),
      'footer'  => esc_html__( 'Footer Navigation Menu', 'brickpoint' ),
    ) );

    // Switch default core markup to HTML5
    add_theme_support( 'html5', array(
      'search-form',
      'comment-form',
      'comment-list',
      'gallery',
      'caption',
      'style',
      'script',
    ) );

    // Custom Logo support (WordPress native)
    add_theme_support( 'custom-logo', array(
      'height'      => 80,
      'width'       => 280,
      'flex-height' => true,
      'flex-width'  => true,
    ) );

    // Selective Refresh for widgets
    add_theme_support( 'customize-selective-refresh-widgets' );

    // Align wide & full
    add_theme_support( 'align-wide' );

    // Responsive embeds
    add_theme_support( 'responsive-embeds' );
  }
endif;
add_action( 'after_setup_theme', 'brickpoint_setup' );

/**
 * Set content width in pixels
 */
function brickpoint_content_width() {
  $GLOBALS['content_width'] = apply_filters( 'brickpoint_content_width', 1200 );
}
add_action( 'after_setup_theme', 'brickpoint_content_width', 0 );
