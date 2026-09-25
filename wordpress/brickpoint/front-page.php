<?php
/**
 * The template for displaying the front page
 *
 * Checks if Elementor is used on this page; if so, outputs the Elementor content!
 * Otherwise, outputs the complete original 9-section BrickPoint homepage layout.
 *
 * @package BrickPoint
 */

if ( ! defined( 'ABSPATH' ) ) {
  exit;
}

get_header();

// Elementor Single/Page Location Check
if ( function_exists( 'elementor_theme_do_location' ) && elementor_theme_do_location( 'single' ) ) {
  get_footer();
  return;
}

// If current page is edited with Elementor, render the Elementor content directly!
if ( have_posts() ) {
  while ( have_posts() ) {
    the_post();
    if ( get_post_meta( get_the_ID(), '_elementor_edit_mode', true ) === 'builder' ) {
      the_content();
      get_footer();
      return;
    }
  }
}

/* ========================================================
 * NATIVE COMPLETE FALLBACK HOMEPAGE (SAME DESIGN & LAYOUT)
 * ======================================================== */
?>

<!-- 1. HERO SECTION -->
<?php get_template_part( 'template-parts/hero' ); ?>

<!-- 2. TRUST / INTRO SECTION ("Why BrickPoint") -->
<section class="bp-section bp-trust-section">
  <div class="bp-container bp-trust-grid">
    <div class="bp-trust-media img-zoom">
      <img src="<?php echo esc_url( bp_asset_image_url( 'kiln.png' ) ); ?>" alt="<?php esc_attr_e( 'Brick kiln production', 'brickpoint' ); ?>" loading="lazy" />
      <div class="bp-trust-cards-overlay">
        <div class="bp-glass-card">
          <p class="bp-card-h-orange"><?php esc_html_e( 'Trusted Supply', 'brickpoint' ); ?></p>
          <p class="bp-card-sub"><?php esc_html_e( 'Consistent quality for every order size', 'brickpoint' ); ?></p>
        </div>
        <div class="bp-glass-card bp-glass-dark">
          <p class="bp-card-h-white"><?php esc_html_e( 'Bulk Ready', 'brickpoint' ); ?></p>
          <p class="bp-card-sub-dim"><?php esc_html_e( 'Contractors & companies welcome', 'brickpoint' ); ?></p>
        </div>
      </div>
    </div>
    <div class="bp-trust-content">
      <div class="bp-section-head-left">
        <p class="bp-eyebrow"><?php esc_html_e( 'Why BrickPoint', 'brickpoint' ); ?></p>
        <h2 class="bp-heading-2"><?php esc_html_e( 'A construction-materials partner you can build on', 'brickpoint' ); ?></h2>
        <p class="bp-body-text"><?php esc_html_e( 'BrickPoint brings together trusted brick manufacturing units and a complete construction-materials range — so contractors, builders and developers can source with confidence.', 'brickpoint' ); ?></p>
      </div>
      <ul class="bp-check-list">
        <li>
          <svg class="bp-icon-check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M20 6 9 17l-5-5"/></svg>
          <span><?php esc_html_e( 'Quality-focused brick manufacturing at multiple bhatta locations', 'brickpoint' ); ?></span>
        </li>
        <li>
          <svg class="bp-icon-check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M20 6 9 17l-5-5"/></svg>
          <span><?php esc_html_e( 'Complete materials range — from cement and steel to finishes', 'brickpoint' ); ?></span>
        </li>
        <li>
          <svg class="bp-icon-check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M20 6 9 17l-5-5"/></svg>
          <span><?php esc_html_e( 'Project-based quotations with delivery coordination', 'brickpoint' ); ?></span>
        </li>
        <li>
          <svg class="bp-icon-check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M20 6 9 17l-5-5"/></svg>
          <span><?php esc_html_e( 'Direct WhatsApp ordering with fast response', 'brickpoint' ); ?></span>
        </li>
      </ul>
      <div class="bp-action-row">
        <a href="<?php echo esc_url( home_url( '/about' ) ); ?>" class="btn-dark"><?php esc_html_e( 'About BrickPoint →', 'brickpoint' ); ?></a>
        <a href="<?php echo esc_url( home_url( '/locations' ) ); ?>" class="btn-ghost"><?php esc_html_e( 'Our Locations', 'brickpoint' ); ?></a>
      </div>
    </div>
  </div>
