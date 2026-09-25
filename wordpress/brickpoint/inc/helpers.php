<?php
/**
 * Helper functions
 *
 * @package BrickPoint
 */

if ( ! defined( 'ABSPATH' ) ) {
  exit;
}

/**
 * Retrieve theme option with default fallback
 */
function bp_option( $key, $default = '' ) {
  $val = get_option( $key );
  if ( false === $val || '' === $val ) {
    $val = get_theme_mod( $key, $default );
  }
  return ( false !== $val && '' !== $val ) ? $val : $default;
}

/**
 * Retrieve post meta with default fallback
 */
function bp_meta( $post_id, $key, $default = '' ) {
  $val = get_post_meta( $post_id, $key, true );
  return ( '' !== $val && false !== $val ) ? $val : $default;
}

/**
 * Return URL to bundled image asset
 */
function bp_asset_image_url( $file ) {
  $custom = bp_option( 'bp_img_' . sanitize_key( $file ) );
  if ( $custom ) {
    return $custom;
  }
  return BRICKPOINT_URI . '/assets/images/' . $file;
}

/**
 * Return SVG icon path or content
 */
function bp_icon( $name ) {
  $path = BRICKPOINT_DIR . '/assets/icons/' . sanitize_key( $name ) . '.svg';
  if ( file_exists( $path ) ) {
    return file_get_contents( $path );
  }
  return '';
}
