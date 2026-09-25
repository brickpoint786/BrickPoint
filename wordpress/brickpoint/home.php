<?php
/**
 * Blog index template
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
    <h1 class="bp-heading-1"><?php esc_html_e( 'Blog', 'brickpoint' ); ?></h1>
    <p class="bp-pagehead-desc"><?php esc_html_e( 'Brick selection, material guides, planning tips and industry updates.', 'brickpoint' ); ?></p>
    <form action="<?php echo esc_url( home_url( '/blog' ) ); ?>" method="get" class="bp-search-form bp-mt">
      <input type="search" name="s" placeholder="<?php esc_attr_e( 'Search articles…', 'brickpoint' ); ?>" value="<?php echo esc_attr( get_search_query() ); ?>" class="bp-input" />
      <button type="submit" class="btn-brick"><?php esc_html_e( 'Search', 'brickpoint' ); ?></button>
    </form>
  </div>
</div>

<section class="bp-section">
  <div class="bp-container">
    <?php
    $categories = get_categories();
    if ( ! empty( $categories ) ) : ?>
      <div class="bp-filters">
        <a href="<?php echo esc_url( home_url( '/blog' ) ); ?>" class="bp-filter-pill active"><?php esc_html_e( 'All', 'brickpoint' ); ?></a>
        <?php foreach ( $categories as $c ) : ?>
          <a href="<?php echo esc_url( get_category_link( $c->term_id ) ); ?>" class="bp-filter-pill"><?php echo esc_html( $c->name ); ?></a>
        <?php endforeach; ?>
      </div>
    <?php endif; ?>

    <div class="bp-grid cols-3 bp-mt">
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
