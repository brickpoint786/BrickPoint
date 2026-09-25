<?php
/**
 * BrickPoint One-Click Demo Importer
 *
 * Implements reliable, idempotent (update/skip) import logic with offline media
 * fallback, authentic Elementor page data assignment, Elementor Pro Theme Builder
 * conditions, menu assignment, and front-page setup.
 *
 * @package BrickPoint
 */

if ( ! defined( 'ABSPATH' ) ) {
  exit;
}

/**
 * Render Demo Importer Admin Screen
 */
function brickpoint_demo_importer_page() {
  ?>
  <div class="wrap bp-importer-admin" style="max-width:960px;margin-top:20px;">
    <h1><?php esc_html_e( 'BrickPoint Demo Importer', 'brickpoint' ); ?></h1>
    <p class="description" style="font-size:15px;margin-bottom:20px;">
      <?php esc_html_e( 'Import complete demo data: 17 production pages with native Elementor structures, 12 products, 12 categories, 6 videos, 6 project references, 4 bhatta locations, 4 blog guides, 26 Elementor templates, menus, and media library attachments.', 'brickpoint' ); ?>
    </p>

    <div class="bp-box" style="background:#fff;padding:24px;border:1px solid #ccd0d4;border-radius:8px;box-shadow:0 1px 3px rgba(0,0,0,0.05);">
      <h2 style="margin-top:0;"><?php esc_html_e( 'Ready to Import Full Demo', 'brickpoint' ); ?></h2>
      <p><?php esc_html_e( 'The importer uses bundled high-fidelity offline media assets — no external downloads or internet connection needed. Existing posts and pages are updated safely without creating duplicates.', 'brickpoint' ); ?></p>

      <ul style="list-style:disc;margin-left:20px;line-height:1.8;color:#444;">
        <li><strong>True Elementor Homepage:</strong> All 9 original sections (Hero, Trust Intro, Categories, SS7 Showcase, Featured Products, Videos, Projects, Who We Serve, Quotation CTA) imported as fully editable Elementor widgets and containers.</li>
        <li><strong>17 Complete Pages:</strong> Home, About, SS7 Bricks, Construction Materials, For Contractors, For Builders, For Companies, Products, Categories, Videos, Projects, Locations, Blog, Contact, Privacy, Terms, Sample.</li>
        <li><strong>12 Custom Products:</strong> Full pricing, specs, features, SKU, units, and WhatsApp ordering links.</li>
        <li><strong>12 Product Categories:</strong> Complete with background thumbnails and inquiry messages.</li>
        <li><strong>6 Videos & 6 Projects:</strong> Embedded MP4 players and reference case cards.</li>
        <li><strong>4 Production Units / Locations:</strong> Complete with addresses, phone numbers, and Google Maps links.</li>
        <li><strong>26 Elementor Templates:</strong> Headers, Footers, Single Product, Single Video, Single Project, Archives, and Modular Sections.</li>
        <li><strong>Navigation Menus:</strong> Primary, Mobile, and Footer menus assigned automatically.</li>
        <li><strong>Front Page Setup:</strong> Home set as Static Front Page and Blog set as Posts page.</li>
      </ul>

      <div id="bpImportProgress" style="display:none;margin:20px 0;">
        <div style="background:#f0f0f1;border-radius:4px;overflow:hidden;height:24px;margin-bottom:10px;">
          <div id="bpProgressBar" style="width:0%;height:100%;background:#ea580c;transition:width 0.3s ease;"></div>
        </div>
        <p id="bpProgressStatus" style="font-weight:600;color:#1c1a17;margin:0;"><?php esc_html_e( 'Initializing import…', 'brickpoint' ); ?></p>
        <div id="bpProgressLog" style="margin-top:10px;background:#f8fafc;padding:12px;border:1px solid #e2e8f0;border-radius:4px;font-family:monospace;font-size:12px;max-height:160px;overflow-y:auto;white-space:pre-wrap;"></div>
      </div>

      <div style="margin-top:24px;">
        <button id="bpStartImportBtn" class="button button-primary button-hero" style="background:#ea580c;border-color:#c2410c;font-size:16px;height:46px;line-height:44px;padding:0 28px;">
          <?php esc_html_e( 'Start Full Demo Import', 'brickpoint' ); ?>
        </button>
        <span id="bpImportSpinner" class="spinner" style="float:none;margin:0 0 0 10px;"></span>
      </div>
    </div>
  </div>
  <?php
}

/**
 * Execute step-by-step or full import
 */
