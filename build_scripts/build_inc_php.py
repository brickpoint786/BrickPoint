import os

DEST = "/home/user/BrickPoint/wordpress/brickpoint"
files = {}

# inc/setup.php
files["inc/setup.php"] = """<?php
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
"""

# inc/enqueue.php
files["inc/enqueue.php"] = """<?php
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
"""

# inc/helpers.php
files["inc/helpers.php"] = """<?php
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
"""

# inc/template-functions.php
files["inc/template-functions.php"] = """<?php
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
"""

# inc/post-types.php
files["inc/post-types.php"] = """<?php
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
"""

# inc/taxonomies.php
files["inc/taxonomies.php"] = """<?php
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
"""

# inc/meta-fields.php
files["inc/meta-fields.php"] = """<?php
/**
 * Register Meta Boxes for CPTs
 *
 * @package BrickPoint
 */

if ( ! defined( 'ABSPATH' ) ) {
  exit;
}

function brickpoint_add_meta_boxes() {
  add_meta_box( 'bp_product_details', esc_html__( 'Product Pricing & Details', 'brickpoint' ), 'bp_product_meta_box_cb', 'bp_product', 'normal', 'high' );
  add_meta_box( 'bp_video_details', esc_html__( 'Video Configuration', 'brickpoint' ), 'bp_video_meta_box_cb', 'bp_video', 'normal', 'high' );
  add_meta_box( 'bp_project_details', esc_html__( 'Project Reference Details', 'brickpoint' ), 'bp_project_meta_box_cb', 'bp_project', 'normal', 'high' );
  add_meta_box( 'bp_location_details', esc_html__( 'Location & Facility Details', 'brickpoint' ), 'bp_location_meta_box_cb', 'bp_location', 'normal', 'high' );
}
add_action( 'add_meta_boxes', 'brickpoint_add_meta_boxes' );

// Product meta box HTML
function bp_product_meta_box_cb( $post ) {
  wp_nonce_field( 'bp_product_meta_nonce', 'bp_product_nonce' );
  $fields = array(
    '_bp_price'        => array( 'label' => 'Price (e.g. Rs 14,000 / Rs 1,450)', 'type' => 'text' ),
    '_bp_price_label'  => array( 'label' => 'Price Label (e.g. per 1,000 bricks)', 'type' => 'text' ),
    '_bp_unit'         => array( 'label' => 'Unit (e.g. 1000 Bricks, Bag, Ton, Bundle)', 'type' => 'text' ),
    '_bp_availability' => array( 'label' => 'Availability (In Stock / Made to Order)', 'type' => 'text' ),
    '_bp_badge'        => array( 'label' => 'Badge Tag (e.g. Flagship / Premium / Popular)', 'type' => 'text' ),
    '_bp_featured'     => array( 'label' => 'Featured Product (1 = yes, 0 = no)', 'type' => 'text' ),
    '_bp_sku'          => array( 'label' => 'SKU / Code', 'type' => 'text' ),
    '_bp_short'        => array( 'label' => 'Short Summary', 'type' => 'textarea' ),
    '_bp_gallery'      => array( 'label' => 'Additional Gallery Image URLs (one per line)', 'type' => 'textarea' ),
    '_bp_specs'        => array( 'label' => 'Specifications (Label: Value, one per line)', 'type' => 'textarea' ),
    '_bp_features'     => array( 'label' => 'Key Features (one per line)', 'type' => 'textarea' ),
    '_bp_video'        => array( 'label' => 'Product MP4 Video URL', 'type' => 'text' ),
    '_bp_brochure'     => array( 'label' => 'Brochure / Specs PDF URL', 'type' => 'text' ),
    '_bp_whatsapp'     => array( 'label' => 'Custom WhatsApp Inquiry Message Override', 'type' => 'textarea' ),
  );

  echo '<div style="display:grid;grid-gap:15px;grid-template-columns:1fr 1fr;">';
  foreach ( $fields as $key => $conf ) {
    $val = get_post_meta( $post->ID, $key, true );
    $span = ( $conf['type'] === 'textarea' ) ? 'grid-column:1/-1;' : '';
    echo '<div style="' . esc_attr( $span ) . '">';
    echo '<label style="display:block;font-weight:600;margin-bottom:4px;">' . esc_html( $conf['label'] ) . '</label>';
    if ( $conf['type'] === 'textarea' ) {
      echo '<textarea name="' . esc_attr( $key ) . '" rows="4" style="width:100%;">' . esc_textarea( $val ) . '</textarea>';
    } else {
      echo '<input type="text" name="' . esc_attr( $key ) . '" value="' . esc_attr( $val ) . '" style="width:100%;" />';
    }
    echo '</div>';
  }
  echo '</div>';
}

// Video meta box HTML
function bp_video_meta_box_cb( $post ) {
  wp_nonce_field( 'bp_video_meta_nonce', 'bp_video_nonce' );
  $source = get_post_meta( $post->ID, '_bpv_source', true );
  $url = get_post_meta( $post->ID, '_bpv_url', true );
  $file = get_post_meta( $post->ID, '_bpv_file', true );
  $dur = get_post_meta( $post->ID, '_bpv_duration', true );
  $feat = get_post_meta( $post->ID, '_bpv_featured', true );
  ?>
  <div style="display:grid;grid-gap:12px;">
    <div>
      <label style="display:block;font-weight:600;">Video Source:</label>
      <select name="_bpv_source" style="width:100%;">
        <option value="mp4" <?php selected( $source, 'mp4' ); ?>>Direct MP4 Video</option>
        <option value="youtube" <?php selected( $source, 'youtube' ); ?>>YouTube Embed</option>
        <option value="vimeo" <?php selected( $source, 'vimeo' ); ?>>Vimeo Embed</option>
      </select>
    </div>
    <div>
      <label style="display:block;font-weight:600;">Video URL / Embed URL:</label>
      <input type="text" name="_bpv_url" value="<?php echo esc_attr( $url ); ?>" style="width:100%;" />
    </div>
    <div>
      <label style="display:block;font-weight:600;">Direct File URL (optional):</label>
      <input type="text" name="_bpv_file" value="<?php echo esc_attr( $file ); ?>" style="width:100%;" />
    </div>
    <div>
      <label style="display:block;font-weight:600;">Duration (e.g. 0:45, 1:20):</label>
      <input type="text" name="_bpv_duration" value="<?php echo esc_attr( $dur ); ?>" style="width:100%;" />
    </div>
    <div>
      <label style="display:block;font-weight:600;">Featured Video (1 or 0):</label>
      <input type="text" name="_bpv_featured" value="<?php echo esc_attr( $feat ); ?>" style="width:100%;" />
    </div>
  </div>
  <?php
}

// Project meta box HTML
function bp_project_meta_box_cb( $post ) {
  wp_nonce_field( 'bp_project_meta_nonce', 'bp_project_nonce' );
  $cat = get_post_meta( $post->ID, '_bpp_category', true );
  $loc = get_post_meta( $post->ID, '_bpp_location', true );
  $status = get_post_meta( $post->ID, '_bpp_status', true );
  ?>
  <div style="display:grid;grid-gap:12px;">
    <div>
      <label style="display:block;font-weight:600;">Project Category (e.g. Residential, Commercial):</label>
      <input type="text" name="_bpp_category" value="<?php echo esc_attr( $cat ); ?>" style="width:100%;" />
    </div>
    <div>
      <label style="display:block;font-weight:600;">Location (e.g. DHA Lahore, Bahria Town Lahore):</label>
      <input type="text" name="_bpp_location" value="<?php echo esc_attr( $loc ); ?>" style="width:100%;" />
    </div>
    <div>
      <label style="display:block;font-weight:600;">Status Label (default: Illustrative construction reference):</label>
      <input type="text" name="_bpp_status" value="<?php echo esc_attr( $status ? $status : 'Illustrative construction reference' ); ?>" style="width:100%;" />
    </div>
  </div>
  <?php
}

// Location meta box HTML
function bp_location_meta_box_cb( $post ) {
  wp_nonce_field( 'bp_location_meta_nonce', 'bp_location_nonce' );
  $addr = get_post_meta( $post->ID, '_bpl_address', true );
  $phone = get_post_meta( $post->ID, '_bpl_phone', true );
  $hours = get_post_meta( $post->ID, '_bpl_hours', true );
  $maps = get_post_meta( $post->ID, '_bpl_maps_url', true );
  $video = get_post_meta( $post->ID, '_bpl_video', true );
  ?>
  <div style="display:grid;grid-gap:12px;">
    <div>
      <label style="display:block;font-weight:600;">Address:</label>
      <input type="text" name="_bpl_address" value="<?php echo esc_attr( $addr ); ?>" style="width:100%;" />
    </div>
    <div>
      <label style="display:block;font-weight:600;">Phone:</label>
      <input type="text" name="_bpl_phone" value="<?php echo esc_attr( $phone ); ?>" style="width:100%;" />
    </div>
    <div>
      <label style="display:block;font-weight:600;">Operating Hours:</label>
      <input type="text" name="_bpl_hours" value="<?php echo esc_attr( $hours ? $hours : 'Mon – Sat: 8:00 AM – 6:00 PM' ); ?>" style="width:100%;" />
    </div>
    <div>
      <label style="display:block;font-weight:600;">Google Maps URL:</label>
      <input type="text" name="_bpl_maps_url" value="<?php echo esc_attr( $maps ); ?>" style="width:100%;" />
    </div>
    <div>
      <label style="display:block;font-weight:600;">Facility MP4 Video URL:</label>
      <input type="text" name="_bpl_video" value="<?php echo esc_attr( $video ); ?>" style="width:100%;" />
    </div>
  </div>
  <?php
}

// Save post hook
function brickpoint_save_post_meta( $post_id ) {
  if ( defined( 'DOING_AUTOSAVE' ) && DOING_AUTOSAVE ) return;

  // Product save
  if ( isset( $_POST['bp_product_nonce'] ) && wp_verify_nonce( $_POST['bp_product_nonce'], 'bp_product_meta_nonce' ) ) {
    $keys = array( '_bp_price', '_bp_price_label', '_bp_unit', '_bp_availability', '_bp_badge', '_bp_featured', '_bp_sku', '_bp_short', '_bp_gallery', '_bp_specs', '_bp_features', '_bp_video', '_bp_brochure', '_bp_whatsapp' );
    foreach ( $keys as $k ) {
      if ( isset( $_POST[ $k ] ) ) {
        update_post_meta( $post_id, $k, sanitize_textarea_field( $_POST[ $k ] ) );
      }
    }
  }

  // Video save
  if ( isset( $_POST['bp_video_nonce'] ) && wp_verify_nonce( $_POST['bp_video_nonce'], 'bp_video_meta_nonce' ) ) {
    $keys = array( '_bpv_source', '_bpv_url', '_bpv_file', '_bpv_duration', '_bpv_featured' );
    foreach ( $keys as $k ) {
      if ( isset( $_POST[ $k ] ) ) {
        update_post_meta( $post_id, $k, sanitize_text_field( $_POST[ $k ] ) );
      }
    }
  }

  // Project save
  if ( isset( $_POST['bp_project_nonce'] ) && wp_verify_nonce( $_POST['bp_project_nonce'], 'bp_project_meta_nonce' ) ) {
    $keys = array( '_bpp_category', '_bpp_location', '_bpp_status' );
    foreach ( $keys as $k ) {
      if ( isset( $_POST[ $k ] ) ) {
        update_post_meta( $post_id, $k, sanitize_text_field( $_POST[ $k ] ) );
      }
    }
  }

  // Location save
  if ( isset( $_POST['bp_location_nonce'] ) && wp_verify_nonce( $_POST['bp_location_nonce'], 'bp_location_meta_nonce' ) ) {
    $keys = array( '_bpl_address', '_bpl_phone', '_bpl_hours', '_bpl_maps_url', '_bpl_video' );
    foreach ( $keys as $k ) {
      if ( isset( $_POST[ $k ] ) ) {
        update_post_meta( $post_id, $k, sanitize_text_field( $_POST[ $k ] ) );
      }
    }
  }
}
add_action( 'save_post', 'brickpoint_save_post_meta' );
"""

