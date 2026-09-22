<?php
if ( ! defined( 'ABSPATH' ) ) { exit; }
class BrickPoint_Product_Grid extends \Elementor\Widget_Base {
  public function get_name() { return 'bp-product-grid'; }
  public function get_title() { return __( 'BP Product Grid', 'brickpoint' ); }
  public function get_icon() { return 'eicon-products'; }
  public function get_categories() { return array( 'brickpoint' ); }
  protected function register_controls() {
    $this->start_controls_section( 'query', array( 'label' => __( 'Query', 'brickpoint' ) ) );
    $this->add_control( 'count', array( 'label' => __( 'Number of products', 'brickpoint' ), 'type' => \Elementor\Controls_Manager::NUMBER, 'default' => 8 ) );
    $this->add_control( 'category', array( 'label' => __( 'Category slug (blank = all)', 'brickpoint' ), 'type' => \Elementor\Controls_Manager::TEXT, 'default' => '' ) );
    $this->add_control( 'featured_only', array( 'label' => __( 'Featured only', 'brickpoint' ), 'type' => \Elementor\Controls_Manager::SWITCHER, 'default' => '' ) );
    $this->add_control( 'orderby', array( 'label' => __( 'Order by', 'brickpoint' ), 'type' => \Elementor\Controls_Manager::SELECT, 'default' => 'date', 'options' => array( 'date' => 'Date', 'title' => 'Title', 'menu_order' => 'Custom order' ) ) );
    $this->add_control( 'columns', array( 'label' => __( 'Columns', 'brickpoint' ), 'type' => \Elementor\Controls_Manager::SELECT, 'default' => '4', 'options' => array( '2' => '2', '3' => '3', '4' => '4' ) ) );
    $this->add_control( 'show_price', array( 'label' => __( 'Show price', 'brickpoint' ), 'type' => \Elementor\Controls_Manager::SWITCHER, 'default' => 'yes' ) );
    $this->add_control( 'show_whatsapp', array( 'label' => __( 'Show WhatsApp button', 'brickpoint' ), 'type' => \Elementor\Controls_Manager::SWITCHER, 'default' => 'yes' ) );
    $this->end_controls_section();
  }
  protected function render() {
    $s = $this->get_settings_for_display();
    $args = array( 'post_type' => 'bp_product', 'posts_per_page' => absint( $s['count'] ), 'orderby' => sanitize_key( $s['orderby'] ) );
    if ( ! empty( $s['category'] ) ) { $args['tax_query'] = array( array( 'taxonomy' => 'bp_product_category', 'field' => 'slug', 'terms' => sanitize_title( $s['category'] ) ) ); }
    if ( ! empty( $s['featured_only'] ) ) { $args['meta_key'] = '_bp_featured'; $args['meta_value'] = '1'; }
    $q = new WP_Query( $args );
    echo '<div class="bp-grid cols-' . esc_attr( $s['columns'] ) . '">';
    while ( $q->have_posts() ) { $q->the_post(); get_template_part( 'template-parts/product-card' ); }
    echo '</div>'; wp_reset_postdata();
  }
}
