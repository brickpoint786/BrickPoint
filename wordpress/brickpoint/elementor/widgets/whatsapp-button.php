<?php
if ( ! defined( 'ABSPATH' ) ) { exit; }
class BrickPoint_WhatsApp_Button extends \Elementor\Widget_Base {
  public function get_name() { return 'bp-whatsapp-button'; }
  public function get_title() { return __( 'BP WhatsApp Button', 'brickpoint' ); }
  public function get_icon() { return 'eicon-button'; }
  public function get_categories() { return array( 'brickpoint' ); }
  protected function register_controls() {
    $this->start_controls_section( 's', array( 'label' => __( 'Settings', 'brickpoint' ) ) );
    $this->add_control( 'label', array( 'label' => __( 'Label', 'brickpoint' ), 'type' => \Elementor\Controls_Manager::TEXT, 'default' => 'Order on WhatsApp' ) );
    $this->add_control( 'message', array( 'label' => __( 'Message (blank = product-aware default)', 'brickpoint' ), 'type' => \Elementor\Controls_Manager::TEXTAREA, 'default' => '' ) );
    $this->add_control( 'style', array( 'label' => __( 'Style', 'brickpoint' ), 'type' => \Elementor\Controls_Manager::SELECT, 'default' => 'btn-whatsapp', 'options' => array( 'btn-whatsapp' => 'WhatsApp', 'btn-brick' => 'Brick', 'btn-dark' => 'Dark', 'btn-ghost' => 'Ghost' ) ) );
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
