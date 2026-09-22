<?php
/**
 * Register Custom Post Types: bp_product, bp_video, bp_project, bp_location
 *
 * @package BrickPoint
 */

if ( ! defined( 'ABSPATH' ) ) {
  exit;
}

function brickpoint_register_cpts() {
  // 1. PRODUCTS (bp_product)
  register_post_type( 'bp_product', array(
    'labels' => array(
      'name'               => esc_html__( 'Products', 'brickpoint' ),
      'singular_name'      => esc_html__( 'Product', 'brickpoint' ),
      'add_new'            => esc_html__( 'Add New Product', 'brickpoint' ),
      'add_new_item'       => esc_html__( 'Add New Product', 'brickpoint' ),
      'edit_item'          => esc_html__( 'Edit Product', 'brickpoint' ),
      'new_item'           => esc_html__( 'New Product', 'brickpoint' ),
      'view_item'          => esc_html__( 'View Product', 'brickpoint' ),
      'search_items'       => esc_html__( 'Search Products', 'brickpoint' ),
      'not_found'          => esc_html__( 'No products found', 'brickpoint' ),
      'not_found_in_trash' => esc_html__( 'No products in Trash', 'brickpoint' ),
    ),
    'public'              => true,
    'has_archive'         => 'products',
    'rewrite'             => array( 'slug' => 'product', 'with_front' => false ),
    'supports'            => array( 'title', 'editor', 'thumbnail', 'excerpt', 'custom-fields' ),
    'menu_icon'           => 'dashicons-cart',
    'show_in_rest'        => true,
    'show_in_elementor'   => true,
  ) );

  // 2. VIDEOS (bp_video)
  register_post_type( 'bp_video', array(
    'labels' => array(
      'name'               => esc_html__( 'Videos', 'brickpoint' ),
      'singular_name'      => esc_html__( 'Video', 'brickpoint' ),
      'add_new'            => esc_html__( 'Add New Video', 'brickpoint' ),
      'add_new_item'       => esc_html__( 'Add New Video', 'brickpoint' ),
      'edit_item'          => esc_html__( 'Edit Video', 'brickpoint' ),
      'view_item'          => esc_html__( 'View Video', 'brickpoint' ),
      'search_items'       => esc_html__( 'Search Videos', 'brickpoint' ),
      'not_found'          => esc_html__( 'No videos found', 'brickpoint' ),
    ),
    'public'              => true,
    'has_archive'         => 'videos',
    'rewrite'             => array( 'slug' => 'video', 'with_front' => false ),
    'supports'            => array( 'title', 'editor', 'thumbnail', 'excerpt', 'custom-fields' ),
    'menu_icon'           => 'dashicons-video-alt3',
    'show_in_rest'        => true,
    'show_in_elementor'   => true,
  ) );

  // 3. PROJECTS (bp_project)
  register_post_type( 'bp_project', array(
    'labels' => array(
      'name'               => esc_html__( 'Projects', 'brickpoint' ),
      'singular_name'      => esc_html__( 'Project', 'brickpoint' ),
      'add_new'            => esc_html__( 'Add New Project', 'brickpoint' ),
      'add_new_item'       => esc_html__( 'Add New Project', 'brickpoint' ),
      'edit_item'          => esc_html__( 'Edit Project', 'brickpoint' ),
      'view_item'          => esc_html__( 'View Project', 'brickpoint' ),
      'search_items'       => esc_html__( 'Search Projects', 'brickpoint' ),
      'not_found'          => esc_html__( 'No projects found', 'brickpoint' ),
    ),
    'public'              => true,
    'has_archive'         => 'projects',
    'rewrite'             => array( 'slug' => 'project', 'with_front' => false ),
    'supports'            => array( 'title', 'editor', 'thumbnail', 'excerpt', 'custom-fields' ),
    'menu_icon'           => 'dashicons-building',
    'show_in_rest'        => true,
    'show_in_elementor'   => true,
  ) );

  // 4. LOCATIONS (bp_location)
  register_post_type( 'bp_location', array(
    'labels' => array(
      'name'               => esc_html__( 'Locations', 'brickpoint' ),
      'singular_name'      => esc_html__( 'Location', 'brickpoint' ),
      'add_new'            => esc_html__( 'Add New Location', 'brickpoint' ),
      'add_new_item'       => esc_html__( 'Add New Location', 'brickpoint' ),
      'edit_item'          => esc_html__( 'Edit Location', 'brickpoint' ),
      'view_item'          => esc_html__( 'View Location', 'brickpoint' ),
      'search_items'       => esc_html__( 'Search Locations', 'brickpoint' ),
      'not_found'          => esc_html__( 'No locations found', 'brickpoint' ),
    ),
    'public'              => true,
    'has_archive'         => 'locations',
    'rewrite'             => array( 'slug' => 'location', 'with_front' => false ),
    'supports'            => array( 'title', 'editor', 'thumbnail', 'excerpt', 'custom-fields' ),
    'menu_icon'           => 'dashicons-location-alt',
    'show_in_rest'        => true,
    'show_in_elementor'   => true,
  ) );
}
add_action( 'init', 'brickpoint_register_cpts' );
