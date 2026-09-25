import fs from "node:fs";
import path from "node:path";

const ROOT = path.join(process.cwd(), "wordpress", "brickpoint");
const files = {};

const add = (p, c) => { files[p] = c; };

/* ============ style.css ============ */
add("style.css", `/*
Theme Name: BrickPoint
Theme URI: https://brickpoint.pk/
Author: BrickPoint
Author URI: https://brickpoint.pk/
Description: Premium construction-materials theme for BrickPoint. Custom Products (bp_product) and Videos (bp_video) post types, WhatsApp inquiry system, locations, projects, Elementor widgets and Theme Builder support. No WooCommerce required.
Version: 1.0.0
Requires at least: 6.0
Tested up to: 6.7
Requires PHP: 7.4
License: GNU General Public License v2 or later
License URI: http://www.gnu.org/licenses/gpl-2.0.html
Text Domain: brickpoint
Tags: construction, bricks, business, responsive, custom-colors, featured-images, threaded-comments
*/
`);

/* ============ functions.php ============ */
add("functions.php", `<?php
/**
 * BrickPoint theme bootstrap.
 *
 * @package BrickPoint
 */
if ( ! defined( 'ABSPATH' ) ) { exit; }

define( 'BRICKPOINT_VERSION', '1.0.0' );
define( 'BRICKPOINT_DIR', get_template_directory() );
define( 'BRICKPOINT_URI', get_template_directory_uri() );

require BRICKPOINT_DIR . '/inc/setup.php';
require BRICKPOINT_DIR . '/inc/enqueue.php';
require BRICKPOINT_DIR . '/inc/helpers.php';
require BRICKPOINT_DIR . '/inc/template-functions.php';
require BRICKPOINT_DIR . '/inc/post-types.php';
require BRICKPOINT_DIR . '/inc/taxonomies.php';
require BRICKPOINT_DIR . '/inc/meta-fields.php';
require BRICKPOINT_DIR . '/inc/whatsapp.php';
require BRICKPOINT_DIR . '/inc/video-functions.php';
require BRICKPOINT_DIR . '/inc/project-functions.php';
require BRICKPOINT_DIR . '/inc/customizer.php';
require BRICKPOINT_DIR . '/inc/elementor.php';
require BRICKPOINT_DIR . '/inc/elementor-widgets.php';
require BRICKPOINT_DIR . '/inc/admin.php';
`);

/* ============ inc/setup.php ============ */
add("inc/setup.php", `<?php
if ( ! defined( 'ABSPATH' ) ) { exit; }

function brickpoint_setup() {
  load_theme_textdomain( 'brickpoint', BRICKPOINT_DIR . '/languages' );
  add_theme_support( 'title-tag' );
  add_theme_support( 'post-thumbnails' );
  add_theme_support( 'custom-logo', array( 'height' => 80, 'width' => 220, 'flex-height' => true, 'flex-width' => true ) );
  add_theme_support( 'html5', array( 'search-form', 'comment-form', 'comment-list', 'gallery', 'caption', 'style', 'script' ) );
  add_theme_support( 'customize-selective-refresh-widgets' );
  add_theme_support( 'responsive-embeds' );
  add_theme_support( 'editor-styles' );
  add_editor_style( 'assets/css/editor.css' );
  add_image_size( 'bp-card', 800, 600, true );
  add_image_size( 'bp-hero', 1600, 900, true );
  register_nav_menus( array(
    'primary' => __( 'Primary Menu', 'brickpoint' ),
    'footer'  => __( 'Footer Menu', 'brickpoint' ),
    'mobile'  => __( 'Mobile Menu', 'brickpoint' ),
  ) );
}
add_action( 'after_setup_theme', 'brickpoint_setup' );

function brickpoint_content_width() {
  $GLOBALS['content_width'] = apply_filters( 'brickpoint_content_width', 1200 );
}
add_action( 'after_setup_theme', 'brickpoint_content_width', 0 );

function brickpoint_widgets_init() {
  register_sidebar( array(
    'name' => __( 'Blog Sidebar', 'brickpoint' ),
    'id' => 'sidebar-blog',
    'before_widget' => '<section class="widget %2$s">',
    'after_widget' => '</section>',
    'before_title' => '<h3 class="widget-title">',
    'after_title' => '</h3>',
  ) );
  for ( $i = 1; $i <= 4; $i++ ) {
    register_sidebar( array(
      'name' => sprintf( __( 'Footer Column %d', 'brickpoint' ), $i ),
      'id' => 'footer-' . $i,
      'before_widget' => '<div class="footer-widget %2$s">',
      'after_widget' => '</div>',
      'before_title' => '<h4 class="footer-widget-title">',
      'after_title' => '</h4>',
    ) );
  }
}
add_action( 'widgets_init', 'brickpoint_widgets_init' );
`);

/* ============ inc/enqueue.php ============ */
add("inc/enqueue.php", `<?php
if ( ! defined( 'ABSPATH' ) ) { exit; }

function brickpoint_assets() {
  $ver = BRICKPOINT_VERSION;
  wp_enqueue_style( 'brickpoint-fonts', 'https://fonts.googleapis.com/css2?family=Archivo:wght@600;700;800;900&family=Inter:wght@400;500;600;700&display=swap', array(), null );
  wp_enqueue_style( 'brickpoint-main', BRICKPOINT_URI . '/assets/css/main.css', array(), $ver );
  wp_enqueue_style( 'brickpoint-animations', BRICKPOINT_URI . '/assets/css/animations.css', array( 'brickpoint-main' ), $ver );
  wp_enqueue_style( 'brickpoint-responsive', BRICKPOINT_URI . '/assets/css/responsive.css', array( 'brickpoint-main' ), $ver );
  wp_enqueue_style( 'brickpoint-style', get_stylesheet_uri(), array( 'brickpoint-main' ), $ver );

  wp_enqueue_script( 'brickpoint-navigation', BRICKPOINT_URI . '/assets/js/navigation.js', array(), $ver, true );
  wp_enqueue_script( 'brickpoint-animations', BRICKPOINT_URI . '/assets/js/animations.js', array(), $ver, true );
  wp_enqueue_script( 'brickpoint-main', BRICKPOINT_URI . '/assets/js/main.js', array(), $ver, true );
  if ( is_singular( 'bp_product' ) || is_post_type_archive( 'bp_product' ) || is_tax( 'bp_product_category' ) ) {
    wp_enqueue_script( 'brickpoint-product', BRICKPOINT_URI . '/assets/js/product.js', array(), $ver, true );
  }
  if ( is_singular( 'bp_video' ) || is_post_type_archive( 'bp_video' ) || is_tax( 'bp_video_category' ) ) {
    wp_enqueue_script( 'brickpoint-video', BRICKPOINT_URI . '/assets/js/video.js', array(), $ver, true );
  }
  wp_enqueue_script( 'brickpoint-ajax', BRICKPOINT_URI . '/assets/js/ajax.js', array(), $ver, true );
  wp_localize_script( 'brickpoint-ajax', 'BRICKPOINT', array(
    'ajaxUrl' => admin_url( 'admin-ajax.php' ),
    'nonce'   => wp_create_nonce( 'brickpoint_nonce' ),
  ) );
  if ( is_singular() && comments_open() && get_option( 'thread_comments' ) ) {
    wp_enqueue_script( 'comment-reply' );
  }
}
add_action( 'wp_enqueue_scripts', 'brickpoint_assets' );
`);

/* ============ inc/helpers.php ============ */
add("inc/helpers.php", `<?php
if ( ! defined( 'ABSPATH' ) ) { exit; }

function bp_get( $key, $default = '' ) {
  $v = get_theme_mod( $key, $default );
  return $v !== '' ? $v : $default;
}
function bp_phone_display() { return bp_get( 'bp_phone_display', '0315 2850818' ); }
function bp_phone_intl() {
  $p = preg_replace( '/\\D/', '', bp_get( 'bp_whatsapp_number', '923152850818' ) );
  return $p ? $p : '923152850818';
}
function bp_email() { return sanitize_email( bp_get( 'bp_email', 'info@brickpoint.pk' ) ); }
function bp_social( $network ) {
  $defaults = array(
    'facebook'  => 'https://www.facebook.com/brickpoint.pk/',
    'instagram' => 'https://www.instagram.com/brickpoint.pk/',
    'twitter'   => 'https://x.com/BrickPointPK',
    'tiktok'    => 'https://www.tiktok.com/@brickpoint.pk/',
  );
  return esc_url( bp_get( 'bp_social_' . $network, isset( $defaults[ $network ] ) ? $defaults[ $network ] : '' ) );
}
function bp_meta( $post_id, $key, $default = '' ) {
  $v = get_post_meta( $post_id, $key, true );
  return ( $v === '' || $v === null ) ? $default : $v;
}
function bp_term_image( $term_id, $key = 'bp_cat_image' ) {
  return esc_url( get_term_meta( $term_id, $key, true ) );
}
function bp_breadcrumbs( $sep = ' / ' ) {
  $items = array( '<a href="' . esc_url( home_url( '/' ) ) . '">' . esc_html__( 'Home', 'brickpoint' ) . '</a>' );
  if ( is_singular( 'bp_product' ) ) {
    $items[] = '<a href="' . esc_url( get_post_type_archive_link( 'bp_product' ) ) . '">' . esc_html__( 'Products', 'brickpoint' ) . '</a>';
    $items[] = '<span>' . esc_html( get_the_title() ) . '</span>';
  } elseif ( is_singular( 'bp_video' ) ) {
    $items[] = '<a href="' . esc_url( get_post_type_archive_link( 'bp_video' ) ) . '">' . esc_html__( 'Videos', 'brickpoint' ) . '</a>';
    $items[] = '<span>' . esc_html( get_the_title() ) . '</span>';
  } elseif ( is_singular( 'post' ) ) {
    $items[] = '<a href="' . esc_url( get_permalink( get_option( 'page_for_posts' ) ) ) . '">' . esc_html__( 'Blog', 'brickpoint' ) . '</a>';
    $items[] = '<span>' . esc_html( get_the_title() ) . '</span>';
  } elseif ( is_archive() ) {
    $items[] = '<span>' . esc_html( get_the_archive_title() ) . '</span>';
  } elseif ( is_search() ) {
    $items[] = '<span>' . sprintf( esc_html__( 'Search: %s', 'brickpoint' ), esc_html( get_search_query() ) ) . '</span>';
  } else {
    $items[] = '<span>' . esc_html( get_the_title() ) . '</span>';
  }
  echo '<nav class="bp-breadcrumbs" aria-label="Breadcrumb">' . wp_kses_post( implode( esc_html( $sep ), $items ) ) . '</nav>';
}
function bp_excerpt( $length = 24 ) {
  $text = get_the_excerpt() ? get_the_excerpt() : get_the_content();
  return wp_trim_words( wp_strip_all_tags( $text ), absint( $length ), '…' );
}
`);

/* ============ inc/template-functions.php ============ */
add("inc/template-functions.php", `<?php
if ( ! defined( 'ABSPATH' ) ) { exit; }

function brickpoint_posted_meta() {
  printf(
    '<div class="entry-meta"><span class="byline">%1$s</span> <span class="posted-on">%2$s</span></div>',
    esc_html( get_the_author() ),
    esc_html( get_the_date() )
  );
}
function brickpoint_pagination() {
  the_posts_pagination( array(
    'mid_size'  => 2,
    'prev_text' => __( '← Previous', 'brickpoint' ),
    'next_text' => __( 'Next →', 'brickpoint' ),
  ) );
}
function brickpoint_related_posts( $count = 3 ) {
  $cats = wp_get_post_categories( get_the_ID() );
  if ( empty( $cats ) ) { return; }
  $q = new WP_Query( array(
    'category__in' => $cats, 'posts_per_page' => absint( $count ),
    'post__not_in' => array( get_the_ID() ), 'ignore_sticky_posts' => true,
  ) );
  if ( $q->have_posts() ) {
    echo '<section class="related-posts"><h2>' . esc_html__( 'Related Articles', 'brickpoint' ) . '</h2><div class="bp-grid cols-3">';
    while ( $q->have_posts() ) { $q->the_post(); get_template_part( 'template-parts/content' ); }
    echo '</div></section>';
  }
  wp_reset_postdata();
}
function brickpoint_hero_defaults() {
  return array(
    'title'    => __( 'Building Strength. Delivering Quality. Shaping Tomorrow.', 'brickpoint' ),
    'subtitle' => __( 'Premium bricks and reliable construction materials for homes, commercial developments, and large-scale building projects.', 'brickpoint' ),
  );
}
`);

/* ============ inc/post-types.php ============ */
add("inc/post-types.php", `<?php
if ( ! defined( 'ABSPATH' ) ) { exit; }

function brickpoint_register_post_types() {
  register_post_type( 'bp_product', array(
    'labels' => array(
      'name' => __( 'Products', 'brickpoint' ),
      'singular_name' => __( 'Product', 'brickpoint' ),
      'add_new_item' => __( 'Add New Product', 'brickpoint' ),
      'edit_item' => __( 'Edit Product', 'brickpoint' ),
    ),
    'public' => true, 'has_archive' => true,
    'rewrite' => array( 'slug' => 'products' ),
    'menu_icon' => 'dashicons-building',
    'supports' => array( 'title', 'editor', 'thumbnail', 'excerpt', 'revisions', 'page-attributes' ),
    'show_in_rest' => true,
  ) );
  register_post_type( 'bp_video', array(
    'labels' => array(
      'name' => __( 'Videos', 'brickpoint' ),
      'singular_name' => __( 'Video', 'brickpoint' ),
      'add_new_item' => __( 'Add New Video', 'brickpoint' ),
      'edit_item' => __( 'Edit Video', 'brickpoint' ),
    ),
    'public' => true, 'has_archive' => true,
    'rewrite' => array( 'slug' => 'videos' ),
    'menu_icon' => 'dashicons-video-alt3',
    'supports' => array( 'title', 'editor', 'thumbnail', 'excerpt', 'revisions' ),
    'show_in_rest' => true,
  ) );
  register_post_type( 'bp_project', array(
    'labels' => array(
      'name' => __( 'Projects', 'brickpoint' ),
      'singular_name' => __( 'Project', 'brickpoint' ),
      'add_new_item' => __( 'Add New Project', 'brickpoint' ),
      'edit_item' => __( 'Edit Project', 'brickpoint' ),
    ),
    'public' => true, 'has_archive' => true,
    'rewrite' => array( 'slug' => 'projects' ),
    'menu_icon' => 'dashicons-portfolio',
    'supports' => array( 'title', 'editor', 'thumbnail', 'excerpt', 'revisions', 'page-attributes' ),
    'show_in_rest' => true,
  ) );
  register_post_type( 'bp_location', array(
    'labels' => array(
      'name' => __( 'Locations', 'brickpoint' ),
      'singular_name' => __( 'Location', 'brickpoint' ),
      'add_new_item' => __( 'Add New Location', 'brickpoint' ),
      'edit_item' => __( 'Edit Location', 'brickpoint' ),
    ),
    'public' => true, 'has_archive' => true,
    'rewrite' => array( 'slug' => 'locations' ),
    'menu_icon' => 'dashicons-location-alt',
    'supports' => array( 'title', 'editor', 'thumbnail', 'excerpt' ),
    'show_in_rest' => true,
  ) );
}
add_action( 'init', 'brickpoint_register_post_types' );
`);

