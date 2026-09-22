<?php
/**
 * Product Archive Template
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
    <p class="bp-eyebrow"><?php esc_html_e( 'Catalogue', 'brickpoint' ); ?></p>
    <h1 class="bp-heading-1"><?php esc_html_e( 'Products', 'brickpoint' ); ?></h1>
    <p class="bp-pagehead-desc"><?php esc_html_e( 'Every product with WhatsApp ordering — no cart, no checkout, just fast quotations.', 'brickpoint' ); ?></p>
    <div class="bp-filters bp-mt">
      <a href="<?php echo esc_url( get_post_type_archive_link( 'bp_product' ) ); ?>" class="bp-filter-pill active"><?php esc_html_e( 'All', 'brickpoint' ); ?></a>
      <?php
      $cats = get_terms( array( 'taxonomy' => 'bp_product_category', 'hide_empty' => false ) );
      if ( ! empty( $cats ) && ! is_wp_error( $cats ) ) :
        foreach ( $cats as $c ) : ?>
          <a href="<?php echo esc_url( get_term_link( $c ) ); ?>" class="bp-filter-pill"><?php echo esc_html( $c->name ); ?></a>
      <?php endforeach; endif; ?>
    </div>
  </div>
</div>

<section class="bp-section">
  <div class="bp-container">
    <div class="bp-grid cols-4">
      <?php
      if ( have_posts() ) :
        while ( have_posts() ) : the_post();
          get_template_part( 'template-parts/product-card' );
        endwhile;
      else : ?>
        <p class="bp-center" style="grid-column:1/-1;"><?php esc_html_e( 'No products found. Please import demo data from Appearance → BrickPoint Demo.', 'brickpoint' ); ?></p>
      <?php endif; ?>
    </div>
    <div class="bp-pagination bp-mt">
      <?php the_posts_pagination(); ?>
    </div>
  </div>
</section>

<?php
get_footer();
