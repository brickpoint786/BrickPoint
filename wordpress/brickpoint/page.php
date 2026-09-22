<?php
/**
 * The template for displaying all pages
 *
 * @package BrickPoint
 */

if ( ! defined( 'ABSPATH' ) ) {
  exit;
}

get_header();

// Elementor Pro single location check
if ( function_exists( 'elementor_theme_do_location' ) && elementor_theme_do_location( 'single' ) ) {
  get_footer();
  return;
}
?>

<main id="primary" class="site-main">
  <?php
  while ( have_posts() ) : the_post();
    // If page is built with Elementor, output content directly full width!
    if ( get_post_meta( get_the_ID(), '_elementor_edit_mode', true ) === 'builder' ) {
      the_content();
    } else {
      ?>
      <div class="bp-pagehead">
        <div class="bp-container">
          <p class="bp-eyebrow"><?php esc_html_e( 'BrickPoint', 'brickpoint' ); ?></p>
          <h1 class="bp-heading-1"><?php the_title(); ?></h1>
        </div>
      </div>
      <div class="bp-section">
        <div class="bp-container bp-prose-wrap">
          <div class="prose-bp">
            <?php the_content(); ?>
          </div>
        </div>
      </div>
      <?php
    }
  endwhile;
  ?>
</main>

<?php
get_footer();
