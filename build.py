#!/usr/bin/env python3
"""Aktual Academy saytının səhifələrini yaradır.

Header, footer və menyu bir yerdədir — dəyişiklikdən sonra:
    python3 build.py
"""
from pathlib import Path

OUT = Path(__file__).parent
PHONE1, PHONE1_TEL = "+994 55 781 25 25", "+994557812525"
PHONE2, PHONE2_TEL = "+994 55 781 25 75", "+994557812575"
EMAIL = "info@aktualacademy.az"
RESULTS_URL = "https://sinaqnetice.com/index.php?menu=resultMAN&opt=participant"

# ---------------------------------------------------------------- Proqramlar
PROGRAMS = [
    dict(slug="etud", title="Etüd", icon="📖", color="blue", img="etud-sm.jpg",
         short="Məktəbdən sonra müəllimlərin nəzarəti və köməyi ilə ev tapşırıqlarının hazırlanması.",
         body="""
<p>Məktəbdən sonra ETÜD saatlarında şagirdlər ev tapşırıqlarını müəllimlərin nəzarəti altında hazırlayır. Müəllimlər tapşırıqlarda çətinlik çəkən şagirdlərə köməklik göstərir.</p>
<p>Bütün sinif otaqlarında 24 saat kamera nəzarəti və elektron lövhələr var. Mərkəzdə həkim, psixoloq, kitabxana, bufet və Wi-Fi xidməti mövcuddur — övladınız günün qalan hissəsini təhlükəsiz və faydalı mühitdə keçirir.</p>""",
         facts=[("👩‍🏫", "Müəllim nəzarəti"), ("📹", "24 saat kamera"), ("🥪", "Bufet"), ("🩺", "Həkim və psixoloq")]),
    dict(slug="xarici-dil", title="Xarici dil", icon="🌍", color="green", img="xarici-dil.jpg",
         short="İngilis, rus, alman və fransız dilləri — danışıq klubu və aylıq sınaqlarla.",
         body="""
<p>Mərkəzimizdə <b>ingilis, rus, alman və fransız</b> dilləri tədris olunur.</p>
<ul class="checks">
  <li>Dərslər həftədə <b>3 dəfə 60 dəqiqə</b> və ya <b>2 dəfə 90 dəqiqə</b></li>
  <li>Hər həftə sonu həm kursumuzun, həm də kənar şagirdlər üçün <b>Conversation Club</b> təşkil olunur</li>
  <li>Hər ayın sonunda <b>sınaq imtahanları</b> keçirilir</li>
</ul>
<div class="note">
  <h4>🇬🇧 Cambridge sınaq imtahanları</h4>
  <p>Cambridge ingilis dili imtahanlarının Azərbaycan üzrə rəsmi hazırlıq və imtahan mərkəzi olan <b>ITAC</b> ilə tərəfdaşlıq çərçivəsində Cambridge ingilis dili sınaq imtahanları təşkil olunur. Sınaq 3 istiqamətdə keçirilir: <b>dinləmə, oxu və yazı</b>. İştirak edərək ingilis dili səviyyənizi Cambridge standartlarında ölçə bilərsiniz. Hər səviyyə üzrə ilk 3 yerin qaliblərinə (minimum balı keçmək şərtilə) sertifikat təqdim olunur.</p>
</div>""",
         facts=[("🇬🇧", "İngilis"), ("🇷🇺", "Rus"), ("🇩🇪", "Alman"), ("🇫🇷", "Fransız")]),
    dict(slug="liseylere-hazirliq", title="Liseylərə hazırlıq", icon="🏛️", color="red", img="tekmillesdirme.jpg",
         short="Respublika lisey və gimnaziyalarına qəbul imtahanlarına peşəkar mütəxəssislərlə hazırlıq.",
         body="__LYCEUMS__",
         facts=[("🏛️", "10 lisey və gimnaziya"), ("🧮", "Riyaziyyat və məntiq"), ("📝", "Test hazırlığı"), ("👩‍🏫", "Peşəkar mütəxəssislər")]),
    dict(slug="abituriyent-hazirligi", title="Buraxılış və abituriyent hazırlığı", icon="🎓", color="blue", img="abituriyent.jpg",
         short="9, 10 və 11-ci siniflər üçün həftəlik quiz və aylıq pulsuz imtahanlarla hazırlıq.",
         body="""
<p>Abituriyent hazırlığımız <b>9, 10 və 11-ci sinifləri</b> əhatə edir.</p>
<ul class="checks">
  <li>Dərslər həftədə <b>3 dəfə</b>, hər fənn üzrə <b>1 saat</b> keçirilir</li>
  <li>Hər həftə <b>quiz</b> imtahanları</li>
  <li>Hər ayın sonunda <b>ödənişsiz</b> imtahan</li>
  <li>Ayda bir dəfə <b>valideyn iclası</b> — müəllimlər hər şagirdin inkişafı barədə məlumat verir</li>
</ul>""",
         facts=[("📅", "Həftədə 3 dəfə"), ("📝", "Həftəlik quiz"), ("🆓", "Aylıq pulsuz imtahan"), ("👪", "Aylıq valideyn iclası")]),
    dict(slug="mektebeqeder-hazirliq", title="Məktəbəqədər hazırlıq", icon="🧸", color="green", img="mektebeqeder.jpg",
         short="Uşaqların məktəbə hazır, özünəinamlı və maraqla başlaması üçün hazırlıq.",
         body="""
<p>Məktəbəqədər hazırlıq proqramı uşaqları birinci sinfə hazırlayır: hərflər və səslər, saymaq, diqqət və yaddaş, rəsm və yaradıcılıq, qrup içində ünsiyyət.</p>
<p>Dərslər uşaqların yaşına uyğun, oyun elementləri ilə keçirilir. Mərkəzimizdə loqoped və psixoloq dəstəyi də mövcuddur.</p>""",
         facts=[("🔤", "Hərflər və səslər"), ("🔢", "Saymaq"), ("🎨", "Yaradıcılıq"), ("🤝", "Ünsiyyət")]),
    dict(slug="ibtidai-sinif-hazirligi", title="İbtidai sinif hazırlığı", icon="✏️", color="red", img="ibtidai.jpg",
         short="1–4-cü sinif şagirdləri üçün möhkəm bilik təməli yaradan dərslər.",
         body="""
<p>İbtidai sinif şagirdləri üçün Azərbaycan dili, riyaziyyat və digər fənlər üzrə məktəb proqramına uyğun dəstək dərsləri.</p>
<p>Məqsəd — şagirdin məktəbdə özünü inamlı hiss etməsi, oxu və yazı vərdişlərinin möhkəmlənməsi və liseylərə qəbula vaxtında hazırlığın başlanmasıdır.</p>""",
         facts=[("📘", "Azərbaycan dili"), ("➗", "Riyaziyyat"), ("📖", "Oxu vərdişi"), ("🏛️", "Liseyə hazırlıq təməli")]),
    dict(slug="tekmillesdirme-hazirligi", title="Təkmilləşdirmə hazırlığı", icon="📈", color="blue", img="tekmillesdirme.jpg",
         short="Fənlər üzrə biliklərin gücləndirilməsi və boşluqların aradan qaldırılması.",
         body="""
<p>Təkmilləşdirmə hazırlığı məktəb fənləri üzrə biliklərini gücləndirmək və boşluqları aradan qaldırmaq istəyən şagirdlər üçündür.</p>
<p>Şagirdin hazırkı səviyyəsi qiymətləndirilir, ona uyğun plan hazırlanır və irəliləyiş müntəzəm sınaqlarla izlənilir.</p>""",
         facts=[("🔍", "Səviyyə qiymətləndirməsi"), ("🗂️", "Fərdi plan"), ("📊", "Müntəzəm sınaqlar"), ("👪", "Valideynə hesabat")]),
    dict(slug="loqoped-psixoloq", title="Loqoped, psixoloq", icon="💬", color="green", img="mektebeqeder.jpg",
         short="Nitq inkişafı üzrə loqoped dəstəyi və uşaqlar üçün psixoloji məsləhət.",
         body="""
<p>Mərkəzimizdə uşaqlar üçün <b>loqoped</b> və <b>psixoloq</b> xidmətləri göstərilir.</p>
<ul class="checks">
  <li>Nitq qüsurlarının müəyyən edilməsi və korreksiyası</li>
  <li>Diqqət, yaddaş və emosional inkişafa dəstək</li>
  <li>Valideynlər üçün məsləhətlər</li>
</ul>""",
         facts=[("🗣️", "Nitq inkişafı"), ("🧠", "Psixoloji dəstək"), ("👪", "Valideyn məsləhəti"), ("🤝", "Fərdi yanaşma")]),
]

