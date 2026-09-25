<?php
/**
 * The template for displaying single blog posts
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
?>

<div class="bp-crumbs-bar">
  <div class="bp-container bp-crumbs">
    <a href="<?php echo esc_url( home_url( '/' ) ); ?>"><?php esc_html_e( 'Home', 'brickpoint' ); ?></a> &gt;
    <a href="<?php echo esc_url( home_url( '/blog' ) ); ?>"><?php esc_html_e( 'Blog', 'brickpoint' ); ?></a> &gt;
    <span><?php the_title(); ?></span>
  </div>
</div>

<article id="post-<?php the_ID(); ?>" <?php post_class( 'bp-container bp-single-post-wrap bp-section' ); ?>>
  <?php
  $cats = get_the_category();
  if ( ! empty( $cats ) ) : ?>
    <span class="bp-badge" style="position:static;display:inline-block;margin-bottom:0.8rem;"><?php echo esc_html( $cats[0]->name ); ?></span>
  <?php endif; ?>

  <h1 class="bp-heading-1"><?php the_title(); ?></h1>

  <div class="bp-post-meta-row">
    <span class="bp-meta-item">
      <svg class="bp-icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
      <?php the_author(); ?>
    </span>
    <span class="bp-meta-item">
      <svg class="bp-icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect width="18" height="18" x="3" y="4" rx="2" ry="2"/><line x1="16" x2="16" y1="2" y2="6"/><line x1="8" x2="8" y1="2" y2="6"/><line x1="3" x2="21" y1="10" y2="10"/></svg>
      <?php echo esc_html( get_the_date() ); ?>
    </span>
    <?php
    $tags = get_the_tags();
    if ( ! empty( $tags ) ) : ?>
      <span class="bp-meta-item">
        <svg class="bp-icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2H2v10l9.29 9.29c.94.94 2.48.94 3.42 0l6.58-6.58c.94-.94.94-2.48 0-3.42L12 2Z"/><path d="M7 7h.01"/></svg>
        <?php the_tags( '', ', ' ); ?>
      </span>
    <?php endif; ?>
  </div>

  <?php if ( has_post_thumbnail() ) : ?>
    <div class="bp-post-hero-img img-zoom">
      <?php the_post_thumbnail( 'large', array( 'class' => 'bp-featured-img' ) ); ?>
    </div>
  <?php endif; ?>

  <div class="bp-post-content-box prose-bp">
    <?php if ( has_excerpt() ) : ?>
      <p class="bp-post-lead"><?php echo esc_html( get_the_excerpt() ); ?></p>
    <?php endif; ?>
    <?php the_content(); ?>
  </div>

  <div class="bp-post-cta-row">
    <a href="<?php echo esc_url( home_url( '/blog' ) ); ?>" class="btn-ghost"><?php esc_html_e( '← All Articles', 'brickpoint' ); ?></a>
    <a href="<?php echo esc_url( home_url( '/products' ) ); ?>" class="btn-dark"><?php esc_html_e( 'Shop Materials', 'brickpoint' ); ?></a>
    <a href="<?php echo esc_url( bp_whatsapp_url( 'Assalam-o-Alaikum BrickPoint, I have an inquiry.' ) ); ?>" target="_blank" rel="noopener" class="btn-whatsapp">
      <span><?php esc_html_e( 'Ask on WhatsApp', 'brickpoint' ); ?></span>
    </a>
  </div>
</article>

<?php
// Related posts
$orig_cats = wp_get_post_categories( get_the_ID() );
if ( ! empty( $orig_cats ) ) {
  $rel_q = new WP_Query( array(
    'category__in'   => $orig_cats,
    'post__not_in'   => array( get_the_ID() ),
    'posts_per_page' => 3,
  ) );
  if ( $rel_q->have_posts() ) : ?>
    <section class="bp-section bp-related-section">
      <div class="bp-container">
        <h2 class="bp-heading-2"><?php esc_html_e( 'Related Articles', 'brickpoint' ); ?></h2>
        <div class="bp-grid cols-3 bp-mt">
          <?php while ( $rel_q->have_posts() ) : $rel_q->the_post(); ?>
            <a href="<?php the_permalink(); ?>" class="bp-card card-hover group">
              <?php if ( has_post_thumbnail() ) : ?>
                <div class="bp-card-media img-zoom">
                  <?php the_post_thumbnail( 'bp-card' ); ?>
                </div>
              <?php endif; ?>
              <div class="bp-card-body">
                <h3><?php the_title(); ?></h3>
              </div>
            </a>
          <?php endwhile; wp_reset_postdata(); ?>
        </div>
      </div>
    </section>
  <?php endif;
}

get_footer();
