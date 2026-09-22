<?php
/**
 * Product Card template part
 *
 * @package BrickPoint
 */

if ( ! defined( 'ABSPATH' ) ) {
  exit;
}

$id = get_the_ID();
$price = bp_meta( $id, '_bp_price', '' );
$price_label = bp_meta( $id, '_bp_price_label', '' );
$unit = bp_meta( $id, '_bp_unit', '' );
$avail = bp_meta( $id, '_bp_availability', 'In Stock' );
$badge = bp_meta( $id, '_bp_badge', '' );
$short = bp_meta( $id, '_bp_short', '' );
$video = bp_meta( $id, '_bp_video', '' );

$terms = get_the_terms( $id, 'bp_product_category' );
$cat_name = ( $terms && ! is_wp_error( $terms ) ) ? $terms[0]->name : '';

$inquiry_text = bp_product_inquiry_message( array(
  'product'  => get_the_title(),
  'category' => $cat_name,
  'price'    => trim( $price . ' ' . $price_label ),
  'unit'     => $unit,
) );
?>
<article class="bp-card card-hover group flex-col">
  <a href="<?php the_permalink(); ?>" class="bp-card-media img-zoom">
    <?php if ( has_post_thumbnail() ) : ?>
      <?php the_post_thumbnail( 'bp-card' ); ?>
    <?php else : ?>
      <img src="<?php echo esc_url( bp_asset_image_url( 'stacked.png' ) ); ?>" alt="<?php the_title_attribute(); ?>" />
    <?php endif; ?>

    <div class="bp-card-badges-top">
      <?php if ( $badge ) : ?>
        <span class="bp-badge"><?php echo esc_html( $badge ); ?></span>
      <?php endif; ?>
      <?php if ( $avail ) : ?>
        <span class="bp-avail <?php echo ( $avail === 'In Stock' ) ? 'in-stock' : ''; ?>"><?php echo esc_html( $avail ); ?></span>
      <?php endif; ?>
    </div>

    <?php if ( $video ) : ?>
      <span class="bp-card-video-play">
        <svg class="bp-icon-xs" viewBox="0 0 24 24" fill="currentColor"><polygon points="6 3 20 12 6 21 6 3"/></svg>
      </span>
    <?php endif; ?>
  </a>

  <div class="bp-card-body flex-1">
    <?php if ( $cat_name ) : ?>
      <p class="bp-card-cat-name"><?php echo esc_html( $cat_name ); ?></p>
    <?php endif; ?>

    <h3 class="bp-card-title">
      <a href="<?php the_permalink(); ?>"><?php the_title(); ?></a>
    </h3>

    <?php if ( $short ) : ?>
      <p class="bp-card-excerpt line-clamp-2"><?php echo esc_html( $short ); ?></p>
    <?php endif; ?>

    <div class="bp-card-pricing bp-mt">
      <?php if ( $price ) : ?>
        <span class="bp-price"><?php echo esc_html( $price ); ?></span>
        <?php if ( $unit ) : ?><span class="bp-unit">/ <?php echo esc_html( $unit ); ?></span><?php endif; ?>
      <?php else : ?>
        <span class="bp-price-ask"><?php esc_html_e( 'Price on request', 'brickpoint' ); ?></span>
      <?php endif; ?>
    </div>
    <?php if ( $price_label ) : ?>
      <p class="bp-price-sub"><?php echo esc_html( $price_label ); ?></p>
    <?php endif; ?>

    <div class="bp-card-cta bp-mt">
      <a href="<?php the_permalink(); ?>" class="btn-ghost btn-sm">
        <span><?php esc_html_e( 'View Product', 'brickpoint' ); ?></span>
      </a>
      <a href="<?php echo esc_url( bp_whatsapp_url( $inquiry_text ) ); ?>" target="_blank" rel="noopener" class="btn-whatsapp btn-sm">
        <svg class="bp-icon-xs" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/></svg>
        <span><?php esc_html_e( 'WhatsApp', 'brickpoint' ); ?></span>
      </a>
    </div>
  </div>
</article>