LYCEUMS = [
    ("FRİTL — Fizika, Riyaziyyat və İnformatika Təmayüllü Respublika Liseyi", "Hazırda 6, 7, 8-ci sinifdə oxuyanlar", "Yalnız Azərbaycan bölməsi",
     ["6-cı sinif: Azərbaycan dili (20), Riyaziyyat (20), Məntiq (20)", "7-ci sinif: Azərbaycan dili (25), Riyaziyyat (25), Məntiq (20)", "8-ci sinif: Azərbaycan dili (30), Riyaziyyat (30), Fizika (20), Kimya (20)"],
     "Bakı, Yasamal r., Əhməd Cəmil küç. 3", None),
    ("KBTRL — Kimya-Biologiya Təmayüllü Respublika Liseyi", "Hazırda 6, 7, 8-ci sinifdə oxuyanlar", "Yalnız Azərbaycan bölməsi",
     ["6-cı sinif: Azərbaycan dili (20), Riyaziyyat (20), Məntiq (20)", "7-ci sinif: Azərbaycan dili (25), Riyaziyyat (25), Məntiq (20)", "8-ci sinif: Azərbaycan dili (30), Riyaziyyat (30), Fizika (20), Kimya (20)"],
     "Bakı, Nizami r., Ş. Mirzəyev küç. 53", None),
    ("Dəyanət Liseyi — Dəyanət Vəqfi Bakı Türk Liseyi", "Hazırda 5 və 8-ci sinifdə oxuyanlar", "Yalnız Azərbaycan bölməsi",
     ["5-ci sinif: Azərbaycan dili (25), Riyaziyyat (25), İngilis dili (25), Tarix (25)", "8-ci sinif, I qrup: Azərbaycan dili, Riyaziyyat, İngilis dili, Fizika, Kimya", "8-ci sinif, II qrup: Azərbaycan dili, Riyaziyyat, İngilis dili, Coğrafiya, Tarix", "8-ci sinif, III qrup: Azərbaycan dili, Riyaziyyat, İngilis dili, Ədəbiyyat, Tarix", "8-ci sinif, IV qrup: Azərbaycan dili, Riyaziyyat, Biologiya, Fizika, Kimya"],
     "Bakı, Nəsimi r., B. Bağırova küç. (Zabitlər parkı yaxınlığı)", "İldə təxminən 130–140 şagird (5-ci sinif) və 25–30 şagird (8-ci sinif) qəbul olunur."),
    ("Bakı Slavyan Liseyi — BSU nəzdində məktəb-lisey kompleksi", "Hazırda 4-cü sinifdə oxuyanlar (boş yer olarsa, digər siniflər də)", "Azərbaycan və rus bölmələri",
     ["Azərbaycan (rus) dili, Riyaziyyat, Məntiq, İngilis dili"],
     "Bakı, S. Rəhimov küç. 145", "Ödənişli liseydir — illik təhsil haqqı 1300 AZN. Bakı Slavyan məktəbi isə ödənişsizdir."),
    ("“Gənc İstedadlar” Liseyi — BDU nəzdində", "Hazırda 4-cü sinifdə oxuyanlar", "Azərbaycan və rus bölmələri",
     ["Azərbaycan (rus) dili — 25 sual", "Riyaziyyat — 25 sual", "Məntiq — 10 sual"],
     "Bakı, Yasamal r., Əhməd Cəmil küç. 53", None),
    ("S. Bəhlulzadə adına Gimnaziya", "Hazırda 4, 5, 6, 7-ci sinifdə oxuyanlar", "Yalnız Azərbaycan bölməsi",
     ["4-cü sinif: Azərbaycan dili (15), Riyaziyyat (15), Məntiq (15)", "5-ci sinif: Azərbaycan dili (20), Riyaziyyat (20), Məntiq (20)", "6-cı sinif: Azərbaycan dili (20), Riyaziyyat (20), Məntiq (20)", "7-ci sinif: Azərbaycan dili (25), Riyaziyyat (25), Məntiq (20)"],
     "Bakı, Nizami r., Cəlal Qurbanov küç. 30", "Boş yer olarsa digər siniflər üzrə də mərkəzləşdirilmiş imtahan keçirilir."),
    ("147 nömrəli Texniki-Humanitar Lisey", "Hazırda 4, 5, 6, 7-ci sinifdə oxuyanlar", "Azərbaycan və rus bölmələri",
     ["4-cü sinif: Azərbaycan/rus dili (15), Riyaziyyat (15), Məntiq (15)", "5-ci sinif: Azərbaycan/rus dili (20), Riyaziyyat (20), Məntiq (20)", "6-cı sinif: Azərbaycan/rus dili (20), Riyaziyyat (20), Məntiq (20)", "7-ci sinif: Azərbaycan/rus dili (25), Riyaziyyat (25), Məntiq (20)"],
     "Bakı, Xətai r., Yusif Səfərov küç. 29", "Boş yer olarsa digər siniflər üzrə də mərkəzləşdirilmiş imtahan keçirilir."),
    ("S.C. Pişəvəri adına Gimnaziya", None, None, [], None, "Ətraflı məlumat üçün bizimlə əlaqə saxlayın."),
    ("Heydər Əliyev adına Lisey", "1–10-cu siniflər (boş yer olmadıqda bəzi siniflərə qəbul olmaya bilər)", "Yalnız Azərbaycan bölməsi",
     ["1-ci sinif: müsahibə", "2–4-cü siniflər: Azərbaycan dili (20), Riyaziyyat (15) — boş yer olarsa", "5-ci sinif: Azərbaycan dili (20), Riyaziyyat (20), İngilis dili (20)", "6–9-cu siniflər, humanitar: Azərbaycan dili, Riyaziyyat, İngilis dili, Tarix", "6–9-cu siniflər, texniki: Azərbaycan dili, Riyaziyyat, İngilis dili, Fizika"],
     "Bakı, Xətai r., Natiq Əliyev küç. 50", "Ödənişsizdir."),
    ("Zərifə Əliyeva adına Lisey", None, None, [], None, "Ətraflı məlumat üçün bizimlə əlaqə saxlayın."),
]

