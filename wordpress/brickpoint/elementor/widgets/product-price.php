<?php
if ( ! defined( 'ABSPATH' ) ) { exit; }
class BrickPoint_Product_Price extends \Elementor\Widget_Base {
  public function get_name() { return 'bp-product-price'; }
  public function get_title() { return __( 'BP Product Price', 'brickpoint' ); }
  public function get_icon() { return 'eicon-price-table'; }
  public function get_categories() { return array( 'brickpoint' ); }
  protected function register_controls() {
    $this->start_controls_section( 's', array( 'label' => __( 'Settings', 'brickpoint' ) ) );
    $this->add_control( 'show_unit', array( 'label' => __( 'Show unit', 'brickpoint' ), 'type' => \Elementor\Controls_Manager::SWITCHER, 'default' => 'yes' ) );
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
