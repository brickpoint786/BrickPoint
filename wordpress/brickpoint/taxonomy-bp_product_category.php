<?php
/**
 * Product Category Taxonomy Template
 *
 * @package BrickPoint
 */

if ( ! defined( 'ABSPATH' ) ) {
  exit;
}

get_header();

if ( function_exists( 'elementor_theme_do_location' ) && elementor_theme_do_location( 'archive' ) ) {
  get_footer();
  return;
}

$term = get_queried_object();
$banner = get_term_meta( $term->term_id, 'bp_cat_banner', true );
if ( ! $banner ) {
  $banner = get_term_meta( $term->term_id, 'bp_cat_image', true );
}
$cat_video = get_term_meta( $term->term_id, 'bp_cat_video', true );
?>

<div class="bp-pagehead" <?php if ( $banner ) : ?>style="background-image:linear-gradient(rgba(20,18,16,0.85), rgba(20,18,16,0.95)), url('<?php echo esc_url( $banner ); ?>'); background-size:cover; background-position:center;"<?php endif; ?>>
  <div class="bp-container">
    <div class="bp-crumbs" style="color:rgba(255,255,255,0.7);">
      <a href="<?php echo esc_url( home_url( '/' ) ); ?>" style="color:inherit;"><?php esc_html_e( 'Home', 'brickpoint' ); ?></a> &gt;
      <a href="<?php echo esc_url( home_url( '/categories' ) ); ?>" style="color:inherit;"><?php esc_html_e( 'Categories', 'brickpoint' ); ?></a> &gt;
      <span><?php echo esc_html( $term->name ); ?></span>
    </div>
    <h1 class="bp-heading-1 bp-mt"><?php echo esc_html( $term->name ); ?></h1>
    <?php if ( $term->description ) : ?>
      <p class="bp-pagehead-desc"><?php echo esc_html( $term->description ); ?></p>
    <?php endif; ?>
    <div class="bp-action-row bp-mt">
      <a href="<?php echo esc_url( bp_whatsapp_url( bp_category_inquiry_message( $term->name ) ) ); ?>" target="_blank" rel="noopener" class="btn-whatsapp">
        <svg class="bp-icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/></svg>
        <span><?php printf( esc_html__( 'Get %s Quote', 'brickpoint' ), esc_html( $term->name ) ); ?></span>
      </a>
      <a href="<?php echo esc_url( home_url( '/products' ) ); ?>" class="btn-ghost" style="color:#fff;border-color:rgba(255,255,255,0.3);">
        <span><?php esc_html_e( 'All Products', 'brickpoint' ); ?></span>
      </a>
    </div>
  </div>
</div>

<?php if ( $cat_video ) : ?>
  <section class="bp-section bp-dark" style="padding:2rem 0;">
    <div class="bp-container bp-narrow">
      <p class="bp-eyebrow" style="margin-bottom:0.8rem;"><?php printf( esc_html__( 'Featured %s Video', 'brickpoint' ), esc_html( $term->name ) ); ?></p>
      <video controls playsinline preload="metadata" class="bp-video-player">
        <source src="<?php echo esc_url( $cat_video ); ?>" type="video/mp4" />
      </video>
    </div>
  </section>
<?php endif; ?>

<section class="bp-section">
  <div class="bp-container">
    <div class="bp-grid cols-4">
      <?php
      if ( have_posts() ) :
        while ( have_posts() ) : the_post();
          get_template_part( 'template-parts/product-card' );
        endwhile;
      else : ?>
        <p class="bp-center" style="grid-column:1/-1;">
          <?php printf( esc_html__( 'No products in %s yet. Ask for rates on WhatsApp.', 'brickpoint' ), esc_html( $term->name ) ); ?>
        </p>
      <?php endif; ?>
    </div>
    <div class="bp-pagination bp-mt">
      <?php the_posts_pagination(); ?>
    </div>
  </div>
</section>

<?php
get_footer();
