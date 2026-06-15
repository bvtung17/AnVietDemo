# -*- coding: utf-8 -*-
"""Generator tĩnh cho site An Việt — xuất HTML thuần dùng chung header/footer."""
import os
import re
import unicodedata

OUT = os.path.dirname(os.path.abspath(__file__))


def slugify(text):
    """Bỏ dấu tiếng Việt + chuẩn hoá thành slug an toàn cho tên file."""
    text = text.replace("đ", "d").replace("Đ", "D")
    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if not unicodedata.combining(c))
    text = re.sub(r"[^a-zA-Z0-9]+", "-", text).strip("-").lower()
    return text

NAV = [
    ("Trang chủ", "index.html", None),
    ("Giới thiệu", "gioi-thieu.html", None),
    ("Sản phẩm", "san-pham.html", [
        ("Đầu phun Sprinkler TITAN", "san-pham.html#sprinkler"),
        ("Bình chữa cháy AN VIỆT", "san-pham.html#binh"),
        ("Hệ thống PCCC tự động", "san-pham.html#tudong"),
        ("Hệ thống chữa cháy di động", "san-pham.html#didong"),
        ("Bơm chữa cháy", "san-pham.html#bom"),
        ("Phương tiện chữa cháy", "san-pham.html#xe"),
        ("Thiết bị báo cháy", "san-pham.html#baochay"),
    ]),
    ("Giải pháp", "giai-phap.html", None),
    ("Dự án", "du-an.html", None),
    ("Ứng dụng", "ung-dung.html", None),
    ("Đại lý", "dai-ly.html", None),
    ("Tuyển dụng", "tuyen-dung.html", None),
    ("Tin tức", "tin-tuc.html", None),
    ("Liên hệ", "lien-he.html", None),
]


def header(active, page_title):
    items = ""
    for label, href, sub in NAV:
        cls = "active" if href == active else ""
        if sub:
            subhtml = "".join(
                '<a href="{}">{}</a>'.format(h, l) for l, h in sub
            )
            items += (
                '<li class="has-sub {cls}"><a class="nav-link" href="{href}">{label}</a>'
                '<div class="submenu">{sub}</div></li>'
            ).format(cls=cls, href=href, label=label, sub=subhtml)
        else:
            items += '<li class="{cls}"><a class="nav-link" href="{href}">{label}</a></li>'.format(
                cls=cls, href=href, label=label
            )
    return """<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="An Việt - Cung cấp giải pháp, thiết bị phòng cháy chữa cháy (PCCC) toàn diện: bình chữa cháy, đầu phun Sprinkler, hệ thống báo cháy, thi công lắp đặt.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Cabin:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
</head>
<body>

<div class="topbar">
  <div class="container">
    <div class="tb-left">
      <span>📞 Hotline: 1900 8114</span>
      <span>✉ info@anviet.vn</span>
    </div>
    <div class="tb-social">
      <a href="#" aria-label="Facebook">Facebook</a>
      <a href="#" aria-label="Youtube">Youtube</a>
      <a href="#" aria-label="Zalo">Zalo</a>
    </div>
  </div>
</div>

<header class="site-header">
  <div class="container">
    <a class="brand" href="index.html">
      <span class="mark">AV</span>
      <span>
        <span class="name">AN <b>VIỆT</b></span>
        <span class="tag">Giải pháp PCCC toàn diện</span>
      </span>
    </a>
    <button class="nav-toggle" aria-label="Mở menu" aria-expanded="false">☰</button>
    <nav class="main-nav">
      <ul>{items}</ul>
    </nav>
    <a class="btn-quote" href="lien-he.html">Nhận báo giá</a>
  </div>
</header>
""".format(title=page_title, items=items)


# ---- SVG icon (currentColor) ----
IC_PHONE = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M6.6 10.8c1.4 2.8 3.8 5.1 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1A17 17 0 0 1 3 4c0-.6.5-1 1-1h3.5c.6 0 1 .4 1 1 0 1.2.2 2.4.6 3.6.1.4 0 .8-.3 1l-2.2 2.2z"/></svg>'
IC_MSG = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.3 2 2 6.2 2 11.6c0 2.9 1.3 5.5 3.4 7.2v3.5l3.1-1.7c.8.2 1.7.3 2.5.3 5.7 0 10-4.2 10-9.6S17.7 2 12 2zm1 12.9l-2.5-2.7-5 2.7 5.5-5.8 2.6 2.7 4.9-2.7-5.5 5.8z"/></svg>'
IC_ZALO = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 3C6.5 3 2 6.9 2 11.6c0 2.5 1.3 4.8 3.4 6.3-.1 1.1-.6 2.4-1.3 3.4 1.7-.2 3.3-.9 4.4-1.7 1.1.3 2.3.5 3.5.5 5.5 0 10-3.9 10-8.5S17.5 3 12 3z"/></svg>'
IC_FB = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M22 12a10 10 0 1 0-11.6 9.9v-7H7.9V12h2.5V9.8c0-2.5 1.5-3.9 3.7-3.9 1.1 0 2.2.2 2.2.2v2.5h-1.2c-1.2 0-1.6.8-1.6 1.6V12h2.7l-.4 2.9h-2.3v7A10 10 0 0 0 22 12z"/></svg>'
IC_SHOPEE = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a4 4 0 0 0-4 4H4.6L3.4 20.2A2 2 0 0 0 5.4 22h13.2a2 2 0 0 0 2-1.8L19.4 6H16a4 4 0 0 0-4-4zm0 2a2 2 0 0 1 2 2h-4a2 2 0 0 1 2-2zm-1.5 7.4c0-.8.8-1.4 1.8-1.4.7 0 1.4.2 1.9.5l-.5 1c-.4-.2-.9-.4-1.4-.4-.4 0-.7.1-.7.4 0 .8 2.6.5 2.6 2.4 0 .9-.8 1.5-2 1.5-.8 0-1.6-.2-2.1-.6l.5-1c.5.3 1 .5 1.6.5.5 0 .8-.2.8-.5 0-.8-2.5-.5-2.5-2.4z"/></svg>'
IC_LAZADA = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2.2 4 6.5v7c0 3.4 3.3 6.6 8 8.3 4.7-1.7 8-4.9 8-8.3v-7L12 2.2zM9.3 8.4l2.7 1.5 2.7-1.5 2.6 1.4-5.3 3-5.3-3 2.6-1.4z"/></svg>'