/* ============ inc/taxonomies.php ============ */
add("inc/taxonomies.php", `<?php
if ( ! defined( 'ABSPATH' ) ) { exit; }

function brickpoint_register_taxonomies() {
  register_taxonomy( 'bp_product_category', 'bp_product', array(
    'labels' => array( 'name' => __( 'Product Categories', 'brickpoint' ), 'singular_name' => __( 'Product Category', 'brickpoint' ) ),
    'public' => true, 'hierarchical' => true,
    'rewrite' => array( 'slug' => 'product-category' ),
    'show_in_rest' => true, 'show_admin_column' => true,
  ) );
  register_taxonomy( 'bp_video_category', 'bp_video', array(
    'labels' => array( 'name' => __( 'Video Categories', 'brickpoint' ), 'singular_name' => __( 'Video Category', 'brickpoint' ) ),
    'public' => true, 'hierarchical' => true,
    'rewrite' => array( 'slug' => 'video-category' ),
    'show_in_rest' => true, 'show_admin_column' => true,
  ) );
}
add_action( 'init', 'brickpoint_register_taxonomies' );

// Category image/icon/banner term meta fields.
function brickpoint_tax_meta_fields( $term = null ) {
  $id = $term ? $term->term_id : 0;
  $image  = $id ? get_term_meta( $id, 'bp_cat_image', true ) : '';
  $icon   = $id ? get_term_meta( $id, 'bp_cat_icon', true ) : '';
  $banner = $id ? get_term_meta( $id, 'bp_cat_banner', true ) : '';
  $video  = $id ? get_term_meta( $id, 'bp_cat_video', true ) : '';
  ?>
  <tr class="form-field"><th><label for="bp_cat_image"><?php esc_html_e( 'Category image URL', 'brickpoint' ); ?></label></th>
    <td><input type="url" name="bp_cat_image" id="bp_cat_image" value="<?php echo esc_attr( $image ); ?>" class="regular-text" />
    <p class="description"><?php esc_html_e( 'Paste an image URL from the Media Library.', 'brickpoint' ); ?></p></td></tr>
  <tr class="form-field"><th><label for="bp_cat_icon"><?php esc_html_e( 'Category icon (name)', 'brickpoint' ); ?></label></th>
    <td><input type="text" name="bp_cat_icon" id="bp_cat_icon" value="<?php echo esc_attr( $icon ); ?>" class="regular-text" /></td></tr>
  <tr class="form-field"><th><label for="bp_cat_banner"><?php esc_html_e( 'Category banner URL', 'brickpoint' ); ?></label></th>
    <td><input type="url" name="bp_cat_banner" id="bp_cat_banner" value="<?php echo esc_attr( $banner ); ?>" class="regular-text" /></td></tr>
  <tr class="form-field"><th><label for="bp_cat_video"><?php esc_html_e( 'Featured video URL (optional)', 'brickpoint' ); ?></label></th>
    <td><input type="url" name="bp_cat_video" id="bp_cat_video" value="<?php echo esc_attr( $video ); ?>" class="regular-text" /></td></tr>
  <?php
}
function brickpoint_tax_meta_save( $term_id ) {
  if ( ! current_user_can( 'manage_categories' ) ) { return; }
  foreach ( array( 'bp_cat_image', 'bp_cat_icon', 'bp_cat_banner', 'bp_cat_video' ) as $k ) {
    if ( isset( $_POST[ $k ] ) ) {
      update_term_meta( $term_id, $k, esc_url_raw( wp_unslash( $_POST[ $k ] ) ) );
    }
  }
}
add_action( 'bp_product_category_add_form_fields', 'brickpoint_tax_meta_fields' );
add_action( 'bp_product_category_edit_form_fields', 'brickpoint_tax_meta_fields' );
add_action( 'created_bp_product_category', 'brickpoint_tax_meta_save' );
add_action( 'edited_bp_product_category', 'brickpoint_tax_meta_save' );
add_action( 'bp_video_category_add_form_fields', 'brickpoint_tax_meta_fields' );
add_action( 'bp_video_category_edit_form_fields', 'brickpoint_tax_meta_fields' );
add_action( 'created_bp_video_category', 'brickpoint_tax_meta_save' );
add_action( 'edited_bp_video_category', 'brickpoint_tax_meta_save' );
`);

/* ============ inc/meta-fields.php ============ */
add("inc/meta-fields.php", `<?php
if ( ! defined( 'ABSPATH' ) ) { exit; }

function brickpoint_product_meta_fields() {
  return array(
    '_bp_price' => __( 'Product price (e.g. Rs. 14,500)', 'brickpoint' ),
    '_bp_price_label' => __( 'Price label (e.g. Market-competitive bulk pricing)', 'brickpoint' ),
    '_bp_unit' => __( 'Unit (e.g. 1000 bricks)', 'brickpoint' ),
    '_bp_availability' => __( 'Availability status', 'brickpoint' ),
    '_bp_badge' => __( 'Product badge (e.g. Best Seller)', 'brickpoint' ),
    '_bp_sku' => __( 'SKU / internal reference', 'brickpoint' ),
    '_bp_short' => __( 'Short description', 'brickpoint' ),
    '_bp_gallery' => __( 'Gallery image URLs (one per line)', 'brickpoint' ),
    '_bp_specs' => __( 'Specifications (one per line as Label: Value)', 'brickpoint' ),
    '_bp_features' => __( 'Features (one per line)', 'brickpoint' ),
    '_bp_video' => __( 'Product video URL (MP4 / YouTube / Vimeo)', 'brickpoint' ),
    '_bp_video_type' => __( 'Video type: mp4, youtube, vimeo', 'brickpoint' ),
    '_bp_brochure' => __( 'Brochure / PDF URL', 'brickpoint' ),
    '_bp_whatsapp' => __( 'Custom WhatsApp message (optional override)', 'brickpoint' ),
    '_bp_related' => __( 'Related product IDs (comma separated)', 'brickpoint' ),
  );
}
function brickpoint_add_meta_boxes() {
  add_meta_box( 'bp_product_details', __( 'Product Details', 'brickpoint' ), 'brickpoint_product_meta_box', 'bp_product', 'normal', 'high' );
  add_meta_box( 'bp_product_featured', __( 'Featured Product', 'brickpoint' ), 'brickpoint_featured_meta_box', 'bp_product', 'side', 'default' );
  add_meta_box( 'bp_video_details', __( 'Video Details', 'brickpoint' ), 'brickpoint_video_meta_box', 'bp_video', 'normal', 'high' );
  add_meta_box( 'bp_project_details', __( 'Project Details', 'brickpoint' ), 'brickpoint_project_meta_box', 'bp_project', 'normal', 'high' );
  add_meta_box( 'bp_location_details', __( 'Location Details', 'brickpoint' ), 'brickpoint_location_meta_box', 'bp_location', 'normal', 'high' );
}
add_action( 'add_meta_boxes', 'brickpoint_add_meta_boxes' );

function brickpoint_product_meta_box( $post ) {
  wp_nonce_field( 'bp_product_meta', 'bp_product_meta_nonce' );
  foreach ( brickpoint_product_meta_fields() as $key => $label ) {
    $val = get_post_meta( $post->ID, $key, true );
    echo '<p><label><strong>' . esc_html( $label ) . '</strong></label><br />';
    if ( in_array( $key, array( '_bp_short', '_bp_gallery', '_bp_specs', '_bp_features', '_bp_whatsapp' ), true ) ) {
      echo '<textarea name="' . esc_attr( $key ) . '" rows="3" style="width:100%">' . esc_textarea( $val ) . '</textarea></p>';
    } else {
      echo '<input type="text" name="' . esc_attr( $key ) . '" value="' . esc_attr( $val ) . '" style="width:100%" /></p>';
    }
  }
  echo '<p class="description">' . esc_html__( 'Tip: use the main content editor for the full description and the Featured Image panel for the main product image.', 'brickpoint' ) . '</p>';
}
function brickpoint_featured_meta_box( $post ) {
  $v = get_post_meta( $post->ID, '_bp_featured', true );
  echo '<label><input type="checkbox" name="_bp_featured" value="1"' . checked( $v, '1', false ) . ' /> ' . esc_html__( 'Mark as featured product', 'brickpoint' ) . '</label>';
}
function brickpoint_video_meta_box( $post ) {
  wp_nonce_field( 'bp_video_meta', 'bp_video_meta_nonce' );
  $fields = array(
    '_bpv_source' => __( 'Source type: mp4, youtube, vimeo, external', 'brickpoint' ),
    '_bpv_url' => __( 'Video URL (YouTube/Vimeo/embed/MP4)', 'brickpoint' ),
    '_bpv_file' => __( 'Self-hosted file URL (optional)', 'brickpoint' ),
    '_bpv_duration' => __( 'Duration (e.g. 2:30)', 'brickpoint' ),
    '_bpv_order' => __( 'Display order (number)', 'brickpoint' ),
    '_bpv_captions' => __( 'Captions/subtitles URL', 'brickpoint' ),
    '_bpv_related_products' => __( 'Related product IDs (comma separated)', 'brickpoint' ),
    '_bpv_related_projects' => __( 'Related project IDs', 'brickpoint' ),
    '_bpv_related_locations' => __( 'Related location IDs', 'brickpoint' ),
  );
  foreach ( $fields as $key => $label ) {
    $val = get_post_meta( $post->ID, $key, true );
    echo '<p><label><strong>' . esc_html( $label ) . '</strong></label><br /><input type="text" name="' . esc_attr( $key ) . '" value="' . esc_attr( $val ) . '" style="width:100%" /></p>';
  }
  $f = get_post_meta( $post->ID, '_bpv_featured', true );
  echo '<p><label><input type="checkbox" name="_bpv_featured" value="1"' . checked( $f, '1', false ) . ' /> ' . esc_html__( 'Featured video', 'brickpoint' ) . '</label></p>';
}
function brickpoint_project_meta_box( $post ) {
  wp_nonce_field( 'bp_project_meta', 'bp_project_meta_nonce' );
  $fields = array(
    '_bpp_location' => __( 'Location (e.g. DHA Lahore)', 'brickpoint' ),
    '_bpp_category' => __( 'Project category', 'brickpoint' ),
    '_bpp_status' => __( 'Status (default: Illustrative construction reference)', 'brickpoint' ),
    '_bpp_gallery' => __( 'Gallery URLs (one per line)', 'brickpoint' ),
    '_bpp_video' => __( 'Project video URL', 'brickpoint' ),
    '_bpp_related' => __( 'Related product IDs', 'brickpoint' ),
  );
  foreach ( $fields as $key => $label ) {
    $val = get_post_meta( $post->ID, $key, true );
    echo '<p><label><strong>' . esc_html( $label ) . '</strong></label><br />';
    if ( $key === '_bpp_gallery' ) { echo '<textarea name="' . esc_attr( $key ) . '" rows="3" style="width:100%">' . esc_textarea( $val ) . '</textarea></p>'; }
    else { echo '<input type="text" name="' . esc_attr( $key ) . '" value="' . esc_attr( $val ) . '" style="width:100%" /></p>'; }
  }
  $f = get_post_meta( $post->ID, '_bpp_featured', true );
  $ill = get_post_meta( $post->ID, '_bpp_illustrative', true );
  if ( $ill === '' ) { $ill = '1'; }
  echo '<p><label><input type="checkbox" name="_bpp_featured" value="1"' . checked( $f, '1', false ) . ' /> ' . esc_html__( 'Featured project', 'brickpoint' ) . '</label></p>';
  echo '<p><label><input type="checkbox" name="_bpp_illustrative" value="1"' . checked( $ill, '1', false ) . ' /> ' . esc_html__( 'Illustrative / inspiration visual (not a claimed BrickPoint project)', 'brickpoint' ) . '</label></p>';
}
function brickpoint_location_meta_box( $post ) {
  wp_nonce_field( 'bp_location_meta', 'bp_location_meta_nonce' );
  $fields = array(
    '_bpl_address' => __( 'Address', 'brickpoint' ),
    '_bpl_maps' => __( 'Google Maps URL', 'brickpoint' ),
    '_bpl_phone' => __( 'Phone', 'brickpoint' ),
    '_bpl_hours' => __( 'Opening hours', 'brickpoint' ),
    '_bpl_video' => __( 'Related video URL (optional)', 'brickpoint' ),
    '_bpl_order' => __( 'Display order', 'brickpoint' ),
  );
  foreach ( $fields as $key => $label ) {
    $val = get_post_meta( $post->ID, $key, true );
    echo '<p><label><strong>' . esc_html( $label ) . '</strong></label><br /><input type="text" name="' . esc_attr( $key ) . '" value="' . esc_attr( $val ) . '" style="width:100%" /></p>';
  }
}

function brickpoint_save_meta( $post_id ) {
  if ( defined( 'DOING_AUTOSAVE' ) && DOING_AUTOSAVE ) { return; }
  $maps = array(
    'bp_product_meta' => array_merge( array_keys( brickpoint_product_meta_fields() ), array( '_bp_featured' ) ),
    'bp_video_meta' => array( '_bpv_source', '_bpv_url', '_bpv_file', '_bpv_duration', '_bpv_order', '_bpv_captions', '_bpv_related_products', '_bpv_related_projects', '_bpv_related_locations', '_bpv_featured' ),
    'bp_project_meta' => array( '_bpp_location', '_bpp_category', '_bpp_status', '_bpp_gallery', '_bpp_video', '_bpp_related', '_bpp_featured', '_bpp_illustrative' ),
    'bp_location_meta' => array( '_bpl_address', '_bpl_maps', '_bpl_phone', '_bpl_hours', '_bpl_video', '_bpl_order' ),
  );
  foreach ( $maps as $nonce => $keys ) {
    if ( ! isset( $_POST[ $nonce ] ) ) { continue; }
    if ( ! wp_verify_nonce( sanitize_text_field( wp_unslash( $_POST[ $nonce ] ) ), $nonce ) ) { continue; }
    if ( ! current_user_can( 'edit_post', $post_id ) ) { continue; }
    foreach ( $keys as $k ) {
      if ( ! isset( $_POST[ $k ] ) ) {
        if ( in_array( $k, array( '_bp_featured', '_bpv_featured', '_bpp_featured', '_bpp_illustrative' ), true ) ) {
          update_post_meta( $post_id, $k, '0' );
        }
        continue;
      }
      $raw = wp_unslash( $_POST[ $k ] );
      if ( strpos( $k, '_url' ) !== false || $k === '_bp_video' || $k === '_bp_brochure' || $k === '_bpp_video' || $k === '_bpl_maps' || $k === '_bpv_file' || $k === '_bpv_captions' ) {
        update_post_meta( $post_id, $k, esc_url_raw( $raw ) );
      } else {
        update_post_meta( $post_id, $k, sanitize_textarea_field( $raw ) );
      }
    }
  }
}
add_action( 'save_post', 'brickpoint_save_meta' );
`);

