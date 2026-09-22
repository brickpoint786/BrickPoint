<?php
/**
 * Single Location Template
 *
 * @package BrickPoint
 */

if ( ! defined( 'ABSPATH' ) ) {
  exit;
}

get_header();

the_post();
$id = get_the_ID();
$addr = bp_meta( $id, '_bpl_address', '' );
$phone = bp_meta( $id, '_bpl_phone', bp_option( 'bp_phone_display', '0315 2850818' ) );
$hours = bp_meta( $id, '_bpl_hours', 'Mon – Sat: 8:00 AM – 6:00 PM' );
$maps = bp_meta( $id, '_bpl_maps_url', '' );
$video = bp_meta( $id, '_bpl_video', '' );
?>

<div class="bp-crumbs-bar">
  <div class="bp-container bp-crumbs">
    <a href="<?php echo esc_url( home_url( '/' ) ); ?>"><?php esc_html_e( 'Home', 'brickpoint' ); ?></a> &gt;
    <a href="<?php echo esc_url( home_url( '/locations' ) ); ?>"><?php esc_html_e( 'Locations', 'brickpoint' ); ?></a> &gt;
    <span><?php the_title(); ?></span>
  </div>
</div>

<article id="location-<?php echo esc_attr( $id ); ?>" class="bp-section">
  <div class="bp-container bp-narrow">
    <h1 class="bp-heading-1"><?php the_title(); ?></h1>

    <?php if ( has_post_thumbnail() ) : ?>
      <div class="bp-post-hero-img img-zoom bp-mt">
        <?php the_post_thumbnail( 'large', array( 'class' => 'bp-featured-img' ) ); ?>
      </div>
    <?php endif; ?>

    <div class="bp-box bp-mt">
      <p class="bp-loc-meta-item">
        <svg class="bp-icon-sm text-orange" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/></svg>
        <strong>Address:</strong> <?php echo esc_html( $addr ); ?>
      </p>
      <p class="bp-loc-meta-item bp-mt">
        <svg class="bp-icon-sm text-orange" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
        <strong>Phone:</strong> <a href="tel:<?php echo esc_attr( $phone ); ?>"><?php echo esc_html( $phone ); ?></a>
      </p>
      <p class="bp-loc-meta-item bp-mt">
        <svg class="bp-icon-sm text-orange" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
        <strong>Hours:</strong> <?php echo esc_html( $hours ); ?>
      </p>
    </div>

    <div class="bp-box prose-bp bp-mt">
      <?php the_content(); ?>
    </div>

    <?php if ( $video ) : ?>
      <div class="bp-box bp-mt">
        <h3><?php esc_html_e( 'Facility Video', 'brickpoint' ); ?></h3>
        <video controls playsinline preload="metadata" class="bp-video-player bp-mt">
          <source src="<?php echo esc_url( $video ); ?>" type="video/mp4" />
        </video>
      </div>
    <?php endif; ?>

    <div class="bp-action-row bp-mt">
      <?php if ( $maps ) : ?>
        <a href="<?php echo esc_url( $maps ); ?>" target="_blank" rel="noopener" class="btn-dark">
          <span><?php esc_html_e( '📍 Open in Google Maps', 'brickpoint' ); ?></span>
        </a>
      <?php endif; ?>
      <a href="<?php echo esc_url( bp_whatsapp_url( 'Assalam-o-Alaikum BrickPoint, I am interested in visiting: ' . get_the_title() ) ); ?>" target="_blank" rel="noopener" class="btn-whatsapp">
        <span><?php esc_html_e( 'WhatsApp Inquiry', 'brickpoint' ); ?></span>
      </a>
      <a href="<?php echo esc_url( home_url( '/locations' ) ); ?>" class="btn-ghost"><?php esc_html_e( 'All Locations', 'brickpoint' ); ?></a>
    </div>
  </div>
</article>

<?php
get_footer();
