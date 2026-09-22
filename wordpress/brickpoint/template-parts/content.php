<?php
/**
 * Standard Post Card template part
 *
 * @package BrickPoint
 */

if ( ! defined( 'ABSPATH' ) ) {
  exit;
}
?>
<article id="post-<?php the_ID(); ?>" <?php post_class( 'bp-card card-hover group flex-col' ); ?>>
  <?php if ( has_post_thumbnail() ) : ?>
    <a href="<?php the_permalink(); ?>" class="bp-card-media img-zoom">
      <?php the_post_thumbnail( 'bp-card' ); ?>
    </a>
  <?php endif; ?>
  <div class="bp-card-body flex-1">
    <div class="bp-post-meta-line">
      <span><?php echo esc_html( get_the_date() ); ?></span> &bull;
      <span><?php the_author(); ?></span>
    </div>
    <h3 class="bp-card-title"><a href="<?php the_permalink(); ?>"><?php the_title(); ?></a></h3>
    <p class="bp-card-excerpt line-clamp-2"><?php echo esc_html( get_the_excerpt() ); ?></p>
    <a href="<?php the_permalink(); ?>" class="bp-readmore-link bp-mt"><?php esc_html_e( 'Read Article →', 'brickpoint' ); ?></a>
  </div>
</article>
