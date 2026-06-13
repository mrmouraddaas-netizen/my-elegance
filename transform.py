import re

with open(r'C:\Users\n1\AppData\Local\Temp\opencode\my-elegance\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ===== META / TITLE =====
html = html.replace(
    '<meta name="description" content="BodyGlad - N°1 Fitness à Alger. Salle de sport premium, équipements modernes, coachs professionnels, suppléments Reborn Nutrition. Abonnements flexibles.">',
    '<meta name="description" content="My Elegance - Montres de luxe en Algérie. Découvrez notre collection de montres élégantes au meilleur prix. Livraison partout en Algérie.">'
)
html = html.replace(
    '<meta name="keywords" content="fitness alger, salle de sport alger, gym cheraga, bodyglad, reborn nutrition, salle de musculation alger">',
    '<meta name="keywords" content="montres alger, montre luxe algerie, my elegance, bijouterie alger, montre homme alger, montre femme alger">'
)
html = html.replace(
    '<title>BodyGlad - N°1 Fitness à Alger</title>',
    '<title>My Elegance - Montres de Luxe en Algérie</title>'
)

# ===== LOGO =====
html = html.replace('assets/images/logo.png', 'assets/images/logo.jpg')
html = html.replace('alt="BodyGlad"', 'alt="My Elegance"')

# ===== PROMO BAR =====
old_promo = '<div class="promo-bar" data-i18n="promo"><span>\U0001f4cd</span> Chéraga, vers GARDEN CITY <span class="promo-sep">|</span> <span>\U0001f4de</span> 0554 67 22 22 <span class="promo-sep">|</span> <span>\U0001f550</span> 6h-00h · 7j/7</div>'
new_promo = '<div class="promo-bar" data-i18n="promo"><span>\U0001f48e</span> Montres de Luxe <span class="promo-sep">|</span> <span>\U0001f4de</span> 0554 67 22 22 <span class="promo-sep">|</span> <span>\U0001f69a</span> Livraison partout en Algérie</div>'
html = html.replace(old_promo, new_promo)

# ===== NAV LINKS =====
old_nav = '<a href="#about" class="nav-link" data-i18n="nav-about">About</a>\n<a href="#schedule" class="nav-link" data-i18n="nav-schedule">Schedule</a>\n<a href="#memberships" class="nav-link" data-i18n="nav-memberships">Memberships</a>\n<a href="#shop" class="nav-link" data-i18n="nav-shop">Shop</a>\n<a href="#gallery" class="nav-link" data-i18n="nav-gallery">Gallery</a>\n<a href="#coaches" class="nav-link" data-i18n="nav-coaches">Coaches</a>\n<a href="#contact-us" class="nav-link" data-i18n="nav-contact">Contact</a>'
new_nav = '<a href="#home" class="nav-link" onclick="showPage(\'home\')" data-i18n="nav-home">Home</a>\n<a href="#about" class="nav-link" data-i18n="nav-about">About</a>\n<a href="#shop" class="nav-link" data-i18n="nav-shop">Shop</a>\n<a href="#gallery" class="nav-link" data-i18n="nav-gallery">Gallery</a>\n<a href="#contact-us" class="nav-link" data-i18n="nav-contact">Contact</a>\n<a href="#testimonials" class="nav-link" data-i18n="nav-testimonials">Testimonials</a>\n<a href="#faq" class="nav-link" data-i18n="nav-faq">FAQ</a>'
html = html.replace(old_nav, new_nav)

# Mobile nav
old_mob = '<a href="#about" class="nav-link" data-i18n="nav-about" onclick="closeMobile()">About</a>\n<a href="#schedule" class="nav-link" data-i18n="nav-schedule" onclick="closeMobile()">Schedule</a>\n<a href="#memberships" class="nav-link" data-i18n="nav-memberships" onclick="closeMobile()">Memberships</a>\n<a href="#shop" class="nav-link" data-i18n="nav-shop" onclick="closeMobile()">Shop</a>\n<a href="#gallery" class="nav-link" data-i18n="nav-gallery" onclick="closeMobile()">Gallery</a>\n<a href="#coaches" class="nav-link" data-i18n="nav-coaches" onclick="closeMobile()">Coaches</a>\n<a href="#workout" class="nav-link" data-i18n="nav-programs" onclick="closeMobile()">Programs</a>\n<a href="#contact-us" class="nav-link" data-i18n="nav-contact" onclick="closeMobile()">Contact</a>'
new_mob = '<a href="#home" class="nav-link" onclick="closeMobile();showPage(\'home\')" data-i18n="nav-home">Home</a>\n<a href="#about" class="nav-link" data-i18n="nav-about" onclick="closeMobile()">About</a>\n<a href="#shop" class="nav-link" data-i18n="nav-shop" onclick="closeMobile()">Shop</a>\n<a href="#gallery" class="nav-link" data-i18n="nav-gallery" onclick="closeMobile()">Gallery</a>\n<a href="#contact-us" class="nav-link" data-i18n="nav-contact" onclick="closeMobile()">Contact</a>\n<a href="#testimonials" class="nav-link" data-i18n="nav-testimonials" onclick="closeMobile()">Testimonials</a>\n<a href="#faq" class="nav-link" data-i18n="nav-faq" onclick="closeMobile()">FAQ</a>'
html = html.replace(old_mob, new_mob)

# ===== HERO =====
hero_badge = html.find('<div class="hero-badge" data-i18n="hero-badge">#1 Gym in Algiers</div>')
if hero_badge > 0:
    old_end = html.find('</section>', hero_badge)
    new_hero_block = '''<div class="hero-badge" data-i18n="hero-badge">\u2728 Luxury Watches</div>
<h1 class="hero-title" data-i18n="hero-title">TIME IS<br><span class="gold-text">ELEGANCE</span></h1>
<p class="hero-sub" data-i18n="hero-sub">My Elegance — Montres de luxe authentiques au meilleur prix. Découvrez l\'élégance à chaque seconde.</p>
<div class="hero-actions">
<a href="#shop" class="btn btn-gold" data-i18n="hero-cta1">Explorer</a>
<a href="#contact-us" class="btn btn-outline" data-i18n="hero-cta2">Nous Contacter</a>
</div>'''
    html = html[:hero_badge] + new_hero_block + html[old_end:]

# ===== MARQUEE =====
html = html.replace('BODYGLAD', 'MY ELEGANCE')

# ===== Remove Schedule section =====
sched_start = html.find('<!-- Schedule -->')
sched_end = html.find('<!-- About -->', sched_start)
if sched_start > 0 and sched_end > 0:
    html = html[:sched_start] + html[sched_end:]

# ===== ABOUT section =====
about_start = html.find('<!-- About -->')
about_end = html.find('<!-- Memberships -->')
if about_start > 0 and about_end > 0:
    new_about = '''<!-- About -->
<section class="section" id="about"><div class="container">
<h2 class="section-title"><span class="gradient-text" data-i18n="about-title">POURQUOI MY ELEGANCE</span></h2>
<p class="section-subtitle" data-i18n="about-sub">Ce qui fait de nous le meilleur choix</p>
<div class="features-grid">
<div class="card-wrap"><div class="feature-card card-inner">
<span class="fi">\u231a</span>
<h4 data-i18n="about-f1-title">Montres Authentiques</h4>
<p data-i18n="about-f1-text">Des pièces d'exception sélectionnées parmi les meilleures marques mondiales. Authenticité garantie.</p>
</div></div>
<div class="card-wrap"><div class="feature-card card-inner">
<span class="fi">\U0001f48e</span>
<h4 data-i18n="about-f2-title">Qualité Premium</h4>
<p data-i18n="about-f2-text">Mouvements suisses et japonais, matériaux nobles : acier inoxydable, cuir véritable, verre saphir.</p>
</div></div>
<div class="card-wrap"><div class="feature-card card-inner">
<span class="fi">\U0001f69a</span>
<h4 data-i18n="about-f3-title">Livraison Nationale</h4>
<p data-i18n="about-f3-text">Livraison rapide et sécurisée dans toute l'Algérie. Suivi de commande en temps réel.</p>
</div></div>
<div class="card-wrap"><div class="feature-card card-inner">
<span class="fi">\U0001f512</span>
<h4 data-i18n="about-f4-title">Paiement Sécurisé</h4>
<p data-i18n="about-f4-text">Paiement à la livraison ou par carte bancaire. Vos informations sont protégées.</p>
</div></div>
<div class="card-wrap"><div class="feature-card card-inner">
<span class="fi">\U0001f4de</span>
<h4 data-i18n="about-f5-title">Service Client</h4>
<p data-i18n="about-f5-text">Une équipe dédiée à votre écoute pour vous conseiller et vous accompagner dans votre choix.</p>
</div></div>
</div>
</div>
</section>'''
    html = html[:about_start] + new_about + html[about_end:]

# ===== Remove Memberships section =====
memb_start = html.find('<!-- Memberships -->')
memb_end = html.find('<!-- Shop -->')
if memb_start > 0 and memb_end > 0:
    html = html[:memb_start] + html[memb_end:]

# ===== SHOP =====
shop_start = html.find('<!-- Shop -->')
shop_end = html.find('<!-- Gallery -->')
if shop_start > 0 and shop_end > 0:
    new_shop = '''<!-- Shop -->
<section class="section" id="shop">
<div class="container">
<h2 class="section-title"><span class="gradient-text" data-i18n="products-title">MY ELEGANCE SHOP</span></h2>
<p class="section-subtitle" data-i18n="products-sub">Découvrez notre collection de montres</p>
<div class="products-grid">
<div class="product-card"><img src="assets/images/watches/classic-chrono.jpg" alt="Classic Chronograph" loading="lazy"><div class="product-info"><div class="p-name">Classic Chronograph</div><div class="p-price">45,000 DA</div><button class="p-add" onclick="addToCart(1)" data-i18n="prod-add">Add to Cart</button></div></div>
<div class="product-card"><img src="assets/images/watches/elegance-gold.jpg" alt="Elegance Gold" loading="lazy"><div class="product-info"><div class="p-name">Elegance Gold</div><div class="p-price">68,000 DA</div><button class="p-add" onclick="addToCart(2)" data-i18n="prod-add">Add to Cart</button></div></div>
<div class="product-card"><img src="assets/images/watches/sport-pro.jpg" alt="Sport Pro" loading="lazy"><div class="product-info"><div class="p-name">Sport Pro</div><div class="p-price">32,000 DA</div><button class="p-add" onclick="addToCart(3)" data-i18n="prod-add">Add to Cart</button></div></div>
<div class="product-card"><img src="assets/images/watches/diamond-series.jpg" alt="Diamond Series" loading="lazy"><div class="product-info"><div class="p-name">Diamond Series</div><div class="p-price">120,000 DA</div><button class="p-add" onclick="addToCart(4)" data-i18n="prod-add">Add to Cart</button></div></div>
<div class="product-card"><img src="assets/images/watches/minimalist-black.jpg" alt="Minimalist Black" loading="lazy"><div class="product-info"><div class="p-name">Minimalist Black</div><div class="p-price">25,000 DA</div><button class="p-add" onclick="addToCart(5)" data-i18n="prod-add">Add to Cart</button></div></div>
<div class="product-card"><img src="assets/images/watches/ocean-blue.jpg" alt="Ocean Blue Diver" loading="lazy"><div class="product-info"><div class="p-name">Ocean Blue Diver</div><div class="p-price">55,000 DA</div><button class="p-add" onclick="addToCart(6)" data-i18n="prod-add">Add to Cart</button></div></div>
<div class="product-card"><img src="assets/images/watches/heritage-auto.jpg" alt="Heritage Automatic" loading="lazy"><div class="product-info"><div class="p-name">Heritage Automatic</div><div class="p-price">89,000 DA</div><button class="p-add" onclick="addToCart(7)" data-i18n="prod-add">Add to Cart</button></div></div>
<div class="product-card"><img src="assets/images/watches/urban-steel.jpg" alt="Urban Steel" loading="lazy"><div class="product-info"><div class="p-name">Urban Steel</div><div class="p-price">38,000 DA</div><button class="p-add" onclick="addToCart(8)" data-i18n="prod-add">Add to Cart</button></div></div>
<div class="product-card"><img src="assets/images/watches/rose-gold.jpg" alt="Rose Gold Lady" loading="lazy"><div class="product-info"><div class="p-name">Rose Gold Lady</div><div class="p-price">72,000 DA</div><button class="p-add" onclick="addToCart(9)" data-i18n="prod-add">Add to Cart</button></div></div>
<div class="product-card"><img src="assets/images/watches/carbon-fiber.jpg" alt="Carbon Fiber X" loading="lazy"><div class="product-info"><div class="p-name">Carbon Fiber X</div><div class="p-price">95,000 DA</div><button class="p-add" onclick="addToCart(10)" data-i18n="prod-add">Add to Cart</button></div></div>
</div>
</div>
</section>'''
    html = html[:shop_start] + new_shop + html[shop_end:]

# ===== GALLERY =====
html = html.replace(
    'data-i18n="gallery-sub">Découvrez notre espace',
    'data-i18n="gallery-sub">Découvrez notre collection'
)

# ===== Remove Coaches section & Modal =====
coach_start = html.find('<!-- Coaches - FC Style -->')
coach_end = html.find('<!-- Trainer Highlight Modal -->')
if coach_start > 0 and coach_end > 0:
    trainer_modal_start = coach_end
    trainer_modal_end = html.find('<!-- Gallery Lightbox -->', trainer_modal_start)
    if trainer_modal_end > 0:
        html = html[:coach_start] + html[trainer_modal_end:]

# ===== Remove Workout Programs =====
wo_start = html.find('<!-- Workout Programs -->')
wo_end = html.find('<!-- Testimonials -->')
if wo_start > 0 and wo_end > 0:
    html = html[:wo_start] + html[wo_end:]

# ===== TESTIMONIALS =====
test_start = html.find('<!-- Testimonials -->')
test_end = html.find('<!-- FAQs -->')
if test_start > 0 and test_end > 0:
    new_test = '''<!-- Testimonials -->
<section class="section" id="testimonials">
<div class="container">
<h2 class="section-title"><span class="gradient-text" data-i18n="testimonials-title">Témoignages</span></h2>
<p class="section-subtitle" data-i18n="testimonials-sub">Ce que nos clients disent de nous</p>
<div class="testimonials-grid">
<div class="card-wrap"><div class="testimonial-card card-inner">
<div class="quote">"</div>
<p data-i18n="testimonial1-text">J\'ai acheté ma montre Classic Chronograph chez My Elegance. Service impeccable, montre authentique et livraison rapide. Je recommande vivement !</p>
<div class="author">
<div class="author-avatar">MK</div>
<div class="author-info"><strong>Mohamed K.</strong><span data-i18n="testimonial1-info">Client satisfait</span></div>
</div>
</div></div>
<div class="card-wrap"><div class="testimonial-card card-inner">
<div class="quote">"</div>
<p data-i18n="testimonial2-text">Une collection magnifique et un service client exceptionnel. Ma montre Elegance Gold est encore plus belle en vrai. Merci My Elegance !</p>
<div class="author">
<div class="author-avatar">SF</div>
<div class="author-info"><strong>Sofia F.</strong><span data-i18n="testimonial2-info">Cliente fidèle</span></div>
</div>
</div></div>
<div class="card-wrap"><div class="testimonial-card card-inner">
<div class="quote">"</div>
<p data-i18n="testimonial3-text">J\'ai offert une montre Heritage Automatic à mon père. Qualité extraordinaire et élégance intemporelle. Le meilleur rapport qualité-prix en Algérie.</p>
<div class="author">
<div class="author-avatar">AB</div>
<div class="author-info"><strong>Amine B.</strong><span data-i18n="testimonial3-info">Client depuis 2025</span></div>
</div>
</div></div>
</div>
</div>
</section>'''
    html = html[:test_start] + new_test + html[test_end:]

# ===== FAQ =====
faq_start = html.find('<!-- FAQs -->')
faq_end = html.find('<!-- Instagram -->')
if faq_start > 0 and faq_end > 0:
    new_faq = '''<!-- FAQs -->
<section class="section" id="faq">
<div class="container">
<h2 class="section-title"><span class="gradient-text" data-i18n="faq-title">FAQs</span></h2>
<p class="section-subtitle" data-i18n="faq-sub">Questions fréquemment posées</p>
<div class="faq-list">
<div class="faq-item">
<button type="button" class="faq-q" onclick="toggleFaq(this)"><span data-i18n="faq1-q">Quels sont les délais de livraison ?</span><span class="icon-text">▼</span></button>
<div class="faq-a" data-i18n="faq1-a">Nous livrons partout en Algérie sous 2 à 5 jours ouvrés. Les grandes villes (Alger, Oran, Constantine) sont desservies sous 24-48h. Livraison gratuite pour les commandes de plus de 50,000 DA.</div>
</div>
<div class="faq-item">
<button type="button" class="faq-q" onclick="toggleFaq(this)"><span data-i18n="faq2-q">Les montres sont-elles authentiques ?</span><span class="icon-text">▼</span></button>
<div class="faq-a" data-i18n="faq2-a">Absolument ! Toutes nos montres sont 100% authentiques et garanties. Nous travaillons directement avec les fabricants et distributeurs agréés. Chaque montre est livrée avec sa boîte d'origine et sa carte de garantie.</div>
</div>
<div class="faq-item">
<button type="button" class="faq-q" onclick="toggleFaq(this)"><span data-i18n="faq3-q">Puis-je retourner ma montre ?</span><span class="icon-text">▼</span></button>
<div class="faq-a" data-i18n="faq3-a">Oui, vous disposez de 14 jours pour retourner votre montre si elle ne vous convient pas. La montre doit être dans son état d'origine, non portée, avec tous ses accessoires. Le remboursement est effectué sous 72h.</div>
</div>
<div class="faq-item">
<button type="button" class="faq-q" onclick="toggleFaq(this)"><span data-i18n="faq4-q">Proposez-vous la gravure ?</span><span class="icon-text">▼</span></button>
<div class="faq-a" data-i18n="faq4-a">Oui, nous proposons un service de gravure personnalisée sur certaines montres sélectionnées. Contactez-nous pour plus d'informations sur les modèles éligibles et les tarifs.</div>
</div>
</div>
</div>
</section>'''
    html = html[:faq_start] + new_faq + html[faq_end:]

# ===== INSTAGRAM / SOCIAL =====
insta_start = html.find('<!-- Instagram -->')
insta_end = html.find('<!-- Contact Section -->')
if insta_start > 0 and insta_end > 0:
    new_insta = '''<!-- Instagram -->
<section class="section instagram-section" id="social">
<div class="container">
<h2 class="section-title"><span class="gradient-text">@myelegance_dz</span></h2>
<p class="section-subtitle" data-i18n="insta-sub">Suivez-nous sur Instagram pour découvrir nos dernières collections</p>
<div class="card-wrap social-wrap">
<a href="https://instagram.com/myelegance_dz" target="_blank" rel="noopener noreferrer" class="instagram-card card-inner">
<div class="instagram-avatar"><span style="font-size:1.5rem">\U0001f48e</span></div>
<div class="instagram-info">
<h3>@myelegance_dz</h3>
<p data-i18n="insta-followers">Suivez-nous sur Instagram</p>
<span class="btn btn-gold btn-sm" data-i18n="insta-btn">Suivre</span>
</div>
</a>
<a href="https://facebook.com/myelegance.dz" target="_blank" rel="noopener noreferrer" class="instagram-card card-inner">
<div class="instagram-avatar"><span style="font-size:1.5rem">\u231a</span></div>
<div class="instagram-info">
<h3>My Elegance</h3>
<p>Facebook</p>
<span class="btn btn-gold btn-sm">Suivre</span>
</div>
</a>
</div>
</div>
</section>'''
    html = html[:insta_start] + new_insta + html[insta_end:]

# ===== CONTACT =====
contact_start = html.find('<!-- Contact Section -->')
contact_end = html.find('</div>\n\n<div id="schedule-page"')
if contact_start > 0 and contact_end > 0:
    new_contact = '''<!-- Contact Section -->
<section class="section" id="contact-us">
<div class="container">
<h2 class="section-title"><span class="gradient-text" data-i18n="contact-title">CONTACT</span></h2>
<p class="section-subtitle" data-i18n="contact-sub">Prenez contact avec nous</p>
<div class="contact-grid">
<div class="card-wrap"><div class="contact-card card-inner">
<span class="ci">\U0001f4cd</span>
<div><h4 data-i18n="contact-address-title">Adresse</h4>
<p>Alger, Algérie</p></div>
</div></div>
<div class="card-wrap"><div class="contact-card card-inner">
<span class="ci">\U0001f4de</span>
<div><h4 data-i18n="contact-phone-title">Téléphone</h4>
<a href="tel:0554672222">0554 67 22 22</a></div>
</div></div>
<div class="card-wrap"><div class="contact-card card-inner">
<span class="ci">\u2709\ufe0f</span>
<div><h4 data-i18n="contact-email-title">Email</h4>
<a href="mailto:contact@myelegance.dz">contact@myelegance.dz</a></div>
</div></div>
<div class="card-wrap"><div class="contact-card card-inner">
<span class="ci">\U0001f550</span>
<div><h4 data-i18n="contact-hours-title">Horaires</h4>
<p data-i18n="contact-hours-text">Sam-Jeu 9h-18h · Ven 14h-18h</p></div>
</div></div>
</div>
</div>
</section>'''
    html = html[:contact_start] + new_contact + html[contact_end:]

# ===== PAGE DIVS =====
old_pages = '<div id="schedule-page" class="page"></div>\n<div id="about-page" class="page"></div>\n<div id="memberships-page" class="page"></div>\n<div id="shop-page" class="page"></div>\n<div id="gallery-page" class="page"></div>\n<div id="coaches-page" class="page"></div>\n<div id="workout-page" class="page"></div>\n<div id="testimonials-page" class="page"></div>\n<div id="faq-page" class="page"></div>\n<div id="social-page" class="page"></div>\n<div id="contact-us-page" class="page"></div>'
new_pages = '<div id="about-page" class="page"></div>\n<div id="shop-page" class="page"></div>\n<div id="gallery-page" class="page"></div>\n<div id="testimonials-page" class="page"></div>\n<div id="faq-page" class="page"></div>\n<div id="social-page" class="page"></div>\n<div id="contact-us-page" class="page"></div>'
html = html.replace(old_pages, new_pages)

# ===== FOOTER =====
html = html.replace(
    '<h4>BodyGlad</h4>\n<p data-i18n="footer-desc">N°1 Fitness à Alger. Rejoignez la communauté qui vous fait progresser.</p>',
    '<h4>My Elegance</h4>\n<p data-i18n="footer-desc">Montres de luxe en Algérie. Découvrez l\'élégance à chaque seconde.</p>'
)

footer_links_old = '<a href="#about" data-i18n="nav-about">About</a>\n<a href="#schedule" data-i18n="nav-schedule">Schedule</a>\n<a href="#memberships" data-i18n="nav-memberships">Memberships</a>\n<a href="#shop" data-i18n="nav-shop">Shop</a>\n<a href="#gallery" data-i18n="nav-gallery">Gallery</a>\n<a href="#coaches" data-i18n="nav-coaches">Coaches</a>\n<a href="#workout" data-i18n="nav-programs">Programs</a>\n<a href="#contact-us" data-i18n="nav-contact">Contact</a>'
footer_links_new = '<a href="#home" data-i18n="nav-home">Home</a>\n<a href="#about" data-i18n="nav-about">About</a>\n<a href="#shop" data-i18n="nav-shop">Shop</a>\n<a href="#gallery" data-i18n="nav-gallery">Gallery</a>\n<a href="#contact-us" data-i18n="nav-contact">Contact</a>\n<a href="#faq" data-i18n="nav-faq">FAQ</a>'
html = html.replace(footer_links_old, footer_links_new)

html = html.replace(
    '<a href="tel:0554672222">0554 67 22 22</a>\n<a href="mailto:bodyglad@gmail.com">bodyglad@gmail.com</a>\n<p>Chéraga, vers GARDEN CITY</p>',
    '<a href="tel:0554672222">0554 67 22 22</a>\n<a href="mailto:contact@myelegance.dz">contact@myelegance.dz</a>\n<p>Alger, Algérie</p>'
)

html = html.replace(
    '<a href="https://instagram.com/body_glad" target="_blank" rel="noopener noreferrer">Instagram</a>\n<a href="https://www.facebook.com/BODY-GLAD-FITNESS-471483903388830" target="_blank" rel="noopener noreferrer">Facebook</a>',
    '<a href="https://instagram.com/myelegance_dz" target="_blank" rel="noopener noreferrer">Instagram</a>\n<a href="https://facebook.com/myelegance.dz" target="_blank" rel="noopener noreferrer">Facebook</a>'
)

html = html.replace('&copy; 2026 BodyGlad.', '&copy; 2026 My Elegance.')

# ===== FAB BUTTONS =====
old_fab = '''<button class="fab-btn" onclick="showPage('schedule')" data-i18n="fab-schedule">Schedule</button>
<button class="fab-btn" onclick="showPage('about')" data-i18n="fab-about">About</button>
<button class="fab-btn" onclick="showPage('memberships')" data-i18n="fab-memberships">Memberships</button>
<button class="fab-btn" onclick="showPage('shop')" data-i18n="nav-shop">Shop</button>
<button class="fab-btn" onclick="showPage('gallery')" data-i18n="fab-gallery">Gallery</button>
<button class="fab-btn" onclick="showPage('coaches')" data-i18n="fab-coaches">Coaches</button>
<button class="fab-btn" onclick="showPage('contact-us')" data-i18n="fab-contact">Contact</button>'''
new_fab = '''<button class="fab-btn" onclick="showPage('about')" data-i18n="fab-about">About</button>
<button class="fab-btn" onclick="showPage('shop')" data-i18n="nav-shop">Shop</button>
<button class="fab-btn" onclick="showPage('gallery')" data-i18n="fab-gallery">Gallery</button>
<button class="fab-btn" onclick="showPage('contact-us')" data-i18n="fab-contact">Contact</button>
<button class="fab-btn" onclick="showPage('faq')" data-i18n="fab-faq">FAQ</button>'''
html = html.replace(old_fab, new_fab)

# ===== JS: PAGE_IDS =====
html = html.replace(
    "const PAGE_IDS = ['schedule','memberships','shop','gallery','coaches','workout','about','testimonials','faq','social','contact-us'];",
    "const PAGE_IDS = ['shop','gallery','about','testimonials','faq','social','contact-us'];"
)

# ===== JS: pageMap =====
html = html.replace(
    "const pageMap={'about':1,'schedule':1,'memberships':1,'shop':1,'gallery':1,'coaches':1,'workout':1,'testimonials':1,'faq':1,'social':1,'contact-us':1,'home':1};",
    "const pageMap={'about':1,'shop':1,'gallery':1,'testimonials':1,'faq':1,'social':1,'contact-us':1,'home':1};"
)

# ===== JS: LOCALSTORAGE KEYS =====
html = html.replace("localStorage.getItem('bg_cart'", "localStorage.getItem('me_cart'")
html = html.replace("localStorage.setItem('bg_cart'", "localStorage.setItem('me_cart'")
html = html.replace("localStorage.getItem('bg_lang'", "localStorage.getItem('me_lang'")
html = html.replace("localStorage.setItem('bg_lang'", "localStorage.setItem('me_lang'")

# ===== JS: EMAIL KEY =====
html = html.replace("h.value='bg2024'", "h.value='myelegance2024'")

# ===== JS: PRODUCTS =====
old_products_start = html.find("const products = {")
old_products_end = html.find("// ========== YALIDINE DELIVERY")
if old_products_start > 0 and old_products_end > 0:
    new_products = '''const products = {
  1:{name:'Classic Chronograph',price:45000,img:'assets/images/watches/classic-chrono.jpg'},
  2:{name:'Elegance Gold',price:68000,img:'assets/images/watches/elegance-gold.jpg'},
  3:{name:'Sport Pro',price:32000,img:'assets/images/watches/sport-pro.jpg'},
  4:{name:'Diamond Series',price:120000,img:'assets/images/watches/diamond-series.jpg'},
  5:{name:'Minimalist Black',price:25000,img:'assets/images/watches/minimalist-black.jpg'},
  6:{name:'Ocean Blue Diver',price:55000,img:'assets/images/watches/ocean-blue-diver.jpg'},
  7:{name:'Heritage Automatic',price:89000,img:'assets/images/watches/heritage-auto.jpg'},
  8:{name:'Urban Steel',price:38000,img:'assets/images/watches/urban-steel.jpg'},
  9:{name:'Rose Gold Lady',price:72000,img:'assets/images/watches/rose-gold.jpg'},
  10:{name:'Carbon Fiber X',price:95000,img:'assets/images/watches/carbon-fiber.jpg'}
};

// ========== YALIDINE DELIVERY'''
    html = html[:old_products_start] + new_products + html[old_products_end:]

# ===== REMOVE WORKOUT JS =====
wo_js_start = html.find("// ========== WORKOUT GENERATOR")
wo_js_end = html.find("// ========== LANGUAGE")
if wo_js_start > 0 and wo_js_end > 0:
    html = html[:wo_js_start] + html[wo_js_end:]

# ===== REMOVE Workout Params Preview =====
wp_start = html.find("// ========== Workout Params Preview")
wp_end = html.find("// ========== Trainer Modal")
if wp_start > 0 and wp_end > 0:
    html = html[:wp_start] + html[wp_end:]

# ===== REMOVE Trainer Modal =====
tm_start = html.find("// ========== Trainer Modal")
tm_end = html.find("// ========== Schedule Tabs")
if tm_start > 0 and tm_end > 0:
    html = html[:tm_start] + html[tm_end:]

# ===== REMOVE Schedule Tabs =====
st_start = html.find("// ========== Schedule Tabs")
st_end = html.find("// ========== INIT")
if st_start > 0 and st_end > 0:
    html = html[:st_start] + html[st_end:]

# ===== UPDATE scroll animation selectors =====
html = html.replace(
    "document.querySelectorAll('.info-card,.membership-card,.trainer-card,.testimonial-card,.faq-item,.instagram-card,.feature-card,.contact-card,.gallery-item,.schedule-card,.workout-builder,.product-card')",
    "document.querySelectorAll('.info-card,.testimonial-card,.faq-item,.instagram-card,.feature-card,.contact-card,.gallery-item,.product-card')"
)

# ===== CLEAN UP CSS: remove Workout Builder CSS =====
wo_css_start = html.find("/* Workout Builder */")
wo_css_end = html.find("/* Shop */")
if wo_css_start > 0 and wo_css_end > 0:
    html = html[:wo_css_start] + html[wo_css_end:]

# ===== CLEAN UP CSS: remove schedule/coach CSS =====
# Remove "/* Schedule Cards */" through the next section
sched_css_start = html.find("/* Schedule Cards */")
sched_css_end = html.find("/* About Features */")
if sched_css_start > 0 and sched_css_end > 0:
    html = html[:sched_css_start] + html[sched_css_end:]

# Remove coaches CSS
coaches_css_start = html.find("/* Coaches - FC Style */")
coaches_css_end = html.find("/* About Features */")
if coaches_css_start > 0 and coaches_css_end > 0:
    html = html[:coaches_css_start] + html[coaches_css_end:]

# Remove "/* Schedule Tabs */" block
sched_tabs_start = html.find("/* Schedule Tabs */")
sched_tabs_end = html.find("/* Gallery */")
if sched_tabs_start > 0 and sched_tabs_end > 0:
    html = html[:sched_tabs_start] + html[sched_tabs_end:]

# ===== REMOVE Memberships CSS =====
memb_css_start = html.find("/* Memberships */")
memb_css_end = html.find("/* Responsive */")
if memb_css_start > 0 and memb_css_end > 0:
    html = html[:memb_css_start] + html[memb_css_end:]

# ===== WRITE =====
with open(r'C:\Users\n1\AppData\Local\Temp\opencode\my-elegance\index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("HTML transformation complete!")
