<?php
/**
 * Projects Archive Template
 *
 * @package BrickPoint
 */

if ( ! defined( 'ABSPATH' ) ) {
  exit;
}

get_header();

if ( function_exists( 'elementor_theme_do_location' ) && elementor_theme_do_location( 'archive' ) ) {
  get_footer();
  return;
}

$societies = array( 'DHA Lahore', 'Bahria Town Lahore', 'Lake City Lahore', 'Etihad Town Lahore', 'Al-Kabir Town', 'LDA City', 'Paragon City', 'Izmir Town' );
?>

<div class="bp-pagehead">
  <div class="bp-container">
    <p class="bp-eyebrow"><?php esc_html_e( 'References & Inspiration', 'brickpoint' ); ?></p>
    <h1 class="bp-heading-1"><?php esc_html_e( 'Projects', 'brickpoint' ); ?></h1>
    <p class="bp-pagehead-desc"><?php esc_html_e( 'Construction references and project inspiration visuals from Lahore housing developments. Visuals are illustrative unless a project is verified by BrickPoint.', 'brickpoint' ); ?></p>
    <div class="bp-societies-row bp-mt">
      <?php foreach ( $societies as $s ) : ?>
        <span class="bp-soc-pill">
          <svg class="bp-icon-xs" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/></svg>
          <?php echo esc_html( $s ); ?>
        </span>
      <?php endforeach; ?>
    </div>
  </div>
</div>

<section class="bp-section">
  <div class="bp-container">
    <div class="bp-notice-box">
      <strong><?php esc_html_e( 'Content notice:', 'brickpoint' ); ?></strong>
      <?php esc_html_e( 'Project visuals on this page are labelled “Illustrative construction reference” or “Project inspiration visual”. BrickPoint does not claim supply to any named society, developer or project unless verified by management.', 'brickpoint' ); ?>
    </div>

    <div class="bp-grid cols-3 bp-mt">
      <?php
      if ( have_posts() ) :
        while ( have_posts() ) : the_post();
          get_template_part( 'template-parts/project-card' );
        endwhile;
      else : ?>
        <p class="bp-center" style="grid-column:1/-1;"><?php esc_html_e( 'No project references loaded.', 'brickpoint' ); ?></p>
      <?php endif; ?>
    </div>

    <div class="bp-pagination bp-mt">
      <?php the_posts_pagination(); ?>
    </div>
  </div>
</section>

<?php
get_footer();
