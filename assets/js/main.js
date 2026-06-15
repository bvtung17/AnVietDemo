/* ===== An Việt - main.js (vanilla) ===== */
(function () {
  'use strict';

  /* ---- Mobile nav toggle ---- */
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.querySelector('.main-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    // submenu accordion on mobile
    nav.querySelectorAll('.has-sub > a').forEach(function (a) {
      a.addEventListener('click', function (e) {
        if (window.innerWidth <= 768) {
          e.preventDefault();
          a.parentElement.classList.toggle('open');
        }
      });
    });
  }

  /* ---- Hero slider ---- */
  var slider = document.querySelector('.slides');
  if (slider) {
    var slides = Array.prototype.slice.call(slider.querySelectorAll('.slide'));
    var dotsWrap = document.querySelector('.slider-dots');
    var current = 0;
    var timer = null;

    slides.forEach(function (_, i) {
      var b = document.createElement('button');
      if (i === 0) b.classList.add('active');
      b.setAttribute('aria-label', 'Slide ' + (i + 1));
      b.addEventListener('click', function () { go(i); });
      dotsWrap.appendChild(b);
    });
    var dots = Array.prototype.slice.call(dotsWrap.children);

    function go(i) {
      slides[current].classList.remove('active');
      dots[current].classList.remove('active');
      current = (i + slides.length) % slides.length;
      slides[current].classList.add('active');
      dots[current].classList.add('active');
      restart();
    }
    function next() { go(current + 1); }
    function prev() { go(current - 1); }
    function restart() { clearInterval(timer); timer = setInterval(next, 6000); }

    var nextBtn = document.querySelector('.slider-arrow.next');
    var prevBtn = document.querySelector('.slider-arrow.prev');
    if (nextBtn) nextBtn.addEventListener('click', next);
    if (prevBtn) prevBtn.addEventListener('click', prev);
    restart();
  }

  /* ---- Animated stats counter ---- */
  var stats = document.querySelectorAll('.stat .num[data-target]');
  if (stats.length) {
    var seen = false;
    var run = function () {
      if (seen) return;
      var first = stats[0].getBoundingClientRect().top;
      if (first < window.innerHeight - 60) {
        seen = true;
        stats.forEach(function (el) {
          var target = parseInt(el.getAttribute('data-target'), 10);
          var suffix = el.getAttribute('data-suffix') || '';
          var step = Math.max(1, Math.floor(target / 60));
          var n = 0;
          var t = setInterval(function () {
            n += step;
            if (n >= target) { n = target; clearInterval(t); }
            el.textContent = n + suffix;
          }, 24);
        });
      }
    };
    window.addEventListener('scroll', run);
    run();
  }

  /* ---- Contact form (front-end only) ---- */
  var form = document.querySelector('#contact-form');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var msg = form.querySelector('.form-msg');
      if (msg) {
        msg.style.display = 'block';
        msg.textContent = 'Cảm ơn bạn! Yêu cầu đã được ghi nhận, An Việt sẽ liên hệ trong thời gian sớm nhất.';
      }
      form.reset();
    });
  }

  /* ---- Lọc đại lý theo tỉnh ---- */
  var provinceFilter = document.querySelector('#province-filter');
  if (provinceFilter) {
    var cards = Array.prototype.slice.call(document.querySelectorAll('.agent-card'));
    provinceFilter.addEventListener('change', function () {
      var val = provinceFilter.value;
      cards.forEach(function (c) {
        c.style.display = (!val || c.getAttribute('data-province') === val) ? '' : 'none';
      });
    });
  }

  /* ---- Footer year ---- */
  var y = document.querySelector('#year');
  if (y) y.textContent = new Date().getFullYear();
})();