FOOTER = """
<!-- Hộp mua hàng (bên trái) -->
<div class="buybar">
  <div class="buybar-title">Mua<br>hàng</div>
  <ul>
    <li class="shopee"><a href="#" target="_blank" rel="noopener" aria-label="Shopee">{shopee}</a></li>
    <li class="lazada"><a href="#" target="_blank" rel="noopener" aria-label="Lazada">{lazada}</a></li>
    <li class="facebook"><a href="#" target="_blank" rel="noopener" aria-label="Facebook">{fb}</a></li>
    <li class="zalo"><a href="#" target="_blank" rel="noopener" aria-label="Zalo">{zalo}</a></li>
  </ul>
</div>

<!-- Nút liên hệ nổi góc dưới phải -->
<div class="fab-stack">
  <a class="fab phone" href="tel:19008114" aria-label="Gọi hotline">
    <span class="fab-ring"></span>{phone}<span class="fab-tip">1900 8114</span></a>
  <a class="fab zalo" href="#" target="_blank" rel="noopener" aria-label="Chat Zalo">
    {zalo}<span class="fab-tip">Chat Zalo</span></a>
  <a class="fab msg" href="#" target="_blank" rel="noopener" aria-label="Nhắn tin Messenger">
    <span class="fab-ring"></span>{msg}<span class="fab-tip">Nhắn tin</span></a>
</div>

<footer class="site-footer">""".format(
    shopee=IC_SHOPEE, lazada=IC_LAZADA, fb=IC_FB, zalo=IC_ZALO, phone=IC_PHONE, msg=IC_MSG
)
FOOTER += """
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <div class="name">AN <b>VIỆT</b></div>
        <p>Công ty Cổ phần An Việt — nhà cung cấp giải pháp và thiết bị phòng cháy chữa cháy
        toàn diện. Vì một Việt Nam an toàn hơn, phát triển bền vững hơn.</p>
        <div class="footer-social">
          <a href="#">F</a><a href="#">Y</a><a href="#">Z</a><a href="#">in</a>
        </div>
      </div>
      <div>
        <h4>Sản phẩm</h4>
        <ul>
          <li><a href="san-pham.html#sprinkler">Đầu phun Sprinkler</a></li>
          <li><a href="san-pham.html#binh">Bình chữa cháy</a></li>
          <li><a href="san-pham.html#tudong">Hệ thống PCCC tự động</a></li>
          <li><a href="san-pham.html#bom">Bơm chữa cháy</a></li>
          <li><a href="san-pham.html#baochay">Thiết bị báo cháy</a></li>
        </ul>
      </div>
      <div>
        <h4>Về chúng tôi</h4>
        <ul>
          <li><a href="gioi-thieu.html">Giới thiệu</a></li>
          <li><a href="giai-phap.html">Giải pháp</a></li>
          <li><a href="du-an.html">Dự án</a></li>
          <li><a href="tin-tuc.html">Tin tức</a></li>
          <li><a href="lien-he.html">Liên hệ</a></li>
        </ul>
      </div>
      <div>
        <h4>Liên hệ</h4>
        <ul>
          <li>📍 Số 20 Ngụy Như Kon Tum, Thanh Xuân, Hà Nội</li>
          <li>📞 1900 8114 - 0359 114 114</li>
          <li>✉ info@anviet.vn</li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      © 2023 - <span id="year">2026</span> An Việt. Bản quyền thuộc về Công ty Cổ phần An Việt.
    </div>
  </div>
</footer>

<script src="assets/js/main.js"></script>
</body>
</html>"""


def page(active, title, body):
    with open(os.path.join(OUT, active), "w", encoding="utf-8") as f:
        f.write(header(active, title) + body + FOOTER)


# ============================ TRANG CHỦ ============================
SLIDES = [
    ("assets/img/big_toa-nha-lanmark-81.jpg", "Giải pháp PCCC",
     "Giải pháp phòng cháy chữa cháy toàn diện",
     "Tư vấn - thiết kế - thi công - bảo trì hệ thống PCCC cho công trình dân dụng và công nghiệp theo tiêu chuẩn quốc gia."),
    ("assets/img/big_san-bay-tan-son-nhat-international-airport.jpg", "Sản phẩm chính hãng",
     "Thiết bị chữa cháy đạt chuẩn",
     "Đầu phun Sprinkler TITAN, bình chữa cháy, hệ thống báo cháy chính hãng — kiểm định đầy đủ, bảo hành dài hạn."),
    ("assets/img/big_lotte-mall-tay-ho.png", "Tự động hóa",
     "Hệ thống chữa cháy tự động",
     "Phát hiện đám cháy sớm, kích hoạt chữa cháy tự động — bảo vệ con người và tài sản 24/7."),
]
slides_html = ""
for i, (img, eye, h2, p) in enumerate(SLIDES):
    slides_html += """
    <div class="slide {act}" style="background-image:url('{img}')">
      <div class="container">
        <div class="slide-inner">
          <span class="eyebrow">{eye}</span>
          <h2>{h2}</h2>
          <p>{p}</p>
          <div class="slide-actions">
            <a class="btn btn-primary" href="san-pham.html">Xem sản phẩm</a>
            <a class="btn btn-ghost" href="lien-he.html">Liên hệ tư vấn</a>
          </div>
        </div>
      </div>
    </div>""".format(act="active" if i == 0 else "", img=img, eye=eye, h2=h2, p=p)

