<?php
if ( ! defined( 'ABSPATH' ) ) { exit; }
class BrickPoint_Video_Card extends \Elementor\Widget_Base {
  public function get_name() { return 'bp-video-card'; }
  public function get_title() { return __( 'BP Video Card (current)', 'brickpoint' ); }
  public function get_icon() { return 'eicon-play'; }
  public function get_categories() { return array( 'brickpoint' ); }
  protected function register_controls() {
    $this->start_controls_section( 's', array( 'label' => __( 'Settings', 'brickpoint' ) ) );
    $this->add_control( 'embed', array( 'label' => __( 'Show player instead of card', 'brickpoint' ), 'type' => \Elementor\Controls_Manager::SWITCHER, 'default' => '' ) );
    $this->end_controls_section();
  }
  protected function render() {
    $s = $this->get_settings_for_display();
    if ( ! empty( $s['embed'] ) ) { echo bp_video_embed_html( get_the_ID() ); return; }
    get_template_part( 'template-parts/video-card' );
  }
}
