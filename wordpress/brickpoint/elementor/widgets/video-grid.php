<?php
if ( ! defined( 'ABSPATH' ) ) { exit; }
class BrickPoint_Video_Grid extends \Elementor\Widget_Base {
  public function get_name() { return 'bp-video-grid'; }
  public function get_title() { return __( 'BP Video Grid', 'brickpoint' ); }
  public function get_icon() { return 'eicon-video'; }
  public function get_categories() { return array( 'brickpoint' ); }
  protected function register_controls() {
    $this->start_controls_section( 'q', array( 'label' => __( 'Query', 'brickpoint' ) ) );
    $this->add_control( 'count', array( 'label' => __( 'Number', 'brickpoint' ), 'type' => \Elementor\Controls_Manager::NUMBER, 'default' => 6 ) );
    $this->add_control( 'category', array( 'label' => __( 'Category slug (blank = all)', 'brickpoint' ), 'type' => \Elementor\Controls_Manager::TEXT, 'default' => '' ) );
    $this->add_control( 'featured_only', array( 'label' => __( 'Featured only', 'brickpoint' ), 'type' => \Elementor\Controls_Manager::SWITCHER, 'default' => '' ) );
    $this->add_control( 'columns', array( 'label' => __( 'Columns', 'brickpoint' ), 'type' => \Elementor\Controls_Manager::SELECT, 'default' => '3', 'options' => array( '2' => '2', '3' => '3', '4' => '4' ) ) );
    $this->end_controls_section();
  }
  protected function render() {
    $s = $this->get_settings_for_display();
    $args = array( 'post_type' => 'bp_video', 'posts_per_page' => absint( $s['count'] ) );
    if ( ! empty( $s['category'] ) ) { $args['tax_query'] = array( array( 'taxonomy' => 'bp_video_category', 'field' => 'slug', 'terms' => sanitize_title( $s['category'] ) ) ); }
    if ( ! empty( $s['featured_only'] ) ) { $args['meta_key'] = '_bpv_featured'; $args['meta_value'] = '1'; }
    $q = new WP_Query( $args );
    echo '<div class="bp-grid cols-' . esc_attr( $s['columns'] ) . '">';
    while ( $q->have_posts() ) { $q->the_post(); get_template_part( 'template-parts/video-card' ); }
    echo '</div>'; wp_reset_postdata();
  }
}
