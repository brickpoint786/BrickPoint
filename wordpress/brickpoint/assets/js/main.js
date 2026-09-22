/**
 * BrickPoint Main Frontend Script
 */
document.addEventListener('DOMContentLoaded', function() {
  // 1. Sticky Header Scroll Effect
  var header = document.getElementById('bpStickyHeader');
  if (header) {
    window.addEventListener('scroll', function() {
      if (window.scrollY > 40) {
        header.classList.add('scrolled');
      } else {
        header.classList.remove('scrolled');
      }
    });
  }

  // 2. Mobile Menu Drawer Toggle
  var menuToggle = document.getElementById('bpMenuToggle');
  var menuClose  = document.getElementById('bpMenuClose');
  var drawer     = document.getElementById('bpMobileDrawer');
  var overlay    = document.getElementById('bpMobileOverlay');

  function openDrawer() {
    if (drawer) {
      drawer.removeAttribute('hidden');
      document.body.style.overflow = 'hidden';
      if (menuToggle) menuToggle.setAttribute('aria-expanded', 'true');
    }
  }

  function closeDrawer() {
    if (drawer) {
      drawer.setAttribute('hidden', '');
      document.body.style.overflow = '';
      if (menuToggle) menuToggle.setAttribute('aria-expanded', 'false');
    }
  }

  if (menuToggle) menuToggle.addEventListener('click', openDrawer);
  if (menuClose) menuClose.addEventListener('click', closeDrawer);
  if (overlay) overlay.addEventListener('click', closeDrawer);

  // 3. Product Gallery Switcher
  var mainImg = document.getElementById('bpMainProductImg');
  var thumbs = document.querySelectorAll('.bp-thumb');
  if (mainImg && thumbs.length > 0) {
    thumbs.forEach(function(th) {
      th.addEventListener('click', function() {
        thumbs.forEach(function(t) { t.classList.remove('active'); });
        th.classList.add('active');
        mainImg.src = th.src;
      });
    });
  }
});