/* ============ inc/whatsapp.php ============ */
add("inc/whatsapp.php", `<?php
if ( ! defined( 'ABSPATH' ) ) { exit; }

function bp_whatsapp_url( $message, $phone = null ) {
  if ( $phone === null ) { $phone = bp_phone_intl(); }
  return 'https://wa.me/' . preg_replace( '/\\D/', '', $phone ) . '?text=' . rawurlencode( $message );
}
function bp_product_whatsapp_message( $post_id ) {
  $custom = bp_meta( $post_id, '_bp_whatsapp', '' );
  if ( $custom ) { return $custom; }
  $cats = get_the_terms( $post_id, 'bp_product_category' );
  $cat = ( $cats && ! is_wp_error( $cats ) ) ? $cats[0]->name : '-';
  $price = bp_meta( $post_id, '_bp_price', '' );
  if ( ! $price ) { $price = __( 'Please quote', 'brickpoint' ); }
  $unit = bp_meta( $post_id, '_bp_unit', '-' );
  $lines = array(
    __( 'Assalam-o-Alaikum BrickPoint,', 'brickpoint' ), '',
    __( 'I am interested in the following product:', 'brickpoint' ), '',
    sprintf( __( 'Product: %s', 'brickpoint' ), get_the_title( $post_id ) ),
    sprintf( __( 'Category: %s', 'brickpoint' ), $cat ),
    sprintf( __( 'Price: %s', 'brickpoint' ), $price ),
    sprintf( __( 'Unit: %s', 'brickpoint' ), $unit ), '',
    __( 'Please share availability, delivery details, and final quotation.', 'brickpoint' ), '',
    __( 'Thank you.', 'brickpoint' ),
  );
  return implode( "\\n", $lines );
}
function bp_category_whatsapp_message( $cat_name ) {
  return implode( "\\n", array(
    __( 'Assalam-o-Alaikum BrickPoint,', 'brickpoint' ), '',
    sprintf( __( 'I want a quotation for: %s', 'brickpoint' ), $cat_name ), '',
    __( 'Please share price, availability and delivery details.', 'brickpoint' ), '',
    __( 'Thank you.', 'brickpoint' ),
  ) );
}
function bp_whatsapp_button( $message, $label = null, $class = 'btn-whatsapp' ) {
  if ( $label === null ) { $label = __( 'Order on WhatsApp', 'brickpoint' ); }
  return '<a class="' . esc_attr( $class ) . '" target="_blank" rel="noopener" href="' . esc_url( bp_whatsapp_url( $message ) ) . '">' . esc_html( $label ) . '</a>';
}
`);

/* ============ inc/video-functions.php ============ */
add("inc/video-functions.php", `<?php
if ( ! defined( 'ABSPATH' ) ) { exit; }

function bp_video_source( $post_id ) {
  $s = bp_meta( $post_id, '_bpv_source', 'mp4' );
  return in_array( $s, array( 'mp4', 'youtube', 'vimeo', 'external' ), true ) ? $s : 'mp4';
}
function bp_video_embed_html( $post_id, $args = array() ) {
  $source = bp_video_source( $post_id );
  $url = bp_meta( $post_id, '_bpv_url', '' );
  $file = bp_meta( $post_id, '_bpv_file', '' );
  $poster = get_the_post_thumbnail_url( $post_id, 'bp-hero' );
  $a = wp_parse_args( $args, array( 'autoplay' => false, 'muted' => true, 'loop' => false, 'controls' => true ) );
  if ( $source === 'youtube' || $source === 'vimeo' ) {
    if ( ! $url ) { return ''; }
    $src = esc_url( $url );
    if ( strpos( $src, 'youtube.com/watch' ) !== false ) {
      parse_str( (string) wp_parse_url( $src, PHP_URL_QUERY ), $qv );
      if ( ! empty( $qv['v'] ) ) { $src = 'https://www.youtube.com/embed/' . sanitize_text_field( $qv['v'] ); }
    } elseif ( strpos( $src, 'youtu.be/' ) !== false ) {
      $code = trim( (string) wp_parse_url( $src, PHP_URL_PATH ), '/' );
      $src = 'https://www.youtube.com/embed/' . sanitize_text_field( $code );
    } elseif ( $source === 'vimeo' && strpos( $src, 'player.vimeo' ) === false ) {
      $parts = explode( '/', trim( (string) wp_parse_url( $src, PHP_URL_PATH ), '/' ) );
      $code = end( $parts );
      if ( is_numeric( $code ) ) { $src = 'https://player.vimeo.com/video/' . $code; }
    }
    return '<div class="bp-video-embed"><iframe src="' . esc_url( $src ) . '" title="' . esc_attr( get_the_title( $post_id ) ) . '" loading="lazy" allow="accelerometer; autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>';
  }
  $src = $file ? $file : $url;
  if ( ! $src ) { return ''; }
  $attrs = 'playsinline preload="metadata"';
  if ( $a['controls'] ) { $attrs .= ' controls'; }
  if ( $a['autoplay'] ) { $attrs .= ' autoplay muted'; }
  elseif ( $a['muted'] ) { $attrs .= ' muted'; }
  if ( $a['loop'] ) { $attrs .= ' loop'; }
  if ( $poster ) { $attrs .= ' poster="' . esc_url( $poster ) . '"'; }
  return '<video class="bp-video-player" ' . $attrs . '><source src="' . esc_url( $src ) . '" type="video/mp4" /></video>';
}
function bp_video_thumbnail_first( $post_id ) {
  // Lightbox-style: thumbnail + play button, loads player on click for performance.
  $thumb = get_the_post_thumbnail_url( $post_id, 'bp-card' );
  $title = get_the_title( $post_id );
  $url = get_permalink( $post_id );
  ob_start(); ?>
  <a class="bp-video-thumb" href="<?php echo esc_url( $url ); ?>" aria-label="<?php echo esc_attr( sprintf( __( 'Watch %s', 'brickpoint' ), $title ) ); ?>">
    <?php if ( $thumb ) : ?>
      <img src="<?php echo esc_url( $thumb ); ?>" alt="<?php echo esc_attr( $title ); ?>" loading="lazy" />
    <?php else : ?>
      <span class="bp-video-thumb-fallback"></span>
    <?php endif; ?>
    <span class="bp-play-btn" aria-hidden="true">▶</span>
  </a>
  <?php
  return ob_get_clean();
}
`);

/* ============ inc/project-functions.php ============ */
add("inc/project-functions.php", `<?php
if ( ! defined( 'ABSPATH' ) ) { exit; }

function bp_project_status( $post_id ) {
  $s = bp_meta( $post_id, '_bpp_status', '' );
  return $s ? $s : __( 'Illustrative construction reference', 'brickpoint' );
}
function bp_project_gallery( $post_id ) {
  $raw = bp_meta( $post_id, '_bpp_gallery', '' );
  if ( ! $raw ) { return array(); }
  return array_values( array_filter( array_map( 'trim', preg_split( '/\\r?\\n/', $raw ) ) ) );
}
function bp_locations_list( $args = array() ) {
  $a = wp_parse_args( $args, array( 'posts_per_page' => 20, 'orderby' => 'meta_value_num', 'meta_key' => '_bpl_order', 'order' => 'ASC' ) );
  return new WP_Query( array_merge( $a, array( 'post_type' => 'bp_location', 'post_status' => 'publish' ) ) );
}
`);

/* ============ inc/customizer.php ============ */
add("inc/customizer.php", `<?php
if ( ! defined( 'ABSPATH' ) ) { exit; }

function brickpoint_customize( $wp_customize ) {
  $wp_customize->add_section( 'bp_contact', array( 'title' => __( 'BrickPoint: Contact', 'brickpoint' ), 'priority' => 30 ) );
  $fields = array(
    'bp_phone_display' => array( __( 'Phone display', 'brickpoint' ), '0315 2850818', 'text' ),
    'bp_whatsapp_number' => array( __( 'WhatsApp number (intl, no +)', 'brickpoint' ), '923152850818', 'text' ),
    'bp_email' => array( __( 'Email', 'brickpoint' ), 'info@brickpoint.pk', 'email' ),
    'bp_address' => array( __( 'Company address', 'brickpoint' ), 'Lahore, Punjab, Pakistan', 'text' ),
    'bp_ceo' => array( __( 'CEO name', 'brickpoint' ), 'Syed Iftikhar Haider', 'text' ),
    'bp_sales' => array( __( 'Sales Manager name', 'brickpoint' ), 'Qasim Iqbal', 'text' ),
    'bp_default_wa' => array( __( 'Default WhatsApp message', 'brickpoint' ), 'Assalam-o-Alaikum BrickPoint, I need a quotation for construction materials.', 'textarea' ),
    'bp_copyright' => array( __( 'Footer copyright', 'brickpoint' ), '© BrickPoint. All rights reserved.', 'text' ),
  );
  foreach ( $fields as $key => $def ) {
    list( $label, $default, $type ) = $def;
    $wp_customize->add_setting( $key, array( 'default' => $default, 'sanitize_callback' => ( $type === 'email' ? 'sanitize_email' : ( $type === 'textarea' ? 'sanitize_textarea_field' : 'sanitize_text_field' ) ) ) );
    $ctl = $type === 'textarea' ? 'WP_Customize_Control' : ( $type === 'email' ? 'WP_Customize_Control' : 'WP_Customize_Control' );
    $wp_customize->add_control( new $ctl( $wp_customize, $key, array( 'label' => $label, 'section' => 'bp_contact', 'type' => $type ) ) );
  }

  $wp_customize->add_section( 'bp_social', array( 'title' => __( 'BrickPoint: Social Links', 'brickpoint' ), 'priority' => 31 ) );
  foreach ( array( 'facebook' => 'Facebook URL', 'instagram' => 'Instagram URL', 'twitter' => 'X / Twitter URL', 'tiktok' => 'TikTok URL' ) as $net => $label ) {
    $defaults = array(
      'facebook' => 'https://www.facebook.com/brickpoint.pk/', 'instagram' => 'https://www.instagram.com/brickpoint.pk/',
      'twitter' => 'https://x.com/BrickPointPK', 'tiktok' => 'https://www.tiktok.com/@brickpoint.pk/',
    );
    $wp_customize->add_setting( 'bp_social_' . $net, array( 'default' => $defaults[ $net ], 'sanitize_callback' => 'esc_url_raw' ) );
    $wp_customize->add_control( 'bp_social_' . $net, array( 'label' => __( $label, 'brickpoint' ), 'section' => 'bp_social', 'type' => 'url' ) );
  }

  $wp_customize->add_section( 'bp_hero', array( 'title' => __( 'BrickPoint: Hero Video', 'brickpoint' ), 'priority' => 32 ) );
  $hero = array(
    'bp_hero_video' => __( 'Hero video file/URL (MP4)', 'brickpoint' ),
    'bp_hero_poster' => __( 'Hero poster image URL', 'brickpoint' ),
    'bp_hero_overlay' => __( 'Hero overlay opacity (0-90)', 'brickpoint' ),
  );
  foreach ( $hero as $key => $label ) {
    $wp_customize->add_setting( $key, array( 'default' => '', 'sanitize_callback' => ( $key === 'bp_hero_overlay' ? 'absint' : 'esc_url_raw' ) ) );
    $wp_customize->add_control( $key, array( 'label' => $label, 'section' => 'bp_hero', 'type' => ( $key === 'bp_hero_overlay' ? 'number' : 'url' ) ) );
  }
  $wp_customize->add_setting( 'bp_hero_video_pos', array( 'default' => 'right', 'sanitize_callback' => 'sanitize_text_field' ) );
  $wp_customize->add_control( 'bp_hero_video_pos', array( 'label' => __( 'Hero video position', 'brickpoint' ), 'section' => 'bp_hero', 'type' => 'select', 'choices' => array( 'right' => 'Right', 'background' => 'Background', 'below' => 'Below content' ) ) );

  $wp_customize->add_section( 'bp_colors', array( 'title' => __( 'BrickPoint: Colors & Design', 'brickpoint' ), 'priority' => 33 ) );
  foreach ( array(
    'bp_primary' => array( __( 'Primary color', 'brickpoint' ), '#c2410c' ),
    'bp_secondary' => array( __( 'Secondary / ink', 'brickpoint' ), '#141210' ),
    'bp_accent' => array( __( 'Accent color', 'brickpoint' ), '#ea580c' ),
  ) as $key => $def ) {
    $wp_customize->add_setting( $key, array( 'default' => $def[1], 'sanitize_callback' => 'sanitize_hex_color' ) );
    $wp_customize->add_control( new WP_Customize_Color_Control( $wp_customize, $key, array( 'label' => $def[0], 'section' => 'bp_colors' ) ) );
  }
  $wp_customize->add_setting( 'bp_radius', array( 'default' => '18', 'sanitize_callback' => 'absint' ) );
  $wp_customize->add_control( 'bp_radius', array( 'label' => __( 'Card border radius (px)', 'brickpoint' ), 'section' => 'bp_colors', 'type' => 'number' ) );
  $wp_customize->add_setting( 'bp_container', array( 'default' => '1200', 'sanitize_callback' => 'absint' ) );
  $wp_customize->add_control( 'bp_container', array( 'label' => __( 'Container width (px)', 'brickpoint' ), 'section' => 'bp_colors', 'type' => 'number' ) );
}
add_action( 'customize_register', 'brickpoint_customize' );

function brickpoint_css_vars() {
  $primary = get_theme_mod( 'bp_primary', '#c2410c' );
  $secondary = get_theme_mod( 'bp_secondary', '#141210' );
  $accent = get_theme_mod( 'bp_accent', '#ea580c' );
  $radius = absint( get_theme_mod( 'bp_radius', 18 ) );
  $container = absint( get_theme_mod( 'bp_container', 1200 ) );
  $css = sprintf(
    ':root{--bp-brick:%s;--bp-ink:%s;--bp-ember:%s;--bp-radius:%dpx;--bp-container:%dpx;}',
    esc_attr( $primary ), esc_attr( $secondary ), esc_attr( $accent ), $radius, $container
  );
  wp_add_inline_style( 'brickpoint-main', $css );
}
add_action( 'wp_enqueue_scripts', 'brickpoint_css_vars', 20 );
`);