POSTS = [
    dict(title="Güvən Sınaq — Buraxılış", date="01 mart 2025", img="blog-guven.jpg",
         text="9, 10 və 11-ci sinif şagirdləri Güvən nəşriyyatının buraxılış və qrup fənləri üzrə sınaq imtahanına dəvət olunur. Sınaq 6 aprel saat 10:00 və 13:30-da Aktual Academy-də keçirilir. Qeydiyyat davam edir."),
    dict(title="Dəyər Sınaq — Buraxılış", date="01 mart 2025", img="blog-deyer-buraxilis.jpg",
         text="Dəyər nəşriyyatının 9 və 10-cu siniflər üçün buraxılış sınağı 16 mart saat 10:00-da keçirilir. Əvvəlcədən qeydiyyat mütləqdir! Əlaqə: 055-781-25-25."),
    dict(title="Dəyər Sınaq — İbtidai, Məktəbli", date="01 mart 2025", img="blog-deyer-ibtidai.jpg",
         text="Dəyər nəşriyyatının 1–8-ci siniflər üçün sınaq imtahanı 16 mart saat 10:00-da keçirilir. Əvvəlcədən qeydiyyat mütləqdir! Əlaqə: 055-781-25-25."),
]

NAV = [
    ("index.html", "Ana səhifə"),
    ("haqqimizda.html", "Haqqımızda"),
    ("proqramlar.html", "Proqramlar"),
    ("sinaq-imtahanlari.html", "Sınaq imtahanları"),
    ("filiallar.html", "Filiallar"),
    ("bloq.html", "Bloq"),
    ("elaqe.html", "Əlaqə"),
]