CATS = [
    ("Đầu phun Sprinkler TITAN", "assets/img/resize_dau-phun-sprinkler-titan-premium-7a2878.png",
     "Đầu phun Sprinkler đạt chuẩn UL/FM, đa dạng kiểu lắp đặt cho mọi công trình."),
    ("Bình chữa cháy AN VIỆT", "assets/img/resize_binh-chua-chay-hafico.png",
     "Bình chữa cháy bột, CO2, gốc nước, foam — cho gia đình, văn phòng, nhà xưởng."),
    ("Hệ thống PCCC tự động", "assets/img/resize_he-thong-phong-chay-chua-chay-tu-dong.png",
     "Phát hiện cháy sớm kết hợp chữa cháy tự động bằng khí, foam, nước."),
    ("Hệ thống chữa cháy di động", "assets/img/resize_he-thong-chua-chay-di-dong.png",
     "Hệ thống chữa cháy bột khô và bọt Foam di động (CAFS) cơ động cao."),
    ("Bơm chữa cháy", "assets/img/resize_bom-chua-chay-an-viet.png",
     "Bơm chữa cháy di động, bơm nổi và hệ thống bơm động cơ Diesel."),
    ("Phương tiện chữa cháy", "assets/img/resize_phuong-tien-chua-chay.png",
     "Xe cứu hỏa, xe cứu hộ, xe vận tải và robot chữa cháy đa năng."),
    ("Thiết bị chữa cháy", "assets/img/resize_voi-ong-chua-chay-va-phu-kien.png",
     "Đầu phun, vòi, cuộn vòi, lăng phun, trụ nước chữa cháy và phụ kiện."),
    ("Thiết bị báo cháy", "assets/img/resize_thiet-bi-bao-chay.jpg",
     "Hệ thống báo cháy thường, báo cháy địa chỉ và hệ thống khẩn cấp."),
]
cats_html = "".join("""
      <a class="card" href="san-pham.html">
        <div class="thumb"><img src="{img}" alt="{name}" loading="lazy"></div>
        <div class="body">
          <h3>{name}</h3>
          <p>{desc}</p>
          <span class="more">Tìm hiểu thêm →</span>
        </div>
      </a>""".format(img=img, name=name, desc=desc) for name, img, desc in CATS)

home_body = """
<section class="hero">
  <div class="slides">{slides}</div>
  <button class="slider-arrow prev" aria-label="Trước">‹</button>
  <button class="slider-arrow next" aria-label="Sau">›</button>
  <div class="slider-dots"></div>
</section>

<section class="section">
  <div class="container">
    <div class="features">
      <div class="feature"><div class="ico">🛡️</div><h3>Chính hãng - kiểm định</h3><p>Thiết bị đạt chuẩn, có đầy đủ giấy kiểm định PCCC.</p></div>
      <div class="feature"><div class="ico">🏗️</div><h3>Thi công trọn gói</h3><p>Tư vấn, thiết kế, thi công và nghiệm thu hệ thống PCCC.</p></div>
      <div class="feature"><div class="ico">⚙️</div><h3>Bảo trì 24/7</h3><p>Đội ngũ kỹ thuật bảo trì, ứng cứu nhanh trên toàn quốc.</p></div>
      <div class="feature"><div class="ico">🤝</div><h3>Giá cạnh tranh</h3><p>Sản xuất và phân phối trực tiếp, tối ưu chi phí cho khách hàng.</p></div>
    </div>
  </div>
</section>

<section class="section alt">
  <div class="container">
    <div class="section-head">
      <span class="kicker">Giải pháp / Sản phẩm</span>
      <h2>Danh mục sản phẩm nổi bật</h2>
      <p>Hệ sinh thái thiết bị và giải pháp PCCC toàn diện cho mọi quy mô công trình.</p>
    </div>
    <div class="grid cols-4">{cats}</div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="split">
      <img src="assets/img/resize_giai-phap-thiet-ke-thi-cong-pccc.png" alt="Thi công PCCC">
      <div>
        <span class="kicker">Về An Việt</span>
        <h2>Đối tác PCCC tin cậy của doanh nghiệp Việt</h2>
        <p>Công ty Cổ phần An Việt chuyên sản xuất, lắp ráp trang thiết bị, phương tiện và cung cấp
        giải pháp tích hợp — thiết kế, thi công lắp đặt hệ thống phòng cháy chữa cháy.</p>
        <ul class="check-list">
          <li>Đội ngũ kỹ sư PCCC nhiều năm kinh nghiệm</li>
          <li>Sản phẩm kiểm định, tuân thủ quy chuẩn quốc gia</li>
          <li>Quy trình khép kín: tư vấn → thi công → bảo trì</li>
          <li>Chính sách bảo hành & hậu mãi rõ ràng</li>
        </ul>
        <a class="btn btn-outline" href="gioi-thieu.html" style="margin-top:18px">Tìm hiểu về chúng tôi</a>
      </div>
    </div>
  </div>
</section>

<section class="section alt">
  <div class="container">
    <div class="stats">
      <div class="stat"><div class="num" data-target="15" data-suffix="+">0</div><div class="label">Năm kinh nghiệm</div></div>
      <div class="stat"><div class="num" data-target="2000" data-suffix="+">0</div><div class="label">Dự án hoàn thành</div></div>
      <div class="stat"><div class="num" data-target="63">0</div><div class="label">Tỉnh thành phủ sóng</div></div>
      <div class="stat"><div class="num" data-target="500" data-suffix="+">0</div><div class="label">Đại lý & đối tác</div></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="kicker">Dự án tiêu biểu</span>
      <h2>Thi công - lắp đặt hệ thống PCCC</h2>
      <p>An Việt tự hào đồng hành cùng các công trình trọng điểm trên khắp cả nước.</p>
    </div>
    <div class="logos">
      <figure><img src="assets/img/big_toa-nha-lanmark-81.jpg" alt="Landmark 81" loading="lazy">
        <figcaption>Tòa tháp Landmark 81, TP. Hồ Chí Minh</figcaption></figure>
      <figure><img src="assets/img/big_san-bay-tan-son-nhat-international-airport.jpg" alt="Sân bay Tân Sơn Nhất" loading="lazy">
        <figcaption>Cảng hàng không Quốc tế Tân Sơn Nhất</figcaption></figure>
      <figure><img src="assets/img/big_lotte-mall-tay-ho.png" alt="Lotte Mall Tây Hồ" loading="lazy">
        <figcaption>Lotte Mall Tây Hồ, Hà Nội</figcaption></figure>
    </div>
    <div style="text-align:center;margin-top:34px">
      <a class="btn btn-outline" href="du-an.html">Xem tất cả dự án</a>
    </div>
  </div>
</section>

<section class="section alt">
  <div class="container">
    <div class="section-head">
      <span class="kicker">Tin tức & Sự kiện</span>
      <h2>Cập nhật mới nhất từ An Việt</h2>
    </div>
    <div class="grid">
      <a class="card news-card" href="tin-tuc.html">
        <div class="thumb"><img src="assets/img/resize_giai-phap-thiet-ke-thi-cong-pccc.png" alt="tin tức" loading="lazy"></div>
        <div class="body"><span class="date">10/06/2026</span>
          <h3>Quy định mới về kiểm định thiết bị PCCC năm 2026</h3>
          <p>Cập nhật những thay đổi quan trọng trong công tác kiểm định và nghiệm thu hệ thống PCCC.</p>
          <span class="more">Đọc tiếp →</span></div>
      </a>
      <a class="card news-card" href="tin-tuc.html">
        <div class="thumb"><img src="assets/img/resize_dau-phun-sprinkler-titan-premium-7a2878.png" alt="tin tức" loading="lazy"></div>
        <div class="body"><span class="date">28/05/2026</span>
          <h3>An Việt ra mắt dòng đầu phun Sprinkler TITAN Premium</h3>
          <p>Sản phẩm đầu phun thế hệ mới với hiệu suất phun và độ bền vượt trội.</p>
          <span class="more">Đọc tiếp →</span></div>
      </a>
      <a class="card news-card" href="tin-tuc.html">
        <div class="thumb"><img src="assets/img/resize_binh-chua-chay-hafico.png" alt="tin tức" loading="lazy"></div>
        <div class="body"><span class="date">15/05/2026</span>
          <h3>Hướng dẫn chọn bình chữa cháy phù hợp cho gia đình</h3>
          <p>Bột, CO2 hay gốc nước? Lựa chọn đúng loại bình giúp xử lý đám cháy hiệu quả.</p>
          <span class="more">Đọc tiếp →</span></div>
      </a>
    </div>
  </div>
</section>

<section class="cta-band">
  <div class="container">
    <h2>Cần tư vấn giải pháp PCCC cho công trình của bạn?</h2>
    <p>Đội ngũ kỹ sư An Việt sẵn sàng khảo sát và báo giá miễn phí.</p>
    <a class="btn btn-ghost" href="lien-he.html">Liên hệ ngay</a>
  </div>
</section>
""".format(slides=slides_html, cats=cats_html)