/* ============ inc/elementor.php ============ */
add("inc/elementor.php", `<?php
if ( ! defined( 'ABSPATH' ) ) { exit; }

function brickpoint_elementor_support() {
  add_theme_support( 'elementor' );
  add_theme_support( 'elementor-theme-builder' );
  // Declare header/footer/single/archive locations for Elementor Pro Theme Builder.
  add_theme_support( 'elementor-pro-locations' );
}
add_action( 'after_setup_theme', 'brickpoint_elementor_support' );

// Render Elementor Pro header/footer locations when available.
function brickpoint_do_location( $location ) {
  if ( function_exists( 'elementor_theme_do_location' ) && elementor_theme_do_location( $location ) ) {
    return true;
  }
  return false;
}
`);

/* ============ inc/elementor-widgets.php ============ */
add("inc/elementor-widgets.php", `<?php
if ( ! defined( 'ABSPATH' ) ) { exit; }

function brickpoint_elementor_category( $elements_manager ) {
  $elements_manager->add_category( 'brickpoint', array( 'title' => __( 'BrickPoint', 'brickpoint' ), 'icon' => 'fa fa-cube' ) );
}
add_action( 'elementor/elements/categories_registered', 'brickpoint_elementor_category' );

function brickpoint_register_elementor_widgets( $widgets_manager ) {
  $dir = BRICKPOINT_DIR . '/elementor/widgets/';
  $widgets = array(
    'product-grid.php', 'product-categories.php', 'product-price.php',
    'whatsapp-button.php', 'video-grid.php', 'video-card.php',
    'project-grid.php', 'location-cards.php', 'social-links.php',
  );
  foreach ( $widgets as $file ) {
    $path = $dir . $file;
    if ( file_exists( $path ) ) { require_once $path; }
  }
  $classes = array(
    'BrickPoint_Product_Grid', 'BrickPoint_Product_Categories', 'BrickPoint_Product_Price',
    'BrickPoint_WhatsApp_Button', 'BrickPoint_Video_Grid', 'BrickPoint_Video_Card',
    'BrickPoint_Project_Grid', 'BrickPoint_Location_Cards', 'BrickPoint_Social_Links',
  );
  foreach ( $classes as $class ) {
    if ( class_exists( $class ) ) { $widgets_manager->register( new $class() ); }
  }
}
add_action( 'elementor/widgets/register', 'brickpoint_register_elementor_widgets' );
`);

/* ============ inc/admin.php ============ */
add("inc/admin.php", `<?php
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
`);

/* ============ header.php / footer.php ============ */
add("header.php", `<?php if ( ! defined( 'ABSPATH' ) ) { exit; } ?><!DOCTYPE html>
<html <?php language_attributes(); ?>>
<head>
<meta charset="<?php bloginfo( 'charset' ); ?>">
<meta name="viewport" content="width=device-width, initial-scale=1">
<?php wp_head(); ?>
</head>
<body <?php body_class(); ?>>
<?php wp_body_open(); ?>
<?php if ( function_exists( 'brickpoint_do_location' ) && brickpoint_do_location( 'header' ) ) : ?>
<?php else : ?>
<div class="bp-topbar">
  <div class="bp-container bp-topbar-inner">
    <span class="bp-topbar-phone"><?php echo esc_html( bp_phone_display() ); ?></span>
    <span class="bp-topbar-units"><?php esc_html_e( 'Masha Allah Bricks Co. • Fine Bricks Co. • SS7 Bricks', 'brickpoint' ); ?></span>
    <span class="bp-topbar-links">
      <a href="<?php echo esc_url( get_post_type_archive_link( 'bp_location' ) ); ?>"><?php esc_html_e( 'Our Bhattas', 'brickpoint' ); ?></a>
      <a href="<?php echo esc_url( get_post_type_archive_link( 'bp_video' ) ); ?>"><?php esc_html_e( 'Videos', 'brickpoint' ); ?></a>
    </span>
  </div>
</div>
<header class="bp-header" id="bpHeader">
  <div class="bp-container bp-header-inner">
    <div class="bp-brand">
      <?php if ( has_custom_logo() ) : the_custom_logo(); else : ?>
        <a class="bp-logo" href="<?php echo esc_url( home_url( '/' ) ); ?>">Brick<span>Point</span></a>
      <?php endif; ?>
    </div>
    <nav class="bp-nav" aria-label="<?php esc_attr_e( 'Main navigation', 'brickpoint' ); ?>">
      <?php wp_nav_menu( array( 'theme_location' => 'primary', 'container' => false, 'menu_class' => 'bp-menu', 'fallback_cb' => false ) ); ?>
    </nav>
    <div class="bp-header-cta">
      <a class="btn-whatsapp" target="_blank" rel="noopener" href="<?php echo esc_url( bp_whatsapp_url( bp_get( 'bp_default_wa', 'Assalam-o-Alaikum BrickPoint' ) ) ); ?>"><?php esc_html_e( 'WhatsApp Us', 'brickpoint' ); ?></a>
      <a class="btn-brick" href="<?php echo esc_url( home_url( '/contact/' ) ); ?>"><?php esc_html_e( 'Request Quote', 'brickpoint' ); ?></a>
    </div>
    <button class="bp-menu-toggle" id="bpMenuToggle" aria-label="<?php esc_attr_e( 'Open menu', 'brickpoint' ); ?>" aria-expanded="false">☰</button>
  </div>
  <div class="bp-mobile-menu" id="bpMobileMenu" hidden>
    <?php wp_nav_menu( array( 'theme_location' => 'mobile', 'container' => false, 'menu_class' => 'bp-menu-mobile', 'fallback_cb' => false ) ); ?>
    <?php wp_nav_menu( array( 'theme_location' => 'primary', 'container' => false, 'menu_class' => 'bp-menu-mobile', 'fallback_cb' => false ) ); ?>
    <div class="bp-mobile-cta">
      <a class="btn-whatsapp" target="_blank" rel="noopener" href="<?php echo esc_url( bp_whatsapp_url( bp_get( 'bp_default_wa', 'Assalam-o-Alaikum BrickPoint' ) ) ); ?>"><?php esc_html_e( 'WhatsApp Us', 'brickpoint' ); ?></a>
    </div>
  </div>
</header>
<?php endif; ?>
<main id="main" class="bp-main">
`);

add("footer.php", `<?php if ( ! defined( 'ABSPATH' ) ) { exit; } ?>
</main>
<?php if ( function_exists( 'brickpoint_do_location' ) && brickpoint_do_location( 'footer' ) ) : ?>
<?php else : ?>
<footer class="bp-footer">
  <div class="bp-container bp-footer-grid">
    <div class="bp-footer-brand">
      <?php if ( has_custom_logo() ) : the_custom_logo(); else : ?>
        <p class="bp-logo">Brick<span>Point</span></p>
      <?php endif; ?>
      <p><?php esc_html_e( 'Premium bricks and reliable construction materials for homes, commercial developments, and large-scale building projects.', 'brickpoint' ); ?></p>
      <p class="bp-footer-contact"><?php echo esc_html( bp_phone_display() ); ?> • <?php echo esc_html( bp_email() ); ?></p>
      <?php get_template_part( 'template-parts/social-links' ); ?>
    </div>
    <div class="bp-footer-col">
      <h4><?php esc_html_e( 'Products', 'brickpoint' ); ?></h4>
      <?php $pcats = get_terms( array( 'taxonomy' => 'bp_product_category', 'number' => 6, 'hide_empty' => false ) );
      if ( $pcats && ! is_wp_error( $pcats ) ) { echo '<ul>'; foreach ( $pcats as $t ) { echo '<li><a href="' . esc_url( get_term_link( $t ) ) . '">' . esc_html( $t->name ) . '</a></li>'; } echo '</ul>'; } ?>
    </div>
    <div class="bp-footer-col">
      <h4><?php esc_html_e( 'Company', 'brickpoint' ); ?></h4>
      <?php wp_nav_menu( array( 'theme_location' => 'footer', 'container' => false, 'menu_class' => 'bp-footer-menu', 'fallback_cb' => false ) ); ?>
    </div>
    <div class="bp-footer-col">
      <h4><?php esc_html_e( 'Get a Quotation', 'brickpoint' ); ?></h4>
      <p><?php esc_html_e( 'Send your material list on WhatsApp for availability and final quotation.', 'brickpoint' ); ?></p>
      <a class="btn-whatsapp" target="_blank" rel="noopener" href="<?php echo esc_url( bp_whatsapp_url( bp_get( 'bp_default_wa', 'Assalam-o-Alaikum BrickPoint' ) ) ); ?>"><?php esc_html_e( 'Chat on WhatsApp', 'brickpoint' ); ?></a>
    </div>
  </div>
  <div class="bp-footer-bottom">
    <div class="bp-container bp-footer-bottom-inner">
      <span><?php echo esc_html( bp_get( 'bp_copyright', '© BrickPoint. All rights reserved.' ) ); ?></span>
      <span class="bp-footer-legal">
        <a href="<?php echo esc_url( home_url( '/privacy-policy/' ) ); ?>"><?php esc_html_e( 'Privacy Policy', 'brickpoint' ); ?></a>
        <a href="<?php echo esc_url( home_url( '/terms-and-conditions/' ) ); ?>"><?php esc_html_e( 'Terms & Conditions', 'brickpoint' ); ?></a>
      </span>
    </div>
  </div>
</footer>
<a class="bp-float-wa" target="_blank" rel="noopener" aria-label="<?php esc_attr_e( 'Chat on WhatsApp', 'brickpoint' ); ?>" href="<?php echo esc_url( bp_whatsapp_url( bp_get( 'bp_default_wa', 'Assalam-o-Alaikum BrickPoint' ) ) ); ?>">✆</a>
<?php endif; ?>
<?php wp_footer(); ?>
</body>
</html>
`);

/* ============ core templates ============ */
add("index.php", `<?php if ( ! defined( 'ABSPATH' ) ) { exit; }
get_header(); ?>
<div class="bp-container bp-section">
  <?php if ( have_posts() ) : ?>
    <div class="bp-grid cols-3">
      <?php while ( have_posts() ) : the_post(); get_template_part( 'template-parts/content' ); endwhile; ?>
    </div>
    <?php brickpoint_pagination(); ?>
  <?php else : ?>
    <p><?php esc_html_e( 'No content found.', 'brickpoint' ); ?></p>
  <?php endif; ?>
</div>
<?php get_footer(); ?>
`);

add("front-page.php", `<?php if ( ! defined( 'ABSPATH' ) ) { exit; }
get_header();
if ( function_exists( 'brickpoint_do_location' ) && brickpoint_do_location( 'single' ) ) { get_footer(); return; }
get_template_part( 'template-parts/hero' ); ?>
<section class="bp-section"><div class="bp-container">
  <p class="bp-eyebrow"><?php esc_html_e( 'Why BrickPoint', 'brickpoint' ); ?></p>
  <h2><?php esc_html_e( 'A construction-materials partner you can build on', 'brickpoint' ); ?></h2>
  <div class="bp-grid cols-4 bp-mt">
    <?php $cats = get_terms( array( 'taxonomy' => 'bp_product_category', 'number' => 8, 'hide_empty' => false ) );
    if ( $cats && ! is_wp_error( $cats ) ) : foreach ( $cats as $t ) :
      $img = get_term_meta( $t->term_id, 'bp_cat_image', true ); ?>
      <a class="bp-cat-card" href="<?php echo esc_url( get_term_link( $t ) ); ?>">
        <?php if ( $img ) : ?><img src="<?php echo esc_url( $img ); ?>" alt="<?php echo esc_attr( $t->name ); ?>" loading="lazy" /><?php endif; ?>
        <span class="bp-cat-card-body"><strong><?php echo esc_html( $t->name ); ?></strong></span>
      </a>
    <?php endforeach; endif; ?>
  </div>
</div></section>
<section class="bp-section bp-dark"><div class="bp-container">
  <p class="bp-eyebrow"><?php esc_html_e( 'Featured Products', 'brickpoint' ); ?></p>
  <h2><?php esc_html_e( 'Materials contractors ask for by name', 'brickpoint' ); ?></h2>
  <div class="bp-grid cols-4 bp-mt">
    <?php $q = new WP_Query( array( 'post_type' => 'bp_product', 'posts_per_page' => 8, 'meta_key' => '_bp_featured', 'meta_value' => '1' ) );
    if ( ! $q->have_posts() ) { $q = new WP_Query( array( 'post_type' => 'bp_product', 'posts_per_page' => 8 ) ); }
    while ( $q->have_posts() ) : $q->the_post(); get_template_part( 'template-parts/product-card' ); endwhile; wp_reset_postdata(); ?>
  </div>
  <p class="bp-center bp-mt"><a class="btn-brick" href="<?php echo esc_url( get_post_type_archive_link( 'bp_product' ) ); ?>"><?php esc_html_e( 'Browse All Products', 'brickpoint' ); ?></a></p>
</div></section>
<section class="bp-section"><div class="bp-container">
  <p class="bp-eyebrow"><?php esc_html_e( 'Inside BrickPoint', 'brickpoint' ); ?></p>
  <h2><?php esc_html_e( 'See the Strength Behind Every Brick', 'brickpoint' ); ?></h2>
  <div class="bp-grid cols-3 bp-mt">
    <?php $v = new WP_Query( array( 'post_type' => 'bp_video', 'posts_per_page' => 3 ) );
    while ( $v->have_posts() ) : $v->the_post(); get_template_part( 'template-parts/video-card' ); endwhile; wp_reset_postdata(); ?>
  </div>
  <p class="bp-center bp-mt"><a class="btn-ghost" href="<?php echo esc_url( get_post_type_archive_link( 'bp_video' ) ); ?>"><?php esc_html_e( 'View All Videos', 'brickpoint' ); ?></a></p>
</div></section>
<?php if ( have_posts() ) : while ( have_posts() ) : the_post(); the_content(); endwhile; endif; ?>
<?php get_footer(); ?>
`);

add("home.php", `<?php if ( ! defined( 'ABSPATH' ) ) { exit; }
get_header(); ?>
<div class="bp-pagehead"><div class="bp-container">
  <p class="bp-eyebrow"><?php esc_html_e( 'Guides & Updates', 'brickpoint' ); ?></p>
  <h1><?php esc_html_e( 'Blog', 'brickpoint' ); ?></h1>
  <?php get_search_form(); ?>
</div></div>
<div class="bp-container bp-section"><div class="bp-grid cols-3">
  <?php while ( have_posts() ) : the_post(); get_template_part( 'template-parts/content' ); endwhile; ?>
</div><?php brickpoint_pagination(); ?></div>
<?php get_footer(); ?>
`);

