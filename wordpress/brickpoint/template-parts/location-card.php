<?php
/**
 * Location Card template part
 *
 * @package BrickPoint
 */

if ( ! defined( 'ABSPATH' ) ) {
  exit;
}

$id = get_the_ID();
$addr = bp_meta( $id, '_bpl_address', '' );
$maps = bp_meta( $id, '_bpl_maps_url', '' );
?>
<article class="bp-card card-hover group flex-col">
  <div class="bp-card-media img-zoom">
    <?php if ( has_post_thumbnail() ) : ?>
      <?php the_post_thumbnail( 'bp-card' ); ?>
    <?php else : ?>
      <img src="<?php echo esc_url( bp_asset_image_url( 'kiln.png' ) ); ?>" alt="<?php the_title_attribute(); ?>" />
    <?php endif; ?>
  </div>
  <div class="bp-card-body flex-1">
    <h3 class="bp-card-title"><?php the_title(); ?></h3>
    <?php if ( $addr ) : ?>
      <p class="bp-loc-item">
        <svg class="bp-icon-xs text-orange" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/></svg>
        <span><?php echo esc_html( $addr ); ?></span>
      </p>
    <?php endif; ?>
    <p class="bp-card-excerpt line-clamp-3"><?php echo esc_html( get_the_excerpt() ); ?></p>
    <div class="bp-card-cta bp-mt">
      <?php if ( $maps ) : ?>
        <a href="<?php echo esc_url( $maps ); ?>" target="_blank" rel="noopener" class="btn-dark btn-sm"><?php esc_html_e( 'Google Maps →', 'brickpoint' ); ?></a>
      <?php endif; ?>
      <a href="<?php echo esc_url( home_url( '/contact' ) ); ?>" class="btn-ghost btn-sm"><?php esc_html_e( 'Contact', 'brickpoint' ); ?></a>
    </div>
  </div>
</article>
