<?php
/**
 * Locations Archive Template (Our Bhattas & Office)
 *
 * @package BrickPoint
 */

if ( ! defined( 'ABSPATH' ) ) {
  exit;
}

get_header();
?>

<div class="bp-pagehead">
  <div class="bp-container">
    <p class="bp-eyebrow"><?php esc_html_e( 'Bhattas & Office', 'brickpoint' ); ?></p>
    <h1 class="bp-heading-1"><?php esc_html_e( 'Our Locations', 'brickpoint' ); ?></h1>
    <p class="bp-pagehead-desc"><?php esc_html_e( 'Three production units plus head office — tap any card for real Google Maps directions.', 'brickpoint' ); ?></p>
  </div>
</div>

<section class="bp-section">
  <div class="bp-container">
    <div class="bp-grid cols-2">
      <?php
      if ( have_posts() ) :
        $unit_num = 1;
        while ( have_posts() ) : the_post();
          $id = get_the_ID();
          $addr = bp_meta( $id, '_bpl_address', '' );
          $phone = bp_meta( $id, '_bpl_phone', bp_option( 'bp_phone_display', '0315 2850818' ) );
          $hours = bp_meta( $id, '_bpl_hours', 'Mon – Sat: 8:00 AM – 6:00 PM' );
          $maps = bp_meta( $id, '_bpl_maps_url', '' );
          $video = bp_meta( $id, '_bpl_video', '' );
      ?>
        <article class="bp-card card-hover group bp-loc-full-card">
          <div class="bp-card-media img-zoom">
            <?php if ( has_post_thumbnail() ) : ?>
              <?php the_post_thumbnail( 'large' ); ?>
            <?php else : ?>
              <img src="<?php echo esc_url( bp_asset_image_url( 'kiln.png' ) ); ?>" alt="<?php the_title_attribute(); ?>" />
            <?php endif; ?>
            <span class="bp-badge"><?php printf( esc_html__( 'Unit %d', 'brickpoint' ), $unit_num ); ?></span>
          </div>
          <div class="bp-card-body">
            <h3><?php the_title(); ?></h3>
            <?php if ( $addr ) : ?>
              <p class="bp-loc-item">
                <svg class="bp-icon-sm text-orange" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/></svg>
                <span><?php echo esc_html( $addr ); ?></span>
              </p>
            <?php endif; ?>
            <p class="bp-loc-desc"><?php echo esc_html( get_the_excerpt() ); ?></p>
            <div class="bp-loc-meta-tags">
              <?php if ( $phone ) : ?><span>📞 <?php echo esc_html( $phone ); ?></span><?php endif; ?>
              <?php if ( $hours ) : ?><span>⏱ <?php echo esc_html( $hours ); ?></span><?php endif; ?>
            </div>
            <?php if ( $video ) : ?>
              <video controls playsinline preload="metadata" class="bp-video-player bp-mt">
                <source src="<?php echo esc_url( $video ); ?>" type="video/mp4" />
              </video>
            <?php endif; ?>
            <div class="bp-card-cta bp-mt">
              <?php if ( $maps ) : ?>
                <a href="<?php echo esc_url( $maps ); ?>" target="_blank" rel="noopener" class="btn-dark btn-sm"><?php esc_html_e( '📍 Directions', 'brickpoint' ); ?></a>
              <?php endif; ?>
              <a href="<?php echo esc_url( bp_whatsapp_url( 'Assalam-o-Alaikum BrickPoint, I want to visit ' . get_the_title() ) ); ?>" target="_blank" rel="noopener" class="btn-whatsapp btn-sm"><?php esc_html_e( 'WhatsApp', 'brickpoint' ); ?></a>
              <a href="<?php echo esc_url( home_url( '/contact' ) ); ?>" class="btn-ghost btn-sm"><?php esc_html_e( 'Contact', 'brickpoint' ); ?></a>
            </div>
          </div>
        </article>
      <?php $unit_num++; endwhile; endif; ?>
    </div>
  </div>
</section>

<?php
get_footer();