add("page.php", `<?php if ( ! defined( 'ABSPATH' ) ) { exit; }
get_header();
while ( have_posts() ) : the_post(); ?>
<article id="post-<?php the_ID(); ?>" <?php post_class( 'bp-page' ); ?>>
  <div class="bp-pagehead"><div class="bp-container">
    <h1><?php the_title(); ?></h1>
    <?php bp_breadcrumbs(); ?>
  </div></div>
  <div class="bp-container bp-section bp-entry"><?php the_content(); ?></div>
</article>
<?php endwhile; get_footer(); ?>
`);

add("single.php", `<?php if ( ! defined( 'ABSPATH' ) ) { exit; }
get_header();
while ( have_posts() ) : the_post(); ?>
<article <?php post_class( 'bp-single' ); ?>>
  <div class="bp-pagehead"><div class="bp-container">
    <h1><?php the_title(); ?></h1>
    <?php brickpoint_posted_meta(); bp_breadcrumbs(); ?>
  </div></div>
  <div class="bp-container bp-narrow bp-section">
    <?php if ( has_post_thumbnail() ) : the_post_thumbnail( 'bp-hero', array( 'class' => 'bp-single-img' ) ); endif; ?>
    <div class="bp-entry"><?php the_content(); ?></div>
    <?php the_tags( '<p class="bp-tags">', ', ', '</p>' ); ?>
    <?php if ( comments_open() || get_comments_number() ) : comments_template(); endif; ?>
  </div>
  <div class="bp-container"><?php brickpoint_related_posts(); ?></div>
</article>
<?php endwhile; get_footer(); ?>
`);

add("archive.php", `<?php if ( ! defined( 'ABSPATH' ) ) { exit; }
get_header(); ?>
<div class="bp-pagehead"><div class="bp-container">
  <h1><?php the_archive_title(); ?></h1>
  <?php the_archive_description( '<p>', '</p>' ); ?>
</div></div>
<div class="bp-container bp-section"><div class="bp-grid cols-3">
  <?php while ( have_posts() ) : the_post(); get_template_part( 'template-parts/content' ); endwhile; ?>
</div><?php brickpoint_pagination(); ?></div>
<?php get_footer(); ?>
`);

add("search.php", `<?php if ( ! defined( 'ABSPATH' ) ) { exit; }
get_header(); ?>
<div class="bp-pagehead"><div class="bp-container">
  <h1><?php printf( esc_html__( 'Search: %s', 'brickpoint' ), esc_html( get_search_query() ) ); ?></h1>
  <?php get_search_form(); ?>
</div></div>
<div class="bp-container bp-section">
  <?php if ( have_posts() ) : ?><div class="bp-grid cols-3">
    <?php while ( have_posts() ) : the_post(); get_template_part( 'template-parts/content' ); endwhile; ?>
  </div><?php brickpoint_pagination(); else : ?>
    <p><?php esc_html_e( 'No results found. Try different keywords.', 'brickpoint' ); ?></p>
  <?php endif; ?>
</div>
<?php get_footer(); ?>
`);

add("404.php", `<?php if ( ! defined( 'ABSPATH' ) ) { exit; }
get_header(); ?>
<div class="bp-container bp-section bp-center">
  <p class="bp-eyebrow"><?php esc_html_e( 'Error 404', 'brickpoint' ); ?></p>
  <h1><?php esc_html_e( 'Page not found', 'brickpoint' ); ?></h1>
  <p><?php esc_html_e( 'The page you requested could not be found. Try the homepage or product catalogue.', 'brickpoint' ); ?></p>
  <p class="bp-mt"><a class="btn-brick" href="<?php echo esc_url( home_url( '/' ) ); ?>"><?php esc_html_e( 'Back to Home', 'brickpoint' ); ?></a>
  <a class="btn-ghost" href="<?php echo esc_url( get_post_type_archive_link( 'bp_product' ) ); ?>"><?php esc_html_e( 'Browse Products', 'brickpoint' ); ?></a></p>
</div>
<?php get_footer(); ?>
`);

add("rtl.css", `/* BrickPoint RTL support */
body{direction:rtl;text-align:right;}
.bp-header-inner,.bp-footer-grid{direction:rtl;}
`);

add("readme.txt", `=== BrickPoint ===
Contributors: brickpoint
Tags: construction, bricks, business, responsive
Requires at least: 6.0
Tested up to: 6.7
Requires PHP: 7.4
Stable tag: 1.0.0
License: GPLv2 or later

Premium construction-materials theme with custom Products, Videos, Projects and Locations. WhatsApp inquiry system. No WooCommerce.

== Installation ==
1. Upload brickpoint.zip via Appearance > Themes > Add New > Upload Theme.
2. Activate the theme.
3. Default product & video categories are created automatically.
4. Set menus under Appearance > Menus (Primary, Footer, Mobile).
5. Configure contact, social links and hero video under Appearance > Customize > BrickPoint.
6. Optionally install Elementor (free) for page editing; Elementor Pro enables Theme Builder header/footer/single templates.
7. Add Products (Products > Add New), Videos, Projects and Locations from the admin menu.

== WhatsApp ==
Set the WhatsApp number under Customize > BrickPoint: Contact. Every product generates a prefilled inquiry message automatically.

== Elementor widgets ==
BrickPoint category: Product Grid, Product Categories, Product Price, WhatsApp Button, Video Grid, Video Card, Project Grid, Location Cards, Social Links.

== Notes ==
No WooCommerce dependency. Project visuals should be labelled illustrative unless verified. Replace demo media with your own bhatta photography.
`);

/* ============ product/video templates ============ */
add("single-bp_product.php", `<?php if ( ! defined( 'ABSPATH' ) ) { exit; }
get_header();
while ( have_posts() ) : the_post();
  $id = get_the_ID();
  $price = bp_meta( $id, '_bp_price', '' ); $unit = bp_meta( $id, '_bp_unit', '' );
  $avail = bp_meta( $id, '_bp_availability', 'In Stock' ); $badge = bp_meta( $id, '_bp_badge', '' );
  $label = bp_meta( $id, '_bp_price_label', '' ); $sku = bp_meta( $id, '_bp_sku', '' );
  $video = bp_meta( $id, '_bp_video', '' ); $vtype = bp_meta( $id, '_bp_video_type', 'mp4' );
  $brochure = bp_meta( $id, '_bp_brochure', '' );
  $cats = get_the_terms( $id, 'bp_product_category' );
  $catname = ( $cats && ! is_wp_error( $cats ) ) ? $cats[0]->name : '';
  $msg = bp_product_whatsapp_message( $id );
  $gallery = array_values( array_filter( array_map( 'trim', preg_split( '/\\r?\\n/', bp_meta( $id, '_bp_gallery', '' ) ) ) ) );
  $specs = array_values( array_filter( array_map( 'trim', preg_split( '/\\r?\\n/', bp_meta( $id, '_bp_specs', '' ) ) ) ) );
  $features = array_values( array_filter( array_map( 'trim', preg_split( '/\\r?\\n/', bp_meta( $id, '_bp_features', '' ) ) ) ) );
?>
<article class="bp-product-single">
  <div class="bp-container bp-crumbs"><?php bp_breadcrumbs(); ?></div>
  <div class="bp-container bp-product-layout">
    <div class="bp-product-media">
      <?php if ( has_post_thumbnail() ) : the_post_thumbnail( 'bp-hero', array( 'class' => 'bp-product-img' ) ); endif; ?>
      <?php if ( $gallery ) : ?><div class="bp-thumbs"><?php foreach ( $gallery as $g ) : ?><img src="<?php echo esc_url( $g ); ?>" alt="" loading="lazy" /><?php endforeach; ?></div><?php endif; ?>
      <?php if ( $video ) : ?><div class="bp-product-video">
        <?php if ( $vtype === 'youtube' || $vtype === 'vimeo' ) : ?>
          <iframe src="<?php echo esc_url( $video ); ?>" loading="lazy" allowfullscreen></iframe>
        <?php else : ?>
          <video controls playsinline preload="metadata" src="<?php echo esc_url( $video ); ?>"></video>
        <?php endif; ?>
      </div><?php endif; ?>
    </div>
    <div class="bp-product-info">
      <?php if ( $catname ) : ?><p class="bp-eyebrow"><?php echo esc_html( $catname ); ?></p><?php endif; ?>
      <h1><?php the_title(); ?></h1>
      <?php $short = bp_meta( $id, '_bp_short', '' ); if ( $short ) : ?><p class="bp-short"><?php echo esc_html( $short ); ?></p><?php endif; ?>
      <p class="bp-price-row">
        <?php if ( $price ) : ?><span class="bp-price"><?php echo esc_html( $price ); ?></span><?php if ( $unit ) : ?><span class="bp-unit">/ <?php echo esc_html( $unit ); ?></span><?php endif; ?>
        <?php else : ?><span class="bp-price"><?php esc_html_e( 'Price on request', 'brickpoint' ); ?></span><?php endif; ?>
        <span class="bp-avail"><?php echo esc_html( $avail ); ?></span>
        <?php if ( $badge ) : ?><span class="bp-badge"><?php echo esc_html( $badge ); ?></span><?php endif; ?>
      </p>
      <?php if ( $label ) : ?><p class="bp-muted"><?php echo esc_html( $label ); ?></p><?php endif; ?>
      <?php if ( $sku ) : ?><p class="bp-muted">SKU: <strong><?php echo esc_html( $sku ); ?></strong></p><?php endif; ?>
      <div class="bp-product-cta">
        <a class="btn-whatsapp" target="_blank" rel="noopener" href="<?php echo esc_url( bp_whatsapp_url( $msg ) ); ?>"><?php esc_html_e( 'Request Quote on WhatsApp', 'brickpoint' ); ?></a>
        <a class="btn-dark" href="tel:<?php echo esc_attr( bp_phone_intl() ); ?>"><?php echo esc_html( bp_phone_display() ); ?></a>
        <a class="btn-brick" href="<?php echo esc_url( home_url( '/contact/' ) ); ?>"><?php esc_html_e( 'Request Quotation', 'brickpoint' ); ?></a>
      </div>
      <?php if ( $features ) : ?><div class="bp-box"><h3><?php esc_html_e( 'Key Features', 'brickpoint' ); ?></h3><ul><?php foreach ( $features as $f ) : ?><li><?php echo esc_html( $f ); ?></li><?php endforeach; ?></ul></div><?php endif; ?>
      <?php if ( $specs ) : ?><div class="bp-box"><h3><?php esc_html_e( 'Specifications', 'brickpoint' ); ?></h3><dl><?php foreach ( $specs as $s ) : $p = explode( ':', $s, 2 ); ?><div><dt><?php echo esc_html( trim( $p[0] ) ); ?></dt><dd><?php echo esc_html( isset( $p[1] ) ? trim( $p[1] ) : '' ); ?></dd></div><?php endforeach; ?></dl></div><?php endif; ?>
      <div class="bp-entry"><?php the_content(); ?></div>
      <?php if ( $brochure ) : ?><p><a class="btn-ghost" target="_blank" rel="noopener" href="<?php echo esc_url( $brochure ); ?>"><?php esc_html_e( 'Download Brochure (PDF)', 'brickpoint' ); ?></a></p><?php endif; ?>
    </div>
  </div>
  <div class="bp-container bp-section">
    <h2><?php esc_html_e( 'Related Products', 'brickpoint' ); ?></h2>
    <div class="bp-grid cols-4">
      <?php $rel = new WP_Query( array( 'post_type' => 'bp_product', 'posts_per_page' => 4, 'post__not_in' => array( $id ) ) );
      while ( $rel->have_posts() ) : $rel->the_post(); get_template_part( 'template-parts/product-card' ); endwhile; wp_reset_postdata(); ?>
    </div>
  </div>
</article>
<?php endwhile; get_footer(); ?>
`);

add("archive-bp_product.php", `<?php if ( ! defined( 'ABSPATH' ) ) { exit; }
get_header(); ?>
<div class="bp-pagehead"><div class="bp-container">
  <p class="bp-eyebrow"><?php esc_html_e( 'Catalogue', 'brickpoint' ); ?></p>
  <h1><?php esc_html_e( 'Products', 'brickpoint' ); ?></h1>
  <div class="bp-filters">
    <?php $cats = get_terms( array( 'taxonomy' => 'bp_product_category', 'hide_empty' => false ) );
    if ( $cats && ! is_wp_error( $cats ) ) : foreach ( $cats as $t ) : ?>
      <a href="<?php echo esc_url( get_term_link( $t ) ); ?>"><?php echo esc_html( $t->name ); ?></a>
    <?php endforeach; endif; ?>
  </div>
</div></div>
<div class="bp-container bp-section"><div class="bp-grid cols-4">
  <?php while ( have_posts() ) : the_post(); get_template_part( 'template-parts/product-card' ); endwhile; ?>
</div><?php brickpoint_pagination(); ?></div>
<?php get_footer(); ?>
`);

add("taxonomy-bp_product_category.php", `<?php if ( ! defined( 'ABSPATH' ) ) { exit; }
get_header();
$term = get_queried_object();
$banner = $term ? get_term_meta( $term->term_id, 'bp_cat_banner', true ) : '';
$video = $term ? get_term_meta( $term->term_id, 'bp_cat_video', true ) : '';
?>
<div class="bp-pagehead bp-pagehead-img" <?php if ( $banner ) : ?>style="background-image:url('<?php echo esc_url( $banner ); ?>')"<?php endif; ?>><div class="bp-container">
  <h1><?php single_term_title(); ?></h1>
  <?php the_archive_description( '<p>', '</p>' ); ?>
  <?php if ( $term ) : ?><p class="bp-mt"><a class="btn-whatsapp" target="_blank" rel="noopener" href="<?php echo esc_url( bp_whatsapp_url( bp_category_whatsapp_message( $term->name ) ) ); ?>"><?php printf( esc_html__( 'Get %s Quote', 'brickpoint' ), esc_html( $term->name ) ); ?></a></p><?php endif; ?>
</div></div>
<?php if ( $video ) : ?><div class="bp-container bp-section"><video class="bp-cat-video" controls playsinline preload="metadata" src="<?php echo esc_url( $video ); ?>"></video></div><?php endif; ?>
<div class="bp-container bp-section"><div class="bp-grid cols-4">
  <?php while ( have_posts() ) : the_post(); get_template_part( 'template-parts/product-card' ); endwhile; ?>
</div><?php brickpoint_pagination(); ?></div>
<?php get_footer(); ?>
`);