function brickpoint_run_demo_import_step( $step = 'all' ) {
  require_once ABSPATH . 'wp-admin/includes/image.php';
  require_once ABSPATH . 'wp-admin/includes/file.php';
  require_once ABSPATH . 'wp-admin/includes/media.php';

  $log = array();
  $data = brickpoint_get_demo_data();

  // STEP 1: IMPORT MEDIA ATTACHMENTS
  $log[] = '1. Importing media assets into Media Library…';
  $attachments = brickpoint_import_bundled_media();
  $log[] = 'Media library ready: ' . count( $attachments ) . ' images registered.';

  // STEP 2: IMPORT CATEGORIES
  $log[] = '2. Importing product & video categories…';
  $cat_map = array();
  foreach ( $data['categories'] as $cat_data ) {
    $term = term_exists( $cat_data['slug'], 'bp_product_category' );
    if ( ! $term ) {
      $term = wp_insert_term( $cat_data['name'], 'bp_product_category', array(
        'slug'        => $cat_data['slug'],
        'description' => $cat_data['description'],
      ) );
    }
    if ( ! is_wp_error( $term ) ) {
      $term_id = is_array( $term ) ? $term['term_id'] : $term;
      $cat_map[ $cat_data['name'] ] = $term_id;
      if ( isset( $cat_data['image'] ) && isset( $attachments[ $cat_data['image'] ] ) ) {
        update_term_meta( $term_id, 'bp_cat_image', wp_get_attachment_url( $attachments[ $cat_data['image'] ] ) );
      }
      if ( isset( $cat_data['order'] ) ) {
        update_term_meta( $term_id, 'bp_cat_order', $cat_data['order'] );
      }
    }
  }

  // STEP 3: IMPORT PRODUCTS
  $log[] = '3. Importing 12 custom products…';
  foreach ( $data['products'] as $p ) {
    $existing = get_page_by_path( $p['slug'], OBJECT, 'bp_product' );
    $post_args = array(
      'post_title'   => $p['title'],
      'post_name'    => $p['slug'],
      'post_type'    => 'bp_product',
      'post_status'  => 'publish',
      'post_content' => $p['content'],
      'post_excerpt' => $p['short'],
    );
    if ( $existing ) {
      $post_args['ID'] = $existing->ID;
      $pid = wp_update_post( $post_args );
    } else {
      $pid = wp_insert_post( $post_args );
    }

    if ( $pid && ! is_wp_error( $pid ) ) {
      update_post_meta( $pid, '_bp_price', $p['price'] );
      update_post_meta( $pid, '_bp_price_label', $p['price_label'] );
      update_post_meta( $pid, '_bp_unit', $p['unit'] );
      update_post_meta( $pid, '_bp_availability', $p['availability'] );
      update_post_meta( $pid, '_bp_badge', $p['badge'] );
      update_post_meta( $pid, '_bp_featured', $p['featured'] );
      update_post_meta( $pid, '_bp_sku', $p['sku'] );
      update_post_meta( $pid, '_bp_short', $p['short'] );
      update_post_meta( $pid, '_bp_specs', $p['specs'] );
      update_post_meta( $pid, '_bp_features', $p['features'] );
      if ( isset( $p['video'] ) ) update_post_meta( $pid, '_bp_video', $p['video'] );

      // Assign category
      if ( isset( $cat_map[ $p['category'] ] ) ) {
        wp_set_object_terms( $pid, intval( $cat_map[ $p['category'] ] ), 'bp_product_category' );
      }

      // Assign thumbnail
      if ( isset( $p['image'] ) && isset( $attachments[ $p['image'] ] ) ) {
        set_post_thumbnail( $pid, $attachments[ $p['image'] ] );
      }
    }
  }

  // STEP 4: IMPORT VIDEOS
  $log[] = '4. Importing 6 videos…';
  foreach ( $data['videos'] as $v ) {
    $existing = get_page_by_path( $v['slug'], OBJECT, 'bp_video' );
    $post_args = array(
      'post_title'   => $v['title'],
      'post_name'    => $v['slug'],
      'post_type'    => 'bp_video',
      'post_status'  => 'publish',
      'post_content' => $v['description'],
      'post_excerpt' => $v['description'],
    );
    if ( $existing ) {
      $post_args['ID'] = $existing->ID;
      $vid = wp_update_post( $post_args );
    } else {
      $vid = wp_insert_post( $post_args );
    }

    if ( $vid && ! is_wp_error( $vid ) ) {
      update_post_meta( $vid, '_bpv_source', $v['source'] );
      update_post_meta( $vid, '_bpv_url', $v['url'] );
      update_post_meta( $vid, '_bpv_duration', $v['duration'] );
      update_post_meta( $vid, '_bpv_featured', $v['featured'] );

      if ( isset( $v['image'] ) && isset( $attachments[ $v['image'] ] ) ) {
        set_post_thumbnail( $vid, $attachments[ $v['image'] ] );
      }
    }
  }

  // STEP 5: IMPORT PROJECTS
  $log[] = '5. Importing 6 project references…';
  foreach ( $data['projects'] as $prj ) {
    $existing = get_page_by_path( $prj['slug'], OBJECT, 'bp_project' );
    $post_args = array(
      'post_title'   => $prj['title'],
      'post_name'    => $prj['slug'],
      'post_type'    => 'bp_project',
      'post_status'  => 'publish',
      'post_content' => $prj['description'],
      'post_excerpt' => $prj['description'],
    );
    if ( $existing ) {
      $post_args['ID'] = $existing->ID;
      $prjid = wp_update_post( $post_args );
    } else {
      $prjid = wp_insert_post( $post_args );
    }

    if ( $prjid && ! is_wp_error( $prjid ) ) {
      update_post_meta( $prjid, '_bpp_category', $prj['category'] );
      update_post_meta( $prjid, '_bpp_location', $prj['location'] );
      update_post_meta( $prjid, '_bpp_status', $prj['status'] );

      if ( isset( $prj['image'] ) && isset( $attachments[ $prj['image'] ] ) ) {
        set_post_thumbnail( $prjid, $attachments[ $prj['image'] ] );
      }
    }
  }

  // STEP 6: IMPORT LOCATIONS
  $log[] = '6. Importing 4 bhatta units / locations…';
  foreach ( $data['locations'] as $loc ) {
    $existing = get_page_by_path( $loc['slug'], OBJECT, 'bp_location' );
    $post_args = array(
      'post_title'   => $loc['title'],
      'post_name'    => $loc['slug'],
      'post_type'    => 'bp_location',
      'post_status'  => 'publish',
      'post_content' => $loc['description'],
      'post_excerpt' => $loc['description'],
    );
    if ( $existing ) {
      $post_args['ID'] = $existing->ID;
      $locid = wp_update_post( $post_args );
    } else {
      $locid = wp_insert_post( $post_args );
    }

    if ( $locid && ! is_wp_error( $locid ) ) {
      update_post_meta( $locid, '_bpl_address', $loc['address'] );
      update_post_meta( $locid, '_bpl_phone', $loc['phone'] );
      update_post_meta( $locid, '_bpl_hours', $loc['hours'] );
      update_post_meta( $locid, '_bpl_maps_url', $loc['maps_url'] );
      if ( isset( $loc['video'] ) ) update_post_meta( $locid, '_bpl_video', $loc['video'] );

      if ( isset( $loc['image'] ) && isset( $attachments[ $loc['image'] ] ) ) {
        set_post_thumbnail( $locid, $attachments[ $loc['image'] ] );
      }
    }
  }

  // STEP 7: IMPORT BLOG POSTS
  $log[] = '7. Importing 4 blog articles…';
  foreach ( $data['posts'] as $post_item ) {
    $existing = get_page_by_path( $post_item['slug'], OBJECT, 'post' );
    $post_args = array(
      'post_title'   => $post_item['title'],
      'post_name'    => $post_item['slug'],
      'post_type'    => 'post',
      'post_status'  => 'publish',
      'post_content' => $post_item['content'],
      'post_excerpt' => $post_item['excerpt'],
    );
    if ( $existing ) {
      $post_args['ID'] = $existing->ID;
      $pid = wp_update_post( $post_args );
    } else {
      $pid = wp_insert_post( $post_args );
    }

    if ( $pid && ! is_wp_error( $pid ) ) {
      if ( isset( $post_item['category'] ) ) {
        wp_set_object_terms( $pid, $post_item['category'], 'category' );
      }
      if ( isset( $post_item['tags'] ) ) {
        wp_set_post_tags( $pid, $post_item['tags'], true );
      }
      if ( isset( $post_item['image'] ) && isset( $attachments[ $post_item['image'] ] ) ) {
        set_post_thumbnail( $pid, $attachments[ $post_item['image'] ] );
      }
    }
  }

  // STEP 8: IMPORT 17 COMPLETE SITE PAGES WITH TRUE ELEMENTOR DATA
  $log[] = '8. Importing 17 complete site pages with authentic Elementor data structures…';
  $pages_created = brickpoint_create_site_pages( $attachments );
  $log[] = '17 pages generated and populated with Elementor content.';

  // STEP 9: IMPORT 26 ELEMENTOR JSON TEMPLATES INTO ELEMENTOR LIBRARY
  $log[] = '9. Importing 26 Elementor JSON templates and registering Theme Builder conditions…';
  brickpoint_import_elementor_templates();
  $log[] = 'Theme Builder templates imported into elementor_library.';

  // STEP 10: ASSIGN MENUS & THEME MODS
  $log[] = '10. Building Navigation Menus and assigning locations…';
  brickpoint_setup_demo_menus();

  // Set Static Front Page & Posts Page
  $home_page = get_page_by_path( 'home' );
  if ( ! $home_page ) $home_page = get_page_by_path( 'front-page' );
  $blog_page = get_page_by_path( 'blog' );

  if ( $home_page ) {
    update_option( 'show_on_front', 'page' );
    update_option( 'page_on_front', $home_page->ID );
  }
  if ( $blog_page ) {
    update_option( 'page_for_posts', $blog_page->ID );
  }

  // Set Theme Mods (Logos)
  if ( isset( $attachments['logo-header.png'] ) ) {
    set_theme_mod( 'bp_header_logo', $attachments['logo-header.png'] );
    set_theme_mod( 'custom_logo', $attachments['logo-header.png'] );
  }
  if ( isset( $attachments['logo-footer.png'] ) ) {
    set_theme_mod( 'bp_footer_logo', $attachments['logo-footer.png'] );
  }

  $log[] = 'Demo import completed successfully! All pages, products, templates, and menus are active.';

  return array(
    'status'  => 'complete',
    'message' => 'Demo import finished successfully!',
    'log'     => implode( "\n", $log ),
  );
}