# inc/whatsapp.php
files["inc/whatsapp.php"] = """<?php
/**
 * WhatsApp Inquiry Generators & Ordering Links
 *
 * @package BrickPoint
 */

if ( ! defined( 'ABSPATH' ) ) {
  exit;
}

/**
 * Return clean WhatsApp numeric phone string
 */
function bp_whatsapp_clean_phone( $phone = '' ) {
  if ( empty( $phone ) ) {
    $phone = bp_option( 'bp_whatsapp_number', '923152850818' );
  }
  return preg_replace( '/[^0-9]/', '', $phone );
}

/**
 * Build direct WhatsApp Web / API click link
 */
function bp_whatsapp_url( $message = '', $phone = '' ) {
  $clean_phone = bp_whatsapp_clean_phone( $phone );
  if ( empty( $message ) ) {
    $message = "Assalam-o-Alaikum BrickPoint,\\n\\nI am interested in getting a quotation for construction materials.\\n\\nThank you.";
  }
  return 'https://api.whatsapp.com/send?phone=' . rawurlencode( $clean_phone ) . '&text=' . rawurlencode( $message );
}

/**
 * Product Inquiry WhatsApp Template
 */
function bp_product_inquiry_message( $args = array() ) {
  $product  = isset( $args['product'] ) ? $args['product'] : 'Construction Material';
  $category = isset( $args['category'] ) ? $args['category'] : 'Materials';
  $price    = isset( $args['price'] ) ? $args['price'] : '';
  $unit     = isset( $args['unit'] ) ? $args['unit'] : '';

  $msg  = "Assalam-o-Alaikum BrickPoint,\\n\\n";
  $msg .= "I am interested in ordering/inquiring about the following product:\\n";
  $msg .= "*Product:* " . $product . "\\n";
  if ( $category ) {
    $msg .= "*Category:* " . $category . "\\n";
  }
  if ( $price ) {
    $msg .= "*Listed Rate:* " . $price . ( $unit ? " / " . $unit : "" ) . "\\n";
  }
  $msg .= "\\nPlease share availability, bulk delivery options to my location, and payment terms.\\n\\n";
  $msg .= "Thank you.";

  return $msg;
}

/**
 * Category Inquiry WhatsApp Template
 */
function bp_category_inquiry_message( $category_name = 'Materials' ) {
  $msg  = "Assalam-o-Alaikum BrickPoint,\\n\\n";
  $msg .= "I am inquiring about *{$category_name}*.\\n";
  $msg .= "Please share the current rate list, available grades/specifications, and delivery terms.\\n\\n";
  $msg .= "Thank you.";
  return $msg;
}
"""