add("single-bp_video.php", `<?php if ( ! defined( 'ABSPATH' ) ) { exit; }
get_header();
while ( have_posts() ) : the_post(); $id = get_the_ID(); ?>
<article class="bp-video-single">
  <div class="bp-container bp-crumbs"><?php bp_breadcrumbs(); ?></div>
  <div class="bp-container bp-section">
    <?php echo bp_video_embed_html( $id, array( 'controls' => true ) ); // phpcs:ignore ?>
    <p class="bp-eyebrow bp-mt"><?php $t = get_the_terms( $id, 'bp_video_category' ); echo ( $t && ! is_wp_error( $t ) ) ? esc_html( $t[0]->name ) : ''; ?></p>
    <h1><?php the_title(); ?></h1>
    <div class="bp-entry"><?php the_content(); ?></div>
    <h2 class="bp-mt"><?php esc_html_e( 'More Videos', 'brickpoint' ); ?></h2>
    <div class="bp-grid cols-3">
      <?php $m = new WP_Query( array( 'post_type' => 'bp_video', 'posts_per_page' => 3, 'post__not_in' => array( $id ) ) );
      while ( $m->have_posts() ) : $m->the_post(); get_template_part( 'template-parts/video-card' ); endwhile; wp_reset_postdata(); ?>
    </div>
  </div>
</article>
<?php endwhile; get_footer(); ?>
`);

add("archive-bp_video.php", `<?php if ( ! defined( 'ABSPATH' ) ) { exit; }
get_header(); ?>
<div class="bp-pagehead"><div class="bp-container">
  <p class="bp-eyebrow"><?php esc_html_e( 'Video Library', 'brickpoint' ); ?></p>
  <h1><?php esc_html_e( 'Inside BrickPoint', 'brickpoint' ); ?></h1>
  <p><?php esc_html_e( 'Explore our products, production process, construction materials, projects, and company updates through video.', 'brickpoint' ); ?></p>
  <div class="bp-filters">
    <?php $cats = get_terms( array( 'taxonomy' => 'bp_video_category', 'hide_empty' => false ) );
    if ( $cats && ! is_wp_error( $cats ) ) : foreach ( $cats as $t ) : ?>
      <a href="<?php echo esc_url( get_term_link( $t ) ); ?>"><?php echo esc_html( $t->name ); ?></a>
    <?php endforeach; endif; ?>
  </div>
</div></div>
<div class="bp-container bp-section"><div class="bp-grid cols-3">
  <?php while ( have_posts() ) : the_post(); get_template_part( 'template-parts/video-card' ); endwhile; ?>
</div><?php brickpoint_pagination(); ?></div>
<?php get_footer(); ?>
`);

add("taxonomy-bp_video_category.php", `<?php if ( ! defined( 'ABSPATH' ) ) { exit; }
get_header(); ?>
<div class="bp-pagehead"><div class="bp-container">
  <p class="bp-eyebrow"><?php esc_html_e( 'Video Category', 'brickpoint' ); ?></p>
  <h1><?php single_term_title(); ?></h1>
  <?php the_archive_description( '<p>', '</p>' ); ?>
</div></div>
<div class="bp-container bp-section"><div class="bp-grid cols-3">
  <?php while ( have_posts() ) : the_post(); get_template_part( 'template-parts/video-card' ); endwhile; ?>
</div><?php brickpoint_pagination(); ?></div>
<?php get_footer(); ?>
`);

/* ============ template-parts ============ */
add("template-parts/content.php", `<?php if ( ! defined( 'ABSPATH' ) ) { exit; } ?>
<article id="post-<?php the_ID(); ?>" <?php post_class( 'bp-card' ); ?>>
  <a class="bp-card-media" href="<?php the_permalink(); ?>"><?php the_post_thumbnail( 'bp-card' ); ?></a>
  <div class="bp-card-body">
    <h3><a href="<?php the_permalink(); ?>"><?php the_title(); ?></a></h3>
    <p><?php echo esc_html( bp_excerpt( 20 ) ); ?></p>
    <?php brickpoint_posted_meta(); ?>
  </div>
</article>
`);

add("template-parts/content-product.php", `<?php if ( ! defined( 'ABSPATH' ) ) { exit; }
get_template_part( 'template-parts/product-card' ); ?>
`);

add("template-parts/content-video.php", `<?php if ( ! defined( 'ABSPATH' ) ) { exit; }
get_template_part( 'template-parts/video-card' ); ?>
`);

add("template-parts/content-project.php", `<?php if ( ! defined( 'ABSPATH' ) ) { exit; } ?>
<article class="bp-card">
  <a class="bp-card-media" href="<?php the_permalink(); ?>"><?php the_post_thumbnail( 'bp-card' ); ?>
    <span class="bp-illus"><?php echo esc_html( bp_project_status( get_the_ID() ) ); ?></span></a>
  <div class="bp-card-body">
    <p class="bp-eyebrow"><?php echo esc_html( bp_meta( get_the_ID(), '_bpp_location', '' ) ); ?></p>
    <h3><a href="<?php the_permalink(); ?>"><?php the_title(); ?></a></h3>
  </div>
</article>
`);

add("template-parts/hero.php", `<?php if ( ! defined( 'ABSPATH' ) ) { exit; }
$d = brickpoint_hero_defaults();
$video = bp_get( 'bp_hero_video', '' ); $poster = bp_get( 'bp_hero_poster', '' );
?>
<section class="bp-hero">
  <div class="bp-container bp-hero-grid">
    <div class="bp-hero-copy">
      <p class="bp-hero-kicker"><?php esc_html_e( 'Masha Allah • Fine Bricks • SS7', 'brickpoint' ); ?></p>
      <h1><?php echo esc_html( $d['title'] ); ?></h1>
      <p><?php echo esc_html( $d['subtitle'] ); ?></p>
      <p class="bp-hero-cta">
        <a class="btn-brick" href="<?php echo esc_url( get_post_type_archive_link( 'bp_product' ) ); ?>"><?php esc_html_e( 'Explore Products', 'brickpoint' ); ?></a>
        <a class="btn-ghost" href="<?php echo esc_url( home_url( '/contact/' ) ); ?>"><?php esc_html_e( 'Request a Quote', 'brickpoint' ); ?></a>
        <a class="btn-whatsapp" target="_blank" rel="noopener" href="<?php echo esc_url( bp_whatsapp_url( bp_get( 'bp_default_wa', 'Assalam-o-Alaikum BrickPoint' ) ) ); ?>"><?php esc_html_e( 'WhatsApp Us', 'brickpoint' ); ?></a>
      </p>
    </div>
    <div class="bp-hero-media">
      <?php if ( $video ) : ?>
        <video class="bp-hero-video" autoplay muted loop playsinline preload="metadata" <?php if ( $poster ) : ?>poster="<?php echo esc_url( $poster ); ?>"<?php endif; ?>>
          <source src="<?php echo esc_url( $video ); ?>" type="video/mp4" />
        </video>
      <?php elseif ( has_post_thumbnail() ) : the_post_thumbnail( 'bp-hero' ); endif; ?>
      <div class="bp-ss7-float"><div class="ss7-brick"><strong>SS7</strong><span><?php esc_html_e( 'Flagship Bricks', 'brickpoint' ); ?></span></div></div>
    </div>
  </div>
</section>
`);

add("template-parts/product-card.php", `<?php if ( ! defined( 'ABSPATH' ) ) { exit; }
$id = get_the_ID();
$price = bp_meta( $id, '_bp_price', '' ); $unit = bp_meta( $id, '_bp_unit', '' );
$avail = bp_meta( $id, '_bp_availability', '' ); $badge = bp_meta( $id, '_bp_badge', '' );
$cats = get_the_terms( $id, 'bp_product_category' );
$catname = ( $cats && ! is_wp_error( $cats ) ) ? $cats[0]->name : '';
?>
<article class="bp-card bp-product-card">
  <a class="bp-card-media" href="<?php the_permalink(); ?>">
    <?php the_post_thumbnail( 'bp-card' ); ?>
    <?php if ( $badge ) : ?><span class="bp-badge"><?php echo esc_html( $badge ); ?></span><?php endif; ?>
    <?php if ( $avail ) : ?><span class="bp-avail"><?php echo esc_html( $avail ); ?></span><?php endif; ?>
  </a>
  <div class="bp-card-body">
    <?php if ( $catname ) : ?><p class="bp-eyebrow"><?php echo esc_html( $catname ); ?></p><?php endif; ?>
    <h3><a href="<?php the_permalink(); ?>"><?php the_title(); ?></a></h3>
    <p class="bp-price-row"><?php if ( $price ) : ?><span class="bp-price"><?php echo esc_html( $price ); ?></span><?php if ( $unit ) : ?><span class="bp-unit">/ <?php echo esc_html( $unit ); ?></span><?php endif; ?><?php else : ?><span class="bp-price"><?php esc_html_e( 'Price on request', 'brickpoint' ); ?></span><?php endif; ?></p>
    <p class="bp-card-cta">
      <a class="btn-dark btn-sm" href="<?php the_permalink(); ?>"><?php esc_html_e( 'View Product', 'brickpoint' ); ?></a>
      <a class="btn-whatsapp btn-sm" target="_blank" rel="noopener" href="<?php echo esc_url( bp_whatsapp_url( bp_product_whatsapp_message( $id ) ) ); ?>"><?php esc_html_e( 'WhatsApp', 'brickpoint' ); ?></a>
    </p>
  </div>
</article>
`);

add("template-parts/video-card.php", `<?php if ( ! defined( 'ABSPATH' ) ) { exit; }
$id = get_the_ID();
$dur = bp_meta( $id, '_bpv_duration', '' );
$feat = bp_meta( $id, '_bpv_featured', '0' ) === '1';
$cats = get_the_terms( $id, 'bp_video_category' );
$catname = ( $cats && ! is_wp_error( $cats ) ) ? $cats[0]->name : '';
?>
<article class="bp-card bp-video-card">
  <a class="bp-card-media bp-video-thumb" href="<?php the_permalink(); ?>">
    <?php the_post_thumbnail( 'bp-card' ); ?>
    <span class="bp-play-btn" aria-hidden="true">▶</span>
    <?php if ( $dur ) : ?><span class="bp-duration"><?php echo esc_html( $dur ); ?></span><?php endif; ?>
    <?php if ( $feat ) : ?><span class="bp-feat"><?php esc_html_e( 'Featured', 'brickpoint' ); ?></span><?php endif; ?>
  </a>
  <div class="bp-card-body">
    <?php if ( $catname ) : ?><p class="bp-eyebrow"><?php echo esc_html( $catname ); ?></p><?php endif; ?>
    <h3><a href="<?php the_permalink(); ?>"><?php the_title(); ?></a></h3>
    <p><?php echo esc_html( bp_excerpt( 16 ) ); ?></p>
  </div>
</article>
`);

add("template-parts/social-links.php", `<?php if ( ! defined( 'ABSPATH' ) ) { exit; } ?>
<div class="bp-social">
  <a href="<?php echo bp_social( 'facebook' ); ?>" target="_blank" rel="noopener" aria-label="Facebook">f</a>
  <a href="<?php echo bp_social( 'instagram' ); ?>" target="_blank" rel="noopener" aria-label="Instagram">ig</a>
  <a href="<?php echo bp_social( 'twitter' ); ?>" target="_blank" rel="noopener" aria-label="X">x</a>
  <a href="<?php echo bp_social( 'tiktok' ); ?>" target="_blank" rel="noopener" aria-label="TikTok">t</a>
</div>
`);