</section>

<!-- 3. PRODUCT CATEGORIES SECTION -->
<section class="bp-section bp-dark">
  <div class="bp-container">
    <div class="bp-section-head bp-head-light">
      <p class="bp-eyebrow"><?php esc_html_e( 'Product Categories', 'brickpoint' ); ?></p>
      <h2 class="bp-heading-2"><?php esc_html_e( 'One supplier for your complete material list', 'brickpoint' ); ?></h2>
      <p class="bp-body-text"><?php esc_html_e( 'From flagship SS7 bricks to cement, aggregates, steel, pipes, electricals and finishes.', 'brickpoint' ); ?></p>
    </div>
    <div class="bp-grid cols-4 bp-mt">
      <?php
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
    <div class="bp-center bp-mt">
      <a href="<?php echo esc_url( home_url( '/categories' ) ); ?>" class="btn-ghost" style="color:#fff;border-color:rgba(255,255,255,0.25);">
        <span><?php esc_html_e( 'View All Categories →', 'brickpoint' ); ?></span>
      </a>
    </div>
  </div>
</section>

<!-- 4. FLAGSHIP SS7 BRICKS SECTION -->
<section class="bp-section bp-ss7-section">
  <div class="bp-container bp-ss7-grid">
    <div class="bp-ss7-content">
      <div class="bp-section-head-left">
        <p class="bp-eyebrow"><?php esc_html_e( 'Flagship Product', 'brickpoint' ); ?></p>
        <h2 class="bp-heading-2"><?php esc_html_e( 'The Strength Behind Every Structure', 'brickpoint' ); ?></h2>
        <p class="bp-body-text"><?php esc_html_e( 'SS7 Bricks — our signature range engineered for strength, shape and lasting performance. Ask for specifications, availability and project pricing on WhatsApp.', 'brickpoint' ); ?></p>
      </div>
      <div class="bp-specs-grid">
        <div class="bp-spec-card">
          <p class="bp-spec-lbl"><?php esc_html_e( 'Size', 'brickpoint' ); ?></p>
          <p class="bp-spec-val"><?php esc_html_e( 'Standard chamber size', 'brickpoint' ); ?></p>
        </div>
        <div class="bp-spec-card">
          <p class="bp-spec-lbl"><?php esc_html_e( 'Type', 'brickpoint' ); ?></p>
          <p class="bp-spec-val"><?php esc_html_e( 'Burnt-clay SS7', 'brickpoint' ); ?></p>
        </div>
        <div class="bp-spec-card">
          <p class="bp-spec-lbl"><?php esc_html_e( 'Usage', 'brickpoint' ); ?></p>
          <p class="bp-spec-val"><?php esc_html_e( 'Homes • Commercial • Boundary', 'brickpoint' ); ?></p>
        </div>
        <div class="bp-spec-card">
          <p class="bp-spec-lbl"><?php esc_html_e( 'Availability', 'brickpoint' ); ?></p>
          <p class="bp-spec-val"><?php esc_html_e( 'Bulk & retail orders', 'brickpoint' ); ?></p>
        </div>
      </div>
      <div class="bp-action-row">
        <a href="<?php echo esc_url( bp_whatsapp_url( bp_category_inquiry_message( 'SS7 Bricks' ) ) ); ?>" target="_blank" rel="noopener" class="btn-whatsapp">
          <svg class="bp-icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/></svg>
          <span><?php esc_html_e( 'Request SS7 Quote', 'brickpoint' ); ?></span>
        </a>
        <a href="<?php echo esc_url( home_url( '/ss7-bricks' ) ); ?>" class="btn-dark"><?php esc_html_e( 'View SS7 Page →', 'brickpoint' ); ?></a>
      </div>
    </div>
    <div class="bp-ss7-gallery-wrap">
      <div class="bp-ss7-main-img img-zoom">
        <img src="<?php echo esc_url( bp_asset_image_url( 'red-stack.png' ) ); ?>" alt="<?php esc_attr_e( 'SS7 Red Bricks Stacked', 'brickpoint' ); ?>" loading="lazy" />
      </div>
      <div class="bp-ss7-thumbs-row">
        <img src="<?php echo esc_url( bp_asset_image_url( 'stacked.png' ) ); ?>" alt="SS7 gallery" loading="lazy" />
        <img src="<?php echo esc_url( bp_asset_image_url( 'pile.png' ) ); ?>" alt="SS7 gallery" loading="lazy" />
        <img src="<?php echo esc_url( bp_asset_image_url( 'worker.png' ) ); ?>" alt="SS7 gallery" loading="lazy" />
      </div>
    </div>
  </div>
