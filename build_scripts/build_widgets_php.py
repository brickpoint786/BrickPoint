import os

DEST = "/home/user/BrickPoint/wordpress/brickpoint"

widgets_php = """<?php
/**
 * BrickPoint Custom Elementor Widgets
 *
 * Implements 13 custom widgets for Elementor Free and Elementor Pro:
 * 1. BrickPoint_Hero_Widget
 * 2. BrickPoint_SS7_Showcase_Widget
 * 3. BrickPoint_Product_Grid_Widget
 * 4. BrickPoint_Category_Grid_Widget
 * 5. BrickPoint_Video_Showcase_Widget
 * 6. BrickPoint_Projects_Grid_Widget
 * 7. BrickPoint_Locations_Grid_Widget
 * 8. BrickPoint_WhatsApp_CTA_Widget
 * 9. BrickPoint_Audience_Cards_Widget
 * 10. BrickPoint_Stats_Bar_Widget
 * 11. BrickPoint_Specifications_Table_Widget
 * 12. BrickPoint_Header_Logo_Widget
 * 13. BrickPoint_Footer_Logo_Widget
 *
 * @package BrickPoint
 */

if ( ! defined( 'ABSPATH' ) ) {
  exit;
}

function brickpoint_register_elementor_custom_widgets( $widgets_manager ) {
  // Check if Elementor widget base class exists
  if ( ! class_exists( '\\Elementor\\Widget_Base' ) ) {
    return;
  }

  // 1. HERO WIDGET
  class BrickPoint_Hero_Widget extends \\Elementor\\Widget_Base {
    public function get_name() { return 'bp_hero'; }
    public function get_title() { return esc_html__( 'BrickPoint Hero Section', 'brickpoint' ); }
    public function get_icon() { return 'eicon-banner'; }
    public function get_categories() { return array( 'brickpoint-elements' ); }

    protected function register_controls() {
      $this->start_controls_section( 'section_content', array( 'label' => esc_html__( 'Content', 'brickpoint' ) ) );
      $this->add_control( 'title', array(
        'label'   => esc_html__( 'Heading Line 1', 'brickpoint' ),
        'type'    => \\Elementor\\Controls_Manager::TEXT,
        'default' => 'Building Strength.',
      ) );
      $this->add_control( 'highlight', array(
        'label'   => esc_html__( 'Orange Highlight Line', 'brickpoint' ),
        'type'    => \\Elementor\\Controls_Manager::TEXT,
        'default' => 'Delivering Quality.',
      ) );
      $this->add_control( 'subline', array(
        'label'   => esc_html__( 'Heading Line 3', 'brickpoint' ),
        'type'    => \\Elementor\\Controls_Manager::TEXT,
        'default' => 'Shaping Tomorrow.',
      ) );
      $this->add_control( 'desc', array(
        'label'   => esc_html__( 'Description', 'brickpoint' ),
        'type'    => \\Elementor\\Controls_Manager::TEXTAREA,
        'default' => 'Premium bricks and reliable construction materials for homes, commercial developments, and large-scale building projects.',
      ) );
      $this->add_control( 'video_url', array(
        'label'   => esc_html__( 'Video MP4 URL', 'brickpoint' ),
        'type'    => \\Elementor\\Controls_Manager::TEXT,
        'default' => 'https://videos.pexels.com/video-files/35411576/15003649_3840_2160_24fps.mp4',
      ) );
      $this->end_controls_section();
    }

    protected function render() {
      $settings = $this->get_settings_for_display();
      ?>
      <section class="bp-hero relative">
        <div class="bp-hero-bg">
          <img src="<?php echo esc_url( bp_asset_image_url( 'brick-mason.png' ) ); ?>" alt="Hero bg" class="bp-hero-bg-img" />
          <div class="bp-hero-overlay"></div>
          <div class="brick-lines absolute-bg"></div>
        </div>
        <div class="bp-container bp-hero-grid relative">
          <div class="bp-hero-text">
            <p class="bp-hero-badge"><span>Masha Allah &bull; Fine Bricks &bull; SS7</span></p>
            <h1 class="bp-hero-title">
              <?php echo esc_html( $settings['title'] ); ?><br />
              <span class="text-orange"><?php echo esc_html( $settings['highlight'] ); ?></span><br />
              <?php echo esc_html( $settings['subline'] ); ?>
            </h1>
            <p class="bp-hero-sub"><?php echo esc_html( $settings['desc'] ); ?></p>
            <div class="bp-hero-cta">
              <a href="<?php echo esc_url( home_url( '/products' ) ); ?>" class="btn-brick"><span>Explore Products</span></a>
              <a href="<?php echo esc_url( home_url( '/contact' ) ); ?>" class="btn-ghost" style="color:#fff;border-color:rgba(255,255,255,0.25);"><span>Request a Quote</span></a>
              <a href="<?php echo esc_url( bp_whatsapp_url( 'Assalam-o-Alaikum BrickPoint, I need a quotation for construction materials.' ) ); ?>" target="_blank" rel="noopener" class="btn-whatsapp">
                <svg class="bp-icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/></svg>
                <span>WhatsApp Us</span>
              </a>
            </div>
            <div class="bp-hero-trust-row">
              <span>Quality-focused supply</span>
              <span>Reliable delivery</span>
              <span>Multiple production locations</span>
            </div>
          </div>
          <div class="bp-hero-media-wrap relative">
            <div class="hero-video-frame relative">
              <video autoplay muted loop playsinline preload="metadata" poster="<?php echo esc_url( bp_asset_image_url( 'hero-poster.png' ) ); ?>" class="bp-hero-video-el">
                <source src="<?php echo esc_url( $settings['video_url'] ); ?>" type="video/mp4" />
              </video>
              <div class="bp-hero-video-overlay">
                <div>
                  <p class="bp-video-eyebrow">SS7 Bricks &bull; In Action</p>
                  <p class="bp-video-caption">See the strength behind every brick</p>
                </div>
                <a href="<?php echo esc_url( home_url( '/videos' ) ); ?>" class="bp-play-circle">
                  <svg class="bp-icon-sm" viewBox="0 0 24 24" fill="currentColor"><polygon points="6 3 20 12 6 21 6 3"/></svg>
                </a>
              </div>
            </div>
            <div class="bp-ss7-float-badge ss7-brick-loop">
              <div class="ss7-brick">
                <img src="<?php echo esc_url( bp_asset_image_url( 'red-stack.png' ) ); ?>" alt="SS7" class="bp-ss7-thumb" />
                <div>
                  <p class="bp-flagship-tag">Flagship</p>
                  <p class="bp-ss7-title">SS7 Bricks</p>
                  <a href="<?php echo esc_url( home_url( '/ss7-bricks' ) ); ?>" class="bp-ss7-link">View SS7 range &rarr;</a>
                </div>
              </div>
            </div>
            <div class="bp-units-pill">
              <p class="bp-units-count">3<span class="text-orange">+</span></p>
              <p class="bp-units-label">Production units</p>
            </div>
          </div>
        </div>
      </section>
      <?php
    }
  }

  // 2. SS7 SHOWCASE WIDGET
  class BrickPoint_SS7_Showcase_Widget extends \\Elementor\\Widget_Base {
    public function get_name() { return 'bp_ss7_showcase'; }
    public function get_title() { return esc_html__( 'BrickPoint SS7 Showcase', 'brickpoint' ); }
    public function get_icon() { return 'eicon-image-box'; }
    public function get_categories() { return array( 'brickpoint-elements' ); }

    protected function render() {
      ?>
      <section class="bp-section bp-ss7-section">
        <div class="bp-container bp-ss7-grid">
          <div class="bp-ss7-content">
            <p class="bp-eyebrow">Flagship Product</p>
            <h2 class="bp-heading-2">The Strength Behind Every Structure</h2>
            <p class="bp-body-text">SS7 Bricks — our signature range engineered for strength, shape and lasting performance. Ask for specifications, availability and project pricing on WhatsApp.</p>
            <div class="bp-specs-grid">
              <div class="bp-spec-card"><p class="bp-spec-lbl">Size</p><p class="bp-spec-val">Standard chamber size</p></div>
              <div class="bp-spec-card"><p class="bp-spec-lbl">Type</p><p class="bp-spec-val">Burnt-clay SS7</p></div>
              <div class="bp-spec-card"><p class="bp-spec-lbl">Usage</p><p class="bp-spec-val">Homes • Commercial • Boundary</p></div>
              <div class="bp-spec-card"><p class="bp-spec-lbl">Availability</p><p class="bp-spec-val">Bulk & retail orders</p></div>
            </div>
            <div class="bp-action-row">
              <a href="<?php echo esc_url( bp_whatsapp_url( bp_category_inquiry_message( 'SS7 Bricks' ) ) ); ?>" target="_blank" rel="noopener" class="btn-whatsapp">
                <svg class="bp-icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/></svg>
                <span>Request SS7 Quote</span>
              </a>
              <a href="<?php echo esc_url( home_url( '/ss7-bricks' ) ); ?>" class="btn-dark">View SS7 Page →</a>
            </div>
          </div>
          <div class="bp-ss7-gallery-wrap">
            <div class="bp-ss7-main-img img-zoom">
              <img src="<?php echo esc_url( bp_asset_image_url( 'red-stack.png' ) ); ?>" alt="SS7 Red Bricks" />
            </div>
            <div class="bp-ss7-thumbs-row">
              <img src="<?php echo esc_url( bp_asset_image_url( 'stacked.png' ) ); ?>" alt="SS7" />
              <img src="<?php echo esc_url( bp_asset_image_url( 'pile.png' ) ); ?>" alt="SS7" />
              <img src="<?php echo esc_url( bp_asset_image_url( 'worker.png' ) ); ?>" alt="SS7" />
            </div>
          </div>
        </div>
      </section>
      <?php
    }
  }

  // 3. PRODUCT GRID WIDGET
  class BrickPoint_Product_Grid_Widget extends \\Elementor\\Widget_Base {
    public function get_name() { return 'bp_product_grid'; }
    public function get_title() { return esc_html__( 'BrickPoint Product Grid', 'brickpoint' ); }
    public function get_icon() { return 'eicon-products'; }
    public function get_categories() { return array( 'brickpoint-elements' ); }

    protected function register_controls() {
      $this->start_controls_section( 'section_settings', array( 'label' => esc_html__( 'Settings', 'brickpoint' ) ) );
      $this->add_control( 'count', array(
        'label'   => esc_html__( 'Number of Products', 'brickpoint' ),
        'type'    => \\Elementor\\Controls_Manager::NUMBER,
        'default' => 8,
      ) );
      $this->add_control( 'columns', array(
        'label'   => esc_html__( 'Columns', 'brickpoint' ),
        'type'    => \\Elementor\\Controls_Manager::SELECT,
        'default' => '4',
        'options' => array( '2' => '2 Columns', '3' => '3 Columns', '4' => '4 Columns' ),
      ) );
      $this->end_controls_section();
    }

    protected function render() {
      $settings = $this->get_settings_for_display();
      $cols = intval( $settings['columns'] );
      $q = new WP_Query( array(
        'post_type'      => 'bp_product',
        'posts_per_page' => intval( $settings['count'] ),
      ) );
      ?>
      <div class="bp-grid cols-<?php echo esc_attr( $cols ); ?>">
        <?php
        if ( $q->have_posts() ) :
          while ( $q->have_posts() ) : $q->the_post();
            get_template_part( 'template-parts/product-card' );
          endwhile;
          wp_reset_postdata();
        else : ?>
          <p><?php esc_html_e( 'No products found.', 'brickpoint' ); ?></p>
        <?php endif; ?>
      </div>
      <?php
    }
  }

  // 4. CATEGORY GRID WIDGET
  class BrickPoint_Category_Grid_Widget extends \\Elementor\\Widget_Base {
    public function get_name() { return 'bp_category_grid'; }
    public function get_title() { return esc_html__( 'BrickPoint Category Grid', 'brickpoint' ); }
    public function get_icon() { return 'eicon-gallery-grid'; }
    public function get_categories() { return array( 'brickpoint-elements' ); }

    protected function render() {
      $categories = get_terms( array(
        'taxonomy'   => 'bp_product_category',
        'hide_empty' => false,
        'number'     => 12,
        'orderby'    => 'meta_value_num',
        'meta_key'   => 'bp_cat_order',
        'order'      => 'ASC',
      ) );
      if ( empty( $categories ) || is_wp_error( $categories ) ) {
        $categories = get_terms( array( 'taxonomy' => 'bp_product_category', 'hide_empty' => false, 'number' => 12 ) );
      }
      ?>
      <div class="bp-grid cols-4">
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
              <span class="bp-cat-desc"><?php echo esc_html( wp_trim_words( $cat->description, 7, '…' ) ); ?></span>
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

  // 5. VIDEO SHOWCASE WIDGET
  class BrickPoint_Video_Showcase_Widget extends \\Elementor\\Widget_Base {
    public function get_name() { return 'bp_video_showcase'; }
    public function get_title() { return esc_html__( 'BrickPoint Video Showcase', 'brickpoint' ); }
    public function get_icon() { return 'eicon-video-playlist'; }
    public function get_categories() { return array( 'brickpoint-elements' ); }

    protected function render() {
      $vq = new WP_Query( array( 'post_type' => 'bp_video', 'posts_per_page' => 3 ) );
      ?>
      <div class="bp-video-featured-grid">
        <div class="bp-video-main hero-video-frame">
          <video controls playsinline preload="metadata" poster="<?php echo esc_url( bp_asset_image_url( 'drone-poster.png' ) ); ?>" class="bp-video-player">
            <source src="<?php echo esc_url( bp_option( 'bp_drone_video', 'https://videos.pexels.com/video-files/27758012/12218981_3840_2160_25fps.mp4' ) ); ?>" type="video/mp4" />
          </video>
          <span class="bp-feat-badge"><?php esc_html_e( 'Featured', 'brickpoint' ); ?></span>
        </div>
        <div class="bp-video-sub-col">
          <div class="bp-video-sub-card">
            <div class="bp-video-sub-thumb">
              <video playsinline muted loop autoplay preload="metadata" poster="<?php echo esc_url( bp_asset_image_url( 'site-poster.png' ) ); ?>">
                <source src="<?php echo esc_url( bp_option( 'bp_site_video', 'https://videos.pexels.com/video-files/11355903/11355903-uhd_3840_2160_25fps.mp4' ) ); ?>" type="video/mp4" />
              </video>
              <span class="bp-video-sub-tag">From the Bhatta to Your Building</span>
            </div>
            <p class="bp-video-sub-desc">Brick preparation, firing, stacking, loading and quality — the journey of every batch.</p>
          </div>
          <div class="bp-video-sub-card">
            <div class="bp-video-sub-thumb">
              <video playsinline muted loop autoplay preload="metadata" poster="<?php echo esc_url( bp_asset_image_url( 'aerial-poster.png' ) ); ?>">
                <source src="<?php echo esc_url( bp_option( 'bp_aerial_video', 'https://videos.pexels.com/video-files/20731372/20731372-uhd_3840_2160_30fps.mp4' ) ); ?>" type="video/mp4" />
              </video>
              <span class="bp-video-sub-tag">Materials That Become Landmarks</span>
            </div>
            <p class="bp-video-sub-desc">Illustrative construction references from housing developments and building work.</p>
          </div>
        </div>
      </div>
      <div class="bp-grid cols-3 bp-mt">
        <?php
        if ( $vq->have_posts() ) :
          while ( $vq->have_posts() ) : $vq->the_post();
            get_template_part( 'template-parts/video-card' );
          endwhile;
          wp_reset_postdata();
        endif;
        ?>
      </div>
      <?php
    }
  }

  // 6. PROJECTS GRID WIDGET
  class BrickPoint_Projects_Grid_Widget extends \\Elementor\\Widget_Base {
    public function get_name() { return 'bp_projects_grid'; }
    public function get_title() { return esc_html__( 'BrickPoint Projects Grid', 'brickpoint' ); }
    public function get_icon() { return 'eicon-gallery-masonry'; }
    public function get_categories() { return array( 'brickpoint-elements' ); }

    protected function render() {
      $pq = new WP_Query( array( 'post_type' => 'bp_project', 'posts_per_page' => 6 ) );
      ?>
      <div class="bp-grid cols-3">
        <?php
        if ( $pq->have_posts() ) :
          while ( $pq->have_posts() ) : $pq->the_post();
            get_template_part( 'template-parts/project-card' );
          endwhile;
          wp_reset_postdata();
        endif;
        ?>
      </div>
      <?php
    }
  }

  // 7. LOCATIONS GRID WIDGET
  class BrickPoint_Locations_Grid_Widget extends \\Elementor\\Widget_Base {
    public function get_name() { return 'bp_locations_grid'; }
    public function get_title() { return esc_html__( 'BrickPoint Locations Grid', 'brickpoint' ); }
    public function get_icon() { return 'eicon-google-maps'; }
    public function get_categories() { return array( 'brickpoint-elements' ); }

    protected function render() {
      $lq = new WP_Query( array( 'post_type' => 'bp_location', 'posts_per_page' => 4 ) );
      ?>
      <div class="bp-grid cols-2">
        <?php
        if ( $lq->have_posts() ) :
          $num = 1;
          while ( $lq->have_posts() ) : $lq->the_post();
            $id = get_the_ID();
            $addr = bp_meta( $id, '_bpl_address', '' );
            $phone = bp_meta( $id, '_bpl_phone', bp_option( 'bp_phone_display', '0315 2850818' ) );
            $hours = bp_meta( $id, '_bpl_hours', 'Mon – Sat: 8:00 AM – 6:00 PM' );
            $maps = bp_meta( $id, '_bpl_maps_url', '' );
          ?>
            <article class="bp-card card-hover group bp-loc-full-card">
              <div class="bp-card-media img-zoom">
                <?php if ( has_post_thumbnail() ) : ?>
                  <?php the_post_thumbnail( 'large' ); ?>
                <?php else : ?>
                  <img src="<?php echo esc_url( bp_asset_image_url( 'kiln.png' ) ); ?>" alt="<?php the_title_attribute(); ?>" />
                <?php endif; ?>
                <span class="bp-badge">Unit <?php echo intval( $num ); ?></span>
              </div>
              <div class="bp-card-body">
                <h3><?php the_title(); ?></h3>
                <?php if ( $addr ) : ?><p class="bp-loc-item"><?php echo esc_html( $addr ); ?></p><?php endif; ?>
                <p class="bp-loc-desc"><?php echo esc_html( get_the_excerpt() ); ?></p>
                <div class="bp-card-cta bp-mt">
                  <?php if ( $maps ) : ?><a href="<?php echo esc_url( $maps ); ?>" target="_blank" rel="noopener" class="btn-dark btn-sm">📍 Directions</a><?php endif; ?>
                  <a href="<?php echo esc_url( bp_whatsapp_url( 'Assalam-o-Alaikum BrickPoint, inquiry about: ' . get_the_title() ) ); ?>" target="_blank" rel="noopener" class="btn-whatsapp btn-sm">WhatsApp</a>
                </div>
              </div>
            </article>
          <?php $num++; endwhile; wp_reset_postdata(); endif; ?>
      </div>
      <?php
    }
  }

  // 8. WHATSAPP CTA WIDGET
  class BrickPoint_WhatsApp_CTA_Widget extends \\Elementor\\Widget_Base {
    public function get_name() { return 'bp_whatsapp_cta'; }
    public function get_title() { return esc_html__( 'BrickPoint WhatsApp CTA Banner', 'brickpoint' ); }
    public function get_icon() { return 'eicon-call-to-action'; }
    public function get_categories() { return array( 'brickpoint-elements' ); }

    protected function render() {
      ?>
      <section class="bp-section bp-cta-section">
        <div class="bp-cta-bg-img">
          <img src="<?php echo esc_url( bp_asset_image_url( 'bricklayer.png' ) ); ?>" alt="" />
          <div class="bp-cta-bg-grad"></div>
        </div>
        <div class="bp-container bp-cta-inner">
          <div class="bp-cta-text">
            <p class="bp-eyebrow">Get a fast quotation</p>
            <h2 class="bp-heading-1">Send your material list.<br />We handle the rest.</h2>
            <p class="bp-cta-meta"><?php echo esc_html( bp_option( 'bp_phone_display', '0315 2850818' ) ); ?> &bull; CEO: <?php echo esc_html( bp_option( 'bp_ceo', 'Syed Iftikhar Haider' ) ); ?> &bull; Sales: <?php echo esc_html( bp_option( 'bp_sales', 'Qasim Iqbal' ) ); ?></p>
          </div>
          <div class="bp-cta-buttons">
            <a href="<?php echo esc_url( bp_whatsapp_url( 'Assalam-o-Alaikum BrickPoint, I need a quotation for construction materials.' ) ); ?>" target="_blank" rel="noopener" class="btn-whatsapp btn-lg">
              <svg class="bp-icon-md" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/></svg>
              <span>WhatsApp Your List</span>
            </a>
            <a href="<?php echo esc_url( home_url( '/contact' ) ); ?>" class="btn-brick btn-lg">Request Quote Form</a>
          </div>
        </div>
      </section>
      <?php
    }
  }

  // 9. AUDIENCE CARDS WIDGET (Who We Serve)
  class BrickPoint_Audience_Cards_Widget extends \\Elementor\\Widget_Base {
    public function get_name() { return 'bp_audience_cards'; }
    public function get_title() { return esc_html__( 'BrickPoint Audience Cards', 'brickpoint' ); }
    public function get_icon() { return 'eicon-columns'; }
    public function get_categories() { return array( 'brickpoint-elements' ); }

    protected function render() {
      ?>
      <div class="bp-grid cols-3">
        <a href="<?php echo esc_url( home_url( '/for-contractors' ) ); ?>" class="bp-audience-card card-hover group">
          <div class="bp-audience-media img-zoom">
            <img src="<?php echo esc_url( bp_asset_image_url( 'site.png' ) ); ?>" alt="For Contractors" />
            <div class="bp-audience-overlay"></div>
          </div>
          <div class="bp-audience-body">
            <h3>For Contractors</h3>
            <p>Bulk material supply, project-based quotations and delivery coordination.</p>
            <span class="bp-audience-link">Learn more →</span>
          </div>
        </a>
        <a href="<?php echo esc_url( home_url( '/for-builders' ) ); ?>" class="bp-audience-card card-hover group">
          <div class="bp-audience-media img-zoom">
            <img src="<?php echo esc_url( bp_asset_image_url( 'bricklayer.png' ) ); ?>" alt="For Builders" />
            <div class="bp-audience-overlay"></div>
          </div>
          <div class="bp-audience-body">
            <h3>For Builders</h3>
            <p>Consistent quality across every batch, with multi-category sourcing.</p>
            <span class="bp-audience-link">Learn more →</span>
          </div>
        </a>
        <a href="<?php echo esc_url( home_url( '/for-companies' ) ); ?>" class="bp-audience-card card-hover group">
          <div class="bp-audience-media img-zoom">
            <img src="<?php echo esc_url( bp_asset_image_url( 'apt.png' ) ); ?>" alt="For Construction Companies" />
            <div class="bp-audience-overlay"></div>
          </div>
          <div class="bp-audience-body">
            <h3>For Construction Companies</h3>
            <p>Large-scale supply, documentation and dedicated contact.</p>
            <span class="bp-audience-link">Learn more →</span>
          </div>
        </a>
      </div>
      <?php
    }
  }

  // 10. STATS BAR WIDGET
  class BrickPoint_Stats_Bar_Widget extends \\Elementor\\Widget_Base {
    public function get_name() { return 'bp_stats_bar'; }
    public function get_title() { return esc_html__( 'BrickPoint Stats & Trust Bar', 'brickpoint' ); }
    public function get_icon() { return 'eicon-counter'; }
    public function get_categories() { return array( 'brickpoint-elements' ); }

    protected function render() {
      ?>
      <div class="bp-stats-row">
        <div class="bp-stat-box">
          <span class="bp-stat-num">3+</span>
          <span class="bp-stat-lbl">Production Units</span>
        </div>
        <div class="bp-stat-box">
          <span class="bp-stat-num">12+</span>
          <span class="bp-stat-lbl">Material Categories</span>
        </div>
        <div class="bp-stat-box">
          <span class="bp-stat-num">100%</span>
          <span class="bp-stat-lbl">Quality Fired</span>
        </div>
        <div class="bp-stat-box">
          <span class="bp-stat-num">24/7</span>
          <span class="bp-stat-lbl">WhatsApp Support</span>
        </div>
      </div>
      <?php
    }
  }

  // 11. SPECIFICATIONS TABLE WIDGET
  class BrickPoint_Specifications_Table_Widget extends \\Elementor\\Widget_Base {
    public function get_name() { return 'bp_specs_table'; }
    public function get_title() { return esc_html__( 'BrickPoint Specifications Table', 'brickpoint' ); }
    public function get_icon() { return 'eicon-table'; }
    public function get_categories() { return array( 'brickpoint-elements' ); }

    protected function render() {
      ?>
      <div class="bp-box">
        <table class="bp-table">
          <thead>
            <tr><th>Property</th><th>Specification</th><th>Field Test</th></tr>
          </thead>
          <tbody>
            <tr><td>Standard Size</td><td>9" x 4.5" x 3" (chamber standard)</td><td>Uniform dimensions</td></tr>
            <tr><td>Clay Grade</td><td>Selected alluvial clay</td><td>Ringing metallic sound</td></tr>
            <tr><td>Firing Type</td><td>High-temperature continuous kiln</td><td>Deep copper-red coloration</td></tr>
            <tr><td>Crushing Strength</td><td>Exceeds standard building codes</td><td>High load resistance</td></tr>
            <tr><td>Water Absorption</td><td>Under 15% weight</td><td>Optimal mortar bonding</td></tr>
          </tbody>
        </table>
      </div>
      <?php
    }
  }

  // 12. INDEPENDENT HEADER LOGO WIDGET
  class BrickPoint_Header_Logo_Widget extends \\Elementor\\Widget_Base {
    public function get_name() { return 'bp_header_logo_widget'; }
    public function get_title() { return esc_html__( 'BrickPoint Header Logo', 'brickpoint' ); }
    public function get_icon() { return 'eicon-site-logo'; }
    public function get_categories() { return array( 'brickpoint-elements' ); }

    protected function render() {
      brickpoint_header_logo();
    }
  }

  // 13. INDEPENDENT FOOTER LOGO WIDGET
  class BrickPoint_Footer_Logo_Widget extends \\Elementor\\Widget_Base {
    public function get_name() { return 'bp_footer_logo_widget'; }
    public function get_title() { return esc_html__( 'BrickPoint Footer Logo', 'brickpoint' ); }
    public function get_icon() { return 'eicon-image'; }
    public function get_categories() { return array( 'brickpoint-elements' ); }

    protected function render() {
      brickpoint_footer_logo();
    }
  }

  // Register all 13 widgets with Elementor
  $widgets_manager->register( new BrickPoint_Hero_Widget() );
  $widgets_manager->register( new BrickPoint_SS7_Showcase_Widget() );
  $widgets_manager->register( new BrickPoint_Product_Grid_Widget() );
  $widgets_manager->register( new BrickPoint_Category_Grid_Widget() );
  $widgets_manager->register( new BrickPoint_Video_Showcase_Widget() );
  $widgets_manager->register( new BrickPoint_Projects_Grid_Widget() );
  $widgets_manager->register( new BrickPoint_Locations_Grid_Widget() );
  $widgets_manager->register( new BrickPoint_WhatsApp_CTA_Widget() );
  $widgets_manager->register( new BrickPoint_Audience_Cards_Widget() );
  $widgets_manager->register( new BrickPoint_Stats_Bar_Widget() );
  $widgets_manager->register( new BrickPoint_Specifications_Table_Widget() );
  $widgets_manager->register( new BrickPoint_Header_Logo_Widget() );
  $widgets_manager->register( new BrickPoint_Footer_Logo_Widget() );
}
add_action( 'elementor/widgets/register', 'brickpoint_register_elementor_custom_widgets' );
"""

out_path = os.path.join(DEST, "inc/elementor-widgets.php")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(widgets_php.strip() + "\n")

print("Wrote inc/elementor-widgets.php successfully with 13 custom widgets.")
