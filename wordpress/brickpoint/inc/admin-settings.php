<?php
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