page("index.html", "An Việt - Giải pháp phòng cháy chữa cháy toàn diện", home_body)


# ============================ helper banner ============================
def banner(title, crumb):
    return """
<section class="page-banner">
  <div class="container">
    <h1>{title}</h1>
    <div class="breadcrumb"><a href="index.html">Trang chủ</a> / {crumb}</div>
  </div>
</section>""".format(title=title, crumb=crumb)


# ============================ GIỚI THIỆU ============================
gt_body = banner("Giới thiệu", "Giới thiệu") + """
<section class="section">
  <div class="container">
    <div class="split">
      <img src="assets/img/resize_giai-phap-thiet-ke-thi-cong-pccc.png" alt="An Việt">
      <div class="prose">
        <span class="kicker" style="color:var(--red);font-weight:700;text-transform:uppercase;letter-spacing:1.5px">Hồ sơ công ty</span>
        <h2 style="margin-top:6px">Công ty Cổ phần An Việt</h2>
        <p>An Việt là doanh nghiệp chuyên nghiên cứu, sản xuất, lắp ráp trang thiết bị, phương tiện
        và cung cấp giải pháp tích hợp trong lĩnh vực phòng cháy chữa cháy. Chúng tôi đặt khách hàng
        làm trung tâm, không ngừng đổi mới để mang lại sản phẩm và dịch vụ tốt nhất.</p>
        <p>Với phương châm <b>"CHẤT LƯỢNG LÀ SỐ 1"</b> đi kèm giá cả cạnh tranh, An Việt cam kết
        đồng hành cùng khách hàng vì một Việt Nam an toàn và phát triển bền vững.</p>
      </div>
    </div>
  </div>
</section>

<section class="section alt">
  <div class="container">
    <div class="grid" style="grid-template-columns:repeat(2,1fr)">
      <div class="feature" style="text-align:left">
        <h3 style="color:var(--red);font-size:20px">🎯 Sứ mệnh</h3>
        <p style="font-size:16px">"Vì một Việt Nam an toàn và phát triển bền vững." Chúng tôi tin rằng
        an toàn là nền tảng thiết yếu cho sự phát triển của mọi cộng đồng.</p>
      </div>
      <div class="feature" style="text-align:left">
        <h3 style="color:var(--red);font-size:20px">🔭 Tầm nhìn</h3>
        <p style="font-size:16px">Trở thành thương hiệu hàng đầu Việt Nam về sản xuất, lắp ráp thiết bị,
        phương tiện và giải pháp thiết kế, thi công lắp đặt hệ thống PCCC.</p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="kicker">Giá trị cốt lõi</span>
      <h2>Giá trị của chúng tôi</h2>
    </div>
    <div class="features">
      <div class="feature"><div class="ico">⚖️</div><h3>Chính trực</h3><p>Tuân thủ các tiêu chuẩn đạo đức cao nhất và trung thực trong mọi giao tiếp.</p></div>
      <div class="feature"><div class="ico">🙌</div><h3>Tôn trọng</h3><p>Hợp tác, tôn trọng và có trách nhiệm với đối tác, khách hàng, đồng nghiệp.</p></div>
      <div class="feature"><div class="ico">👥</div><h3>Làm việc nhóm</h3><p>Đặt mục tiêu tập thể lên trên lợi ích cá nhân, đề cao tinh thần hợp tác.</p></div>
      <div class="feature"><div class="ico">❤️</div><h3>Con người</h3><p>Con người là trung tâm, là xương sống cho sự phát triển của doanh nghiệp.</p></div>
    </div>
  </div>
</section>
"""
page("gioi-thieu.html", "Giới thiệu - An Việt", gt_body)


