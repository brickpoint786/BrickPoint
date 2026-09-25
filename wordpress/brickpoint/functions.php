<?php
/**
 * BrickPoint Theme Bootstrap
 *
 * @package BrickPoint
 * @version 1.0.0
 */

if ( ! defined( 'ABSPATH' ) ) {
  exit;
}

define( 'BRICKPOINT_VERSION', '1.0.0' );
define( 'BRICKPOINT_DIR', get_template_directory() );
define( 'BRICKPOINT_URI', get_template_directory_uri() );

// Core modules
require_once BRICKPOINT_DIR . '/inc/setup.php';
require_once BRICKPOINT_DIR . '/inc/enqueue.php';
require_once BRICKPOINT_DIR . '/inc/helpers.php';
require_once BRICKPOINT_DIR . '/inc/template-functions.php';
require_once BRICKPOINT_DIR . '/inc/post-types.php';
require_once BRICKPOINT_DIR . '/inc/taxonomies.php';
require_once BRICKPOINT_DIR . '/inc/meta-fields.php';
require_once BRICKPOINT_DIR . '/inc/whatsapp.php';
require_once BRICKPOINT_DIR . '/inc/customizer.php';
require_once BRICKPOINT_DIR . '/inc/admin-settings.php';
require_once BRICKPOINT_DIR . '/inc/admin.php';
require_once BRICKPOINT_DIR . '/inc/project-functions.php';
require_once BRICKPOINT_DIR . '/inc/video-functions.php';
require_once BRICKPOINT_DIR . '/inc/elementor.php';
require_once BRICKPOINT_DIR . '/inc/elementor-widgets.php';
require_once BRICKPOINT_DIR . '/inc/demo-data.php';
require_once BRICKPOINT_DIR . '/inc/demo-importer.php';
require_once BRICKPOINT_DIR . '/inc/ajax-handlers.php';
