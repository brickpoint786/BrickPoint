<?php
/**
 * Video Category Taxonomy Template
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
?>

<div class="bp-pagehead">
  <div class="bp-container">
    <div class="bp-crumbs" style="color:rgba(255,255,255,0.7);">
      <a href="<?php echo esc_url( home_url( '/' ) ); ?>" style="color:inherit;"><?php esc_html_e( 'Home', 'brickpoint' ); ?></a> &gt;
      <a href="<?php echo esc_url( home_url( '/videos' ) ); ?>" style="color:inherit;"><?php esc_html_e( 'Videos', 'brickpoint' ); ?></a> &gt;
      <span><?php echo esc_html( $term->name ); ?></span>
    </div>
    <h1 class="bp-heading-1 bp-mt"><?php echo esc_html( $term->name ); ?></h1>
    <?php if ( $term->description ) : ?>
      <p class="bp-pagehead-desc"><?php echo esc_html( $term->description ); ?></p>
    <?php endif; ?>
  </div>
</div>

<section class="bp-section">
  <div class="bp-container">
    <div class="bp-grid cols-3">
      <?php
      if ( have_posts() ) :
        while ( have_posts() ) : the_post();
          get_template_part( 'template-parts/video-card' );
        endwhile;
      else : ?>
        <p class="bp-center" style="grid-column:1/-1;"><?php esc_html_e( 'No videos in this category yet.', 'brickpoint' ); ?></p>
      <?php endif; ?>
    </div>
    <div class="bp-pagination bp-mt">
      <?php the_posts_pagination(); ?>
    </div>
  </div>
</section>

<?php
get_footer();