# inc/customizer.php
files["inc/customizer.php"] = """<?php
/**
 * BrickPoint Customizer Settings
 *
 * Implements independent Header Logo & Footer Logo controls with responsive sizing,
 * phone, email, addresses, social links, and theme branding.
 *
 * @package BrickPoint
 */

if ( ! defined( 'ABSPATH' ) ) {
  exit;
}

function brickpoint_customize_register( $wp_customize ) {
  // Panel: BrickPoint Options
  $wp_customize->add_panel( 'bp_theme_panel', array(
    'title'       => esc_html__( 'BrickPoint Theme Options', 'brickpoint' ),
    'priority'    => 30,
    'description' => esc_html__( 'Configure independent header/footer logos, contact info, WhatsApp and branding.', 'brickpoint' ),
  ) );

  // Section 1: Header Logo & Navigation
  $wp_customize->add_section( 'bp_header_section', array(
    'title'    => esc_html__( 'Header & Header Logo', 'brickpoint' ),
    'panel'    => 'bp_theme_panel',
    'priority' => 10,
  ) );

  $wp_customize->add_setting( 'bp_header_logo', array( 'default' => '', 'sanitize_callback' => 'absint' ) );
  $wp_customize->add_control( new WP_Customize_Media_Control( $wp_customize, 'bp_header_logo', array(
    'label'       => esc_html__( 'Independent Header Logo', 'brickpoint' ),
    'description' => esc_html__( 'Used exclusively in the sticky top header and mobile navigation drawer.', 'brickpoint' ),
    'section'     => 'bp_header_section',
    'mime_type'   => 'image',
  ) ) );

  $wp_customize->add_setting( 'bp_header_logo_height_desktop', array( 'default' => 44, 'sanitize_callback' => 'absint' ) );
  $wp_customize->add_control( 'bp_header_logo_height_desktop', array(
    'label'       => esc_html__( 'Desktop Header Logo Height (px)', 'brickpoint' ),
    'section'     => 'bp_header_section',
    'type'        => 'number',
    'input_attrs' => array( 'min' => 20, 'max' => 120, 'step' => 2 ),
  ) );

  $wp_customize->add_setting( 'bp_header_logo_height_mobile', array( 'default' => 36, 'sanitize_callback' => 'absint' ) );
  $wp_customize->add_control( 'bp_header_logo_height_mobile', array(
    'label'       => esc_html__( 'Mobile Header Logo Height (px)', 'brickpoint' ),
    'section'     => 'bp_header_section',
    'type'        => 'number',
    'input_attrs' => array( 'min' => 18, 'max' => 80, 'step' => 2 ),
  ) );

  // Section 2: Footer Logo & Footer Info
  $wp_customize->add_section( 'bp_footer_section', array(
    'title'    => esc_html__( 'Footer & Footer Logo', 'brickpoint' ),
    'panel'    => 'bp_theme_panel',
    'priority' => 20,
  ) );

  $wp_customize->add_setting( 'bp_footer_logo', array( 'default' => '', 'sanitize_callback' => 'absint' ) );
  $wp_customize->add_control( new WP_Customize_Media_Control( $wp_customize, 'bp_footer_logo', array(
    'label'       => esc_html__( 'Independent Footer Logo', 'brickpoint' ),
    'description' => esc_html__( 'Used exclusively in the dark footer. You can select a reversed or custom footer variation here.', 'brickpoint' ),
    'section'     => 'bp_footer_section',
    'mime_type'   => 'image',
  ) ) );

  $wp_customize->add_setting( 'bp_footer_logo_height_desktop', array( 'default' => 52, 'sanitize_callback' => 'absint' ) );
  $wp_customize->add_control( 'bp_footer_logo_height_desktop', array(
    'label'       => esc_html__( 'Desktop Footer Logo Height (px)', 'brickpoint' ),
    'section'     => 'bp_footer_section',
    'type'        => 'number',
    'input_attrs' => array( 'min' => 24, 'max' => 140, 'step' => 2 ),
  ) );

  $wp_customize->add_setting( 'bp_footer_logo_height_mobile', array( 'default' => 42, 'sanitize_callback' => 'absint' ) );
  $wp_customize->add_control( 'bp_footer_logo_height_mobile', array(
    'label'       => esc_html__( 'Mobile Footer Logo Height (px)', 'brickpoint' ),
    'section'     => 'bp_footer_section',
    'type'        => 'number',
    'input_attrs' => array( 'min' => 20, 'max' => 100, 'step' => 2 ),
  ) );

  $wp_customize->add_setting( 'bp_footer_desc', array(
    'default'           => 'Premium bricks and reliable construction materials for homes, commercial developments, and large-scale building projects.',
    'sanitize_callback' => 'sanitize_textarea_field',
  ) );
  $wp_customize->add_control( 'bp_footer_desc', array(
    'label'   => esc_html__( 'Footer About Text', 'brickpoint' ),
    'section' => 'bp_footer_section',
    'type'    => 'textarea',
  ) );

  // Section 3: Contact Details & WhatsApp
  $wp_customize->add_section( 'bp_contact_section', array(
    'title'    => esc_html__( 'Contact & WhatsApp Numbers', 'brickpoint' ),
    'panel'    => 'bp_theme_panel',
    'priority' => 30,
  ) );

  $wp_customize->add_setting( 'bp_phone_display', array( 'default' => '0315 2850818', 'sanitize_callback' => 'sanitize_text_field' ) );
  $wp_customize->add_control( 'bp_phone_display', array( 'label' => esc_html__( 'Phone (Display Format)', 'brickpoint' ), 'section' => 'bp_contact_section', 'type' => 'text' ) );

  $wp_customize->add_setting( 'bp_whatsapp_number', array( 'default' => '923152850818', 'sanitize_callback' => 'sanitize_text_field' ) );
  $wp_customize->add_control( 'bp_whatsapp_number', array( 'label' => esc_html__( 'WhatsApp Number (Digits with country code, e.g. 923152850818)', 'brickpoint' ), 'section' => 'bp_contact_section', 'type' => 'text' ) );

  $wp_customize->add_setting( 'bp_email', array( 'default' => 'info@brickpoint.pk', 'sanitize_callback' => 'sanitize_email' ) );
  $wp_customize->add_control( 'bp_email', array( 'label' => esc_html__( 'Contact Email', 'brickpoint' ), 'section' => 'bp_contact_section', 'type' => 'text' ) );

  $wp_customize->add_setting( 'bp_address', array( 'default' => 'Lahore, Punjab, Pakistan', 'sanitize_callback' => 'sanitize_text_field' ) );
  $wp_customize->add_control( 'bp_address', array( 'label' => esc_html__( 'Main Office Address', 'brickpoint' ), 'section' => 'bp_contact_section', 'type' => 'text' ) );

  $wp_customize->add_setting( 'bp_ceo', array( 'default' => 'Syed Iftikhar Haider', 'sanitize_callback' => 'sanitize_text_field' ) );
  $wp_customize->add_control( 'bp_ceo', array( 'label' => esc_html__( 'CEO / Contact Person', 'brickpoint' ), 'section' => 'bp_contact_section', 'type' => 'text' ) );

  $wp_customize->add_setting( 'bp_sales', array( 'default' => 'Qasim Iqbal', 'sanitize_callback' => 'sanitize_text_field' ) );
  $wp_customize->add_control( 'bp_sales', array( 'label' => esc_html__( 'Sales Manager', 'brickpoint' ), 'section' => 'bp_contact_section', 'type' => 'text' ) );

  // Section 4: Social Links
  $wp_customize->add_section( 'bp_social_section', array(
    'title'    => esc_html__( 'Social Media Links', 'brickpoint' ),
    'panel'    => 'bp_theme_panel',
    'priority' => 40,
  ) );

  $socials = array(
    'bp_social_facebook'  => 'https://www.facebook.com/brickpoint.pk/',
    'bp_social_instagram' => 'https://www.instagram.com/brickpoint.pk/',
    'bp_social_twitter'   => 'https://x.com/BrickPointPK',
    'bp_social_tiktok'    => 'https://www.tiktok.com/@brickpoint.pk/',
  );
  foreach ( $socials as $k => $def ) {
    $wp_customize->add_setting( $k, array( 'default' => $def, 'sanitize_callback' => 'esc_url_raw' ) );
    $wp_customize->add_control( $k, array( 'label' => ucwords( str_replace( array( 'bp_social_', '_' ), array( '', ' ' ), $k ) ) . ' URL', 'section' => 'bp_social_section', 'type' => 'url' ) );
  }
}
add_action( 'customize_register', 'brickpoint_customize_register' );
"""

