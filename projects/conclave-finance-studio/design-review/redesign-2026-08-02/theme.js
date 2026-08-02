/* Theme switch for the review prototype.
   ?theme=dark on any prototype URL renders that screen in the product's dark
   theme. The dark token block in ds.css is copied VERBATIM from the running
   pilot — this file only selects between them, so what you see is the
   product's own dark palette, not a prototype-only approximation.
   Runs synchronously in <head>, before first paint, so there is no flash. */
(function () {
  var t = new URLSearchParams(location.search).get('theme');
  if (t === 'dark') document.documentElement.setAttribute('data-theme', 'dark');
  document.addEventListener('DOMContentLoaded', function () {
    /* Keep ?theme= sticky across every in-prototype click, so a dark
       walkthrough stays dark for the whole journey. */
    if (t !== 'dark') return;
    var as = document.querySelectorAll('a[href]');
    for (var i = 0; i < as.length; i++) {
      var h = as[i].getAttribute('href');
      if (!h || h.charAt(0) === '#' || h.indexOf('://') > -1) continue;
      as[i].setAttribute('href', h.indexOf('?') > -1 ? h + '&theme=dark'
                                                     : h + '?theme=dark');
    }
  });
})();
