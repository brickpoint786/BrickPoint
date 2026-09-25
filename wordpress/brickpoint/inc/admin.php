<?php
if ( ! defined( 'ABSPATH' ) ) { exit; }

function brickpoint_admin_columns_product( $cols ) {
  $cols['bp_price'] = __( 'Price', 'brickpoint' );
  $cols['bp_featured'] = __( 'Featured', 'brickpoint' );
  return $cols;
}
add_filter( 'manage_bp_product_posts_columns', 'brickpoint_admin_columns_product' );
function brickpoint_admin_column_product( $col, $post_id ) {
  if ( $col === 'bp_price' ) { echo esc_html( bp_meta( $post_id, '_bp_price', '—' ) ); }
  if ( $col === 'bp_featured' ) { echo bp_meta( $post_id, '_bp_featured', '0' ) === '1' ? '★' : '—'; }
}
add_action( 'manage_bp_product_posts_custom_column', 'brickpoint_admin_column_product', 10, 2 );

function brickpoint_admin_notice() {
  if ( ! current_user_can( 'manage_options' ) ) { return; }
  if ( get_option( 'brickpoint_seeded' ) ) { return; }
  echo '<div class="notice notice-info"><p>' . esc_html__( 'BrickPoint: create your Product Categories and Video Categories under Products → Product Categories and Videos → Video Categories, then add products and videos. No WooCommerce needed.', 'brickpoint' ) . '</p></div>';
}
add_action( 'admin_notices', 'brickpoint_admin_notice' );

// Seed default categories once.
function brickpoint_seed_terms() {
  if ( get_option( 'brickpoint_seeded' ) ) { return; }
  $product_cats = array( 'Bricks', 'SS7 Bricks', 'Cement', 'Bajri / Crush', 'Sand / Rait', 'Steel', 'Electric Conduit Pipes', 'Plumbing Pipes and Fittings', 'Construction Chemicals', 'Insulation and Membrane', 'Cables and Wires', 'Paints', 'Lights', 'Switches and Sockets', 'Other Construction Materials' );
  foreach ( $product_cats as $name ) {
    if ( ! term_exists( $name, 'bp_product_category' ) ) { wp_insert_term( $name, 'bp_product_category' ); }
  }
  $video_cats = array( 'SS7 Bricks', 'Brick Manufacturing', 'Our Bhattas', 'Brick Quality', 'Construction Projects', 'Construction Materials', 'Cement', 'Bajri / Crush', 'Sand / Rait', 'Steel', 'Company / Brand', 'Promotional Videos', 'Product Videos', 'Behind the Scenes', 'Other Videos' );
  foreach ( $video_cats as $name ) {
    if ( ! term_exists( $name, 'bp_video_category' ) ) { wp_insert_term( $name, 'bp_video_category' ); }
  }
  update_option( 'brickpoint_seeded', 1 );
}
add_action( 'after_switch_theme', 'brickpoint_seed_terms' );
