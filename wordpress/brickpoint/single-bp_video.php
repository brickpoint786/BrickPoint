<?php
/**
 * Single Video Template
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
$source = bp_meta( $id, '_bpv_source', 'mp4' );
$url = bp_meta( $id, '_bpv_url', '' );
$file = bp_meta( $id, '_bpv_file', '' );
$dur = bp_meta( $id, '_bpv_duration', '' );
$feat = bp_meta( $id, '_bpv_featured', '0' );

$is_embed = ( $source === 'youtube' || $source === 'vimeo' || strpos( $url, 'embed' ) !== false );
?>

<div class="bp-dark" style="padding:1.5rem 0 3rem 0;">
  <div class="bp-container">
    <div class="bp-crumbs" style="color:rgba(255,255,255,0.6);margin-bottom:1.5rem;">
      <a href="<?php echo esc_url( home_url( '/' ) ); ?>" style="color:inherit;"><?php esc_html_e( 'Home', 'brickpoint' ); ?></a> &gt;
      <a href="<?php echo esc_url( home_url( '/videos' ) ); ?>" style="color:inherit;"><?php esc_html_e( 'Videos', 'brickpoint' ); ?></a> &gt;
      <span><?php the_title(); ?></span>
    </div>

    <!-- Video Embed / Player -->
    <div class="bp-video-stage hero-video-frame">
      <?php if ( $is_embed ) : ?>
        <iframe src="<?php echo esc_url( $url ); ?>" title="<?php the_title_attribute(); ?>" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen class="bp-video-embed"></iframe>
      <?php else : ?>
        <video controls playsinline preload="metadata" poster="<?php echo esc_url( get_the_post_thumbnail_url( $id, 'large' ) ); ?>" class="bp-video-player">
          <source src="<?php echo esc_url( $file ? $file : $url ); ?>" type="video/mp4" />
        </video>
      <?php endif; ?>
    </div>

    <div class="bp-video-meta-box bp-mt">
      <?php
      $cats = get_the_terms( $id, 'bp_video_category' );
      if ( ! empty( $cats ) && ! is_wp_error( $cats ) ) : ?>
        <p class="bp-eyebrow"><?php echo esc_html( $cats[0]->name ); ?></p>
      <?php endif; ?>
      <h1 class="bp-heading-1 bp-head-light"><?php the_title(); ?></h1>
      <div class="bp-video-specs bp-mt">
        <?php if ( $dur ) : ?>
          <span class="bp-meta-pill">⏱ <?php echo esc_html( $dur ); ?></span>
        <?php endif; ?>
        <span class="bp-meta-pill">📅 <?php echo esc_html( get_the_date() ); ?></span>
        <?php if ( $feat === '1' ) : ?>
          <span class="bp-badge" style="position:static;"><?php esc_html_e( 'Featured', 'brickpoint' ); ?></span>
        <?php endif; ?>
      </div>
      <div class="bp-video-desc prose-bp bp-mt" style="color:rgba(255,255,255,0.8);">
        <?php the_content(); ?>
      </div>
      <div class="bp-action-row bp-mt">
        <a href="<?php echo esc_url( home_url( '/videos' ) ); ?>" class="btn-ghost" style="color:#fff;border-color:rgba(255,255,255,0.3);"><?php esc_html_e( '← All Videos', 'brickpoint' ); ?></a>
        <a href="<?php echo esc_url( home_url( '/products' ) ); ?>" class="btn-brick"><?php esc_html_e( 'Related Products', 'brickpoint' ); ?></a>
        <a href="<?php echo esc_url( bp_whatsapp_url( 'Assalam-o-Alaikum BrickPoint, I saw your video: ' . get_the_title() ) ); ?>" target="_blank" rel="noopener" class="btn-whatsapp">
          <span><?php esc_html_e( 'WhatsApp Us', 'brickpoint' ); ?></span>
        </a>
      </div>
    </div>

    <!-- More Videos -->
    <?php
    $more = new WP_Query( array(
      'post_type'      => 'bp_video',
      'posts_per_page' => 3,
      'post__not_in'   => array( $id ),
    ) );
    if ( $more->have_posts() ) : ?>
      <div class="bp-mt" style="padding-top:3rem;">
        <h2 class="bp-heading-2 bp-head-light"><?php esc_html_e( 'More Videos', 'brickpoint' ); ?></h2>
        <div class="bp-grid cols-3 bp-mt">
          <?php while ( $more->have_posts() ) : $more->the_post();
            get_template_part( 'template-parts/video-card' );
          endwhile; wp_reset_postdata(); ?>
        </div>
      </div>
    <?php endif; ?>
  </div>
</div>

<?php
get_footer();