/* ============ assets/css ============ */
add("assets/css/main.css", `:root{--bp-ink:#141210;--bp-charcoal:#1c1a17;--bp-brick:#c2410c;--bp-ember:#ea580c;--bp-sand:#f6f1ea;--bp-muted:#6b6560;--bp-radius:18px;--bp-container:1200px;}
*{box-sizing:border-box}body{margin:0;font-family:Inter,system-ui,sans-serif;background:#faf8f5;color:var(--bp-ink);overflow-x:hidden}
img{max-width:100%;height:auto}.bp-container{max-width:var(--bp-container);margin:0 auto;padding:0 1.25rem}
.bp-section{padding:3.5rem 0}.bp-mt{margin-top:1.5rem}.bp-center{text-align:center}.bp-narrow{max-width:800px}
.bp-eyebrow{font-size:.72rem;font-weight:800;text-transform:uppercase;letter-spacing:.2em;color:var(--bp-ember)}
h1,h2,h3{font-family:Archivo,Inter,sans-serif;letter-spacing:-.02em;line-height:1.15}
.bp-pagehead{background:var(--bp-ink);color:#fff;padding:3rem 0}.bp-pagehead h1{margin:.4rem 0}.bp-pagehead-img{background-size:cover;background-position:center}
.bp-topbar{background:#0f0e0c;color:rgba(255,255,255,.75);font-size:.75rem}.bp-topbar-inner{display:flex;gap:1rem;justify-content:space-between;padding:.5rem 1.25rem}.bp-topbar a{color:#fff}
.bp-header{position:sticky;top:0;z-index:50;background:rgba(20,18,16,.92);backdrop-filter:blur(12px);transition:box-shadow .3s}
.bp-header-inner{display:flex;align-items:center;gap:1rem;height:72px}.bp-logo{font-family:Archivo;font-weight:900;font-size:1.4rem;color:#fff;text-decoration:none}.bp-logo span{color:var(--bp-ember)}
.bp-menu{display:flex;gap:.25rem;list-style:none;margin:0;padding:0}.bp-menu a{color:rgba(255,255,255,.85);text-decoration:none;font-weight:600;font-size:.9rem;padding:.6rem .8rem;border-radius:.6rem}.bp-menu a:hover{background:rgba(255,255,255,.1);color:#fff}
.bp-header-cta{margin-left:auto;display:flex;gap:.5rem}.bp-menu-toggle{display:none;background:rgba(255,255,255,.1);color:#fff;border:0;border-radius:.7rem;width:44px;height:44px;font-size:1.2rem}
.btn-brick,.btn-dark,.btn-whatsapp,.btn-ghost{display:inline-flex;align-items:center;gap:.5rem;border-radius:.8rem;padding:.8rem 1.4rem;font-weight:700;font-size:.9rem;text-decoration:none;border:0;cursor:pointer}
.btn-brick{background:linear-gradient(135deg,var(--bp-ember),var(--bp-brick));color:#fff}.btn-dark{background:var(--bp-ink);color:#fff}.btn-whatsapp{background:#128c4b;color:#fff}.btn-ghost{border:1px solid rgba(0,0,0,.15);color:var(--bp-ink);background:#fff}.bp-dark .btn-ghost{border-color:rgba(255,255,255,.25);color:#fff;background:transparent}
.btn-sm{padding:.6rem .9rem;font-size:.78rem}
.bp-hero{background:var(--bp-ink);color:#fff;padding:4rem 0}.bp-hero-grid{display:grid;gap:2.5rem;grid-template-columns:1.05fr .95fr;align-items:center}.bp-hero h1{font-size:clamp(2.2rem,4.5vw,3.6rem);font-weight:900}.bp-hero-cta{display:flex;flex-wrap:wrap;gap:.6rem;margin-top:1.5rem}
.bp-hero-video{width:100%;border-radius:1.4rem;box-shadow:0 30px 80px rgba(0,0,0,.45)}
.bp-grid{display:grid;gap:1.25rem}.cols-3{grid-template-columns:repeat(3,1fr)}.cols-4{grid-template-columns:repeat(4,1fr)}
.bp-dark{background:var(--bp-charcoal);color:#fff}.bp-dark h2{color:#fff}
.bp-card{background:#fff;border:1px solid rgba(0,0,0,.06);border-radius:var(--bp-radius);overflow:hidden;transition:transform .35s,box-shadow .35s}.bp-card:hover{transform:translateY(-6px);box-shadow:0 24px 60px rgba(20,18,16,.16)}
.bp-card-media{display:block;position:relative;aspect-ratio:4/3;overflow:hidden;background:#e7e2d9}.bp-card-media img{width:100%;height:100%;object-fit:cover;transition:transform .6s}.bp-card:hover .bp-card-media img{transform:scale(1.06)}
.bp-card-body{padding:1.25rem}.bp-card-body h3{margin:.3rem 0;font-size:1.05rem}.bp-card-body h3 a{color:inherit;text-decoration:none}.bp-card-body p{color:var(--bp-muted);font-size:.9rem}
.bp-badge{position:absolute;left:.8rem;top:.8rem;background:var(--bp-brick);color:#fff;font-size:.68rem;font-weight:800;text-transform:uppercase;padding:.3rem .7rem;border-radius:99px}.bp-avail{position:absolute;left:.8rem;top:2.6rem;background:#047857;color:#fff;font-size:.68rem;font-weight:700;padding:.3rem .7rem;border-radius:99px}
.bp-price{font-weight:900;font-size:1.2rem;color:var(--bp-ink)}.bp-unit{color:var(--bp-muted);font-size:.8rem}.bp-card-cta{display:flex;gap:.5rem;margin-top:.8rem}
.bp-cat-card{display:block;background:var(--bp-charcoal);border-radius:var(--bp-radius);overflow:hidden;text-decoration:none;color:#fff}.bp-cat-card img{width:100%;aspect-ratio:16/9;object-fit:cover}.bp-cat-card-body{display:block;padding:1rem}
.bp-video-thumb{position:relative}.bp-play-btn{position:absolute;inset:0;margin:auto;width:56px;height:56px;display:grid;place-items:center;background:var(--bp-ember);color:#fff;border-radius:50%;font-size:1.2rem}
.bp-duration{position:absolute;right:.8rem;bottom:.8rem;background:rgba(0,0,0,.8);color:#fff;font-size:.7rem;font-weight:700;padding:.25rem .6rem;border-radius:.5rem}.bp-feat{position:absolute;left:.8rem;top:.8rem;background:#fbbf24;color:#000;font-size:.68rem;font-weight:800;padding:.3rem .7rem;border-radius:99px}
.bp-video-embed iframe,.bp-video-player{width:100%;aspect-ratio:16/9;border:0;border-radius:var(--bp-radius);background:#000}
.bp-filters{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:1rem}.bp-filters a{background:rgba(255,255,255,.1);color:#fff;text-decoration:none;font-size:.75rem;font-weight:700;padding:.5rem 1rem;border-radius:99px}
.bp-product-layout{display:grid;grid-template-columns:1fr 1fr;gap:2.5rem;padding:2.5rem 0}.bp-product-img,.bp-single-img{width:100%;border-radius:1.4rem}.bp-thumbs{display:grid;grid-template-columns:repeat(4,1fr);gap:.6rem;margin-top:.8rem}.bp-thumbs img{border-radius:.8rem;aspect-ratio:1;object-fit:cover}
.bp-product-cta{display:grid;grid-template-columns:repeat(3,1fr);gap:.5rem;margin:1.2rem 0}.bp-box{border:1px solid rgba(0,0,0,.08);border-radius:1rem;padding:1.2rem;margin:1rem 0;background:#fff}.bp-box dl div{display:grid;grid-template-columns:140px 1fr;padding:.5rem 0;border-bottom:1px solid #eee}
.bp-entry{line-height:1.75;color:#3d3833}.bp-crumbs{padding:1rem 0;font-size:.8rem;color:var(--bp-muted)}.bp-illus{position:absolute;left:.8rem;top:.8rem;background:rgba(0,0,0,.7);color:#fff;font-size:.68rem;font-weight:700;padding:.3rem .7rem;border-radius:99px}
.bp-footer{background:var(--bp-ink);color:#fff;margin-top:2rem}.bp-footer-grid{display:grid;grid-template-columns:1.4fr 1fr 1fr 1fr;gap:2rem;padding:3.5rem 0}.bp-footer a{color:rgba(255,255,255,.7);text-decoration:none;font-size:.88rem}.bp-footer a:hover{color:#fff}
.bp-footer-bottom{border-top:1px solid rgba(255,255,255,.1)}.bp-footer-bottom-inner{display:flex;justify-content:space-between;padding:1.2rem;font-size:.75rem;color:rgba(255,255,255,.5)}
.bp-social{display:flex;gap:.5rem;margin-top:1rem}.bp-social a{display:grid;place-items:center;width:40px;height:40px;background:rgba(255,255,255,.1);border-radius:.7rem;color:#fff;font-weight:800}
.bp-float-wa{position:fixed;right:1.2rem;bottom:1.2rem;z-index:60;width:56px;height:56px;display:grid;place-items:center;background:#128c4b;color:#fff;border-radius:50%;font-size:1.4rem;text-decoration:none;box-shadow:0 12px 30px rgba(0,0,0,.35)}
.entry-meta{font-size:.78rem;color:var(--bp-muted)}.bp-tags{font-size:.8rem}.related-posts{margin-top:2rem}
`);

add("assets/css/responsive.css", `@media(max-width:1024px){.cols-4{grid-template-columns:repeat(3,1fr)}.bp-hero-grid{grid-template-columns:1fr}.bp-product-layout{grid-template-columns:1fr}.bp-footer-grid{grid-template-columns:1fr 1fr}}
@media(max-width:820px){.bp-nav,.bp-header-cta{display:none}.bp-menu-toggle{display:grid;place-items:center;margin-left:auto}.cols-3,.cols-4{grid-template-columns:repeat(2,1fr)}.bp-product-cta{grid-template-columns:1fr}}
@media(max-width:480px){.cols-3,.cols-4{grid-template-columns:1fr}.bp-footer-grid{grid-template-columns:1fr}.bp-section{padding:2.5rem 0}.bp-topbar-units{display:none}}
.bp-mobile-menu{background:var(--bp-charcoal);padding:1rem;border-top:1px solid rgba(255,255,255,.1)}.bp-menu-mobile{list-style:none;margin:0;padding:0}.bp-menu-mobile a{display:block;color:#fff;text-decoration:none;font-weight:600;padding:.8rem;border-radius:.6rem}.bp-menu-mobile a:hover{background:rgba(255,255,255,.08)}
`);

add("assets/css/animations.css", `.reveal{opacity:0;transform:translateY(28px);transition:opacity .7s,transform .7s}.reveal.visible{opacity:1;transform:none}
@keyframes ss7-approach{0%{transform:scale(.72) translateY(46px);filter:brightness(.72);opacity:.55}55%{transform:scale(.94) translateY(8px);opacity:.95}100%{transform:scale(1);opacity:1}}
.ss7-brick{transform-origin:center;animation:ss7-approach 2.6s cubic-bezier(.22,.61,.36,1) both;background:#1c1a17;border:1px solid rgba(255,255,255,.12);border-radius:1rem;padding:1rem 1.4rem;display:flex;gap:.8rem;align-items:center;box-shadow:0 24px 60px rgba(0,0,0,.4)}
.ss7-brick strong{font-family:Archivo;font-size:1.6rem;color:#fbbf24}
@keyframes bp-float{0%,100%{transform:translateY(-8px)}50%{transform:translateY(10px)}}
.bp-ss7-float{margin-top:1rem;animation:bp-float 6s ease-in-out 2.6s infinite}
@media(prefers-reduced-motion:reduce){.ss7-brick,.bp-ss7-float{animation:none!important}.reveal{opacity:1;transform:none;transition:none}}
`);

add("assets/css/editor.css", `body{font-family:Inter,system-ui,sans-serif;color:#141210}.editor-post-title__input{font-family:Archivo,sans-serif;font-weight:900}
`);

/* ============ assets/js ============ */
add("assets/js/main.js", `(function(){document.addEventListener('DOMContentLoaded',function(){
var h=document.getElementById('bpHeader');
function onScroll(){if(h){h.classList.toggle('scrolled',window.scrollY>24);}}
window.addEventListener('scroll',onScroll,{passive:true});onScroll();
});})();
`);

add("assets/js/navigation.js", `(function(){document.addEventListener('DOMContentLoaded',function(){
var t=document.getElementById('bpMenuToggle'),m=document.getElementById('bpMobileMenu');
if(!t||!m)return;
t.addEventListener('click',function(){var open=m.hasAttribute('hidden');if(open){m.removeAttribute('hidden');t.setAttribute('aria-expanded','true');document.body.style.overflow='hidden';}else{m.setAttribute('hidden','');t.setAttribute('aria-expanded','false');document.body.style.overflow='';}});
});})();
`);

add("assets/js/animations.js", `(function(){document.addEventListener('DOMContentLoaded',function(){
if(!('IntersectionObserver' in window))return;
var els=document.querySelectorAll('.reveal');
var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('visible');io.unobserve(e.target);}});},{threshold:.12});
els.forEach(function(el){io.observe(el);});
});})();
`);

add("assets/js/product.js", `(function(){document.addEventListener('DOMContentLoaded',function(){
document.querySelectorAll('.bp-thumbs img').forEach(function(th){
th.style.cursor='pointer';
th.addEventListener('click',function(){
var main=document.querySelector('.bp-product-img');
if(main){var s=main.src;main.src=th.src;th.src=s;}
});
});
});})();
`);

add("assets/js/video.js", `(function(){document.addEventListener('DOMContentLoaded',function(){
if(window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches){
document.querySelectorAll('video[autoplay]').forEach(function(v){v.removeAttribute('autoplay');v.pause&&v.pause();});
}
});})();
`);

add("assets/js/ajax.js", `(function(){
document.addEventListener('submit',function(e){
var f=e.target;
if(!f||!f.classList||!f.classList.contains('bp-quote-form'))return;
e.preventDefault();
var data=new FormData(f);data.append('action','brickpoint_quote');data.append('nonce',(window.BRICKPOINT&&BRICKPOINT.nonce)||'');
var btn=f.querySelector('[type=submit]');if(btn){btn.disabled=true;}
fetch((window.BRICKPOINT&&BRICKPOINT.ajaxUrl)||'/wp-admin/admin-ajax.php',{method:'POST',body:data,credentials:'same-origin'})
.then(function(r){return r.json();}).then(function(j){
var n=f.querySelector('.bp-form-note');if(n){n.textContent=(j&&j.data)||'';}
if(btn){btn.disabled=false;}
}).catch(function(){if(btn){btn.disabled=false;}});
});
})();
`);

/* ============ elementor widgets ============ */
const widgetHeader = `<?php
if ( ! defined( 'ABSPATH' ) ) { exit; }
`;

add("elementor/widgets/product-grid.php", widgetHeader + `class BrickPoint_Product_Grid extends \\Elementor\\Widget_Base {
  public function get_name() { return 'bp-product-grid'; }
  public function get_title() { return __( 'BP Product Grid', 'brickpoint' ); }
  public function get_icon() { return 'eicon-products'; }
  public function get_categories() { return array( 'brickpoint' ); }
  protected function register_controls() {
    $this->start_controls_section( 'query', array( 'label' => __( 'Query', 'brickpoint' ) ) );
    $this->add_control( 'count', array( 'label' => __( 'Number of products', 'brickpoint' ), 'type' => \\Elementor\\Controls_Manager::NUMBER, 'default' => 8 ) );
    $this->add_control( 'category', array( 'label' => __( 'Category slug (blank = all)', 'brickpoint' ), 'type' => \\Elementor\\Controls_Manager::TEXT, 'default' => '' ) );
    $this->add_control( 'featured_only', array( 'label' => __( 'Featured only', 'brickpoint' ), 'type' => \\Elementor\\Controls_Manager::SWITCHER, 'default' => '' ) );
    $this->add_control( 'orderby', array( 'label' => __( 'Order by', 'brickpoint' ), 'type' => \\Elementor\\Controls_Manager::SELECT, 'default' => 'date', 'options' => array( 'date' => 'Date', 'title' => 'Title', 'menu_order' => 'Custom order' ) ) );
    $this->add_control( 'columns', array( 'label' => __( 'Columns', 'brickpoint' ), 'type' => \\Elementor\\Controls_Manager::SELECT, 'default' => '4', 'options' => array( '2' => '2', '3' => '3', '4' => '4' ) ) );
    $this->add_control( 'show_price', array( 'label' => __( 'Show price', 'brickpoint' ), 'type' => \\Elementor\\Controls_Manager::SWITCHER, 'default' => 'yes' ) );
    $this->add_control( 'show_whatsapp', array( 'label' => __( 'Show WhatsApp button', 'brickpoint' ), 'type' => \\Elementor\\Controls_Manager::SWITCHER, 'default' => 'yes' ) );
    $this->end_controls_section();
  }
  protected function render() {
    $s = $this->get_settings_for_display();
    $args = array( 'post_type' => 'bp_product', 'posts_per_page' => absint( $s['count'] ), 'orderby' => sanitize_key( $s['orderby'] ) );
    if ( ! empty( $s['category'] ) ) { $args['tax_query'] = array( array( 'taxonomy' => 'bp_product_category', 'field' => 'slug', 'terms' => sanitize_title( $s['category'] ) ) ); }
    if ( ! empty( $s['featured_only'] ) ) { $args['meta_key'] = '_bp_featured'; $args['meta_value'] = '1'; }
    $q = new WP_Query( $args );
    echo '<div class="bp-grid cols-' . esc_attr( $s['columns'] ) . '">';
    while ( $q->have_posts() ) { $q->the_post(); get_template_part( 'template-parts/product-card' ); }
    echo '</div>'; wp_reset_postdata();
  }
}
`);

