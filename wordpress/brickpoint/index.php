<?php if ( ! defined( 'ABSPATH' ) ) { exit; }
get_header(); ?>
<div class="bp-container bp-section">
  <?php if ( have_posts() ) : ?>
    <div class="bp-grid cols-3">
      <?php while ( have_posts() ) : the_post(); get_template_part( 'template-parts/content' ); endwhile; ?>
    </div>
    <?php brickpoint_pagination(); ?>
  <?php else : ?>
    <p><?php esc_html_e( 'No content found.', 'brickpoint' ); ?></p>
  <?php endif; ?>
</div>
<?php get_footer(); ?>