# ============================ SẢN PHẨM ============================
PRODUCT_SECTIONS = [
    ("sprinkler", "Đầu phun Sprinkler TITAN", [
        ("Đầu phun Sprinkler TITAN Premium", "assets/img/resize_dau-phun-sprinkler-titan-premium-7a2878.png"),
        ("Đầu phun Sprinkler tiêu chuẩn", "assets/img/resize_dau-phun-sprinkler.jpg"),
    ]),
    ("binh", "Bình chữa cháy AN VIỆT", [
        ("Bình chữa cháy bột khô ABC", "assets/img/resize_binh-chua-chay-bot-kho-abc-hafico.png"),
        ("Bình chữa cháy khí CO2", "assets/img/resize_binh-chua-chay-khi-co2-hafico.png"),
        ("Bình chữa cháy gốc nước NANO/WB", "assets/img/resize_binh-chua-chay-goc-nuoc-hafico-nanowb.png"),
    ]),
    ("tudong", "Hệ thống PCCC tự động", [
        ("Hệ thống PCCC tự động", "assets/img/resize_he-thong-phong-chay-chua-chay-tu-dong.png"),
        ("Hệ thống chữa cháy tự động bằng khí", "assets/img/resize_he-thong-chua-chay-tu-dong-bang-khi.png"),
    ]),
    ("didong", "Hệ thống chữa cháy di động", [
        ("Hệ thống chữa cháy di động", "assets/img/resize_he-thong-chua-chay-di-dong.png"),
    ]),
    ("bom", "Bơm chữa cháy", [
        ("Bơm chữa cháy AN VIỆT", "assets/img/resize_bom-chua-chay-an-viet.png"),
    ]),
    ("xe", "Phương tiện chữa cháy", [
        ("Xe cứu hỏa đa năng", "assets/img/resize_xe-cuu-hoa-da-nang.png"),
        ("Robot chữa cháy đa năng", "assets/img/resize_robot-chua-chay-da-nang.png"),
    ]),
    ("baochay", "Thiết bị báo cháy", [
        ("Thiết bị báo cháy", "assets/img/resize_thiet-bi-bao-chay.jpg"),
        ("Chất chữa cháy", "assets/img/resize_chat-chua-chay.jpg"),
    ]),
]
# Gán slug duy nhất cho mỗi sản phẩm -> trang chi tiết "sp-<slug>.html"
PRODUCTS = []  # (slug, name, img, anchor, sec_title)
for anchor, sec_title, prods in PRODUCT_SECTIONS:
    for name, img in prods:
        PRODUCTS.append(("sp-" + slugify(name) + ".html", name, img, anchor, sec_title))

DETAIL_FEATURES = [
    "Sản phẩm chính hãng, có đầy đủ giấy kiểm định PCCC theo quy chuẩn Việt Nam.",
    "Vật liệu bền bỉ, hoạt động ổn định trong môi trường khắc nghiệt.",
    "Lắp đặt nhanh, tương thích với hệ thống PCCC tiêu chuẩn.",
    "Bảo hành chính hãng, hỗ trợ kỹ thuật và bảo trì trọn đời.",
]
features_html = "".join("<li>{}</li>".format(f) for f in DETAIL_FEATURES)

# ----- Trang danh sách sản phẩm -----
sp_inner = ""
for anchor, sec_title, prods in PRODUCT_SECTIONS:
    cards = ""
    for name, img in prods:
        slug = "sp-" + slugify(name) + ".html"
        cards += """
        <a class="card" href="{slug}">
          <div class="thumb"><img src="{img}" alt="{name}" loading="lazy"></div>
          <div class="body"><h3>{name}</h3><p>Sản phẩm chính hãng, kiểm định đầy đủ theo quy chuẩn PCCC.</p>
          <span class="more">Xem chi tiết →</span></div>
        </a>""".format(slug=slug, img=img, name=name)
    sp_inner += """
  <div id="{anchor}">
    <h2 style="font-size:26px;font-weight:800;margin:0 0 22px;border-left:4px solid var(--red);padding-left:14px">{title}</h2>
    <div class="grid" style="margin-bottom:48px">{cards}</div>
  </div>""".format(anchor=anchor, title=sec_title, cards=cards)

sp_body = banner("Sản phẩm", "Sản phẩm") + """
<section class="section">
  <div class="container">{inner}</div>
</section>
""".format(inner=sp_inner)
page("san-pham.html", "Sản phẩm - An Việt", sp_body)