# ---------------------------------------------------------------- Ortaq hissələr
def nav_html(active):
    items = []
    for href, label in NAV:
        cls = ' class="active"' if href == active or (href == "proqramlar.html" and active.startswith("proqram-")) else ""
        if href == "proqramlar.html":
            sub = "".join(f'<a href="proqram-{p["slug"]}.html">{p["icon"]} {p["title"]}</a>' for p in PROGRAMS)
            items.append(f'<div class="dropdown"><a href="{href}"{cls}>{label} <span class="caret">▾</span></a><div class="dropdown__menu">{sub}</div></div>')
        else:
            items.append(f'<a href="{href}"{cls}>{label}</a>')
    return "\n        ".join(items)


def page(filename, title, description, body, home=False):
    head_title = "Aktual Academy — Müasir tədris mərkəzi | Bakı" if home else f"{title} — Aktual Academy"
    html = f"""<!DOCTYPE html>
<html lang="az">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{head_title}</title>
  <meta name="description" content="{description}">
  <link rel="icon" href="assets/logo.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="styles.css">
</head>
<body>

  <div class="topbar">
    <div class="container topbar__inner">
      <span>🕗 B.e.–C. 08:00–18:00 · Ş. 08:00–17:00</span>
      <span class="topbar__right">
        <a href="tel:{PHONE1_TEL}">📞 {PHONE1}</a>
        <a href="mailto:{EMAIL}">✉️ {EMAIL}</a>
      </span>
    </div>
  </div>

  <header class="header" id="header">
    <div class="container header__inner">
      <a href="index.html" class="logo"><img src="assets/logo.png" alt="Aktual Academy"></a>
      <nav class="nav" id="nav">
        {nav_html(filename)}
        <a href="elaqe.html#qeydiyyat" class="btn btn--sm">Qeydiyyat</a>
      </nav>
      <button class="burger" id="burger" aria-label="Menyu"><span></span><span></span><span></span></button>
    </div>
  </header>

{body}

  <footer class="footer">
    <div class="container footer__inner">
      <div>
        <img src="assets/logo.png" alt="Aktual Academy" class="footer__logo">
        <p>Qırmızı atestatla məzun olmaq Aktual ilə mümkündür!</p>
        <p class="footer__hours">B.e.–C.: 08:00–18:00<br>Şənbə: 08:00–17:00<br>Bazar: istirahət günü</p>
      </div>
      <div>
        <h5>Menyu</h5>
        {"".join(f'<a href="{h}">{l}</a>' for h, l in NAV)}
      </div>
      <div>
        <h5>Proqramlar</h5>
        {"".join(f'<a href="proqram-{p["slug"]}.html">{p["title"]}</a>' for p in PROGRAMS)}
      </div>
      <div>
        <h5>Əlaqə</h5>
        <a href="tel:{PHONE1_TEL}">{PHONE1}</a>
        <a href="tel:{PHONE2_TEL}">{PHONE2}</a>
        <a href="mailto:{EMAIL}">{EMAIL}</a>
        <a href="filiallar.html">İnşaatçılar · Əhmədli</a>
      </div>
    </div>
    <div class="container footer__bottom">© <span id="year"></span> Aktual Academy. Bütün hüquqlar qorunur.</div>
  </footer>

  <a href="https://wa.me/{PHONE1_TEL[1:]}?text=Salam" class="wa" target="_blank" rel="noopener" aria-label="WhatsApp">
    <svg viewBox="0 0 32 32" width="30" height="30" fill="#fff"><path d="M16 3C9 3 3.3 8.7 3.3 15.7c0 2.2.6 4.4 1.7 6.3L3 29l7.2-1.9c1.8 1 3.9 1.5 5.9 1.5 7 0 12.7-5.7 12.7-12.7S23 3 16 3zm0 23.3c-1.9 0-3.8-.5-5.4-1.5l-.4-.2-4.3 1.1 1.1-4.2-.3-.4c-1.1-1.7-1.6-3.6-1.6-5.5C5.1 9.9 10 5.1 16 5.1s10.9 4.9 10.9 10.9S22 26.3 16 26.3zm6-8.2c-.3-.2-1.9-.9-2.2-1-.3-.1-.5-.2-.7.2-.2.3-.8 1-1 1.2-.2.2-.4.2-.7.1-.3-.2-1.4-.5-2.6-1.6-1-.9-1.6-1.9-1.8-2.2-.2-.3 0-.5.1-.7l.5-.6c.2-.2.2-.3.3-.5.1-.2 0-.4 0-.6l-1-2.4c-.3-.6-.5-.5-.7-.5h-.6c-.2 0-.6.1-.9.4-.3.3-1.2 1.1-1.2 2.8s1.2 3.2 1.4 3.5c.2.2 2.4 3.6 5.8 5 .8.4 1.4.6 1.9.7.8.3 1.5.2 2.1.1.6-.1 1.9-.8 2.2-1.5.3-.7.3-1.4.2-1.5-.1-.2-.3-.3-.6-.4z"/></svg>
  </a>

  <script src="script.js"></script>
</body>
</html>
"""
    (OUT / filename).write_text(html, encoding="utf-8")
    print("✓", filename)


def page_hero(title, crumbs, subtitle=""):
    trail = ' <span>/</span> '.join(
        [f'<a href="index.html">Ana səhifə</a>'] +
        [f'<a href="{h}">{l}</a>' if h else f'<b>{l}</b>' for h, l in crumbs])
    sub = f"<p>{subtitle}</p>" if subtitle else ""
    return f"""  <section class="page-hero">
    <div class="shape shape--1"></div><div class="shape shape--2"></div>
    <div class="container">
      <nav class="crumbs">{trail}</nav>
      <h1>{title}</h1>
      {sub}
    </div>
  </section>"""


