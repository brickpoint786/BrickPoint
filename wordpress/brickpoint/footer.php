<?php
/**
 * The footer template for BrickPoint
 *
 * @package BrickPoint
 */

if ( ! defined( 'ABSPATH' ) ) {
  exit;
}

// Elementor Pro Theme Builder: Footer Location Check
if ( function_exists( 'elementor_theme_do_location' ) && elementor_theme_do_location( 'footer' ) ) {
  wp_footer();
  echo '</body></html>';
  return;
}
?>

<footer class="bp-footer">
  <div class="brick-lines absolute-bg"></div>
  <div class="bp-container bp-footer-grid">
    <!-- Col 1: About & Independent Footer Logo -->
    <div class="bp-footer-col">
      <div class="bp-footer-logo-wrap">
        <?php brickpoint_footer_logo(); ?>
      </div>
      <p class="bp-footer-desc">
        <?php echo esc_html( bp_option( 'bp_footer_desc', 'Premium bricks and reliable construction materials for homes, commercial developments, and large-scale building projects.' ) ); ?>
      </p>
      <div class="bp-footer-contact">
        <p class="bp-footer-contact-item">
          <svg class="bp-icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
          <a href="tel:<?php echo esc_attr( bp_option( 'bp_phone_display', '0315 2850818' ) ); ?>"><?php echo esc_html( bp_option( 'bp_phone_display', '0315 2850818' ) ); ?></a>
        </p>
        <p class="bp-footer-contact-item">
          <svg class="bp-icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg>
          <a href="mailto:<?php echo esc_attr( bp_option( 'bp_email', 'info@brickpoint.pk' ) ); ?>"><?php echo esc_html( bp_option( 'bp_email', 'info@brickpoint.pk' ) ); ?></a>
        </p>
        <p class="bp-footer-contact-item">
          <svg class="bp-icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></svg>
          <span><?php echo esc_html( bp_option( 'bp_address', 'Lahore, Punjab, Pakistan' ) ); ?></span>
        </p>
      </div>

      <!-- Social Links -->
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
    </div>

    <!-- Col 2: Products & Company -->
    <div class="bp-footer-col">
      <h4 class="bp-footer-title"><?php esc_html_e( 'Products', 'brickpoint' ); ?></h4>
      <ul class="bp-footer-links">
        <li><a href="<?php echo esc_url( home_url( '/ss7-bricks' ) ); ?>"><?php esc_html_e( 'SS7 Bricks', 'brickpoint' ); ?></a></li>
        <li><a href="<?php echo esc_url( home_url( '/products' ) ); ?>"><?php esc_html_e( 'All Products', 'brickpoint' ); ?></a></li>
        <li><a href="<?php echo esc_url( home_url( '/categories' ) ); ?>"><?php esc_html_e( 'Product Categories', 'brickpoint' ); ?></a></li>
        <li><a href="<?php echo esc_url( home_url( '/construction-materials' ) ); ?>"><?php esc_html_e( 'Construction Materials', 'brickpoint' ); ?></a></li>
        <li><a href="<?php echo esc_url( home_url( '/videos' ) ); ?>"><?php esc_html_e( 'Product Videos', 'brickpoint' ); ?></a></li>
      </ul>

      <h4 class="bp-footer-title" style="margin-top:1.5rem;"><?php esc_html_e( 'Company', 'brickpoint' ); ?></h4>
      <ul class="bp-footer-links">
        <li><a href="<?php echo esc_url( home_url( '/about' ) ); ?>"><?php esc_html_e( 'About Us', 'brickpoint' ); ?></a></li>
        <li><a href="<?php echo esc_url( home_url( '/projects' ) ); ?>"><?php esc_html_e( 'Projects', 'brickpoint' ); ?></a></li>
        <li><a href="<?php echo esc_url( home_url( '/blog' ) ); ?>"><?php esc_html_e( 'Blog', 'brickpoint' ); ?></a></li>
        <li><a href="<?php echo esc_url( home_url( '/locations' ) ); ?>"><?php esc_html_e( 'Locations', 'brickpoint' ); ?></a></li>
      </ul>
    </div>

    <!-- Col 3: Who We Serve & Our Units -->
    <div class="bp-footer-col">
      <h4 class="bp-footer-title"><?php esc_html_e( 'Who We Serve', 'brickpoint' ); ?></h4>
      <ul class="bp-footer-links">
        <li><a href="<?php echo esc_url( home_url( '/for-contractors' ) ); ?>"><?php esc_html_e( 'For Contractors', 'brickpoint' ); ?></a></li>
        <li><a href="<?php echo esc_url( home_url( '/for-builders' ) ); ?>"><?php esc_html_e( 'For Builders', 'brickpoint' ); ?></a></li>
        <li><a href="<?php echo esc_url( home_url( '/for-companies' ) ); ?>"><?php esc_html_e( 'For Construction Companies', 'brickpoint' ); ?></a></li>
        <li><a href="<?php echo esc_url( home_url( '/contact' ) ); ?>"><?php esc_html_e( 'Request Quotation', 'brickpoint' ); ?></a></li>
      </ul>

      <h4 class="bp-footer-title" style="margin-top:1.5rem;"><?php esc_html_e( 'Our Units', 'brickpoint' ); ?></h4>
      <ul class="bp-footer-links bp-dim-links">
        <li>Masha Allah Bricks Company</li>
        <li>Fine Bricks Company</li>
        <li>SS7 Bricks</li>
        <li style="opacity:0.6;">CEO: <?php echo esc_html( bp_option( 'bp_ceo', 'Syed Iftikhar Haider' ) ); ?></li>
        <li style="opacity:0.6;">Sales: <?php echo esc_html( bp_option( 'bp_sales', 'Qasim Iqbal' ) ); ?></li>
      </ul>
    </div>

    <!-- Col 4: Quotation & WhatsApp -->
    <div class="bp-footer-col">
      <h4 class="bp-footer-title"><?php esc_html_e( 'Get a Quotation', 'brickpoint' ); ?></h4>
      <p class="bp-footer-desc">
        <?php esc_html_e( 'Send your material list on WhatsApp and get availability, delivery details, and final quotation.', 'brickpoint' ); ?>
      </p>
      <a href="<?php echo esc_url( bp_whatsapp_url( 'Assalam-o-Alaikum BrickPoint, I need a quotation for construction materials.' ) ); ?>" target="_blank" rel="noopener" class="btn-whatsapp btn-block" style="margin-top:1rem;">
        <svg class="bp-icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/></svg>
        <span><?php esc_html_e( 'Chat on WhatsApp', 'brickpoint' ); ?></span>
      </a>
      <a href="<?php echo esc_url( home_url( '/contact' ) ); ?>" class="btn-ghost btn-block" style="margin-top:0.5rem;color:#fff;border-color:rgba(255,255,255,0.2);">
        <span><?php esc_html_e( 'Contact Form', 'brickpoint' ); ?></span>
      </a>
      <a href="<?php echo esc_url( admin_url( 'themes.php?page=brickpoint-demo' ) ); ?>" class="btn-ghost btn-block" style="margin-top:0.5rem;color:#ea580c;border-color:rgba(234,88,12,0.4);background:rgba(234,88,12,0.08);">
        <span><?php esc_html_e( 'Demo Importer', 'brickpoint' ); ?></span>
      </a>
    </div>
  </div>

  <!-- Copyright Bar -->
  <div class="bp-footer-bottom">
    <div class="bp-container bp-footer-bottom-inner">
      <p>&copy; <?php echo esc_html( date( 'Y' ) ); ?> BrickPoint. <?php esc_html_e( 'All rights reserved.', 'brickpoint' ); ?></p>
      <div class="bp-footer-legal">
        <a href="<?php echo esc_url( home_url( '/privacy' ) ); ?>"><?php esc_html_e( 'Privacy Policy', 'brickpoint' ); ?></a>
        <a href="<?php echo esc_url( home_url( '/terms' ) ); ?>"><?php esc_html_e( 'Terms & Conditions', 'brickpoint' ); ?></a>
        <a href="<?php echo esc_url( home_url( '/locations' ) ); ?>"><?php esc_html_e( 'Locations', 'brickpoint' ); ?></a>
      </div>
    </div>
  </div>
</footer>

<!-- Floating WhatsApp Action -->
<a href="<?php echo esc_url( bp_whatsapp_url( 'Assalam-o-Alaikum BrickPoint, I need a quotation for construction materials.' ) ); ?>" target="_blank" rel="noopener" class="bp-float-wa" aria-label="<?php esc_attr_e( 'Chat on WhatsApp', 'brickpoint' ); ?>">
  <svg class="bp-icon-md" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/></svg>
  <span class="bp-ping-dot"></span>
</a>

<?php wp_footer(); ?>
</body>
</html>
