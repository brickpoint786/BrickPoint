<?php
/**
 * Register Taxonomies: bp_product_category, bp_video_category
 *
 * @package BrickPoint
 */

if ( ! defined( 'ABSPATH' ) ) {
  exit;
}

function brickpoint_register_taxonomies() {
  // 1. PRODUCT CATEGORIES (bp_product_category)
  register_taxonomy( 'bp_product_category', array( 'bp_product' ), array(
    'labels' => array(
      'name'              => esc_html__( 'Product Categories', 'brickpoint' ),
      'singular_name'     => esc_html__( 'Product Category', 'brickpoint' ),
      'search_items'      => esc_html__( 'Search Categories', 'brickpoint' ),
      'all_items'         => esc_html__( 'All Categories', 'brickpoint' ),
      'parent_item'       => esc_html__( 'Parent Category', 'brickpoint' ),
      'parent_item_colon' => esc_html__( 'Parent Category:', 'brickpoint' ),
      'edit_item'         => esc_html__( 'Edit Category', 'brickpoint' ),
      'update_item'       => esc_html__( 'Update Category', 'brickpoint' ),
      'add_new_item'      => esc_html__( 'Add New Category', 'brickpoint' ),
      'new_item_name'     => esc_html__( 'New Category Name', 'brickpoint' ),
      'menu_name'         => esc_html__( 'Categories', 'brickpoint' ),
    ),
    'hierarchical'      => true,
    'show_ui'           => true,
    'show_admin_column' => true,
    'query_var'         => true,
    'rewrite'           => array( 'slug' => 'product-category', 'with_front' => false ),
    'show_in_rest'      => true,
  ) );

  // 2. VIDEO CATEGORIES (bp_video_category)
  register_taxonomy( 'bp_video_category', array( 'bp_video' ), array(
    'labels' => array(
      'name'              => esc_html__( 'Video Categories', 'brickpoint' ),
      'singular_name'     => esc_html__( 'Video Category', 'brickpoint' ),
      'search_items'      => esc_html__( 'Search Video Categories', 'brickpoint' ),
      'all_items'         => esc_html__( 'All Video Categories', 'brickpoint' ),
      'edit_item'         => esc_html__( 'Edit Video Category', 'brickpoint' ),
      'update_item'       => esc_html__( 'Update Video Category', 'brickpoint' ),
      'add_new_item'      => esc_html__( 'Add New Video Category', 'brickpoint' ),
      'new_item_name'     => esc_html__( 'New Video Category Name', 'brickpoint' ),
      'menu_name'         => esc_html__( 'Video Categories', 'brickpoint' ),
    ),
    'hierarchical'      => true,
    'show_ui'           => true,
    'show_admin_column' => true,
    'query_var'         => true,
    'rewrite'           => array( 'slug' => 'video-category', 'with_front' => false ),
    'show_in_rest'      => true,
  ) );
}
add_action( 'init', 'brickpoint_register_taxonomies' );
