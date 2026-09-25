<?php
/**
 * Social Links template part
 *
 * @package BrickPoint
 */

if ( ! defined( 'ABSPATH' ) ) {
  exit;
}
?>
<div class="bp-social">
  <a href="<?php echo esc_url( bp_option( 'bp_social_facebook', 'https://www.facebook.com/brickpoint.pk/' ) ); ?>" target="_blank" rel="noopener" aria-label="Facebook">
    <svg class="bp-icon-sm" viewBox="0 0 24 24" fill="currentColor"><path d="M13.5 21v-7h2.4l.4-3h-2.8V9.1c0-.9.3-1.5 1.6-1.5h1.3V4.9c-.3 0-1.1-.1-2-.1-2 0-3.4 1.2-3.4 3.5V11H7.5v3H10v7h3.5Z"/></svg>
  </a>
  <a href="<?php echo esc_url( bp_option( 'bp_social_instagram', 'https://www.instagram.com/brickpoint.pk/' ) ); ?>" target="_blank" rel="noopener" aria-label="Instagram">
    <svg class="bp-icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.2" cy="6.8" r="1.2" fill="currentColor" stroke="none"/></svg>
  </a>
  <a href="<?php echo esc_url( bp_option( 'bp_social_twitter', 'https://x.com/BrickPointPK' ) ); ?>" target="_blank" rel="noopener" aria-label="X Twitter">
    <svg class="bp-icon-sm" viewBox="0 0 24 24" fill="currentColor"><path d="M17.7 3H21l-7.1 8.2L22.2 21h-6.6l-5.1-6.1L4.6 21H1.3l7.6-8.7L1.8 3h6.7l4.6 5.6L17.7 3Zm-1.2 16h1.8L7.1 4.9H5.2L16.5 19Z"/></svg>
  </a>
  <a href="<?php echo esc_url( bp_option( 'bp_social_tiktok', 'https://www.tiktok.com/@brickpoint.pk/' ) ); ?>" target="_blank" rel="noopener" aria-label="TikTok">
    <span style="font-weight:900;font-size:0.9rem;">T</span>
  </a>
</div>