def program_cards(link=True):
    cards = []
    for p in PROGRAMS:
        cards.append(f"""        <a href="proqram-{p['slug']}.html" class="program reveal" style="--c: var(--{p['color']})">
          <div class="program__icon">{p['icon']}</div>
          <h3>{p['title']}</h3>
          <p>{p['short']}</p>
          <span class="program__more">Ətraflı →</span>
        </a>""")
    return "\n".join(cards)


def reg_form():
    grades = "".join(f"<option>{g}</option>" for g in ["Məktəbəqədər"] + [str(i) for i in range(1, 12)] + ["Məzun"])
    progs = "".join(f"<option>{p['title']}</option>" for p in PROGRAMS) + "<option>Sınaq imtahanı</option>"
    return f"""      <form class="form reveal" id="form">
        <h3>Qeydiyyat forması</h3>
        <label>Valideynin adı<input type="text" name="parent" required></label>
        <label>Telefon<input type="tel" name="phone" required placeholder="+994"></label>
        <div class="form__row">
          <label>Şagirdin sinfi<select name="grade">{grades}</select></label>
          <label>Filial<select name="branch"><option>İnşaatçılar</option><option>Əhmədli</option></select></label>
        </div>
        <label>Proqram<select name="program">{progs}</select></label>
        <button type="submit" class="btn btn--full">WhatsApp ilə göndər</button>
        <small class="form__hint">Müraciətiniz WhatsApp vasitəsilə birbaşa bizə çatacaq.</small>
      </form>"""


def contact_list():
    return f"""        <ul class="contact__list">
          <li><span>📞</span><div><small>Telefon</small><a href="tel:{PHONE1_TEL}">{PHONE1}</a> / <a href="tel:{PHONE2_TEL}">{PHONE2}</a></div></li>
          <li><span>✉️</span><div><small>E-poçt</small><a href="mailto:{EMAIL}">{EMAIL}</a></div></li>
          <li><span>📍</span><div><small>Ünvan</small>Bakı, A.M. Şərifzadə küç. 168K · Məhəmməd Hadi küç. 51C</div></li>
          <li><span>🕗</span><div><small>İş saatları</small>B.e.–C.: 08:00–18:00 · Ş.: 08:00–17:00 · B.: istirahət</div></li>
        </ul>"""


CTA = """  <section class="cta-band">
    <div class="container cta-band__inner reveal">
      <div>
        <h2>Övladınızın gələcəyinə bu gün başlayın</h2>
        <p>Pulsuz məsləhət üçün bizə yazın və ya zəng edin.</p>
      </div>
      <div class="cta-band__actions">
        <a href="elaqe.html#qeydiyyat" class="btn btn--white">Qeydiyyat</a>
        <a href="tel:+994557812525" class="btn btn--outline-white">📞 Zəng et</a>
      </div>
    </div>
  </section>"""

FACILITIES = """      <div class="facilities">
        <div class="facility reveal"><span>📹</span><b>24 saat kamera</b><small>Bütün sinif otaqlarında</small></div>
        <div class="facility reveal"><span>🖥️</span><b>Elektron lövhələr</b><small>Hər sinifdə</small></div>
        <div class="facility reveal"><span>🩺</span><b>Həkim</b><small>Mərkəzdə tibbi nəzarət</small></div>
        <div class="facility reveal"><span>🧠</span><b>Psixoloq</b><small>Uşaqlara dəstək</small></div>
        <div class="facility reveal"><span>📚</span><b>Kitabxana</b><small>Oxu və hazırlıq üçün</small></div>
        <div class="facility reveal"><span>🥪</span><b>Bufet</b><small>Fasilələrdə qidalanma</small></div>
        <div class="facility reveal"><span>📶</span><b>Wi-Fi</b><small>Bütün mərkəzdə</small></div>
        <div class="facility reveal"><span>👩‍🏫</span><b>ETÜD</b><small>Ev tapşırığına köməklik</small></div>
      </div>"""

BRANCHES = """      <div class="branches">
        <div class="branch reveal">
          <iframe loading="lazy" title="İnşaatçılar filialı xəritəsi" src="https://maps.google.com/maps?q=A.M.+%C5%9E%C9%99rifzad%C9%99+k%C3%BC%C3%A7%C9%99si+168K,+Bak%C4%B1&output=embed"></iframe>
          <div class="branch__info">
            <h3>İnşaatçılar filialı</h3>
            <p>📍 A.M. Şərifzadə küçəsi, 168K (3153-cü məhəllə, 13 nömrəli məktəbin qarşısı)</p>
            <p>📞 <a href="tel:+994557812525">+994 55 781 25 25</a></p>
            <p>🕗 B.e.–C. 08:00–18:00 · Ş. 08:00–17:00</p>
          </div>
        </div>
        <div class="branch reveal">
          <iframe loading="lazy" title="Əhmədli filialı xəritəsi" src="https://maps.google.com/maps?q=M%C9%99h%C9%99mm%C9%99d+Hadi+51C,+%C6%8Fhm%C9%99dli,+Bak%C4%B1&output=embed"></iframe>
          <div class="branch__info">
            <h3>Əhmədli filialı</h3>
            <p>📍 Məhəmməd Hadi küçəsi, 51C</p>
            <p>📞 <a href="tel:+994557812575">+994 55 781 25 75</a></p>
            <p>🕗 B.e.–C. 08:00–18:00 · Ş. 08:00–17:00</p>
          </div>
        </div>
      </div>"""