</section>

<!-- 5. FEATURED PRODUCTS SECTION -->
<section class="bp-section">
  <div class="bp-container">
    <div class="bp-section-head">
      <p class="bp-eyebrow"><?php esc_html_e( 'Featured Products', 'brickpoint' ); ?></p>
      <h2 class="bp-heading-2"><?php esc_html_e( 'Materials contractors ask for by name', 'brickpoint' ); ?></h2>
      <p class="bp-body-text"><?php esc_html_e( 'Live from the product catalogue — prices, units and WhatsApp ordering on every card.', 'brickpoint' ); ?></p>
    </div>
    <div class="bp-grid cols-4 bp-mt">
      <?php
      $pq = new WP_Query( array(
        'post_type'      => 'bp_product',
        'posts_per_page' => 8,
        'meta_key'       => '_bp_featured',
        'meta_value'     => '1',
      ) );
      if ( ! $pq->have_posts() ) {
        $pq = new WP_Query( array( 'post_type' => 'bp_product', 'posts_per_page' => 8 ) );
      }
      if ( $pq->have_posts() ) :
        while ( $pq->have_posts() ) : $pq->the_post();
          get_template_part( 'template-parts/product-card' );
        endwhile;
        wp_reset_postdata();
      else :
        for ( $i = 1; $i <= 4; $i++ ) : ?>
          <div class="bp-placeholder-card">
            <p><strong><?php esc_html_e( 'Products loading from catalogue…', 'brickpoint' ); ?></strong></p>
            <p class="bp-sub"><?php esc_html_e( 'Run Appearance → BrickPoint Demo to load demo products.', 'brickpoint' ); ?></p>
          </div>
      <?php endfor; endif; ?>
    </div>
    <div class="bp-center bp-mt">
      <a href="<?php echo esc_url( home_url( '/products' ) ); ?>" class="btn-brick">
        <span><?php esc_html_e( 'Browse All Products →', 'brickpoint' ); ?></span>
      </a>
    </div>
  </div>
</section>

<!-- 6. VIDEO SHOWCASE SECTION -->
<section class="bp-section bp-dark">
  <div class="bp-container">
    <div class="bp-video-header-row">
      <div class="bp-section-head-left">
        <p class="bp-eyebrow"><?php esc_html_e( 'Inside BrickPoint', 'brickpoint' ); ?></p>
        <h2 class="bp-heading-2 bp-head-light"><?php esc_html_e( 'See the Strength Behind Every Brick', 'brickpoint' ); ?></h2>
        <p class="bp-body-text bp-head-light-dim"><?php esc_html_e( 'Manufacturing, bhattas, quality checks, materials and project references — on video.', 'brickpoint' ); ?></p>
      </div>
      <a href="<?php echo esc_url( home_url( '/videos' ) ); ?>" class="btn-ghost" style="color:#fff;border-color:rgba(255,255,255,0.25);">
        <span><?php esc_html_e( 'View All Videos →', 'brickpoint' ); ?></span>
      </a>
    </div>
    <div class="bp-video-featured-grid bp-mt">
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
            <span class="bp-video-sub-tag"><?php esc_html_e( 'From the Bhatta to Your Building', 'brickpoint' ); ?></span>
          </div>
          <p class="bp-video-sub-desc"><?php esc_html_e( 'Brick preparation, firing, stacking, loading and quality — the journey of every batch.', 'brickpoint' ); ?></p>
        </div>
        <div class="bp-video-sub-card">
          <div class="bp-video-sub-thumb">
            <video playsinline muted loop autoplay preload="metadata" poster="<?php echo esc_url( bp_asset_image_url( 'aerial-poster.png' ) ); ?>">
              <source src="<?php echo esc_url( bp_option( 'bp_aerial_video', 'https://videos.pexels.com/video-files/20731372/20731372-uhd_3840_2160_30fps.mp4' ) ); ?>" type="video/mp4" />
            </video>
            <span class="bp-video-sub-tag"><?php esc_html_e( 'Materials That Become Landmarks', 'brickpoint' ); ?></span>
          </div>
          <p class="bp-video-sub-desc"><?php esc_html_e( 'Illustrative construction references from housing developments and building work.', 'brickpoint' ); ?></p>
        </div>
      </div>
    </div>
    <!-- 3 Recent Video Cards -->
    <div class="bp-grid cols-3 bp-mt">
      <?php
      $vq = new WP_Query( array( 'post_type' => 'bp_video', 'posts_per_page' => 3 ) );
      if ( $vq->have_posts() ) :
        while ( $vq->have_posts() ) : $vq->the_post();
          get_template_part( 'template-parts/video-card' );
        endwhile;
        wp_reset_postdata();
      endif;
      ?>
    </div>
  </div>