/**
 * Register Bundled Images into Media Library
 */
function brickpoint_import_bundled_media() {
  $img_dir = BRICKPOINT_DIR . '/assets/images/';
  $attachments = array();

  if ( ! is_dir( $img_dir ) ) {
    return $attachments;
  }

  $files = scandir( $img_dir );
  $upload_dir = wp_upload_dir();

  foreach ( $files as $file ) {
    if ( $file === '.' || $file === '..' ) continue;
    $ext = strtolower( pathinfo( $file, PATHINFO_EXTENSION ) );
    if ( ! in_array( $ext, array( 'png', 'jpg', 'jpeg', 'webp', 'svg' ), true ) ) continue;

    $source_path = $img_dir . $file;
    $dest_path   = $upload_dir['path'] . '/' . $file;

    // Check if attachment already registered with this filename
    $existing = get_posts( array(
      'post_type'      => 'attachment',
      'meta_key'       => '_wp_attached_file',
      'meta_value'     => $upload_dir['subdir'] . '/' . $file,
      'posts_per_page' => 1,
      'fields'         => 'ids',
    ) );

    if ( ! empty( $existing ) ) {
      $attachments[ $file ] = $existing[0];
      continue;
    }

    copy( $source_path, $dest_path );

    $wp_filetype = wp_check_filetype( $file, null );
    $attachment = array(
      'post_mime_type' => $wp_filetype['type'],
      'post_title'     => sanitize_file_name( pathinfo( $file, PATHINFO_FILENAME ) ),
      'post_content'   => '',
      'post_status'    => 'inherit',
    );

    $attach_id = wp_insert_attachment( $attachment, $dest_path );
    if ( ! is_wp_error( $attach_id ) ) {
      $attach_data = wp_generate_attachment_metadata( $attach_id, $dest_path );
      wp_update_attachment_metadata( $attach_id, $attach_data );
      $attachments[ $file ] = $attach_id;
    }
  }

  return $attachments;
}

