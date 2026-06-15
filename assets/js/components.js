/* ===== An Việt - components.js =====
 * Header & footer dùng chung dưới dạng Web Component (custom element).
 * Template nhúng thẳng trong file này (KHÔNG fetch) -> mở file:// vẫn chạy, không cần server.
 * Sửa header/footer: chỉ sửa file này. build.py chỉ phát <site-header>/<site-footer>.
 *
 * Lưu ý CSS: cần `site-header, site-footer { display: contents }` để header sticky hoạt động.
 */
(function () {
  'use strict';

  /* ---- SVG icon (currentColor) ---- */
  var IC_PHONE = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M6.6 10.8c1.4 2.8 3.8 5.1 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1A17 17 0 0 1 3 4c0-.6.5-1 1-1h3.5c.6 0 1 .4 1 1 0 1.2.2 2.4.6 3.6.1.4 0 .8-.3 1l-2.2 2.2z"/></svg>';
  var IC_MSG = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.3 2 2 6.2 2 11.6c0 2.9 1.3 5.5 3.4 7.2v3.5l3.1-1.7c.8.2 1.7.3 2.5.3 5.7 0 10-4.2 10-9.6S17.7 2 12 2zm1 12.9l-2.5-2.7-5 2.7 5.5-5.8 2.6 2.7 4.9-2.7-5.5 5.8z"/></svg>';
  var IC_ZALO = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 3C6.5 3 2 6.9 2 11.6c0 2.5 1.3 4.8 3.4 6.3-.1 1.1-.6 2.4-1.3 3.4 1.7-.2 3.3-.9 4.4-1.7 1.1.3 2.3.5 3.5.5 5.5 0 10-3.9 10-8.5S17.5 3 12 3z"/></svg>';
  var IC_FB = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M22 12a10 10 0 1 0-11.6 9.9v-7H7.9V12h2.5V9.8c0-2.5 1.5-3.9 3.7-3.9 1.1 0 2.2.2 2.2.2v2.5h-1.2c-1.2 0-1.6.8-1.6 1.6V12h2.7l-.4 2.9h-2.3v7A10 10 0 0 0 22 12z"/></svg>';
  var IC_SHOPEE = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a4 4 0 0 0-4 4H4.6L3.4 20.2A2 2 0 0 0 5.4 22h13.2a2 2 0 0 0 2-1.8L19.4 6H16a4 4 0 0 0-4-4zm0 2a2 2 0 0 1 2 2h-4a2 2 0 0 1 2-2zm-1.5 7.4c0-.8.8-1.4 1.8-1.4.7 0 1.4.2 1.9.5l-.5 1c-.4-.2-.9-.4-1.4-.4-.4 0-.7.1-.7.4 0 .8 2.6.5 2.6 2.4 0 .9-.8 1.5-2 1.5-.8 0-1.6-.2-2.1-.6l.5-1c.5.3 1 .5 1.6.5.5 0 .8-.2.8-.5 0-.8-2.5-.5-2.5-2.4z"/></svg>';
  var IC_LAZADA = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2.2 4 6.5v7c0 3.4 3.3 6.6 8 8.3 4.7-1.7 8-4.9 8-8.3v-7L12 2.2zM9.3 8.4l2.7 1.5 2.7-1.5 2.6 1.4-5.3 3-5.3-3 2.6-1.4z"/></svg>';

  /* ---- Menu (nguồn duy nhất) ---- */
  var NAV = [
    ['Trang chủ', 'index.html', null],
    ['Giới thiệu', 'gioi-thieu.html', null],
    ['Sản phẩm', 'san-pham.html', [
      ['Đầu phun Sprinkler TITAN', 'san-pham.html#sprinkler'],
      ['Bình chữa cháy AN VIỆT', 'san-pham.html#binh'],
      ['Hệ thống PCCC tự động', 'san-pham.html#tudong'],
      ['Hệ thống chữa cháy di động', 'san-pham.html#didong'],
      ['Bơm chữa cháy', 'san-pham.html#bom'],
      ['Phương tiện chữa cháy', 'san-pham.html#xe'],
      ['Thiết bị báo cháy', 'san-pham.html#baochay'],
      ['Trang bị bảo hộ PCCC', 'san-pham.html#baoho']
    ]],
    ['Giải pháp', 'giai-phap.html', null],
    ['Dự án', 'du-an.html', null],
    ['Ứng dụng', 'ung-dung.html', null],
    ['Đại lý', 'dai-ly.html', null],
    ['Tuyển dụng', 'tuyen-dung.html', null],
    ['Tin tức', 'tin-tuc.html', null],
    ['Liên hệ', 'lien-he.html', null]
  ];

  function navHtml(active) {
    return NAV.map(function (it) {
      var label = it[0], href = it[1], sub = it[2];
      var cls = href === active ? 'active' : '';
      if (sub) {
        var s = sub.map(function (x) {
          return '<a href="' + x[1] + '">' + x[0] + '</a>';
        }).join('');
        return '<li class="has-sub ' + cls + '"><a class="nav-link" href="' + href + '">' + label +
          '</a><div class="submenu">' + s + '</div></li>';
      }
      return '<li class="' + cls + '"><a class="nav-link" href="' + href + '">' + label + '</a></li>';
    }).join('');
  }

  function headerHtml(active) {
    return '' +
      '<div class="topbar">' +
      '  <div class="container">' +
      '    <div class="tb-left">' +
      '      <span>📞 Hotline: 0866 19 29 59</span>' +
      '      <span>✉ anviet.firebuild.group@gmail.com</span>' +
      '    </div>' +
      '    <div class="tb-social">' +
      '      <a href="#" aria-label="Facebook">Facebook</a>' +
      '      <a href="#" aria-label="Youtube">Youtube</a>' +
      '      <a href="#" aria-label="Zalo">Zalo</a>' +
      '    </div>' +
      '  </div>' +
      '</div>' +
      '<header class="site-header">' +
      '  <div class="container">' +
      '    <a class="brand" href="index.html">' +
      '      <span class="mark">AV</span>' +
      '      <span>' +
      '        <span class="name">AN <b>VIỆT</b></span>' +
      '        <span class="tag">Giải pháp PCCC toàn diện</span>' +
      '      </span>' +
      '    </a>' +
      '    <button class="nav-toggle" aria-label="Mở menu" aria-expanded="false">☰</button>' +
      '    <nav class="main-nav"><ul>' + navHtml(active) + '</ul></nav>' +
      '    <a class="btn-quote" href="lien-he.html">Nhận báo giá</a>' +
      '  </div>' +
      '</header>';
  }

  function footerHtml() {
    return '' +
      '<div class="buybar">' +
      '  <div class="buybar-title">Mua<br>hàng</div>' +
      '  <ul>' +
      '    <li class="shopee"><a href="#" target="_blank" rel="noopener" aria-label="Shopee">' + IC_SHOPEE + '</a></li>' +
      '    <li class="lazada"><a href="#" target="_blank" rel="noopener" aria-label="Lazada">' + IC_LAZADA + '</a></li>' +
      '    <li class="facebook"><a href="#" target="_blank" rel="noopener" aria-label="Facebook">' + IC_FB + '</a></li>' +
      '    <li class="zalo"><a href="#" target="_blank" rel="noopener" aria-label="Zalo">' + IC_ZALO + '</a></li>' +
      '  </ul>' +
      '</div>' +
      '<div class="fab-stack">' +
      '  <a class="fab phone" href="tel:0866192959" aria-label="Gọi hotline">' +
      '    <span class="fab-ring"></span>' + IC_PHONE + '<span class="fab-tip">0866 19 29 59</span></a>' +
      '  <a class="fab zalo" href="#" target="_blank" rel="noopener" aria-label="Chat Zalo">' +
      IC_ZALO + '<span class="fab-tip">Chat Zalo</span></a>' +
      '  <a class="fab msg" href="#" target="_blank" rel="noopener" aria-label="Nhắn tin Messenger">' +
      '    <span class="fab-ring"></span>' + IC_MSG + '<span class="fab-tip">Nhắn tin</span></a>' +
      '</div>' +
      '<footer class="site-footer">' +
      '  <div class="container">' +
      '    <div class="footer-grid">' +
      '      <div class="footer-brand">' +
      '        <div class="name">AN <b>VIỆT</b></div>' +
      '        <p>Công ty TNHH PCCC An Việt Group — nhà cung cấp giải pháp và thiết bị phòng cháy chữa cháy toàn diện. Vì một Việt Nam an toàn hơn, phát triển bền vững hơn.</p>' +
      '        <div class="footer-social"><a href="#">F</a><a href="#">Y</a><a href="#">Z</a><a href="#">in</a></div>' +
      '      </div>' +
      '      <div>' +
      '        <h4>Sản phẩm</h4>' +
      '        <ul>' +
      '          <li><a href="san-pham.html#sprinkler">Đầu phun Sprinkler</a></li>' +
      '          <li><a href="san-pham.html#binh">Bình chữa cháy</a></li>' +
      '          <li><a href="san-pham.html#tudong">Hệ thống PCCC tự động</a></li>' +
      '          <li><a href="san-pham.html#bom">Bơm chữa cháy</a></li>' +
      '          <li><a href="san-pham.html#baochay">Thiết bị báo cháy</a></li>' +
      '        </ul>' +
      '      </div>' +
      '      <div>' +
      '        <h4>Về chúng tôi</h4>' +
      '        <ul>' +
      '          <li><a href="gioi-thieu.html">Giới thiệu</a></li>' +
      '          <li><a href="giai-phap.html">Giải pháp</a></li>' +
      '          <li><a href="du-an.html">Dự án</a></li>' +
      '          <li><a href="tin-tuc.html">Tin tức</a></li>' +
      '          <li><a href="lien-he.html">Liên hệ</a></li>' +
      '        </ul>' +
      '      </div>' +
      '      <div>' +
      '        <h4>Liên hệ</h4>' +
      '        <ul>' +
      '          <li>📍 T1 Nhà liền kề Vin Nguyệt Quế 25-26, KĐT Vinhomes Riverside 2, P. Phúc Lợi, Hà Nội</li>' +
      '          <li>📞 0866 19 29 59</li>' +
      '          <li>✉ anviet.firebuild.group@gmail.com</li>' +
      '        </ul>' +
      '      </div>' +
      '    </div>' +
      '    <div class="footer-bottom">© <span id="year">2026</span> An Việt. Bản quyền thuộc về Công ty TNHH PCCC An Việt Group. &nbsp;|&nbsp; MST: 0111535730</div>' +
      '  </div>' +
      '</footer>';
  }

  if ('customElements' in window) {
    customElements.define('site-header', class extends HTMLElement {
      connectedCallback() {
        this.innerHTML = headerHtml(this.getAttribute('active') || '');
      }
    });
    customElements.define('site-footer', class extends HTMLElement {
      connectedCallback() {
        this.innerHTML = footerHtml();
      }
    });
  }
})();