</section>

<!-- 7. PROJECT REFERENCES PREVIEW SECTION -->
<section class="bp-section">
  <div class="bp-container">
    <div class="bp-section-head">
      <p class="bp-eyebrow"><?php esc_html_e( 'Project References', 'brickpoint' ); ?></p>
      <h2 class="bp-heading-2"><?php esc_html_e( 'Materials that become landmarks', 'brickpoint' ); ?></h2>
      <p class="bp-body-text"><?php esc_html_e( 'Illustrative construction references from Lahore housing societies and building work.', 'brickpoint' ); ?></p>
    </div>
    <div class="bp-grid cols-3 bp-mt">
      <?php
      $proj_q = new WP_Query( array( 'post_type' => 'bp_project', 'posts_per_page' => 3 ) );
      if ( $proj_q->have_posts() ) :
        while ( $proj_q->have_posts() ) : $proj_q->the_post();
          get_template_part( 'template-parts/project-card' );
        endwhile;
        wp_reset_postdata();
      else :
        $default_projs = array(
          array( 'title' => 'DHA Lahore — Villa Reference', 'loc' => 'DHA Lahore', 'img' => bp_asset_image_url( 'villa1.png' ) ),
          array( 'title' => 'Bahria Town — Housing Reference', 'loc' => 'Bahria Town Lahore', 'img' => bp_asset_image_url( 'villa2.png' ) ),
          array( 'title' => 'Lake City — Development Reference', 'loc' => 'Lake City Lahore', 'img' => bp_asset_image_url( 'apt.png' ) ),
        );
        foreach ( $default_projs as $dp ) : ?>
          <a href="<?php echo esc_url( home_url( '/projects' ) ); ?>" class="bp-card card-hover group">
            <div class="bp-card-media img-zoom">
              <img src="<?php echo esc_url( $dp['img'] ); ?>" alt="<?php echo esc_attr( $dp['title'] ); ?>" loading="lazy" />
              <span class="bp-illus-badge"><?php esc_html_e( 'Illustrative construction reference', 'brickpoint' ); ?></span>
            </div>
            <div class="bp-card-body">
              <p class="bp-card-loc"><?php echo esc_html( $dp['loc'] ); ?></p>
              <h3><?php echo esc_html( $dp['title'] ); ?></h3>
            </div>
          </a>
      <?php endforeach; endif; ?>
    </div>
  </div>
</section>

