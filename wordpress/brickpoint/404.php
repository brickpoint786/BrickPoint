<?php
/**
 * The template for displaying 404 pages (Not Found)
 *
 * @package BrickPoint
 */

if ( ! defined( 'ABSPATH' ) ) {
  exit;
}

get_header();
?>

<div class="bp-section bp-center" style="padding:6rem 0;">
  <div class="bp-container bp-narrow">
    <p class="bp-eyebrow"><?php esc_html_e( '404 Error', 'brickpoint' ); ?></p>
    <h1 class="bp-heading-1 bp-mt"><?php esc_html_e( 'Page Not Found', 'brickpoint' ); ?></h1>
    <p class="bp-body-text bp-mt"><?php esc_html_e( 'The page you are looking for does not exist or has been moved.', 'brickpoint' ); ?></p>
    <div class="bp-action-row bp-mt" style="justify-content:center;">
      <a href="<?php echo esc_url( home_url( '/' ) ); ?>" class="btn-brick"><?php esc_html_e( 'Back to Home', 'brickpoint' ); ?></a>
      <a href="<?php echo esc_url( home_url( '/products' ) ); ?>" class="btn-dark"><?php esc_html_e( 'Browse Products', 'brickpoint' ); ?></a>
      <a href="<?php echo esc_url( home_url( '/contact' ) ); ?>" class="btn-ghost"><?php esc_html_e( 'Contact Us', 'brickpoint' ); ?></a>
    </div>
  </div>
</div>

<?php
get_footer();
