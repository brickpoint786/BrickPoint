<?php
/**
 * Project Card template part
 *
 * @package BrickPoint
 */

if ( ! defined( 'ABSPATH' ) ) {
  exit;
}

$id = get_the_ID();
$loc = bp_meta( $id, '_bpp_location', 'Lahore' );
$status = bp_meta( $id, '_bpp_status', 'Illustrative construction reference' );
?>
<a href="<?php echo esc_url( home_url( '/projects' ) ); ?>" class="bp-card card-hover group">
  <div class="bp-card-media img-zoom">
    <?php if ( has_post_thumbnail() ) : ?>
      <?php the_post_thumbnail( 'bp-card' ); ?>
    <?php else : ?>
      <img src="<?php echo esc_url( bp_asset_image_url( 'villa1.png' ) ); ?>" alt="<?php the_title_attribute(); ?>" />
    <?php endif; ?>
    <span class="bp-illus-badge"><?php echo esc_html( $status ); ?></span>
  </div>
  <div class="bp-card-body">
    <p class="bp-card-loc"><?php echo esc_html( $loc ); ?></p>
    <h3 class="bp-card-title"><?php the_title(); ?></h3>
  </div>
</a>
