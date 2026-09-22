<?php
/**
 * The archive template for blog posts
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
    <p class="bp-eyebrow"><?php esc_html_e( 'Guides & Updates', 'brickpoint' ); ?></p>
    <h1 class="bp-heading-1"><?php the_archive_title(); ?></h1>
    <p class="bp-pagehead-desc"><?php the_archive_description(); ?></p>
  </div>
</div>

<section class="bp-section">
  <div class="bp-container">
    <div class="bp-grid cols-3">
      <?php
      if ( have_posts() ) :
        while ( have_posts() ) : the_post();
          get_template_part( 'template-parts/content' );
        endwhile;
      else : ?>
        <p><?php esc_html_e( 'No posts found.', 'brickpoint' ); ?></p>
      <?php endif; ?>
    </div>
    <div class="bp-pagination bp-mt">
      <?php the_posts_pagination(); ?>
    </div>
  </div>
</section>

<?php
get_footer();