# ----- Trang chi tiết từng sản phẩm -----
for slug, name, img, anchor, sec_title in PRODUCTS:
    related = [p for p in PRODUCTS if p[3] == anchor and p[0] != slug][:3]
    related_html = "".join("""
        <a class="card" href="{s}">
          <div class="thumb"><img src="{i}" alt="{n}" loading="lazy"></div>
          <div class="body"><h3>{n}</h3><span class="more">Xem chi tiết →</span></div>
        </a>""".format(s=s, i=i, n=n) for s, n, i, a, st in related)
    related_block = ""
    if related_html:
        related_block = """
<section class="section alt">
  <div class="container">
    <div class="section-head"><span class="kicker">Cùng danh mục</span><h2>Sản phẩm liên quan</h2></div>
    <div class="grid">{rel}</div>
  </div>
</section>""".format(rel=related_html)

    detail_body = """
<section class="page-banner">
  <div class="container">
    <h1>{name}</h1>
    <div class="breadcrumb"><a href="index.html">Trang chủ</a> / <a href="san-pham.html">Sản phẩm</a>
      / <a href="san-pham.html#{anchor}">{sec}</a> / {name}</div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="split">
      <div class="product-gallery"><img src="{img}" alt="{name}"></div>
      <div>
        <span class="kicker" style="color:var(--red);font-weight:700;text-transform:uppercase;letter-spacing:1.5px">{sec}</span>
        <h2 style="font-size:30px;font-weight:800;margin:6px 0 14px">{name}</h2>
        <p style="color:var(--slate);margin-bottom:18px">{name} do An Việt cung cấp — thiết bị PCCC
        đạt chuẩn, phù hợp cho công trình dân dụng và công nghiệp. Liên hệ để được tư vấn và báo giá tốt nhất.</p>
        <ul class="check-list">{feats}</ul>
        <div class="slide-actions" style="margin-top:22px">
          <a class="btn btn-primary" href="lien-he.html">Nhận báo giá</a>
          <a class="btn btn-outline" href="tel:19008114">Gọi 1900 8114</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section alt">
  <div class="container">
    <div class="prose" style="max-width:840px;margin:0 auto">
      <h2>Mô tả sản phẩm</h2>
      <p>{name} là giải pháp thuộc nhóm <b>{sec}</b> trong hệ sinh thái sản phẩm PCCC của An Việt.
      Sản phẩm được sản xuất theo tiêu chuẩn nghiêm ngặt, đảm bảo độ tin cậy và hiệu quả chữa cháy cao.</p>
      <h3>Thông số & đặc điểm</h3>
      <ul>{feats}</ul>
      <h3>Ứng dụng</h3>
      <p>Phù hợp lắp đặt cho tòa nhà cao tầng, nhà xưởng, khu công nghiệp, trung tâm thương mại,
      kho bãi và công trình dân dụng. Vui lòng liên hệ kỹ sư An Việt để được tư vấn chi tiết theo nhu cầu.</p>
    </div>
  </div>
</section>
{related}
""".format(name=name, anchor=anchor, sec=sec_title, img=img, feats=features_html, related=related_block)
    page(slug, name + " - An Việt", detail_body)


# ============================ GIẢI PHÁP ============================
gp_body = banner("Giải pháp thiết kế thi công PCCC", "Giải pháp") + """
<section class="section">
  <div class="container">
    <div class="split">
      <div class="prose">
        <span class="kicker" style="color:var(--red);font-weight:700;text-transform:uppercase;letter-spacing:1.5px">Quy trình</span>
        <h2 style="margin-top:6px">Giải pháp PCCC trọn gói</h2>
        <p>An Việt cung cấp dịch vụ tư vấn, thiết kế, thi công và bảo trì hệ thống phòng cháy chữa cháy
        cho công trình dân dụng và công nghiệp, đảm bảo tuân thủ quy chuẩn, tiêu chuẩn hiện hành.</p>
        <ul>
          <li>Khảo sát hiện trạng & đánh giá rủi ro cháy nổ</li>
          <li>Thiết kế hệ thống PCCC, lập hồ sơ thẩm duyệt</li>
          <li>Cung cấp vật tư, thiết bị chính hãng</li>
          <li>Thi công, lắp đặt & nghiệm thu</li>
          <li>Bảo trì, bảo dưỡng định kỳ</li>
        </ul>
      </div>
      <img src="assets/img/resize_giai-phap-thiet-ke-thi-cong-pccc.png" alt="Giải pháp PCCC">
    </div>
  </div>
</section>

<section class="section alt">
  <div class="container">
    <div class="section-head">
      <span class="kicker">Lĩnh vực</span>
      <h2>Giải pháp theo loại hình công trình</h2>
    </div>
    <div class="features">
      <div class="feature"><div class="ico">🏢</div><h3>Tòa nhà cao tầng</h3><p>Sprinkler, báo cháy địa chỉ, hệ thống tăng áp cầu thang.</p></div>
      <div class="feature"><div class="ico">🏭</div><h3>Nhà xưởng - KCN</h3><p>Hệ thống chữa cháy nước, foam, bột cho diện tích lớn.</p></div>
      <div class="feature"><div class="ico">🏬</div><h3>TTTM - siêu thị</h3><p>Giải pháp phát hiện sớm & chữa cháy tự động an toàn cho đám đông.</p></div>
      <div class="feature"><div class="ico">🏠</div><h3>Dân dụng - gia đình</h3><p>Bình chữa cháy, thiết bị báo khói, giải pháp PCCC gia đình.</p></div>
    </div>
  </div>
</section>

<section class="cta-band">
  <div class="container">
    <h2>Nhận tư vấn & khảo sát miễn phí</h2>
    <p>Gọi ngay 1900 8114 hoặc để lại thông tin, kỹ sư An Việt sẽ liên hệ với bạn.</p>
    <a class="btn btn-ghost" href="lien-he.html">Yêu cầu tư vấn</a>
  </div>
</section>
"""
page("giai-phap.html", "Giải pháp thiết kế thi công PCCC - An Việt", gp_body)


