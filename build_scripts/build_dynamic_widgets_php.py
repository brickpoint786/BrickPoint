import os

DEST = "/home/user/BrickPoint/wordpress/brickpoint/inc/elementor-widgets.php"

widgets_code = """<?php
/**
 * BrickPoint Genuine Dynamic Elementor Widgets
 *
 * Implements dynamic querying widgets with rich Elementor controls:
 * 1. BrickPoint_Product_Grid_Widget
 * 2. BrickPoint_Category_Grid_Widget
 * 3. BrickPoint_Video_Grid_Widget
 * 4. BrickPoint_Project_Grid_Widget
 * 5. BrickPoint_Location_Grid_Widget
 * 6. BrickPoint_Blog_Grid_Widget
 * 7. BrickPoint_Header_Logo_Widget
 * 8. BrickPoint_Footer_Logo_Widget
 *
 * @package BrickPoint
 */

if ( ! defined( 'ABSPATH' ) ) {
  exit;
}

function brickpoint_register_elementor_dynamic_widgets( $widgets_manager ) {
  if ( ! class_exists( '\\Elementor\\Widget_Base' ) ) {
    return;
  }

  // 1. DYNAMIC PRODUCT GRID WIDGET
  class BrickPoint_Product_Grid_Widget extends \\Elementor\\Widget_Base {
    public function get_name() { return 'bp_product_grid'; }
    public function get_title() { return esc_html__( 'Product Grid (Dynamic)', 'brickpoint' ); }
    public function get_icon() { return 'eicon-products'; }
    public function get_categories() { return array( 'brickpoint-elements' ); }

    protected function register_controls() {
      $this->start_controls_section( 'section_query', array( 'label' => esc_html__( 'Query & Filter', 'brickpoint' ) ) );
      $this->add_control( 'count', array(
        'label'   => esc_html__( 'Number of Products', 'brickpoint' ),
        'type'    => \\Elementor\\Controls_Manager::NUMBER,
        'default' => 8,
        'min'     => 1,
        'max'     => 48,
      ) );
      $this->add_control( 'columns', array(
        'label'   => esc_html__( 'Columns', 'brickpoint' ),
        'type'    => \\Elementor\\Controls_Manager::SELECT,
        'default' => '4',
        'options' => array( '2' => '2 Columns', '3' => '3 Columns', '4' => '4 Columns' ),
      ) );
      $this->add_control( 'category', array(
        'label'       => esc_html__( 'Filter by Category Slug', 'brickpoint' ),
        'type'        => \\Elementor\\Controls_Manager::TEXT,
        'description' => esc_html__( 'Leave empty to display from all categories', 'brickpoint' ),
        'default'     => '',
      ) );
      $this->add_control( 'featured_only', array(
        'label'        => esc_html__( 'Featured Only', 'brickpoint' ),
        'type'         => \\Elementor\\Controls_Manager::SWITCHER,
        'label_on'     => esc_html__( 'Yes', 'brickpoint' ),
        'label_off'    => esc_html__( 'No', 'brickpoint' ),
        'return_value' => 'yes',
        'default'      => '',
      ) );
      $this->add_control( 'show_price', array(
        'label'        => esc_html__( 'Show Price & Unit', 'brickpoint' ),
        'type'         => \\Elementor\\Controls_Manager::SWITCHER,
        'default'      => 'yes',
      ) );
      $this->add_control( 'show_whatsapp', array(
        'label'        => esc_html__( 'Show WhatsApp Order Button', 'brickpoint' ),
        'type'         => \\Elementor\\Controls_Manager::SWITCHER,
        'default'      => 'yes',
      ) );
      $this->end_controls_section();
    }

    protected function render() {
      $s = $this->get_settings_for_display();
      $args = array(
        'post_type'      => 'bp_product',
        'posts_per_page' => intval( $s['count'] ),
        'post_status'    => 'publish',
      );
      if ( ! empty( $s['category'] ) ) {
        $args['tax_query'] = array(
          array(
            'taxonomy' => 'bp_product_category',
            'field'    => 'slug',
            'terms'    => sanitize_title( $s['category'] ),
          ),
        );
      }
      if ( 'yes' === $s['featured_only'] ) {
        $args['meta_key'] = '_bp_featured';
        $args['meta_value'] = '1';
      }

      $q = new WP_Query( $args );
      $cols = in_array( $s['columns'], array( '2', '3', '4' ), true ) ? $s['columns'] : '4';
      ?>
      <div class="bp-grid cols-<?php echo esc_attr( $cols ); ?>">
        <?php
        if ( $q->have_posts() ) :
          while ( $q->have_posts() ) : $q->the_post();
            get_template_part( 'template-parts/product-card' );
          endwhile;
          wp_reset_postdata();
        else : ?>
          <p class="bp-center" style="grid-column:1/-1;padding:2rem;color:#888;"><?php esc_html_e( 'No products found.', 'brickpoint' ); ?></p>
        <?php endif; ?>
      </div>
      <?php
    }
  }

  // 2. DYNAMIC CATEGORY GRID WIDGET
  class BrickPoint_Category_Grid_Widget extends \\Elementor\\Widget_Base {
    public function get_name() { return 'bp_category_grid'; }
    public function get_title() { return esc_html__( 'Category Grid (Dynamic)', 'brickpoint' ); }
    public function get_icon() { return 'eicon-gallery-grid'; }
    public function get_categories() { return array( 'brickpoint-elements' ); }

    protected function register_controls() {
      $this->start_controls_section( 'section_settings', array( 'label' => esc_html__( 'Display Settings', 'brickpoint' ) ) );
      $this->add_control( 'count', array(
        'label'   => esc_html__( 'Number of Categories', 'brickpoint' ),
        'type'    => \\Elementor\\Controls_Manager::NUMBER,
        'default' => 12,
        'min'     => 1,
        'max'     => 30,
      ) );
      $this->add_control( 'columns', array(
        'label'   => esc_html__( 'Columns', 'brickpoint' ),
        'type'    => \\Elementor\\Controls_Manager::SELECT,
        'default' => '4',
        'options' => array( '2' => '2 Columns', '3' => '3 Columns', '4' => '4 Columns' ),
      ) );
      $this->add_control( 'show_description', array(
        'label'   => esc_html__( 'Show Description', 'brickpoint' ),
        'type'    => \\Elementor\\Controls_Manager::SWITCHER,
        'default' => 'yes',
      ) );
      $this->end_controls_section();
    }

    protected function render() {
      $s = $this->get_settings_for_display();
      $categories = get_terms( array(
        'taxonomy'   => 'bp_product_category',
        'hide_empty' => false,
        'number'     => intval( $s['count'] ),
        'orderby'    => 'meta_value_num',
        'meta_key'   => 'bp_cat_order',
        'order'      => 'ASC',
      ) );
      if ( empty( $categories ) || is_wp_error( $categories ) ) {
        $categories = get_terms( array( 'taxonomy' => 'bp_product_category', 'hide_empty' => false, 'number' => intval( $s['count'] ) ) );
      }
      $cols = in_array( $s['columns'], array( '2', '3', '4' ), true ) ? $s['columns'] : '4';
      ?>
      <div class="bp-grid cols-<?php echo esc_attr( $cols ); ?>">
        <?php
        if ( ! empty( $categories ) && ! is_wp_error( $categories ) ) :
          foreach ( $categories as $cat ) :
            $cat_img = get_term_meta( $cat->term_id, 'bp_cat_image', true );
            if ( ! $cat_img ) {
              $cat_img = bp_asset_image_url( 'stacked.png' );
            }
            $cat_link = ( $cat->slug === 'ss7-bricks' ) ? home_url( '/ss7-bricks' ) : get_term_link( $cat );
        ?>
          <a href="<?php echo esc_url( $cat_link ); ?>" class="bp-cat-card card-hover group">
            <div class="bp-cat-media img-zoom">
              <img src="<?php echo esc_url( $cat_img ); ?>" alt="<?php echo esc_attr( $cat->name ); ?>" loading="lazy" />
              <div class="bp-cat-grad"></div>
              <p class="bp-cat-name"><?php echo esc_html( $cat->name ); ?></p>
            </div>
            <div class="bp-cat-card-foot">
              <?php if ( 'yes' === $s['show_description'] ) : ?>
                <span class="bp-cat-desc"><?php echo esc_html( wp_trim_words( $cat->description, 7, '…' ) ); ?></span>
              <?php endif; ?>
              <span class="bp-cat-arrow">
                <svg class="bp-icon-xs" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>
              </span>
            </div>
          </a>
        <?php endforeach; endif; ?>
      </div>
      <?php
    }
  }

  // 3. DYNAMIC VIDEO GRID WIDGET
  class BrickPoint_Video_Grid_Widget extends \\Elementor\\Widget_Base {
    public function get_name() { return 'bp_video_grid'; }
    public function get_title() { return esc_html__( 'Video Grid (Dynamic)', 'brickpoint' ); }
    public function get_icon() { return 'eicon-video-playlist'; }
    public function get_categories() { return array( 'brickpoint-elements' ); }

    protected function register_controls() {
      $this->start_controls_section( 'section_settings', array( 'label' => esc_html__( 'Query & Layout', 'brickpoint' ) ) );
      $this->add_control( 'count', array(
        'label'   => esc_html__( 'Number of Videos', 'brickpoint' ),
        'type'    => \\Elementor\\Controls_Manager::NUMBER,
        'default' => 6,
      ) );
      $this->add_control( 'columns', array(
        'label'   => esc_html__( 'Columns', 'brickpoint' ),
        'type'    => \\Elementor\\Controls_Manager::SELECT,
        'default' => '3',
        'options' => array( '2' => '2 Columns', '3' => '3 Columns' ),
      ) );
      $this->end_controls_section();
    }

    protected function render() {
      $s = $this->get_settings_for_display();
      $q = new WP_Query( array(
        'post_type'      => 'bp_video',
        'posts_per_page' => intval( $s['count'] ),
        'post_status'    => 'publish',
      ) );
      $cols = in_array( $s['columns'], array( '2', '3' ), true ) ? $s['columns'] : '3';
      ?>
      <div class="bp-grid cols-<?php echo esc_attr( $cols ); ?>">
        <?php
        if ( $q->have_posts() ) :
          while ( $q->have_posts() ) : $q->the_post();
            get_template_part( 'template-parts/video-card' );
          endwhile;
          wp_reset_postdata();
        endif;
        ?>
      </div>
      <?php
    }
  }

  // 4. DYNAMIC PROJECT GRID WIDGET
  class BrickPoint_Project_Grid_Widget extends \\Elementor\\Widget_Base {
    public function get_name() { return 'bp_project_grid'; }
    public function get_title() { return esc_html__( 'Project Grid (Dynamic)', 'brickpoint' ); }
    public function get_icon() { return 'eicon-gallery-masonry'; }
    public function get_categories() { return array( 'brickpoint-elements' ); }

    protected function register_controls() {
      $this->start_controls_section( 'section_settings', array( 'label' => esc_html__( 'Query & Layout', 'brickpoint' ) ) );
      $this->add_control( 'count', array(
        'label'   => esc_html__( 'Number of Projects', 'brickpoint' ),
        'type'    => \\Elementor\\Controls_Manager::NUMBER,
        'default' => 6,
      ) );
      $this->add_control( 'columns', array(
        'label'   => esc_html__( 'Columns', 'brickpoint' ),
        'type'    => \\Elementor\\Controls_Manager::SELECT,
        'default' => '3',
        'options' => array( '2' => '2 Columns', '3' => '3 Columns' ),
      ) );
      $this->end_controls_section();
    }

    protected function render() {
      $s = $this->get_settings_for_display();
      $q = new WP_Query( array(
        'post_type'      => 'bp_project',
        'posts_per_page' => intval( $s['count'] ),
        'post_status'    => 'publish',
      ) );
      $cols = in_array( $s['columns'], array( '2', '3' ), true ) ? $s['columns'] : '3';
      ?>
      <div class="bp-grid cols-<?php echo esc_attr( $cols ); ?>">
        <?php
        if ( $q->have_posts() ) :
          while ( $q->have_posts() ) : $q->the_post();
            get_template_part( 'template-parts/project-card' );
          endwhile;
          wp_reset_postdata();
        endif;
        ?>
      </div>
      <?php
    }
  }

  // 5. DYNAMIC LOCATION GRID WIDGET
  class BrickPoint_Location_Grid_Widget extends \\Elementor\\Widget_Base {
    public function get_name() { return 'bp_location_grid'; }
    public function get_title() { return esc_html__( 'Location Grid (Dynamic)', 'brickpoint' ); }
    public function get_icon() { return 'eicon-google-maps'; }
    public function get_categories() { return array( 'brickpoint-elements' ); }

    protected function register_controls() {
      $this->start_controls_section( 'section_settings', array( 'label' => esc_html__( 'Query & Layout', 'brickpoint' ) ) );
      $this->add_control( 'count', array(
        'label'   => esc_html__( 'Number of Locations', 'brickpoint' ),
        'type'    => \\Elementor\\Controls_Manager::NUMBER,
        'default' => 4,
      ) );
      $this->end_controls_section();
    }

    protected function render() {
      $s = $this->get_settings_for_display();
      $q = new WP_Query( array(
        'post_type'      => 'bp_location',
        'posts_per_page' => intval( $s['count'] ),
        'post_status'    => 'publish',
      ) );
      ?>
      <div class="bp-grid cols-2">
        <?php
        if ( $q->have_posts() ) :
          while ( $q->have_posts() ) : $q->the_post();
            get_template_part( 'template-parts/location-card' );
          endwhile;
          wp_reset_postdata();
        endif;
        ?>
      </div>
      <?php
    }
  }

  // 6. DYNAMIC BLOG GRID WIDGET
  class BrickPoint_Blog_Grid_Widget extends \\Elementor\\Widget_Base {
    public function get_name() { return 'bp_blog_grid'; }
    public function get_title() { return esc_html__( 'Blog Grid (Dynamic)', 'brickpoint' ); }
    public function get_icon() { return 'eicon-post-list'; }
    public function get_categories() { return array( 'brickpoint-elements' ); }

    protected function register_controls() {
      $this->start_controls_section( 'section_settings', array( 'label' => esc_html__( 'Query & Layout', 'brickpoint' ) ) );
      $this->add_control( 'count', array(
        'label'   => esc_html__( 'Number of Posts', 'brickpoint' ),
        'type'    => \\Elementor\\Controls_Manager::NUMBER,
        'default' => 6,
      ) );
      $this->add_control( 'columns', array(
        'label'   => esc_html__( 'Columns', 'brickpoint' ),
        'type'    => \\Elementor\\Controls_Manager::SELECT,
        'default' => '3',
        'options' => array( '2' => '2 Columns', '3' => '3 Columns' ),
      ) );
      $this->end_controls_section();
    }

    protected function render() {
      $s = $this->get_settings_for_display();
      $q = new WP_Query( array(
        'post_type'      => 'post',
        'posts_per_page' => intval( $s['count'] ),
        'post_status'    => 'publish',
      ) );
      $cols = in_array( $s['columns'], array( '2', '3' ), true ) ? $s['columns'] : '3';
      ?>
      <div class="bp-grid cols-<?php echo esc_attr( $cols ); ?>">
        <?php
        if ( $q->have_posts() ) :
          while ( $q->have_posts() ) : $q->the_post();
            get_template_part( 'template-parts/content' );
          endwhile;
          wp_reset_postdata();
        endif;
        ?>
      </div>
      <?php
    }
  }

  // 7. INDEPENDENT HEADER LOGO WIDGET
  class BrickPoint_Header_Logo_Widget extends \\Elementor\\Widget_Base {
    public function get_name() { return 'bp_header_logo_widget'; }
    public function get_title() { return esc_html__( 'Header Logo (Independent)', 'brickpoint' ); }
    public function get_icon() { return 'eicon-site-logo'; }
    public function get_categories() { return array( 'brickpoint-elements' ); }

    protected function register_controls() {
      $this->start_controls_section( 'section_logo', array( 'label' => esc_html__( 'Header Logo Settings', 'brickpoint' ) ) );
      $this->add_control( 'custom_logo', array(
        'label'   => esc_html__( 'Custom Logo Image (Optional override)', 'brickpoint' ),
        'type'    => \\Elementor\\Controls_Manager::MEDIA,
        'default' => array( 'url' => '' ),
      ) );
      $this->add_responsive_control( 'desktop_height', array(
        'label'      => esc_html__( 'Logo Height (px)', 'brickpoint' ),
        'type'       => \\Elementor\\Controls_Manager::SLIDER,
        'size_units' => array( 'px' ),
        'range'      => array(
          'px' => array( 'min' => 20, 'max' => 120, 'step' => 1 ),
        ),
        'default'    => array( 'unit' => 'px', 'size' => 44 ),
        'selectors'  => array(
          '{{WRAPPER}} .bp-header-logo-img' => 'height: {{SIZE}}{{UNIT}} !important; width: auto;',
        ),
      ) );
      $this->add_responsive_control( 'alignment', array(
        'label'     => esc_html__( 'Alignment', 'brickpoint' ),
        'type'      => \\Elementor\\Controls_Manager::CHOOSE,
        'options'   => array(
          'left'   => array( 'title' => esc_html__( 'Left', 'brickpoint' ), 'icon' => 'eicon-text-align-left' ),
          'center' => array( 'title' => esc_html__( 'Center', 'brickpoint' ), 'icon' => 'eicon-text-align-center' ),
          'right'  => array( 'title' => esc_html__( 'Right', 'brickpoint' ), 'icon' => 'eicon-text-align-right' ),
        ),
        'default'   => 'left',
        'selectors' => array(
          '{{WRAPPER}}' => 'text-align: {{VALUE}};',
        ),
      ) );
      $this->end_controls_section();
    }

    protected function render() {
      $s = $this->get_settings_for_display();
      if ( ! empty( $s['custom_logo']['url'] ) ) {
        ?>
        <a href="<?php echo esc_url( home_url( '/' ) ); ?>" class="bp-logo-link" rel="home">
          <img src="<?php echo esc_url( $s['custom_logo']['url'] ); ?>" alt="<?php bloginfo( 'name' ); ?>" class="bp-logo bp-header-logo-img" />
        </a>
        <?php
      } else {
        brickpoint_header_logo();
      }
    }
  }

  // 8. INDEPENDENT FOOTER LOGO WIDGET
  class BrickPoint_Footer_Logo_Widget extends \\Elementor\\Widget_Base {
    public function get_name() { return 'bp_footer_logo_widget'; }
    public function get_title() { return esc_html__( 'Footer Logo (Independent)', 'brickpoint' ); }
    public function get_icon() { return 'eicon-image'; }
    public function get_categories() { return array( 'brickpoint-elements' ); }

    protected function register_controls() {
      $this->start_controls_section( 'section_logo', array( 'label' => esc_html__( 'Footer Logo Settings', 'brickpoint' ) ) );
      $this->add_control( 'custom_logo', array(
        'label'   => esc_html__( 'Custom Logo Image (Optional override)', 'brickpoint' ),
        'type'    => \\Elementor\\Controls_Manager::MEDIA,
        'default' => array( 'url' => '' ),
      ) );
      $this->add_responsive_control( 'desktop_height', array(
        'label'      => esc_html__( 'Logo Height (px)', 'brickpoint' ),
        'type'       => \\Elementor\\Controls_Manager::SLIDER,
        'size_units' => array( 'px' ),
        'range'      => array(
          'px' => array( 'min' => 20, 'max' => 140, 'step' => 1 ),
        ),
        'default'    => array( 'unit' => 'px', 'size' => 52 ),
        'selectors'  => array(
          '{{WRAPPER}} .bp-footer-logo-img' => 'height: {{SIZE}}{{UNIT}} !important; width: auto;',
        ),
      ) );
      $this->add_responsive_control( 'alignment', array(
        'label'     => esc_html__( 'Alignment', 'brickpoint' ),
        'type'      => \\Elementor\\Controls_Manager::CHOOSE,
        'options'   => array(
          'left'   => array( 'title' => esc_html__( 'Left', 'brickpoint' ), 'icon' => 'eicon-text-align-left' ),
          'center' => array( 'title' => esc_html__( 'Center', 'brickpoint' ), 'icon' => 'eicon-text-align-center' ),
          'right'  => array( 'title' => esc_html__( 'Right', 'brickpoint' ), 'icon' => 'eicon-text-align-right' ),
        ),
        'default'   => 'left',
        'selectors' => array(
          '{{WRAPPER}}' => 'text-align: {{VALUE}};',
        ),
      ) );
      $this->end_controls_section();
    }

    protected function render() {
      $s = $this->get_settings_for_display();
      if ( ! empty( $s['custom_logo']['url'] ) ) {
        ?>
        <a href="<?php echo esc_url( home_url( '/' ) ); ?>" class="bp-footer-logo-link" rel="home">
          <img src="<?php echo esc_url( $s['custom_logo']['url'] ); ?>" alt="<?php bloginfo( 'name' ); ?>" class="bp-footer-logo-img" />
        </a>
        <?php
      } else {
        brickpoint_footer_logo();
      }
    }
  }

  // Register widgets
  $widgets_manager->register( new BrickPoint_Product_Grid_Widget() );
  $widgets_manager->register( new BrickPoint_Category_Grid_Widget() );
  $widgets_manager->register( new BrickPoint_Video_Grid_Widget() );
  $widgets_manager->register( new BrickPoint_Project_Grid_Widget() );
  $widgets_manager->register( new BrickPoint_Location_Grid_Widget() );
  $widgets_manager->register( new BrickPoint_Blog_Grid_Widget() );
  $widgets_manager->register( new BrickPoint_Header_Logo_Widget() );
  $widgets_manager->register( new BrickPoint_Footer_Logo_Widget() );
}
add_action( 'elementor/widgets/register', 'brickpoint_register_elementor_dynamic_widgets' );
"""

with open(DEST, "w", encoding="utf-8") as f:
    f.write(widgets_code.strip() + "\n")

print(f"Wrote {DEST} successfully with genuine dynamic widgets.")
