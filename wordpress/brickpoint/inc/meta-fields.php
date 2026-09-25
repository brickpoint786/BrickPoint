<?php
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