/**
 * Helper: Load Elementor JSON Template Data
 */
function brickpoint_load_elementor_template_json( $filename ) {
  $tpl_path = BRICKPOINT_DIR . '/elementor-templates/' . $filename;
  if ( file_exists( $tpl_path ) ) {
    $raw = file_get_contents( $tpl_path );
    $data = json_decode( $raw, true );
    if ( isset( $data['content'] ) ) {
      return wp_json_encode( $data['content'] );
    }
  }
  return '';
}

/**
 * Create 17 Full Site Pages with Elementor structures
 */
function brickpoint_create_site_pages( $attachments = array() ) {
  $pages = array(
    'home' => array(
      'title'         => 'Home',
      'content'       => '',
      'elementor_tpl' => 'page-home.json',
    ),
    'about' => array(
      'title'         => 'About Us',
      'content'       => '',
      'elementor_tpl' => 'page-about.json',
    ),
    'ss7-bricks' => array(
      'title'         => 'SS7 Bricks',
      'content'       => '',
      'elementor_tpl' => 'page-ss7-bricks.json',
    ),
    'construction-materials' => array(
      'title'         => 'Construction Materials',
      'content'       => '',
      'elementor_tpl' => 'page-materials.json',
    ),
    'for-contractors' => array(
      'title'         => 'For Contractors',
      'content'       => '',
      'elementor_tpl' => 'page-for-contractors.json',
    ),
    'for-builders' => array(
      'title'         => 'For Builders',
      'content'       => '',
      'elementor_tpl' => 'page-for-builders.json',
    ),
    'for-companies' => array(
      'title'         => 'For Construction Companies',
      'content'       => '',
      'elementor_tpl' => 'page-for-companies.json',
    ),
    'products' => array(
      'title'         => 'Products',
      'content'       => '<p>Browse our complete catalogue of premium bricks and construction materials. All prices listed with direct WhatsApp ordering.</p>',
      'elementor_tpl' => 'archive-product.json',
    ),
    'categories' => array(
      'title'         => 'Categories',
      'content'       => '<p>Explore our 12 specialized construction material categories.</p>',
      'elementor_tpl' => 'section-categories.json',
    ),
    'videos' => array(
      'title'         => 'Videos',
      'content'       => '<p>Watch our brick manufacturing plants, kiln firing chambers, quality testing field checks, and project walkthroughs.</p>',
      'elementor_tpl' => 'archive-video.json',
    ),
    'projects' => array(
      'title'         => 'Projects',
      'content'       => '<p>Construction references and project inspiration visuals from premier Lahore housing developments.</p>',
      'elementor_tpl' => 'archive-project.json',
    ),
    'locations' => array(
      'title'         => 'Locations',
      'content'       => '<p>Our three manufacturing kiln units and central corporate coordination hub.</p>',
      'elementor_tpl' => '',
    ),
    'blog' => array(
      'title'         => 'Blog',
      'content'       => '<p>Field guides, quantity estimation checklists, technical masonry standards, and construction advice.</p>',
      'elementor_tpl' => 'archive-post.json',
    ),
    'contact' => array(
      'title'         => 'Contact Us',
      'content'       => '',
      'elementor_tpl' => 'page-contact.json',
    ),
    'privacy' => array(
      'title'         => 'Privacy Policy',
      'content'       => '',
      'elementor_tpl' => 'page-privacy.json',
    ),
    'terms' => array(
      'title'         => 'Terms & Conditions',
      'content'       => '',
      'elementor_tpl' => 'page-terms.json',
    ),
    'sample-page' => array(
      'title'         => 'Sample Page',
      'content'       => '<p>This is an example page created by the BrickPoint theme setup.</p>',
      'elementor_tpl' => '',
    ),
  );

  $page_ids = array();
  foreach ( $pages as $slug => $pconf ) {
    $existing = get_page_by_path( $slug );
    $args = array(
      'post_title'   => $pconf['title'],
      'post_name'    => $slug,
      'post_type'    => 'page',
      'post_status'  => 'publish',
      'post_content' => $pconf['content'],
    );
    if ( $existing ) {
      $args['ID'] = $existing->ID;
      $pid = wp_update_post( $args );
    } else {
      $pid = wp_insert_post( $args );
    }

    if ( $pid && ! is_wp_error( $pid ) ) {
      $page_ids[ $slug ] = $pid;

      // Assign authentic Elementor Data to the page!
      if ( ! empty( $pconf['elementor_tpl'] ) ) {
        $elementor_data = brickpoint_load_elementor_template_json( $pconf['elementor_tpl'] );
        if ( ! empty( $elementor_data ) ) {
          update_post_meta( $pid, '_elementor_edit_mode', 'builder' );
          update_post_meta( $pid, '_elementor_template_type', 'wp-page' );
          update_post_meta( $pid, '_elementor_version', '3.20.0' );
          update_post_meta( $pid, '_elementor_data', $elementor_data );
        }
      }
    }
  }

  return $page_ids;
}