<!-- 8. WHO WE SERVE SECTION -->
<section class="bp-section bp-sand-section">
  <div class="bp-container">
    <div class="bp-section-head">
      <p class="bp-eyebrow"><?php esc_html_e( 'Who We Serve', 'brickpoint' ); ?></p>
      <h2 class="bp-heading-2"><?php esc_html_e( 'Built for the way you build', 'brickpoint' ); ?></h2>
      <p class="bp-body-text"><?php esc_html_e( 'Bulk supply, project quotations and coordinated materials — for every scale of builder.', 'brickpoint' ); ?></p>
    </div>
    <div class="bp-grid cols-3 bp-mt">
      <!-- For Contractors -->
      <a href="<?php echo esc_url( home_url( '/for-contractors' ) ); ?>" class="bp-audience-card card-hover group">
        <div class="bp-audience-media img-zoom">
          <img src="<?php echo esc_url( bp_asset_image_url( 'site.png' ) ); ?>" alt="<?php esc_attr_e( 'For Contractors', 'brickpoint' ); ?>" loading="lazy" />
          <div class="bp-audience-overlay"></div>
        </div>
        <div class="bp-audience-body">
          <h3><?php esc_html_e( 'For Contractors', 'brickpoint' ); ?></h3>
          <p><?php esc_html_e( 'Bulk material supply, project-based quotations and delivery coordination.', 'brickpoint' ); ?></p>
          <span class="bp-audience-link"><?php esc_html_e( 'Learn more →', 'brickpoint' ); ?></span>
        </div>
      </a>
      <!-- For Builders -->
      <a href="<?php echo esc_url( home_url( '/for-builders' ) ); ?>" class="bp-audience-card card-hover group">
        <div class="bp-audience-media img-zoom">
          <img src="<?php echo esc_url( bp_asset_image_url( 'bricklayer.png' ) ); ?>" alt="<?php esc_attr_e( 'For Builders', 'brickpoint' ); ?>" loading="lazy" />
          <div class="bp-audience-overlay"></div>
        </div>
        <div class="bp-audience-body">
          <h3><?php esc_html_e( 'For Builders', 'brickpoint' ); ?></h3>
          <p><?php esc_html_e( 'Consistent quality across every batch, with multi-category sourcing.', 'brickpoint' ); ?></p>
          <span class="bp-audience-link"><?php esc_html_e( 'Learn more →', 'brickpoint' ); ?></span>
        </div>
      </a>
      <!-- For Construction Companies -->
      <a href="<?php echo esc_url( home_url( '/for-companies' ) ); ?>" class="bp-audience-card card-hover group">
        <div class="bp-audience-media img-zoom">
          <img src="<?php echo esc_url( bp_asset_image_url( 'apt.png' ) ); ?>" alt="<?php esc_attr_e( 'For Construction Companies', 'brickpoint' ); ?>" loading="lazy" />
          <div class="bp-audience-overlay"></div>
        </div>
        <div class="bp-audience-body">
          <h3><?php esc_html_e( 'For Construction Companies', 'brickpoint' ); ?></h3>
          <p><?php esc_html_e( 'Large-scale supply, documentation and dedicated contact.', 'brickpoint' ); ?></p>
          <span class="bp-audience-link"><?php esc_html_e( 'Learn more →', 'brickpoint' ); ?></span>
        </div>
      </a>
    </div>
  </div>
</section>

<!-- 9. CTA SECTION -->
<section class="bp-section bp-cta-section">
  <div class="bp-cta-bg-img">
    <img src="<?php echo esc_url( bp_asset_image_url( 'bricklayer.png' ) ); ?>" alt="" loading="lazy" />
    <div class="bp-cta-bg-grad"></div>
  </div>
  <div class="bp-container bp-cta-inner">
    <div class="bp-cta-text">
      <p class="bp-eyebrow"><?php esc_html_e( 'Get a fast quotation', 'brickpoint' ); ?></p>
      <h2 class="bp-heading-1"><?php esc_html_e( 'Send your material list.', 'brickpoint' ); ?><br /><?php esc_html_e( 'We handle the rest.', 'brickpoint' ); ?></h2>
      <p class="bp-cta-meta">
        <svg class="bp-icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
        <span><?php echo esc_html( bp_option( 'bp_phone_display', '0315 2850818' ) ); ?> &bull; CEO: <?php echo esc_html( bp_option( 'bp_ceo', 'Syed Iftikhar Haider' ) ); ?> &bull; Sales: <?php echo esc_html( bp_option( 'bp_sales', 'Qasim Iqbal' ) ); ?></span>
      </p>
    </div>
    <div class="bp-cta-buttons">
      <a href="<?php echo esc_url( bp_whatsapp_url( "Assalam-o-Alaikum BrickPoint,\n\nPlease share a quotation for my construction materials.\n\nThank you." ) ); ?>" target="_blank" rel="noopener" class="btn-whatsapp btn-lg">
        <svg class="bp-icon-md" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/></svg>
        <span><?php esc_html_e( 'WhatsApp Your List', 'brickpoint' ); ?></span>
      </a>
      <a href="<?php echo esc_url( home_url( '/contact' ) ); ?>" class="btn-brick btn-lg">
        <span><?php esc_html_e( 'Request Quote Form', 'brickpoint' ); ?></span>
      </a>
    </div>
  </div>
</section>

<?php
if ( have_posts() ) {
  while ( have_posts() ) {
    the_post();
    the_content();
  }
}

get_footer();
