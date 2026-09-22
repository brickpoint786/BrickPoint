<?php
/**
 * Hero template part
 *
 * @package BrickPoint
 */

if ( ! defined( 'ABSPATH' ) ) {
  exit;
}

$hero_img = bp_asset_image_url( 'brick-mason.png' );
$hero_video = bp_option( 'bp_hero_video', 'https://videos.pexels.com/video-files/35411576/15003649_3840_2160_24fps.mp4' );
$hero_poster = bp_asset_image_url( 'hero-poster.png' );
?>
<section class="bp-hero relative">
  <div class="bp-hero-bg">
    <img src="<?php echo esc_url( $hero_img ); ?>" alt="<?php esc_attr_e( 'Bricklayers building a wall', 'brickpoint' ); ?>" class="bp-hero-bg-img" />
    <div class="bp-hero-overlay"></div>
    <div class="brick-lines absolute-bg"></div>
  </div>

  <div class="bp-container bp-hero-grid relative">
    <!-- Left Hero Column -->
    <div class="bp-hero-text">
      <p class="bp-hero-badge">
        <svg class="bp-icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 20a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8l-7 5V8l-7 5V4a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2Z"/></svg>
        <span>Masha Allah &bull; Fine Bricks &bull; SS7</span>
      </p>

      <h1 class="bp-hero-title">
        Building Strength.<br />
        <span class="text-orange">Delivering Quality.</span><br />
        Shaping Tomorrow.
      </h1>

      <p class="bp-hero-sub">
        Premium bricks and reliable construction materials for homes, commercial developments, and large-scale building projects.
      </p>

      <div class="bp-hero-cta">
        <a href="<?php echo esc_url( home_url( '/products' ) ); ?>" class="btn-brick">
          <span><?php esc_html_e( 'Explore Products', 'brickpoint' ); ?></span>
          <svg class="bp-icon-xs" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>
        </a>
        <a href="<?php echo esc_url( home_url( '/contact' ) ); ?>" class="btn-ghost" style="color:#fff;border-color:rgba(255,255,255,0.25);">
          <span><?php esc_html_e( 'Request a Quote', 'brickpoint' ); ?></span>
        </a>
        <a href="<?php echo esc_url( bp_whatsapp_url( 'Assalam-o-Alaikum BrickPoint, I need a quotation for construction materials.' ) ); ?>" target="_blank" rel="noopener" class="btn-whatsapp">
          <svg class="bp-icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/></svg>
          <span><?php esc_html_e( 'WhatsApp Us', 'brickpoint' ); ?></span>
        </a>
      </div>

      <div class="bp-hero-trust-row">
        <span><svg class="bp-icon-sm text-green" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/></svg> Quality-focused supply</span>
        <span><svg class="bp-icon-sm text-green" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 18V6a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2v11a1 1 0 0 0 1 1h2"/><path d="M15 18H9"/><path d="M19 18h2a1 1 0 0 0 1-1v-3.65a1 1 0 0 0-.22-.624l-3.48-4.35A1 1 0 0 0 17.52 8H14"/><circle cx="17" cy="18.5" r="2.5"/><circle cx="7" cy="18.5" r="2.5"/></svg> Reliable delivery</span>
        <span><svg class="bp-icon-sm text-green" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 20a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8l-7 5V8l-7 5V4a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2Z"/></svg> Multiple production locations</span>
      </div>
    </div>

    <!-- Right Hero Column: Video Frame + SS7 Animated Floating Card -->
    <div class="bp-hero-media-wrap relative">
      <div class="hero-video-frame relative">
        <video autoplay muted loop playsinline preload="metadata" poster="<?php echo esc_url( $hero_poster ); ?>" class="bp-hero-video-el" aria-label="BrickPoint brick construction video">
          <source src="<?php echo esc_url( $hero_video ); ?>" type="video/mp4" />
        </video>
        <div class="bp-hero-video-overlay">
          <div>
            <p class="bp-video-eyebrow">SS7 Bricks &bull; In Action</p>
            <p class="bp-video-caption">See the strength behind every brick</p>
          </div>
          <a href="<?php echo esc_url( home_url( '/videos' ) ); ?>" class="bp-play-circle" aria-label="Watch all videos">
            <svg class="bp-icon-sm" viewBox="0 0 24 24" fill="currentColor"><polygon points="6 3 20 12 6 21 6 3"/></svg>
          </a>
        </div>
      </div>

      <!-- SS7 3D Floating Brick Card -->
      <div class="bp-ss7-float-badge ss7-brick-loop">
        <div class="ss7-brick">
          <img src="<?php echo esc_url( bp_asset_image_url( 'red-stack.png' ) ); ?>" alt="SS7 brick close up" class="bp-ss7-thumb" />
          <div>
            <p class="bp-flagship-tag">
              <svg class="bp-icon-xs text-gold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="8" r="6"/><path d="m15.477 12.89 1.515 8.526a.5.5 0 0 1-.722.522l-4.27-2.247-4.27 2.247a.5.5 0 0 1-.722-.522l1.515-8.526"/></svg> Flagship
            </p>
            <p class="bp-ss7-title">SS7 Bricks</p>
            <a href="<?php echo esc_url( home_url( '/ss7-bricks' ) ); ?>" class="bp-ss7-link">View SS7 range &rarr;</a>
          </div>
        </div>
      </div>

      <!-- Production Units Pill -->
      <div class="bp-units-pill">
        <p class="bp-units-count">3<span class="text-orange">+</span></p>
        <p class="bp-units-label">Production units</p>
      </div>
    </div>
  </div>

  <!-- Marquee Bar -->
  <div class="bp-marquee-bar">
    <div class="marquee-track">
      <div class="marquee-group">
        <span><span class="bp-dot-orange"></span>SS7 Bricks</span>
        <span><span class="bp-dot-orange"></span>Cement</span>
        <span><span class="bp-dot-orange"></span>Bajri / Crush</span>
        <span><span class="bp-dot-orange"></span>Sand / Rait</span>
        <span><span class="bp-dot-orange"></span>Steel</span>
        <span><span class="bp-dot-orange"></span>Pipes</span>
        <span><span class="bp-dot-orange"></span>Chemicals</span>
        <span><span class="bp-dot-orange"></span>Cables</span>
        <span><span class="bp-dot-orange"></span>Paints</span>
        <span><span class="bp-dot-orange"></span>Lights</span>
      </div>
      <div class="marquee-group">
        <span><span class="bp-dot-orange"></span>SS7 Bricks</span>
        <span><span class="bp-dot-orange"></span>Cement</span>
        <span><span class="bp-dot-orange"></span>Bajri / Crush</span>
        <span><span class="bp-dot-orange"></span>Sand / Rait</span>
        <span><span class="bp-dot-orange"></span>Steel</span>
        <span><span class="bp-dot-orange"></span>Pipes</span>
        <span><span class="bp-dot-orange"></span>Chemicals</span>
        <span><span class="bp-dot-orange"></span>Cables</span>
        <span><span class="bp-dot-orange"></span>Paints</span>
        <span><span class="bp-dot-orange"></span>Lights</span>
      </div>
    </div>
  </div>
</section>
