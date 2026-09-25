<?php
/**
 * Video Card template part
 *
 * @package BrickPoint
 */

if ( ! defined( 'ABSPATH' ) ) {
  exit;
}

$id = get_the_ID();
$dur = bp_meta( $id, '_bpv_duration', '' );
$feat = bp_meta( $id, '_bpv_featured', '0' );

$terms = get_the_terms( $id, 'bp_video_category' );
$cat_name = ( $terms && ! is_wp_error( $terms ) ) ? $terms[0]->name : '';
?>
<a href="<?php the_permalink(); ?>" class="bp-card card-hover group bp-video-card">
  <div class="bp-card-media img-zoom bp-video-thumb">
    <?php if ( has_post_thumbnail() ) : ?>
      <?php the_post_thumbnail( 'bp-card' ); ?>
    <?php else : ?>
      <img src="<?php echo esc_url( bp_asset_image_url( 'drone-poster.png' ) ); ?>" alt="<?php the_title_attribute(); ?>" />
    <?php endif; ?>
    <div class="bp-video-thumb-overlay"></div>
    <span class="bp-play-btn">
      <svg class="bp-icon-sm" viewBox="0 0 24 24" fill="currentColor"><polygon points="6 3 20 12 6 21 6 3"/></svg>
    </span>
    <?php if ( $dur ) : ?>
      <span class="bp-duration"><?php echo esc_html( $dur ); ?></span>
    <?php endif; ?>
    <?php if ( $feat === '1' ) : ?>
      <span class="bp-feat"><?php esc_html_e( 'Featured', 'brickpoint' ); ?></span>
    <?php endif; ?>
  </div>
  <div class="bp-card-body">
    <?php if ( $cat_name ) : ?>
      <p class="bp-card-cat-name"><?php echo esc_html( $cat_name ); ?></p>
    <?php endif; ?>
    <h3 class="bp-card-title"><?php the_title(); ?></h3>
    <p class="bp-card-excerpt line-clamp-2"><?php echo esc_html( get_the_excerpt() ); ?></p>
  </div>
</a>
