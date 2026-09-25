<?php
/**
 * Single Product template (No WooCommerce, Direct WhatsApp Ordering)
 *
 * @package BrickPoint
 */

if ( ! defined( 'ABSPATH' ) ) {
  exit;
}

get_header();

if ( function_exists( 'elementor_theme_do_location' ) && elementor_theme_do_location( 'single' ) ) {
  get_footer();
  return;
}

the_post();
$id = get_the_ID();
$price = bp_meta( $id, '_bp_price', '' );
$price_label = bp_meta( $id, '_bp_price_label', '' );
$unit = bp_meta( $id, '_bp_unit', '' );
$avail = bp_meta( $id, '_bp_availability', 'In Stock' );
$badge = bp_meta( $id, '_bp_badge', '' );
$sku = bp_meta( $id, '_bp_sku', '' );
$short = bp_meta( $id, '_bp_short', '' );
$gallery_raw = bp_meta( $id, '_bp_gallery', '' );
$specs_raw = bp_meta( $id, '_bp_specs', '' );
$features_raw = bp_meta( $id, '_bp_features', '' );
$video_url = bp_meta( $id, '_bp_video', '' );
$brochure_url = bp_meta( $id, '_bp_brochure', '' );
$wa_override = bp_meta( $id, '_bp_whatsapp', '' );

$terms = get_the_terms( $id, 'bp_product_category' );
$cat_name = ( $terms && ! is_wp_error( $terms ) ) ? $terms[0]->name : '';
$cat_link = ( $terms && ! is_wp_error( $terms ) ) ? get_term_link( $terms[0] ) : '';

$inquiry_text = $wa_override ? $wa_override : bp_product_inquiry_message( array(
  'product'  => get_the_title(),
  'category' => $cat_name,
  'price'    => trim( $price . ' ' . $price_label ),
  'unit'     => $unit,
) );
?>

<div class="bp-crumbs-bar">
  <div class="bp-container bp-crumbs">
    <a href="<?php echo esc_url( home_url( '/' ) ); ?>"><?php esc_html_e( 'Home', 'brickpoint' ); ?></a> &gt;
    <a href="<?php echo esc_url( home_url( '/products' ) ); ?>"><?php esc_html_e( 'Products', 'brickpoint' ); ?></a> &gt;
    <?php if ( $cat_name ) : ?>
      <a href="<?php echo esc_url( $cat_link ); ?>"><?php echo esc_html( $cat_name ); ?></a> &gt;
    <?php endif; ?>
    <span><?php the_title(); ?></span>
  </div>
</div>

