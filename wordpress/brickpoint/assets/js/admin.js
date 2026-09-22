/**
 * BrickPoint Admin Demo Importer Script
 */
jQuery(document).ready(function($) {
  var $btn = $('#bpStartImportBtn');
  var $progress = $('#bpImportProgress');
  var $bar = $('#bpProgressBar');
  var $status = $('#bpProgressStatus');
  var $log = $('#bpProgressLog');
  var $spinner = $('#bpImportSpinner');

  $btn.on('click', function(e) {
    e.preventDefault();
    if (!confirm('This will import complete demo data: 17 pages, 12 products, 6 videos, 6 projects, 4 locations, 4 blog guides, 24 Elementor templates, menus, and media. Proceed?')) {
      return;
    }

    $btn.prop('disabled', true);
    $spinner.addClass('is-active');
    $progress.show();
    $bar.css('width', '25%');
    $status.text('Importing media, products, and pages…');
    $log.text('Import started…\n');

    $.ajax({
      url: bpAdminConfig.ajaxUrl,
      type: 'POST',
      dataType: 'json',
      data: {
        action: 'brickpoint_run_demo_import',
        nonce: bpAdminConfig.nonce,
        step: 'all'
      },
      success: function(resp) {
        $spinner.removeClass('is-active');
        if (resp.success) {
          $bar.css('width', '100%');
          $status.text('Demo Import Complete! Check frontend.');
          $log.text(resp.data.log || 'Success!');
          alert('BrickPoint Demo Data Imported Successfully!');
        } else {
          $status.text('Import error: ' + (resp.data.message || 'Unknown error'));
          $log.text(resp.data.message || 'Error occurred.');
          $btn.prop('disabled', false);
        }
      },
      error: function(xhr, status, error) {
        $spinner.removeClass('is-active');
        $status.text('Server error during import: ' + error);
        $btn.prop('disabled', false);
      }
    });
  });
});
