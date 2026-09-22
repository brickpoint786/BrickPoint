<?php
if ( ! defined( 'ABSPATH' ) ) { exit; }
class BrickPoint_Product_Categories extends \Elementor\Widget_Base {
  public function get_name() { return 'bp-product-categories'; }
  public function get_title() { return __( 'BP Product Categories', 'brickpoint' ); }
  public function get_icon() { return 'eicon-gallery-grid'; }
  public function get_categories() { return array( 'brickpoint' ); }
  protected function register_controls() {
    $this->start_controls_section( 'q', array( 'label' => __( 'Settings', 'brickpoint' ) ) );
    $this->add_control( 'count', array( 'label' => __( 'Number', 'brickpoint' ), 'type' => \Elementor\Controls_Manager::NUMBER, 'default' => 8 ) );
    $this->add_control( 'columns', array( 'label' => __( 'Columns', 'brickpoint' ), 'type' => \Elementor\Controls_Manager::SELECT, 'default' => '4', 'options' => array( '2' => '2', '3' => '3', '4' => '4' ) ) );
    $this->end_controls_section();
  }
  protected function render() {
    $s = $this->get_settings_for_display();
    $cats = get_terms( array( 'taxonomy' => 'bp_product_category', 'number' => absint( $s['count'] ), 'hide_empty' => false ) );
    if ( ! $cats || is_wp_error( $cats ) ) { return; }
    echo '<div class="bp-grid cols-' . esc_attr( $s['columns'] ) . '">';
    foreach ( $cats as $t ) {
      $img = get_term_meta( $t->term_id, 'bp_cat_image', true );
      echo '<a class="bp-cat-card" href="' . esc_url( get_term_link( $t ) ) . '">';
      if ( $img ) { echo '<img src="' . esc_url( $img ) . '" alt="' . esc_attr( $t->name ) . '" loading="lazy" />'; }
      echo '<span class="bp-card-body"><strong>' . esc_html( $t->name ) . '</strong><br><small>' . esc_html( wp_trim_words( $t->description, 12 ) ) . '</small></span></a>';
    }
    echo '</div>';
  }
}
