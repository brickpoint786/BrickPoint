<?php
if ( ! defined( 'ABSPATH' ) ) { exit; }
class BrickPoint_Location_Cards extends \Elementor\Widget_Base {
  public function get_name() { return 'bp-location-cards'; }
  public function get_title() { return __( 'BP Location Cards', 'brickpoint' ); }
  public function get_icon() { return 'eicon-google-maps'; }
  public function get_categories() { return array( 'brickpoint' ); }
  protected function register_controls() {
    $this->start_controls_section( 'q', array( 'label' => __( 'Settings', 'brickpoint' ) ) );
    $this->add_control( 'count', array( 'label' => __( 'Number', 'brickpoint' ), 'type' => \Elementor\Controls_Manager::NUMBER, 'default' => 4 ) );
    $this->add_control( 'columns', array( 'label' => __( 'Columns', 'brickpoint' ), 'type' => \Elementor\Controls_Manager::SELECT, 'default' => '2', 'options' => array( '1' => '1', '2' => '2', '3' => '3', '4' => '4' ) ) );
    $this->end_controls_section();
  }
  protected function render() {
    $s = $this->get_settings_for_display();
    $q = new WP_Query( array( 'post_type' => 'bp_location', 'posts_per_page' => absint( $s['count'] ), 'orderby' => 'meta_value_num', 'meta_key' => '_bpl_order', 'order' => 'ASC' ) );
    echo '<div class="bp-grid cols-' . esc_attr( $s['columns'] ) . '">';
    while ( $q->have_posts() ) { $q->the_post();
      $id = get_the_ID();
      echo '<article class="bp-card"><a class="bp-card-media" href="' . esc_url( get_permalink() ) . '">';
      if ( has_post_thumbnail() ) { the_post_thumbnail( 'bp-card' ); }
      echo '</a><div class="bp-card-body"><h3>' . esc_html( get_the_title() ) . '</h3><p>' . esc_html( bp_meta( $id, '_bpl_address', '' ) ) . '</p><p class="bp-card-cta">';
      $maps = bp_meta( $id, '_bpl_maps', '' );
      if ( $maps ) { echo '<a class="btn-dark btn-sm" target="_blank" rel="noopener" href="' . esc_url( $maps ) . '">' . esc_html__( 'Directions', 'brickpoint' ) . '</a>'; }
      echo '<a class="btn-whatsapp btn-sm" target="_blank" rel="noopener" href="' . esc_url( bp_whatsapp_url( bp_get( 'bp_default_wa', 'Assalam-o-Alaikum BrickPoint' ) ) ) . '">WhatsApp</a>';
      echo '</p></div></article>';
    }
    echo '</div>'; wp_reset_postdata();
  }
}
