<?php
if ( ! defined( 'ABSPATH' ) ) { exit; }
class BrickPoint_Social_Links extends \Elementor\Widget_Base {
  public function get_name() { return 'bp-social-links'; }
  public function get_title() { return __( 'BP Social Links', 'brickpoint' ); }
  public function get_icon() { return 'eicon-social-icons'; }
  public function get_categories() { return array( 'brickpoint' ); }
  protected function register_controls() {
    $this->start_controls_section( 's', array( 'label' => __( 'Settings', 'brickpoint' ) ) );
    $this->add_control( 'note', array( 'type' => \Elementor\Controls_Manager::RAW_HTML, 'raw' => __( 'URLs come from Customize → BrickPoint: Social Links.', 'brickpoint' ) ) );
    $this->end_controls_section();
  }
  protected function render() { get_template_part( 'template-parts/social-links' ); }
}
