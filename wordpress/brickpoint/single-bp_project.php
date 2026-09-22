<?php
/**
 * Single Project Template
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
$cat = bp_meta( $id, '_bpp_category', 'Residential' );
$loc = bp_meta( $id, '_bpp_location', 'Lahore' );
$status = bp_meta( $id, '_bpp_status', 'Illustrative construction reference' );
?>

<div class="bp-crumbs-bar">
  <div class="bp-container bp-crumbs">
    <a href="<?php echo esc_url( home_url( '/' ) ); ?>"><?php esc_html_e( 'Home', 'brickpoint' ); ?></a> &gt;
    <a href="<?php echo esc_url( home_url( '/projects' ) ); ?>"><?php esc_html_e( 'Projects', 'brickpoint' ); ?></a> &gt;
    <span><?php the_title(); ?></span>
  </div>
</div>

<article id="project-<?php echo esc_attr( $id ); ?>" class="bp-section">
  <div class="bp-container bp-narrow">
    <div class="bp-notice-box">
      <strong><?php esc_html_e( 'Content notice:', 'brickpoint' ); ?></strong>
      <em>“<?php echo esc_html( $status ); ?>”</em>. <?php esc_html_e( 'BrickPoint does not claim supply to any named society or developer unless verified by management.', 'brickpoint' ); ?>
    </div>

    <div class="bp-mt">
      <p class="bp-eyebrow"><?php echo esc_html( $loc ); ?> &bull; <?php echo esc_html( $cat ); ?></p>
      <h1 class="bp-heading-1"><?php the_title(); ?></h1>
    </div>

    <?php if ( has_post_thumbnail() ) : ?>
      <div class="bp-post-hero-img img-zoom bp-mt">
        <?php the_post_thumbnail( 'large', array( 'class' => 'bp-featured-img' ) ); ?>
      </div>
    <?php endif; ?>

    <div class="bp-box prose-bp bp-mt">
      <?php the_content(); ?>
    </div>

    <div class="bp-action-row bp-mt">
      <a href="<?php echo esc_url( home_url( '/projects' ) ); ?>" class="btn-ghost"><?php esc_html_e( '← All Projects', 'brickpoint' ); ?></a>
      <a href="<?php echo esc_url( bp_whatsapp_url( 'Assalam-o-Alaikum BrickPoint, I need materials like the ones in project: ' . get_the_title() ) ); ?>" target="_blank" rel="noopener" class="btn-whatsapp">
        <svg class="bp-icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/></svg>
        <span><?php esc_html_e( 'Inquire on WhatsApp', 'brickpoint' ); ?></span>
      </a>
      <a href="<?php echo esc_url( home_url( '/contact' ) ); ?>" class="btn-brick"><?php esc_html_e( 'Request Quotation', 'brickpoint' ); ?></a>
    </div>
  </div>
</article>

<?php
get_footer();
