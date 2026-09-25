<?php
/**
 * Video Library Archive
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
?>

<div class="bp-pagehead">
  <div class="bp-container">
    <p class="bp-eyebrow"><?php esc_html_e( 'Video Library', 'brickpoint' ); ?></p>
    <h1 class="bp-heading-1"><?php esc_html_e( 'Inside BrickPoint', 'brickpoint' ); ?></h1>
    <p class="bp-pagehead-desc"><?php esc_html_e( 'Explore our products, production process, construction materials, projects, and company updates through video.', 'brickpoint' ); ?></p>
    <div class="bp-filters bp-mt">
      <a href="<?php echo esc_url( get_post_type_archive_link( 'bp_video' ) ); ?>" class="bp-filter-pill active"><?php esc_html_e( 'All Videos', 'brickpoint' ); ?></a>
      <?php
      $vcats = get_terms( array( 'taxonomy' => 'bp_video_category', 'hide_empty' => false ) );
      if ( ! empty( $vcats ) && ! is_wp_error( $vcats ) ) :
        foreach ( $vcats as $vc ) : ?>
          <a href="<?php echo esc_url( get_term_link( $vc ) ); ?>" class="bp-filter-pill"><?php echo esc_html( $vc->name ); ?></a>
      <?php endforeach; endif; ?>
    </div>
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
        <p class="bp-center" style="grid-column:1/-1;"><?php esc_html_e( 'No videos found.', 'brickpoint' ); ?></p>
      <?php endif; ?>
    </div>
    <div class="bp-pagination bp-mt">
      <?php the_posts_pagination(); ?>
    </div>
  </div>
</section>

<?php
get_footer();
