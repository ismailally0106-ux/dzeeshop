function toggleSidebar() {
  var sidebar = document.getElementById('sidebar');
  var overlay = document.getElementById('overlay');
  if (sidebar) sidebar.classList.toggle('open');
  if (overlay) overlay.classList.toggle('show');
}

function setActive(el) {
  document.querySelectorAll('.sidebar-item').forEach(function(item) {
    item.classList.remove('active');
  });
  el.classList.add('active');
}

function handleSearch(e) {
  var query = e.target.value.toLowerCase().trim();
  document.querySelectorAll('.metric-card, .category-item, .order-table tr, .founder-card, .timeline-item').forEach(function(el) {
    el.style.outline = (query && el.textContent.toLowerCase().indexOf(query) !== -1)
      ? '2px solid #ff6a00'
      : 'none';
  });
}

document.addEventListener('keydown', function(e) {
  if (e.key === 'Escape') {
    var sidebar = document.getElementById('sidebar');
    var overlay = document.getElementById('overlay');
    if (sidebar && sidebar.classList.contains('open')) {
      sidebar.classList.remove('open');
      if (overlay) overlay.classList.remove('show');
    }
  }
});