# inc/admin-settings.php
files["inc/admin-settings.php"] = """<?php
/**
 * Admin Settings & Setup Menu
 *
 * @package BrickPoint
 */

if ( ! defined( 'ABSPATH' ) ) {
  exit;
}

function brickpoint_add_admin_pages() {
  add_theme_page(
    esc_html__( 'BrickPoint Demo Importer', 'brickpoint' ),
    esc_html__( 'BrickPoint Demo', 'brickpoint' ),
    'manage_options',
    'brickpoint-demo',
    'brickpoint_demo_importer_page'
  );

  add_theme_page(
    esc_html__( 'BrickPoint Settings', 'brickpoint' ),
    esc_html__( 'Theme Settings', 'brickpoint' ),
    'manage_options',
    'brickpoint-settings',
    'brickpoint_settings_page'
  );
}
add_action( 'admin_menu', 'brickpoint_add_admin_pages' );

function brickpoint_settings_page() {
  if ( isset( $_POST['bp_settings_submit'] ) && check_admin_referer( 'bp_settings_action', 'bp_settings_nonce' ) ) {
    update_option( 'bp_phone_display', sanitize_text_field( $_POST['bp_phone_display'] ) );
    update_option( 'bp_whatsapp_number', sanitize_text_field( $_POST['bp_whatsapp_number'] ) );
    update_option( 'bp_email', sanitize_email( $_POST['bp_email'] ) );
    update_option( 'bp_address', sanitize_text_field( $_POST['bp_address'] ) );
    echo '<div class="updated notice is-dismissible"><p>Settings saved successfully!</p></div>';
  }

  $phone = bp_option( 'bp_phone_display', '0315 2850818' );
  $wa = bp_option( 'bp_whatsapp_number', '923152850818' );
  $email = bp_option( 'bp_email', 'info@brickpoint.pk' );
  $addr = bp_option( 'bp_address', 'Lahore, Punjab, Pakistan' );
  ?>
  <div class="wrap">
    <h1><?php esc_html_e( 'BrickPoint Theme Settings', 'brickpoint' ); ?></h1>
    <form method="post" action="">
      <?php wp_nonce_field( 'bp_settings_action', 'bp_settings_nonce' ); ?>
      <table class="form-table">
        <tr>
          <th><label for="bp_phone_display"><?php esc_html_e( 'Phone (Display)', 'brickpoint' ); ?></label></th>
          <td><input type="text" name="bp_phone_display" id="bp_phone_display" value="<?php echo esc_attr( $phone ); ?>" class="regular-text" /></td>
        </tr>
        <tr>
          <th><label for="bp_whatsapp_number"><?php esc_html_e( 'WhatsApp Digits (with country code)', 'brickpoint' ); ?></label></th>
          <td><input type="text" name="bp_whatsapp_number" id="bp_whatsapp_number" value="<?php echo esc_attr( $wa ); ?>" class="regular-text" /><p class="description">e.g. 923152850818</p></td>
        </tr>
        <tr>
          <th><label for="bp_email"><?php esc_html_e( 'Email', 'brickpoint' ); ?></label></th>
          <td><input type="email" name="bp_email" id="bp_email" value="<?php echo esc_attr( $email ); ?>" class="regular-text" /></td>
        </tr>
        <tr>
          <th><label for="bp_address"><?php esc_html_e( 'Office Address', 'brickpoint' ); ?></label></th>
          <td><input type="text" name="bp_address" id="bp_address" value="<?php echo esc_attr( $addr ); ?>" class="regular-text" /></td>
        </tr>
      </table>
      <p class="submit">
        <input type="submit" name="bp_settings_submit" class="button button-primary" value="<?php esc_attr_e( 'Save Changes', 'brickpoint' ); ?>" />
      </p>
    </form>
  </div>
  <?php
}
"""

# inc/elementor.php
files["inc/elementor.php"] = """<?php
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
"""

# inc/ajax-handlers.php
files["inc/ajax-handlers.php"] = """<?php
/**
 * AJAX Handlers for Demo Importer
 *
 * @package BrickPoint
 */

if ( ! defined( 'ABSPATH' ) ) {
  exit;
}

function brickpoint_ajax_run_demo_import() {
  check_ajax_referer( 'bp_demo_import_nonce', 'nonce' );

  if ( ! current_user_can( 'manage_options' ) ) {
    wp_send_json_error( array( 'message' => 'Unauthorized permissions.' ) );
  }

  $step = isset( $_POST['step'] ) ? sanitize_text_field( $_POST['step'] ) : 'all';

  $result = brickpoint_run_demo_import_step( $step );

  if ( is_wp_error( $result ) ) {
    wp_send_json_error( array( 'message' => $result->get_error_message() ) );
  }

  wp_send_json_success( $result );
}
add_action( 'wp_ajax_brickpoint_run_demo_import', 'brickpoint_ajax_run_demo_import' );
"""

# Write all inc files
for rel_path, content in files.items():
    full_path = os.path.join(DEST, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")

print(f"Wrote {len(files)} include PHP files successfully.")
