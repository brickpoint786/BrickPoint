<?php
if ( ! defined( 'ABSPATH' ) ) { exit; }
class BrickPoint_Project_Grid extends \Elementor\Widget_Base {
  public function get_name() { return 'bp-project-grid'; }
  public function get_title() { return __( 'BP Project Grid', 'brickpoint' ); }
  public function get_icon() { return 'eicon-gallery-masonry'; }
  public function get_categories() { return array( 'brickpoint' ); }
  protected function register_controls() {
    $this->start_controls_section( 'q', array( 'label' => __( 'Query', 'brickpoint' ) ) );
    $this->add_control( 'count', array( 'label' => __( 'Number', 'brickpoint' ), 'type' => \Elementor\Controls_Manager::NUMBER, 'default' => 6 ) );
    $this->add_control( 'columns', array( 'label' => __( 'Columns', 'brickpoint' ), 'type' => \Elementor\Controls_Manager::SELECT, 'default' => '3', 'options' => array( '2' => '2', '3' => '3', '4' => '4' ) ) );
    $this->end_controls_section();
  }
  protected function render() {
    $s = $this->get_settings_for_display();
    $q = new WP_Query( array( 'post_type' => 'bp_project', 'posts_per_page' => absint( $s['count'] ) ) );
    echo '<div class="bp-grid cols-' . esc_attr( $s['columns'] ) . '">';
    while ( $q->have_posts() ) { $q->the_post(); get_template_part( 'template-parts/content-project' ); }
    echo '</div>'; wp_reset_postdata();
  }
}
