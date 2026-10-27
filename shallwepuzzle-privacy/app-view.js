// Hide the language header when the app opens this same policy page.
if (new URLSearchParams(window.location.search).get('view') === 'app') {
  document.documentElement.classList.add('app-view');
}
