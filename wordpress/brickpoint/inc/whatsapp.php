<?php
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
    $message = "Assalam-o-Alaikum BrickPoint,\n\nI am interested in getting a quotation for construction materials.\n\nThank you.";
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

  $msg  = "Assalam-o-Alaikum BrickPoint,\n\n";
  $msg .= "I am interested in ordering/inquiring about the following product:\n";
  $msg .= "*Product:* " . $product . "\n";
  if ( $category ) {
    $msg .= "*Category:* " . $category . "\n";
  }
  if ( $price ) {
    $msg .= "*Listed Rate:* " . $price . ( $unit ? " / " . $unit : "" ) . "\n";
  }
  $msg .= "\nPlease share availability, bulk delivery options to my location, and payment terms.\n\n";
  $msg .= "Thank you.";

  return $msg;
}

/**
 * Category Inquiry WhatsApp Template
 */
function bp_category_inquiry_message( $category_name = 'Materials' ) {
  $msg  = "Assalam-o-Alaikum BrickPoint,\n\n";
  $msg .= "I am inquiring about *{$category_name}*.\n";
  $msg .= "Please share the current rate list, available grades/specifications, and delivery terms.\n\n";
  $msg .= "Thank you.";
  return $msg;
}