# ---------------------------------------------------------------- Səhifələr
def build_home():
    body = f"""  <section class="hero">
    <div class="shape shape--1"></div><div class="shape shape--2"></div><div class="shape shape--3"></div>
    <div class="container hero__inner">
      <div class="hero__text reveal">
        <span class="badge">✨ 2021-ci ildən sizinlə</span>
        <h1>Qırmızı atestatla məzun olmaq <span class="hl">Aktual</span> ilə mümkündür!</h1>
        <p>Məktəbəqədər hazırlıqdan abituriyent hazırlığına qədər — övladınızın təhsili üçün müasir standartlara uyğun tədris mərkəzi.</p>
        <div class="hero__actions">
          <a href="elaqe.html#qeydiyyat" class="btn">Qeydiyyatdan keç</a>
          <a href="proqramlar.html" class="btn btn--ghost">Proqramlar</a>
        </div>
      </div>
      <div class="hero__media reveal">
        <div class="hero__photo"><img src="assets/etud.jpg" alt="Aktual Academy-də dərs prosesi"></div>
        <div class="float-card float-card--a"><b>📹</b><span>24 saat kamera nəzarəti</span></div>
        <div class="float-card float-card--b"><b>🖥️</b><span>Elektron lövhələr</span></div>
      </div>
    </div>
  </section>

  <section class="facts">
    <div class="container facts__grid">
      <div class="fact reveal"><strong>2021</strong><span>ildən fəaliyyətdəyik</span></div>
      <div class="fact reveal"><strong>2</strong><span>filial: İnşaatçılar və Əhmədli</span></div>
      <div class="fact reveal"><strong>{len(PROGRAMS)}</strong><span>tədris istiqaməti</span></div>
      <div class="fact reveal"><strong>24/7</strong><span>sinif otaqlarında kamera</span></div>
    </div>
  </section>

  <section class="section">
    <div class="container about">
      <div class="about__img reveal"><img src="assets/logo.png" alt="Aktual Academy loqosu"></div>
      <div class="reveal">
        <span class="eyebrow">Haqqımızda</span>
        <h2>Gələcəyimiz olan övladlarımızın təhsili — bizim əsas işimizdir</h2>
        <p>Aktual Academy təhsil və tədris sahəsində ən son standartlara uyğun fəaliyyət göstərən hazırlıq müəssisəsidir. Valideyn və şagirdlərə məktəbəqədər, ibtidai sinif, təkmilləşdirmə, buraxılış, liseylərə, abituriyent və xarici dil hazırlığı üzrə xidmət göstəririk.</p>
        <a href="haqqimizda.html" class="btn btn--ghost">Ətraflı oxu</a>
      </div>
    </div>
  </section>

  <section class="section section--alt">
    <div class="container">
      <div class="section__head reveal">
        <span class="eyebrow">Proqramlar</span>
        <h2>Doğru təhsil, parlaq gələcək!</h2>
      </div>
      <div class="programs">
{program_cards()}
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section__head reveal">
        <span class="eyebrow">Şərait</span>
        <h2>Övladınız üçün təhlükəsiz və rahat mühit</h2>
      </div>
{FACILITIES}
    </div>
  </section>

  <section class="section section--dark">
    <div class="container sinaq">
      <div class="reveal">
        <span class="eyebrow">Sınaq imtahanları</span>
        <h2>Biliyinizi real imtahan şəraitində yoxlayın</h2>
        <p>Mərkəzimizdə müntəzəm olaraq ibtidai, məktəbli və buraxılış sinifləri üçün sınaq imtahanları keçirilir. Qeydiyyat mütləqdir!</p>
        <div class="sinaq__actions">
          <a href="{RESULTS_URL}" target="_blank" rel="noopener" class="btn btn--white">📊 İmtahan nəticəsinə bax</a>
          <a href="sinaq-imtahanlari.html" class="btn btn--outline-white">Ətraflı</a>
        </div>
      </div>
      <ul class="sinaq__list reveal">
        <li><b>1–4</b><span>İbtidai siniflər</span></li>
        <li><b>5–8</b><span>Məktəbli sınaqları</span></li>
        <li><b>9–11</b><span>Buraxılış sınaqları</span></li>
      </ul>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section__head reveal">
        <span class="eyebrow">Filiallar</span>
        <h2>Sizə yaxın filialı seçin</h2>
      </div>
{BRANCHES}
    </div>
  </section>

  <section class="section section--alt">
    <div class="container contact">
      <div class="reveal">
        <span class="eyebrow">Qeydiyyat</span>
        <h2>Övladınızı indi qeydiyyatdan keçirin</h2>
        <p class="muted">Formu doldurun — müraciətiniz birbaşa WhatsApp vasitəsilə bizə çatacaq.</p>
{contact_list()}
      </div>
{reg_form()}
    </div>
  </section>"""
    page("index.html", "Ana səhifə",
         "Aktual Academy — 2021-ci ildən fəaliyyət göstərən tədris mərkəzi. Etüd, xarici dil, liseylərə və abituriyent hazırlığı. İnşaatçılar və Əhmədli filialları.",
         body, home=True)