# ============================ DỰ ÁN ============================
PROJECTS = [
    ("Tòa tháp Landmark 81, TP.HCM", "assets/img/big_toa-nha-lanmark-81.jpg"),
    ("Lotte Mall Tây Hồ, Hà Nội", "assets/img/big_lotte-mall-tay-ho.png"),
    ("Sân bay Quốc tế Tân Sơn Nhất", "assets/img/big_san-bay-tan-son-nhat-international-airport.jpg"),
    ("Tập đoàn Dầu khí Việt Nam", "assets/img/big_tap-doan-dau-khi-viet-nam.jpg"),
    ("Đường sắt Việt Nam", "assets/img/big_duong-sat-viet-nam-24062916193154788.jpg"),
    ("Cảnh sát biển Việt Nam", "assets/img/big_canh-sat-bien-viet-nam.png"),
]
proj_html = "".join("""
      <figure>
        <img src="{img}" alt="{name}" loading="lazy">
        <figcaption>{name}</figcaption>
      </figure>""".format(img=img, name=name) for name, img in PROJECTS)
da_body = banner("Dự án tiêu biểu", "Dự án") + """
<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="kicker">Thi công - lắp đặt</span>
      <h2>Các dự án An Việt đã đồng hành</h2>
      <p>Niềm tin từ những công trình trọng điểm trên khắp cả nước.</p>
    </div>
    <div class="logos">{proj}</div>
  </div>
</section>
""".format(proj=proj_html)
page("du-an.html", "Dự án - An Việt", da_body)


# ============================ TIN TỨC ============================
NEWS = [
    ("Quy định mới về kiểm định thiết bị PCCC năm 2026", "10/06/2026",
     "assets/img/resize_giai-phap-thiet-ke-thi-cong-pccc.png",
     "Cập nhật những thay đổi quan trọng trong công tác kiểm định và nghiệm thu hệ thống PCCC."),
    ("An Việt ra mắt dòng đầu phun Sprinkler TITAN Premium", "28/05/2026",
     "assets/img/resize_dau-phun-sprinkler-titan-premium-7a2878.png",
     "Sản phẩm đầu phun thế hệ mới với hiệu suất phun và độ bền vượt trội."),
    ("Hướng dẫn chọn bình chữa cháy phù hợp cho gia đình", "15/05/2026",
     "assets/img/resize_binh-chua-chay-hafico.png",
     "Bột, CO2 hay gốc nước? Lựa chọn đúng loại bình giúp xử lý đám cháy hiệu quả và an toàn."),
    ("Bảo trì hệ thống PCCC: vì sao không nên bỏ qua?", "02/05/2026",
     "assets/img/resize_he-thong-phong-chay-chua-chay-tu-dong.png",
     "Bảo trì định kỳ đảm bảo hệ thống luôn sẵn sàng hoạt động khi có sự cố."),
    ("Robot chữa cháy đa năng - xu hướng PCCC hiện đại", "20/04/2026",
     "assets/img/resize_robot-chua-chay-da-nang.png",
     "Ứng dụng robot trong chữa cháy giúp tiếp cận khu vực nguy hiểm, bảo vệ lực lượng cứu hỏa."),
    ("An Việt mở rộng hệ thống đại lý toàn quốc", "05/04/2026",
     "assets/img/resize_phuong-tien-chua-chay.png",
     "Mạng lưới đại lý phủ rộng giúp khách hàng tiếp cận sản phẩm và dịch vụ nhanh chóng hơn."),
]
news_html = "".join("""
      <a class="card news-card" href="tin-tuc.html">
        <div class="thumb"><img src="{img}" alt="{title}" loading="lazy"></div>
        <div class="body">
          <span class="date">{date}</span>
          <h3>{title}</h3>
          <p>{desc}</p>
          <span class="more">Đọc tiếp →</span>
        </div>
      </a>""".format(img=img, title=title, date=date, desc=desc)
    for title, date, img, desc in NEWS)
tt_body = banner("Tin tức & Sự kiện", "Tin tức") + """
<section class="section">
  <div class="container">
    <div class="grid">{news}</div>
  </div>
</section>
""".format(news=news_html)
page("tin-tuc.html", "Tin tức - An Việt", tt_body)


# ============================ LIÊN HỆ ============================
lh_body = banner("Liên hệ", "Liên hệ") + """
<section class="section">
  <div class="container">
    <div class="contact-grid">
      <div class="contact-info">
        <h2 style="font-size:28px;font-weight:800;margin-bottom:18px">Công ty Cổ phần An Việt</h2>
        <div class="item"><span class="ico">🏢</span><div><h4>Trụ sở chính - Hà Nội</h4><p>Số 20 Ngụy Như Kon Tum, P. Thanh Xuân, Hà Nội</p></div></div>
        <div class="item"><span class="ico">🏢</span><div><h4>Chi nhánh miền Nam - TP.HCM</h4><p>Số 1185 Lê Đức Anh, KP.14, P. An Lạc, TP.HCM</p></div></div>
        <div class="item"><span class="ico">📞</span><div><h4>Hotline</h4><p>1900 8114 - 0359 114 114</p></div></div>
        <div class="item"><span class="ico">✉</span><div><h4>Email</h4><p>info@anviet.vn</p></div></div>
      </div>
      <div class="form-card">
        <h2 style="font-size:24px;font-weight:800;margin-bottom:18px">Gửi yêu cầu tư vấn</h2>
        <form id="contact-form">
          <div class="form-row">
            <div class="field"><label>Họ và tên *</label><input type="text" required></div>
            <div class="field"><label>Điện thoại *</label><input type="tel" required></div>
          </div>
          <div class="field"><label>Email</label><input type="email"></div>
          <div class="field"><label>Tiêu đề</label><input type="text"></div>
          <div class="field"><label>Nội dung *</label><textarea rows="5" required></textarea></div>
          <button type="submit" class="btn btn-primary" style="width:100%">Gửi thông tin</button>
          <p class="form-msg"></p>
        </form>
      </div>
    </div>
  </div>
</section>
"""
page("lien-he.html", "Liên hệ - An Việt", lh_body)