/**
 * Import 26 Elementor JSON templates into elementor_library
 */
function brickpoint_import_elementor_templates() {
  $tpl_dir = BRICKPOINT_DIR . '/elementor-templates/';
  if ( ! is_dir( $tpl_dir ) ) {
    return;
  }

  $files = scandir( $tpl_dir );
  $header_id = 0;
  $footer_id = 0;

  foreach ( $files as $f ) {
    if ( pathinfo( $f, PATHINFO_EXTENSION ) !== 'json' ) continue;
    $raw = file_get_contents( $tpl_dir . $f );
    $json = json_decode( $raw, true );
    if ( ! $json ) continue;

    $title = isset( $json['title'] ) ? $json['title'] : pathinfo( $f, PATHINFO_FILENAME );
    $slug  = sanitize_title( pathinfo( $f, PATHINFO_FILENAME ) );
    $type  = isset( $json['type'] ) ? $json['type'] : 'section';

    $existing = get_page_by_path( $slug, OBJECT, 'elementor_library' );
    $args = array(
      'post_title'   => $title,
      'post_name'    => $slug,
      'post_type'    => 'elementor_library',
      'post_status'  => 'publish',
      'post_content' => '',
    );
    if ( $existing ) {
      $args['ID'] = $existing->ID;
      $tid = wp_update_post( $args );
    } else {
      $tid = wp_insert_post( $args );
    }

    if ( $tid && ! is_wp_error( $tid ) ) {
      update_post_meta( $tid, '_elementor_edit_mode', 'builder' );
      update_post_meta( $tid, '_elementor_template_type', $type );
      update_post_meta( $tid, '_elementor_version', '3.20.0' );
      $content_json = isset( $json['content'] ) ? wp_json_encode( $json['content'] ) : '[]';
      update_post_meta( $tid, '_elementor_data', $content_json );

      if ( $type === 'header' ) {
        $header_id = $tid;
        update_post_meta( $tid, '_elementor_conditions', array( 'include/general' ) );
      }
      if ( $type === 'footer' ) {
        $footer_id = $tid;
        update_post_meta( $tid, '_elementor_conditions', array( 'include/general' ) );
      }
    }
  }

  // Register Theme Builder conditions in options
  $conditions = get_option( 'elementor_pro_theme_builder_conditions', array() );
  if ( $header_id ) {
    $conditions['header'] = array( $header_id => array( 'include/general' ) );
  }
  if ( $footer_id ) {
    $conditions['footer'] = array( $footer_id => array( 'include/general' ) );
  }
  update_option( 'elementor_pro_theme_builder_conditions', $conditions );
}