def build_about():
    body = f"""{page_hero("Haqqımızda", [(None, "Haqqımızda")], "Doğru təhsil, parlaq gələcək!")}

  <section class="section">
    <div class="container about">
      <div class="about__photo reveal"><img src="assets/etud.jpg" alt="Aktual Academy-də dərs"></div>
      <div class="reveal">
        <span class="eyebrow">Biz kimik</span>
        <h2>Müasir standartlara uyğun hazırlıq müəssisəsi</h2>
        <p class="muted">Aktual Academy təhsil və tədris sahəsində ən son standartlara uyğun fəaliyyət göstərən hazırlıq müəssisəsidir. Tədris mərkəzimiz <b>2021-ci ildən</b> fəaliyyətə başlamışdır.</p>
        <p class="muted">Valideyn və şagirdlərə məktəbəqədər, ibtidai sinif, təkmilləşdirmə, buraxılış, liseylərə, abituriyent və xarici dil hazırlığı üzrə xidmət göstəririk.</p>
        <p class="muted">Gələcəyimiz olan övladlarımız üçün edəcəyimiz ən gözəl və təqdirəlayiq iş onların təhsilinə xüsusi önəm verməyimizdir.</p>
      </div>
    </div>
  </section>

  <section class="section section--alt">
    <div class="container">
      <div class="values">
        <div class="value reveal" style="--c: var(--red)">
          <span>🎯</span>
          <h3>Məqsədimiz</h3>
          <p>Övladlarımızın müasir tədris mərkəzində həm yüksək səviyyədə təhsil almaları, həm də sosial cəhətdən fəal şəxsiyyət kimi yetişmələri.</p>
        </div>
        <div class="value reveal" style="--c: var(--blue)">
          <span>🌍</span>
          <h3>Prioritetimiz</h3>
          <p>Dünya və Avropa təcrübəsinə əsaslanaraq Azərbaycan təhsilində yüksək nailiyyətlər əldə etmək.</p>
        </div>
        <div class="value reveal" style="--c: var(--green)">
          <span>👩‍🏫</span>
          <h3>Komandamız</h3>
          <p>Mərkəzimizdə dərs deyən müəllim və idarə kollektivi öz sahəsində peşəkar şəxslərdir.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section__head reveal">
        <span class="eyebrow">Şərait</span>
        <h2>Mərkəzimizdə sizi nə gözləyir</h2>
        <p class="muted">Bütün sinif otaqlarında 24 saat kamera nəzarəti və elektron lövhələr quraşdırılıb. Məktəbdən sonra ETÜD saatlarında müəllimlər ev tapşırıqlarına nəzarət edir və köməklik göstərir.</p>
      </div>
{FACILITIES}
    </div>
  </section>

{CTA}"""
    page("haqqimizda.html", "Haqqımızda", "Aktual Academy haqqında: 2021-ci ildən fəaliyyət, məqsədimiz, komandamız və şəraitimiz.", body)


def build_programs():
    body = f"""{page_hero("Proqramlar", [(None, "Proqramlar")], "Məktəbəqədər yaşdan abituriyentə qədər — hər yaşa və hədəfə uyğun hazırlıq.")}

  <section class="section">
    <div class="container">
      <div class="programs">
{program_cards()}
      </div>
    </div>
  </section>

{CTA}"""
    page("proqramlar.html", "Proqramlar", "Aktual Academy proqramları: Etüd, xarici dil, liseylərə hazırlıq, abituriyent hazırlığı, məktəbəqədər və ibtidai sinif hazırlığı.", body)


def lyceums_html():
    items = []
    for i, (name, grades, lang, exams, addr, note) in enumerate(LYCEUMS, 1):
        rows = ""
        if grades: rows += f"<li><b>Qəbul:</b> {grades}</li>"
        if lang: rows += f"<li><b>Bölmə:</b> {lang}</li>"
        if addr: rows += f"<li><b>Ünvan:</b> {addr}</li>"
        ex = "".join(f"<li>{e}</li>" for e in exams)
        ex_html = f'<h5>İmtahan fənləri (sual sayı)</h5><ul class="exam-list">{ex}</ul>' if ex else ""
        note_html = f'<p class="lyceum__note">ℹ️ {note}</p>' if note else ""
        items.append(f"""<details class="lyceum"{' open' if i == 1 else ''}>
  <summary><span class="lyceum__num">{i}</span>{name}</summary>
  <div class="lyceum__body"><ul class="lyceum__meta">{rows}</ul>{ex_html}{note_html}</div>
</details>""")
    return f"""
<p>Övladınızı respublikanın aparıcı lisey və gimnaziyalarına qəbul imtahanlarına <b>peşəkar mütəxəssislərlə</b> hazırlayın. Aşağıda məktəblər üzrə qəbul şərtləri və imtahan fənləri verilib.</p>
<div class="lyceums">{''.join(items)}</div>
<p class="muted small">Məlumatlar məktəblərin rəsmi sosial şəbəkə səhifələrindən və məlumat xidmətlərindən götürülüb. Qəbul şərtləri hər il dəyişə bilər.</p>"""


def build_program_pages():
    for p in PROGRAMS:
        body_html = lyceums_html() if p["body"] == "__LYCEUMS__" else p["body"]
        facts = "".join(f'<div class="pfact"><span>{ic}</span>{t}</div>' for ic, t in p["facts"])
        others = "".join(
            f'<a href="proqram-{o["slug"]}.html"{" class=active" if o is p else ""}>{o["icon"]} {o["title"]}</a>'
            for o in PROGRAMS)
        body = f"""{page_hero(p["title"], [("proqramlar.html", "Proqramlar"), (None, p["title"])], p["short"])}

  <section class="section">
    <div class="container detail">
      <article class="detail__main reveal">
        <img class="detail__img" src="assets/{p['img']}" alt="{p['title']}">
        <div class="pfacts">{facts}</div>
        <div class="prose">{body_html}</div>
      </article>
      <aside class="detail__side">
        <div class="side-card reveal">
          <h4>Bütün proqramlar</h4>
          <nav class="side-nav">{others}</nav>
        </div>
        <div class="side-card side-card--accent reveal">
          <h4>Qeydiyyat</h4>
          <p>Bu proqrama yazılmaq və ya məsləhət almaq üçün bizimlə əlaqə saxlayın.</p>
          <a href="tel:{PHONE1_TEL}" class="side-phone">📞 {PHONE1}</a>
          <a href="elaqe.html#qeydiyyat" class="btn btn--white btn--full">Müraciət et</a>
        </div>
        <div class="side-card reveal">
          <h4>İş saatları</h4>
          <p class="hours"><span>B.e.–C.</span><b>08:00–18:00</b></p>
          <p class="hours"><span>Şənbə</span><b>08:00–17:00</b></p>
          <p class="hours"><span>Bazar</span><b>İstirahət</b></p>
        </div>
      </aside>
    </div>
  </section>"""
        page(f"proqram-{p['slug']}.html", p["title"], f"Aktual Academy — {p['title']}: {p['short']}", body)