<article id="product-<?php echo esc_attr( $id ); ?>" class="bp-section">
  <div class="bp-container bp-product-layout">
    <!-- Left Column: Media & Gallery -->
    <div class="bp-product-media-col">
      <div class="bp-product-hero-media img-zoom">
        <?php if ( has_post_thumbnail() ) : ?>
          <?php the_post_thumbnail( 'large', array( 'id' => 'bpMainProductImg', 'class' => 'bp-product-img' ) ); ?>
        <?php else : ?>
          <img id="bpMainProductImg" src="<?php echo esc_url( bp_asset_image_url( 'stacked.png' ) ); ?>" alt="<?php the_title_attribute(); ?>" class="bp-product-img" />
        <?php endif; ?>
        <?php if ( $badge ) : ?><span class="bp-badge"><?php echo esc_html( $badge ); ?></span><?php endif; ?>
      </div>

      <?php
      $gallery = array_filter( array_map( 'trim', explode( "\n", $gallery_raw ) ) );
      if ( ! empty( $gallery ) ) : ?>
        <div class="bp-thumbs bp-mt">
          <?php if ( has_post_thumbnail() ) : ?>
            <img src="<?php echo esc_url( get_the_post_thumbnail_url( $id, 'thumbnail' ) ); ?>" alt="thumb" class="bp-thumb active" onclick="document.getElementById('bpMainProductImg').src='<?php echo esc_url( get_the_post_thumbnail_url( $id, 'large' ) ); ?>'" />
          <?php endif; ?>
          <?php foreach ( $gallery as $img_url ) : ?>
            <img src="<?php echo esc_url( $img_url ); ?>" alt="gallery thumb" class="bp-thumb" onclick="document.getElementById('bpMainProductImg').src='<?php echo esc_url( $img_url ); ?>'" />
          <?php endforeach; ?>
        </div>
      <?php endif; ?>

      <?php if ( $video_url ) : ?>
        <div class="bp-box bp-mt">
          <h4><?php esc_html_e( 'Product Video', 'brickpoint' ); ?></h4>
          <video controls playsinline preload="metadata" class="bp-video-player bp-mt">
            <source src="<?php echo esc_url( $video_url ); ?>" type="video/mp4" />
          </video>
        </div>
      <?php endif; ?>
    </div>

    <!-- Right Column: Product Details & WhatsApp Ordering -->
    <div class="bp-product-info-col">
      <?php if ( $cat_name ) : ?>
        <p class="bp-eyebrow"><a href="<?php echo esc_url( $cat_link ); ?>" style="color:inherit;text-decoration:none;"><?php echo esc_html( $cat_name ); ?></a></p>
      <?php endif; ?>

      <h1 class="bp-heading-1"><?php the_title(); ?></h1>

      <div class="bp-product-price-box bp-mt">
        <?php if ( $price ) : ?>
          <span class="bp-price-main"><?php echo esc_html( $price ); ?></span>
          <?php if ( $unit ) : ?><span class="bp-unit-tag">/ <?php echo esc_html( $unit ); ?></span><?php endif; ?>
        <?php else : ?>
          <span class="bp-price-main"><?php esc_html_e( 'Price on request', 'brickpoint' ); ?></span>
        <?php endif; ?>
        <?php if ( $price_label ) : ?>
          <p class="bp-price-lbl"><?php echo esc_html( $price_label ); ?></p>
        <?php endif; ?>
      </div>

      <?php if ( $avail ) : ?>
        <p class="bp-avail-tag"><span class="bp-dot"></span> <?php echo esc_html( $avail ); ?></p>
      <?php endif; ?>

      <?php if ( $sku ) : ?>
        <p class="bp-sku-tag">SKU: <strong><?php echo esc_html( $sku ); ?></strong></p>
      <?php endif; ?>

      <?php if ( $short ) : ?>
        <div class="bp-short-desc bp-mt">
          <p><?php echo esc_html( $short ); ?></p>
        </div>
      <?php endif; ?>

      <!-- Ordering Buttons: WhatsApp & Phone -->
      <div class="bp-product-cta bp-mt">
        <a href="<?php echo esc_url( bp_whatsapp_url( $inquiry_text ) ); ?>" target="_blank" rel="noopener" class="btn-whatsapp btn-lg btn-block">
          <svg class="bp-icon-md" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/></svg>
          <span><?php esc_html_e( 'Order on WhatsApp', 'brickpoint' ); ?></span>
        </a>
        <a href="tel:<?php echo esc_attr( bp_option( 'bp_phone_display', '0315 2850818' ) ); ?>" class="btn-ghost btn-lg btn-block">
          <svg class="bp-icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
          <span><?php esc_html_e( 'Call for Rate', 'brickpoint' ); ?></span>
        </a>
      </div>

      <!-- Specifications Table -->
      <?php
      $specs = array_filter( array_map( 'trim', explode( "\n", $specs_raw ) ) );
      if ( ! empty( $specs ) ) : ?>
        <div class="bp-box bp-mt">
          <h3><?php esc_html_e( 'Product Specifications', 'brickpoint' ); ?></h3>
          <dl class="bp-specs-dl">
            <?php foreach ( $specs as $line ) :
              $parts = explode( ':', $line, 2 );
              if ( count( $parts ) === 2 ) : ?>
                <div class="bp-spec-row">
                  <dt><?php echo esc_html( trim( $parts[0] ) ); ?></dt>
                  <dd><?php echo esc_html( trim( $parts[1] ) ); ?></dd>
                </div>
            <?php endif; endforeach; ?>
          </dl>
        </div>
      <?php endif; ?>

      <!-- Features Checklist -->
      <?php
      $features = array_filter( array_map( 'trim', explode( "\n", $features_raw ) ) );
      if ( ! empty( $features ) ) : ?>
        <div class="bp-box bp-mt">
          <h3><?php esc_html_e( 'Key Features', 'brickpoint' ); ?></h3>
          <ul class="bp-check-list bp-mt">
            <?php foreach ( $features as $feat ) : ?>
              <li>
                <svg class="bp-icon-check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M20 6 9 17l-5-5"/></svg>
                <span><?php echo esc_html( $feat ); ?></span>
              </li>
            <?php endforeach; ?>
          </ul>
        </div>
      <?php endif; ?>

      <?php if ( $brochure_url ) : ?>
        <p class="bp-mt">
          <a href="<?php echo esc_url( $brochure_url ); ?>" target="_blank" rel="noopener" class="btn-ghost">
            <span><?php esc_html_e( '📄 Download Brochure / Specs PDF', 'brickpoint' ); ?></span>
          </a>
        </p>
      <?php endif; ?>
    </div>
  </div>

  <!-- Full Description Tab/Box -->
  <div class="bp-container bp-mt">
    <div class="bp-box prose-bp">
      <h2><?php esc_html_e( 'Product Description', 'brickpoint' ); ?></h2>
      <?php the_content(); ?>
    </div>
  </div>

  <!-- Related Products Section -->
  <?php
  if ( $terms && ! is_wp_error( $terms ) ) {
    $rel_p = new WP_Query( array(
      'post_type'      => 'bp_product',
      'posts_per_page' => 4,
      'post__not_in'   => array( $id ),
      'tax_query'      => array(
        array(
          'taxonomy' => 'bp_product_category',
          'field'    => 'term_id',
          'terms'    => $terms[0]->term_id,
        ),
      ),
    ) );
    if ( $rel_p->have_posts() ) : ?>
      <div class="bp-container bp-mt" style="padding-top:2rem;">
        <h2 class="bp-heading-2"><?php esc_html_e( 'Related Products', 'brickpoint' ); ?></h2>
        <div class="bp-grid cols-4 bp-mt">
          <?php while ( $rel_p->have_posts() ) : $rel_p->the_post();
            get_template_part( 'template-parts/product-card' );
          endwhile; wp_reset_postdata(); ?>
        </div>
      </div>
    <?php endif;
  }
  ?>
</article>

<?php
get_footer();