add("elementor/widgets/product-categories.php", widgetHeader + `class BrickPoint_Product_Categories extends \\Elementor\\Widget_Base {
  public function get_name() { return 'bp-product-categories'; }
  public function get_title() { return __( 'BP Product Categories', 'brickpoint' ); }
  public function get_icon() { return 'eicon-gallery-grid'; }
  public function get_categories() { return array( 'brickpoint' ); }
  protected function register_controls() {
    $this->start_controls_section( 'q', array( 'label' => __( 'Settings', 'brickpoint' ) ) );
    $this->add_control( 'count', array( 'label' => __( 'Number', 'brickpoint' ), 'type' => \\Elementor\\Controls_Manager::NUMBER, 'default' => 8 ) );
    $this->add_control( 'columns', array( 'label' => __( 'Columns', 'brickpoint' ), 'type' => \\Elementor\\Controls_Manager::SELECT, 'default' => '4', 'options' => array( '2' => '2', '3' => '3', '4' => '4' ) ) );
    $this->end_controls_section();
  }
  protected function render() {
    $s = $this->get_settings_for_display();
    $cats = get_terms( array( 'taxonomy' => 'bp_product_category', 'number' => absint( $s['count'] ), 'hide_empty' => false ) );
    if ( ! $cats || is_wp_error( $cats ) ) { return; }
    echo '<div class="bp-grid cols-' . esc_attr( $s['columns'] ) . '">';
    foreach ( $cats as $t ) {
      $img = get_term_meta( $t->term_id, 'bp_cat_image', true );
      echo '<a class="bp-cat-card" href="' . esc_url( get_term_link( $t ) ) . '">';
      if ( $img ) { echo '<img src="' . esc_url( $img ) . '" alt="' . esc_attr( $t->name ) . '" loading="lazy" />'; }
      echo '<span class="bp-card-body"><strong>' . esc_html( $t->name ) . '</strong><br><small>' . esc_html( wp_trim_words( $t->description, 12 ) ) . '</small></span></a>';
    }
    echo '</div>';
  }
}
`);

add("elementor/widgets/product-price.php", widgetHeader + `class BrickPoint_Product_Price extends \\Elementor\\Widget_Base {
  public function get_name() { return 'bp-product-price'; }
  public function get_title() { return __( 'BP Product Price', 'brickpoint' ); }
  public function get_icon() { return 'eicon-price-table'; }
  public function get_categories() { return array( 'brickpoint' ); }
  protected function register_controls() {
    $this->start_controls_section( 's', array( 'label' => __( 'Settings', 'brickpoint' ) ) );
    $this->add_control( 'show_unit', array( 'label' => __( 'Show unit', 'brickpoint' ), 'type' => \\Elementor\\Controls_Manager::SWITCHER, 'default' => 'yes' ) );
    $this->end_controls_section();
  }
  protected function render() {
    $id = get_the_ID();
    if ( get_post_type( $id ) !== 'bp_product' ) { echo esc_html__( 'Place on a Single Product template.', 'brickpoint' ); return; }
    $price = bp_meta( $id, '_bp_price', '' ); $unit = bp_meta( $id, '_bp_unit', '' );
    $s = $this->get_settings_for_display();
    if ( $price ) { echo '<p class="bp-price-row"><span class="bp-price">' . esc_html( $price ) . '</span>'; if ( $unit && ! empty( $s['show_unit'] ) ) { echo ' <span class="bp-unit">/ ' . esc_html( $unit ) . '</span>'; } echo '</p>'; }
    else { echo '<p class="bp-price">' . esc_html__( 'Price on request', 'brickpoint' ) . '</p>'; }
  }
}
`);

add("elementor/widgets/whatsapp-button.php", widgetHeader + `class BrickPoint_WhatsApp_Button extends \\Elementor\\Widget_Base {
  public function get_name() { return 'bp-whatsapp-button'; }
  public function get_title() { return __( 'BP WhatsApp Button', 'brickpoint' ); }
  public function get_icon() { return 'eicon-button'; }
  public function get_categories() { return array( 'brickpoint' ); }
  protected function register_controls() {
    $this->start_controls_section( 's', array( 'label' => __( 'Settings', 'brickpoint' ) ) );
    $this->add_control( 'label', array( 'label' => __( 'Label', 'brickpoint' ), 'type' => \\Elementor\\Controls_Manager::TEXT, 'default' => 'Order on WhatsApp' ) );
    $this->add_control( 'message', array( 'label' => __( 'Message (blank = product-aware default)', 'brickpoint' ), 'type' => \\Elementor\\Controls_Manager::TEXTAREA, 'default' => '' ) );
    $this->add_control( 'style', array( 'label' => __( 'Style', 'brickpoint' ), 'type' => \\Elementor\\Controls_Manager::SELECT, 'default' => 'btn-whatsapp', 'options' => array( 'btn-whatsapp' => 'WhatsApp', 'btn-brick' => 'Brick', 'btn-dark' => 'Dark', 'btn-ghost' => 'Ghost' ) ) );
    $this->end_controls_section();
  }
  protected function render() {
    $s = $this->get_settings_for_display();
    $msg = $s['message'];
    if ( ! $msg ) {
      $id = get_the_ID();
      $msg = ( get_post_type( $id ) === 'bp_product' ) ? bp_product_whatsapp_message( $id ) : bp_get( 'bp_default_wa', 'Assalam-o-Alaikum BrickPoint' );
    }
    echo '<a class="' . esc_attr( $s['style'] ) . '" target="_blank" rel="noopener" href="' . esc_url( bp_whatsapp_url( $msg ) ) . '">' . esc_html( $s['label'] ) . '</a>';
  }
}
`);

add("elementor/widgets/video-grid.php", widgetHeader + `class BrickPoint_Video_Grid extends \\Elementor\\Widget_Base {
  public function get_name() { return 'bp-video-grid'; }
  public function get_title() { return __( 'BP Video Grid', 'brickpoint' ); }
  public function get_icon() { return 'eicon-video'; }
  public function get_categories() { return array( 'brickpoint' ); }
  protected function register_controls() {
    $this->start_controls_section( 'q', array( 'label' => __( 'Query', 'brickpoint' ) ) );
    $this->add_control( 'count', array( 'label' => __( 'Number', 'brickpoint' ), 'type' => \\Elementor\\Controls_Manager::NUMBER, 'default' => 6 ) );
    $this->add_control( 'category', array( 'label' => __( 'Category slug (blank = all)', 'brickpoint' ), 'type' => \\Elementor\\Controls_Manager::TEXT, 'default' => '' ) );
    $this->add_control( 'featured_only', array( 'label' => __( 'Featured only', 'brickpoint' ), 'type' => \\Elementor\\Controls_Manager::SWITCHER, 'default' => '' ) );
    $this->add_control( 'columns', array( 'label' => __( 'Columns', 'brickpoint' ), 'type' => \\Elementor\\Controls_Manager::SELECT, 'default' => '3', 'options' => array( '2' => '2', '3' => '3', '4' => '4' ) ) );
    $this->end_controls_section();
  }
  protected function render() {
    $s = $this->get_settings_for_display();
    $args = array( 'post_type' => 'bp_video', 'posts_per_page' => absint( $s['count'] ) );
    if ( ! empty( $s['category'] ) ) { $args['tax_query'] = array( array( 'taxonomy' => 'bp_video_category', 'field' => 'slug', 'terms' => sanitize_title( $s['category'] ) ) ); }
    if ( ! empty( $s['featured_only'] ) ) { $args['meta_key'] = '_bpv_featured'; $args['meta_value'] = '1'; }
    $q = new WP_Query( $args );
    echo '<div class="bp-grid cols-' . esc_attr( $s['columns'] ) . '">';
    while ( $q->have_posts() ) { $q->the_post(); get_template_part( 'template-parts/video-card' ); }
    echo '</div>'; wp_reset_postdata();
  }
}
`);

add("elementor/widgets/video-card.php", widgetHeader + `class BrickPoint_Video_Card extends \\Elementor\\Widget_Base {
  public function get_name() { return 'bp-video-card'; }
  public function get_title() { return __( 'BP Video Card (current)', 'brickpoint' ); }
  public function get_icon() { return 'eicon-play'; }
  public function get_categories() { return array( 'brickpoint' ); }
  protected function register_controls() {
    $this->start_controls_section( 's', array( 'label' => __( 'Settings', 'brickpoint' ) ) );
    $this->add_control( 'embed', array( 'label' => __( 'Show player instead of card', 'brickpoint' ), 'type' => \\Elementor\\Controls_Manager::SWITCHER, 'default' => '' ) );
    $this->end_controls_section();
  }
  protected function render() {
    $s = $this->get_settings_for_display();
    if ( ! empty( $s['embed'] ) ) { echo bp_video_embed_html( get_the_ID() ); return; }
    get_template_part( 'template-parts/video-card' );
  }
}
`);

add("elementor/widgets/project-grid.php", widgetHeader + `class BrickPoint_Project_Grid extends \\Elementor\\Widget_Base {
  public function get_name() { return 'bp-project-grid'; }
  public function get_title() { return __( 'BP Project Grid', 'brickpoint' ); }
  public function get_icon() { return 'eicon-gallery-masonry'; }
  public function get_categories() { return array( 'brickpoint' ); }
  protected function register_controls() {
    $this->start_controls_section( 'q', array( 'label' => __( 'Query', 'brickpoint' ) ) );
    $this->add_control( 'count', array( 'label' => __( 'Number', 'brickpoint' ), 'type' => \\Elementor\\Controls_Manager::NUMBER, 'default' => 6 ) );
    $this->add_control( 'columns', array( 'label' => __( 'Columns', 'brickpoint' ), 'type' => \\Elementor\\Controls_Manager::SELECT, 'default' => '3', 'options' => array( '2' => '2', '3' => '3', '4' => '4' ) ) );
    $this->end_controls_section();
  }
  protected function render() {
    $s = $this->get_settings_for_display();
    $q = new WP_Query( array( 'post_type' => 'bp_project', 'posts_per_page' => absint( $s['count'] ) ) );
    echo '<div class="bp-grid cols-' . esc_attr( $s['columns'] ) . '">';
    while ( $q->have_posts() ) { $q->the_post(); get_template_part( 'template-parts/content-project' ); }
    echo '</div>'; wp_reset_postdata();
  }
}
`);

add("elementor/widgets/location-cards.php", widgetHeader + `class BrickPoint_Location_Cards extends \\Elementor\\Widget_Base {
  public function get_name() { return 'bp-location-cards'; }
  public function get_title() { return __( 'BP Location Cards', 'brickpoint' ); }
  public function get_icon() { return 'eicon-google-maps'; }
  public function get_categories() { return array( 'brickpoint' ); }
  protected function register_controls() {
    $this->start_controls_section( 'q', array( 'label' => __( 'Settings', 'brickpoint' ) ) );
    $this->add_control( 'count', array( 'label' => __( 'Number', 'brickpoint' ), 'type' => \\Elementor\\Controls_Manager::NUMBER, 'default' => 4 ) );
    $this->add_control( 'columns', array( 'label' => __( 'Columns', 'brickpoint' ), 'type' => \\Elementor\\Controls_Manager::SELECT, 'default' => '2', 'options' => array( '1' => '1', '2' => '2', '3' => '3', '4' => '4' ) ) );
    $this->end_controls_section();
  }
  protected function render() {
    $s = $this->get_settings_for_display();
    $q = new WP_Query( array( 'post_type' => 'bp_location', 'posts_per_page' => absint( $s['count'] ), 'orderby' => 'meta_value_num', 'meta_key' => '_bpl_order', 'order' => 'ASC' ) );
    echo '<div class="bp-grid cols-' . esc_attr( $s['columns'] ) . '">';
    while ( $q->have_posts() ) { $q->the_post();
      $id = get_the_ID();
      echo '<article class="bp-card"><a class="bp-card-media" href="' . esc_url( get_permalink() ) . '">';
      if ( has_post_thumbnail() ) { the_post_thumbnail( 'bp-card' ); }
      echo '</a><div class="bp-card-body"><h3>' . esc_html( get_the_title() ) . '</h3><p>' . esc_html( bp_meta( $id, '_bpl_address', '' ) ) . '</p><p class="bp-card-cta">';
      $maps = bp_meta( $id, '_bpl_maps', '' );
      if ( $maps ) { echo '<a class="btn-dark btn-sm" target="_blank" rel="noopener" href="' . esc_url( $maps ) . '">' . esc_html__( 'Directions', 'brickpoint' ) . '</a>'; }
      echo '<a class="btn-whatsapp btn-sm" target="_blank" rel="noopener" href="' . esc_url( bp_whatsapp_url( bp_get( 'bp_default_wa', 'Assalam-o-Alaikum BrickPoint' ) ) ) . '">WhatsApp</a>';
      echo '</p></div></article>';
    }
    echo '</div>'; wp_reset_postdata();
  }
}
`);

add("elementor/widgets/social-links.php", widgetHeader + `class BrickPoint_Social_Links extends \\Elementor\\Widget_Base {
  public function get_name() { return 'bp-social-links'; }
  public function get_title() { return __( 'BP Social Links', 'brickpoint' ); }
  public function get_icon() { return 'eicon-social-icons'; }
  public function get_categories() { return array( 'brickpoint' ); }
  protected function register_controls() {
    $this->start_controls_section( 's', array( 'label' => __( 'Settings', 'brickpoint' ) ) );
    $this->add_control( 'note', array( 'type' => \\Elementor\\Controls_Manager::RAW_HTML, 'raw' => __( 'URLs come from Customize → BrickPoint: Social Links.', 'brickpoint' ) ) );
    $this->end_controls_section();
  }
  protected function render() { get_template_part( 'template-parts/social-links' ); }
}
`);

add("elementor/templates/readme.txt", `BrickPoint Elementor templates (optional JSON exports) can be placed here.
Build pages with Elementor using the BrickPoint widget category.
Recommended: Home, SS7 Bricks, Videos, Locations, Contact.
`);

add("languages/brickpoint.pot", `msgid ""
msgstr ""
"Project-Id-Version: BrickPoint 1.0.0\\n"
"Content-Type: text/plain; charset=UTF-8\\n"

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
`);

add("assets/images/readme.txt", `Place brand imagery here (logo, hero poster, category banners).`);
add("assets/icons/readme.txt", `Place SVG icons here.`);

// Write all files
let count = 0;
for (const [rel, content] of Object.entries(files)) {
  const full = path.join(ROOT, rel);
  fs.mkdirSync(path.dirname(full), { recursive: true });
  fs.writeFileSync(full, content);
  count++;
}
console.log("Wrote " + count + " theme files to " + ROOT);