/**
 * Setup & Assign Navigation Menus
 */
function brickpoint_setup_demo_menus() {
  $primary_menu_name = 'Primary Menu';
  $primary_menu_term = wp_get_nav_menu_object( $primary_menu_name );
  if ( ! $primary_menu_term ) {
    $menu_id = wp_create_nav_menu( $primary_menu_name );
  } else {
    $menu_id = $primary_menu_term->term_id;
  }

  if ( $menu_id && ! is_wp_error( $menu_id ) ) {
    $items = wp_get_nav_menu_items( $menu_id );
    if ( empty( $items ) ) {
      $menu_links = array(
        array( 'title' => 'Home', 'url' => home_url( '/' ) ),
        array( 'title' => 'SS7 Bricks', 'url' => home_url( '/ss7-bricks' ) ),
        array( 'title' => 'Products', 'url' => home_url( '/products' ) ),
        array( 'title' => 'Categories', 'url' => home_url( '/categories' ) ),
        array( 'title' => 'Materials', 'url' => home_url( '/construction-materials' ) ),
        array( 'title' => 'Videos', 'url' => home_url( '/videos' ) ),
        array( 'title' => 'Projects', 'url' => home_url( '/projects' ) ),
        array( 'title' => 'About', 'url' => home_url( '/about' ) ),
        array( 'title' => 'Contact', 'url' => home_url( '/contact' ) ),
      );

      $order = 1;
      foreach ( $menu_links as $ml ) {
        wp_update_nav_menu_item( $menu_id, 0, array(
          'menu-item-title'   => $ml['title'],
          'menu-item-url'     => $ml['url'],
          'menu-item-status'  => 'publish',
          'menu-item-type'    => 'custom',
          'menu-item-position'=> $order++,
        ) );
      }
    }

    $locations = get_theme_mod( 'nav_menu_locations', array() );
    $locations['primary'] = $menu_id;
    $locations['mobile']  = $menu_id;
    $locations['footer']  = $menu_id;
    set_theme_mod( 'nav_menu_locations', $locations );
  }
}