def build_exams():
    body = f"""{page_hero("Sınaq imtahanları", [(None, "Sınaq imtahanları")], "Biliyinizi real imtahan şəraitində yoxlayın.")}

  <section class="section">
    <div class="container">
      <div class="results-box reveal">
        <div>
          <h2>İmtahan nəticəsi</h2>
          <p>Sınaq imtahanının nəticəsini iştirakçı kodunuz ilə onlayn yoxlayın.</p>
        </div>
        <a href="{RESULTS_URL}" target="_blank" rel="noopener" class="btn">📊 Nəticəyə bax</a>
      </div>

      <div class="section__head reveal" style="margin-top:80px">
        <span class="eyebrow">Sınaq növləri</span>
        <h2>Hər sinif üçün sınaq</h2>
      </div>
      <div class="exam-types">
        <div class="exam-type reveal" style="--c: var(--green)"><b>1–4</b><h3>İbtidai siniflər</h3><p>Dəyər və digər nəşriyyatların ibtidai sinif sınaqları.</p></div>
        <div class="exam-type reveal" style="--c: var(--blue)"><b>5–8</b><h3>Məktəbli sınaqları</h3><p>Fənlər üzrə bilik səviyyəsinin ölçülməsi.</p></div>
        <div class="exam-type reveal" style="--c: var(--red)"><b>9–11</b><h3>Buraxılış və qrup fənləri</h3><p>Dəyər və Güvən nəşriyyatlarının buraxılış sınaqları.</p></div>
        <div class="exam-type reveal" style="--c: var(--blue-dark)"><b>EN</b><h3>Cambridge sınağı</h3><p>ITAC ilə tərəfdaşlıqda: dinləmə, oxu və yazı.</p></div>
      </div>

      <div class="notice reveal">
        <span>⚠️</span>
        <p><b>Əvvəlcədən qeydiyyat mütləqdir!</b> Növbəti sınaq tarixləri üçün bizə zəng edin: <a href="tel:{PHONE1_TEL}">{PHONE1}</a></p>
      </div>

      <div class="section__head reveal" style="margin-top:80px">
        <span class="eyebrow">Elanlar</span>
        <h2>Son sınaq elanları</h2>
      </div>
      <div class="posts">{posts_html()}</div>
    </div>
  </section>

{CTA}"""
    page("sinaq-imtahanlari.html", "Sınaq imtahanları", "Aktual Academy sınaq imtahanları: ibtidai, məktəbli, buraxılış və Cambridge sınaqları. İmtahan nəticəsinə bax.", body)


def posts_html():
    return "".join(f"""
        <article class="post reveal">
          <img src="assets/{p['img']}" alt="{p['title']}">
          <div class="post__body">
            <time>📅 {p['date']}</time>
            <h3>{p['title']}</h3>
            <p>{p['text']}</p>
          </div>
        </article>""" for p in POSTS)


def build_branches():
    body = f"""{page_hero("Filiallar", [(None, "Filiallar")], "Bakıda 2 filialımız sizə xidmət göstərir.")}

  <section class="section">
    <div class="container">
{BRANCHES}
    </div>
  </section>

{CTA}"""
    page("filiallar.html", "Filiallar", "Aktual Academy filialları: İnşaatçılar (A.M. Şərifzadə 168K) və Əhmədli (Məhəmməd Hadi 51C).", body)


def build_blog():
    body = f"""{page_hero("Bloq", [(None, "Bloq")], "Xəbərlər, elanlar və sınaq imtahanları.")}

  <section class="section">
    <div class="container">
      <div class="posts">{posts_html()}</div>
    </div>
  </section>"""
    page("bloq.html", "Bloq", "Aktual Academy xəbərləri və elanları.", body)


def build_contact():
    body = f"""{page_hero("Əlaqə", [(None, "Əlaqə")], "Suallarınızı məmnuniyyətlə cavablandırarıq.")}

  <section class="section section--alt" id="qeydiyyat">
    <div class="container contact">
      <div class="reveal">
        <span class="eyebrow">Bizimlə əlaqə</span>
        <h2>Qeydiyyat və məsləhət</h2>
        <p class="muted">Formu doldurun — müraciətiniz WhatsApp vasitəsilə birbaşa bizə çatacaq. Və ya zəng edin.</p>
{contact_list()}
      </div>
{reg_form()}
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section__head reveal">
        <span class="eyebrow">Filiallar</span>
        <h2>Bizi ziyarət edin</h2>
      </div>
{BRANCHES}
    </div>
  </section>"""
    page("elaqe.html", "Əlaqə", "Aktual Academy ilə əlaqə: +994 55 781 25 25, info@aktualacademy.az. Onlayn qeydiyyat.", body)


if __name__ == "__main__":
    build_home()
    build_about()
    build_programs()
    build_program_pages()
    build_exams()
    build_branches()
    build_blog()
    build_contact()
