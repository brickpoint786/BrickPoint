<?php
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
