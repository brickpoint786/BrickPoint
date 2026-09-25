<?php
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