# ============================ ỨNG DỤNG ============================
APPS = [
    ("🪖", "PCCC Quân đội & Cảnh sát", "Giải pháp phòng cháy chữa cháy chuyên dụng cho lực lượng vũ trang."),
    ("✈️", "PCCC Hàng không", "Hệ thống chữa cháy cho sân bay, nhà ga và phương tiện hàng không."),
    ("⛽", "PCCC Dầu, khí đốt & điện", "Giải pháp cho kho xăng dầu, nhà máy khí, trạm điện và hóa chất."),
    ("🏙️", "PCCC Khu dân cư & thương mại", "Bảo vệ chung cư, văn phòng, trung tâm thương mại và nhà ở."),
    ("🚇", "PCCC Xe điện & tàu điện ngầm", "Hệ thống PCCC cho phương tiện giao thông công cộng và metro."),
    ("⛏️", "PCCC Mỏ", "Giải pháp chữa cháy cho hầm mỏ và khu vực khai thác khoáng sản."),
]
apps_html = "".join("""
      <div class="feature" style="text-align:left">
        <div class="ico">{ic}</div><h3>{t}</h3><p>{d}</p>
      </div>""".format(ic=ic, t=t, d=d) for ic, t, d in APPS)
ud_body = banner("Ứng dụng", "Ứng dụng") + """
<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="kicker">Lĩnh vực ứng dụng</span>
      <h2>Giải pháp PCCC cho mọi ngành</h2>
      <p>An Việt cung cấp giải pháp phòng cháy chữa cháy phù hợp cho từng lĩnh vực đặc thù.</p>
    </div>
    <div class="features">{apps}</div>
  </div>
</section>
""".format(apps=apps_html)
page("ung-dung.html", "Ứng dụng - An Việt", ud_body)


# ============================ ĐẠI LÝ ============================
AGENTS = [
    ("Hà Nội", "Đại lý An Việt Hà Nội", "Số 20 Ngụy Như Kon Tum, P. Thanh Xuân, Hà Nội", "0359 114 114"),
    ("Hải Dương", "Đại lý An Việt Hải Dương", "CCN Gia Xuyên, P. Thạch Khôi, TP. Hải Dương", "1900 8114"),
    ("TP. Hồ Chí Minh", "Đại lý An Việt TP.HCM", "Số 1185 Lê Đức Anh, KP.14, P. An Lạc, TP.HCM", "0286 685 6888"),
]
agents_opts = "".join('<option value="{p}">{p}</option>'.format(p=p) for p, *_ in AGENTS)
agents_html = "".join("""
      <div class="agent-card" data-province="{p}">
        <span class="agent-prov">{p}</span>
        <h3>{n}</h3>
        <p>📍 {a}</p>
        <p>📞 <a href="tel:{tel}">{tel}</a></p>
      </div>""".format(p=p, n=n, a=a, tel=tel.replace(" ", "")) for p, n, a, tel in AGENTS)
dl_body = banner("Hệ thống đại lý", "Đại lý") + """
<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="kicker">Phân phối toàn quốc</span>
      <h2>Tìm đại lý An Việt gần bạn</h2>
    </div>
    <div style="max-width:420px;margin:0 auto 36px">
      <select id="province-filter" class="field" style="width:100%;padding:12px 14px;border:1px solid var(--line);border-radius:8px;font:inherit">
        <option value="">Tất cả tỉnh thành</option>
        {opts}
      </select>
    </div>
    <div class="agent-grid">{agents}</div>
  </div>
</section>
""".format(opts=agents_opts, agents=agents_html)
page("dai-ly.html", "Hệ thống đại lý - An Việt", dl_body)


# ============================ TUYỂN DỤNG ============================
JOBS = [
    ("Nhân viên Kinh doanh - Chi nhánh Miền Nam",
     "Số 1185 Lê Đức Anh, KP.14, P. An Lạc, TP.HCM", "Thỏa thuận", "3", "Đang tuyển"),
    ("Nhân viên Kinh doanh - Miền Bắc",
     "Số 20 Ngụy Như Kon Tum, P. Thanh Xuân, Hà Nội", "Thỏa thuận", "5", "Đang tuyển"),
    ("Thực tập sinh Marketing",
     "Số 20 Ngụy Như Kon Tum, P. Thanh Xuân, Hà Nội", "Thỏa thuận", "5", "Đang tuyển"),
]
jobs_html = "".join("""
      <div class="job-card">
        <div class="job-main">
          <h3>{title}</h3>
          <p>📍 {loc}</p>
        </div>
        <div class="job-meta">
          <span class="job-salary">{sal}</span>
          <span class="job-qty">Số lượng: {qty}</span>
          <span class="job-status">{st}</span>
          <a class="btn btn-primary" href="lien-he.html">Ứng tuyển</a>
        </div>
      </div>""".format(title=title, loc=loc, sal=sal, qty=qty, st=st)
    for title, loc, sal, qty, st in JOBS)
td_body = banner("Tuyển dụng", "Tuyển dụng") + """
<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="kicker">Cơ hội nghề nghiệp</span>
      <h2>Thông tin tuyển dụng</h2>
      <p>Gia nhập An Việt — cùng kiến tạo một Việt Nam an toàn hơn, phát triển bền vững hơn.</p>
    </div>
    <div class="job-list">{jobs}</div>
  </div>
</section>
""".format(jobs=jobs_html)
page("tuyen-dung.html", "Tuyển dụng - An Việt", td_body)


print("Đã tạo các trang chính + {} trang chi tiết sản phẩm".format(len(PRODUCTS)))
