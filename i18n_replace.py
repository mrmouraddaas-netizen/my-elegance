import re

with open(r'C:\Users\n1\AppData\Local\Temp\opencode\my-elegance\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find the i18n section
lang_start = html.find('// ========== LANGUAGE ==========')
lang_obj_start = html.find('const i18n={', lang_start)
lang_obj_end = html.find('function setLang(lang)', lang_obj_start)

# The i18n object ends with "};" before setLang - the "};" line
# Find the last "};" before setLang
search_from = lang_obj_end - 100
closing = html.rfind('};', search_from, lang_obj_end)
# Move to end of that line
closing_end = closing + 2

print(f"lang_start={lang_start}, obj_start={lang_obj_start}, closing_at={closing}, setLang_at={lang_obj_end}")

new_i18n = '''const i18n={
  en:{
    promo:'\U0001f48e Luxury Watches Algeria | \U0001f4de 0554 67 22 22 | \U0001f69a Delivery nationwide',
    'nav-home':'Home','nav-about':'About','nav-shop':'Shop','nav-gallery':'Gallery','nav-contact':'Contact','nav-testimonials':'Testimonials','nav-faq':'FAQ',
    'products-title':'MY ELEGANCE SHOP','products-sub':'Discover our watch collection','prod-add':'Add to Cart',
    'fab-about':'About','fab-gallery':'Gallery','fab-contact':'Contact','fab-faq':'FAQ',
    'hero-badge':'\u2728 Luxury Watches','hero-title':'TIME IS<br><span class="gold-text">ELEGANCE</span>',
    'hero-sub':'My Elegance — Authentic luxury watches at the best prices. Discover elegance at every second.',
    'hero-cta1':'Explore','hero-cta2':'Contact Us',
    'about-title':'WHY MY ELEGANCE','about-sub':'What makes us the best choice',
    'about-f1-title':'Authentic Watches','about-f1-text':'Exceptional timepieces selected from the world\'s finest brands. Authenticity guaranteed.',
    'about-f2-title':'Premium Quality','about-f2-text':'Swiss and Japanese movements, noble materials: stainless steel, genuine leather, sapphire crystal.',
    'about-f3-title':'Nationwide Delivery','about-f3-text':'Fast and secure delivery across Algeria. Real-time order tracking.',
    'about-f4-title':'Secure Payment','about-f4-text':'Pay on delivery or by card. Your information is protected.',
    'about-f5-title':'Customer Service','about-f5-text':'A dedicated team to advise and support you in your choice.',
    'gallery-title':'GALLERY','gallery-sub':'Discover our collection',
    'contact-title':'CONTACT','contact-sub':'Get in touch with us',
    'contact-address-title':'Address','contact-phone-title':'Phone','contact-email-title':'Email','contact-hours-title':'Hours','contact-hours-text':'Sat-Thu 9AM-6PM · Fri 2PM-6PM',
    'testimonials-title':'Testimonials','testimonials-sub':'What our customers say about us',
    'testimonial1-text':'I bought my Classic Chronograph at My Elegance. Impeccable service, authentic watch and fast delivery. Highly recommend!',
    'testimonial1-info':'Satisfied customer',
    'testimonial2-text':'A magnificent collection and exceptional customer service. My Elegance Gold is even more beautiful in person. Thank you My Elegance!',
    'testimonial2-info':'Loyal customer',
    'testimonial3-text':'I gifted a Heritage Automatic to my father. Extraordinary quality and timeless elegance. Best value in Algeria.',
    'testimonial3-info':'Customer since 2025',
    'faq-title':'FAQs','faq-sub':'Frequently asked questions',
    'faq1-q':'What are the delivery times?','faq1-a':'We deliver across Algeria within 2-5 business days. Major cities (Algiers, Oran, Constantine) within 24-48h. Free delivery for orders over 50,000 DA.',
    'faq2-q':'Are the watches authentic?','faq2-a':'Absolutely! All our watches are 100% authentic and guaranteed. We work directly with manufacturers and authorized distributors. Each watch comes with its original box and warranty card.',
    'faq3-q':'Can I return my watch?','faq3-a':'Yes, you have 14 days to return your watch if it does not suit you. The watch must be in its original condition, unworn, with all accessories. Refund within 72h.',
    'faq4-q':'Do you offer engraving?','faq4-a':'Yes, we offer personalized engraving on selected watches. Contact us for more information on eligible models and pricing.',
    'insta-sub':'Follow us on Instagram to discover our latest collections','insta-followers':'Follow us on Instagram','insta-btn':'Follow',
    'footer-desc':'Luxury watches in Algeria. Discover elegance at every second.',
    'footer-links-title':'Links','footer-contact-title':'Contact','footer-social-title':'Follow Us','footer-rights':'All rights reserved.',
    'cart-title':'Your Cart','cart-empty':'Your cart is empty','cart-total':'Total','cart-checkout':'Order Now',
    'checkout-title':'Delivery Information','checkout-name':'Full Name','checkout-phone':'Phone','checkout-wilaya':'Wilaya','checkout-delivery-type':'Delivery Type','delivery-stop-desk':'Stop Desk (Pickup point)','delivery-home':'Home Delivery','delivery-cost-label':'Delivery fee','checkout-address':'Full Address','checkout-submit':'Confirm Order','checkout-back':'Back to cart',
    'delivery-fee':'Delivery','cart-grand-total':'Total with delivery',
    'success-title':'Order Sent!','success-text':'Thank you! Your order has been sent. We will contact you shortly.','success-close':'Close'
  },
  fr:{
    promo:'\U0001f48e Montres de Luxe Algérie | \U0001f4de 0554 67 22 22 | \U0001f69a Livraison partout en Algérie',
    'nav-home':'Accueil','nav-about':'À propos','nav-shop':'Boutique','nav-gallery':'Galerie','nav-contact':'Contact','nav-testimonials':'Témoignages','nav-faq':'FAQ',
    'products-title':'MY ELEGANCE SHOP','products-sub':'Découvrez notre collection de montres','prod-add':'Ajouter au panier',
    'fab-about':'À propos','fab-gallery':'Galerie','fab-contact':'Contact','fab-faq':'FAQ',
    'hero-badge':'\u2728 Montres de Luxe','hero-title':'LE TEMPS<br><span class="gold-text">EST ÉLÉGANCE</span>',
    'hero-sub':'My Elegance — Montres de luxe authentiques au meilleur prix. Découvrez l\'élégance à chaque seconde.',
    'hero-cta1':'Explorer','hero-cta2':'Nous Contacter',
    'about-title':'POURQUOI MY ELEGANCE','about-sub':'Ce qui fait de nous le meilleur choix',
    'about-f1-title':'Montres Authentiques','about-f1-text':'Des pièces d\'exception sélectionnées parmi les meilleures marques mondiales. Authenticité garantie.',
    'about-f2-title':'Qualité Premium','about-f2-text':'Mouvements suisses et japonais, matériaux nobles : acier inoxydable, cuir véritable, verre saphir.',
    'about-f3-title':'Livraison Nationale','about-f3-text':'Livraison rapide et sécurisée dans toute l\'Algérie. Suivi de commande en temps réel.',
    'about-f4-title':'Paiement Sécurisé','about-f4-text':'Paiement à la livraison ou par carte bancaire. Vos informations sont protégées.',
    'about-f5-title':'Service Client','about-f5-text':'Une équipe dédiée à votre écoute pour vous conseiller et vous accompagner dans votre choix.',
    'gallery-title':'GALERIE','gallery-sub':'Découvrez notre collection',
    'contact-title':'CONTACT','contact-sub':'Prenez contact avec nous',
    'contact-address-title':'Adresse','contact-phone-title':'Téléphone','contact-email-title':'Email','contact-hours-title':'Horaires','contact-hours-text':'Sam-Jeu 9h-18h · Ven 14h-18h',
    'testimonials-title':'Témoignages','testimonials-sub':'Ce que nos clients disent de nous',
    'testimonial1-text':'J\'ai acheté ma montre Classic Chronograph chez My Elegance. Service impeccable, montre authentique et livraison rapide. Je recommande vivement !',
    'testimonial1-info':'Client satisfait',
    'testimonial2-text':'Une collection magnifique et un service client exceptionnel. Ma montre Elegance Gold est encore plus belle en vrai. Merci My Elegance !',
    'testimonial2-info':'Cliente fidèle',
    'testimonial3-text':'J\'ai offert une montre Heritage Automatic à mon père. Qualité extraordinaire et élégance intemporelle. Le meilleur rapport qualité-prix en Algérie.',
    'testimonial3-info':'Client depuis 2025',
    'faq-title':'FAQs','faq-sub':'Questions fréquemment posées',
    'faq1-q':'Quels sont les délais de livraison ?','faq1-a':'Nous livrons partout en Algérie sous 2 à 5 jours ouvrés. Les grandes villes (Alger, Oran, Constantine) sont desservies sous 24-48h. Livraison gratuite pour les commandes de plus de 50,000 DA.',
    'faq2-q':'Les montres sont-elles authentiques ?','faq2-a':'Absolument ! Toutes nos montres sont 100% authentiques et garanties. Nous travaillons directement avec les fabricants et distributeurs agréés. Chaque montre est livrée avec sa boîte d\'origine et sa carte de garantie.',
    'faq3-q':'Puis-je retourner ma montre ?','faq3-a':'Oui, vous disposez de 14 jours pour retourner votre montre si elle ne vous convient pas. La montre doit être dans son état d\'origine, non portée, avec tous ses accessoires. Le remboursement est effectué sous 72h.',
    'faq4-q':'Proposez-vous la gravure ?','faq4-a':'Oui, nous proposons un service de gravure personnalisée sur certaines montres sélectionnées. Contactez-nous pour plus d\'informations sur les modèles éligibles et les tarifs.',
    'insta-sub':'Suivez-nous sur Instagram pour découvrir nos dernières collections','insta-followers':'Suivez-nous sur Instagram','insta-btn':'Suivre',
    'footer-desc':'Montres de luxe en Algérie. Découvrez l\'élégance à chaque seconde.',
    'footer-links-title':'Liens','footer-contact-title':'Contact','footer-social-title':'Suivez-nous','footer-rights':'Tous droits réservés.',
    'cart-title':'Votre Panier','cart-empty':'Votre panier est vide','cart-total':'Total','cart-checkout':'Commander',
    'checkout-title':'Informations de livraison','checkout-name':'Nom complet','checkout-phone':'Téléphone','checkout-wilaya':'Wilaya','checkout-delivery-type':'Type de livraison','delivery-stop-desk':'Stop Desk (Point relais)','delivery-home':'Livraison à domicile','delivery-cost-label':'Frais de livraison','checkout-address':'Adresse complète','checkout-submit':'Confirmer la commande','checkout-back':'Retour au panier',
    'delivery-fee':'Livraison','cart-grand-total':'Total avec livraison',
    'success-title':'Commande envoyée !','success-text':'Merci ! Votre commande a été envoyée. Nous vous contacterons dans les plus brefs délais.','success-close':'Fermer'
  },
  ar:{
    promo:'\U0001f48e ساعات فاخرة الجزائر | \U0001f4de 0554 67 22 22 | \U0001f69a توصيل إلى جميع أنحاء الجزائر',
    'nav-home':'الرئيسية','nav-about':'من نحن','nav-shop':'المتجر','nav-gallery':'المعرض','nav-contact':'اتصل بنا','nav-testimonials':'الشهادات','nav-faq':'الأسئلة الشائعة',
    'products-title':'متجر MY ELEGANCE','products-sub':'اكتشف مجموعتنا من الساعات','prod-add':'أضف إلى السلة',
    'fab-about':'من نحن','fab-gallery':'المعرض','fab-contact':'اتصل بنا','fab-faq':'الأسئلة الشائعة',
    'hero-badge':'\u2728 ساعات فاخرة','hero-title':'الوقت<br><span class="gold-text">أناقة</span>',
    'hero-sub':'My Elegance — ساعات فاخرة أصلية بأفضل الأسعار. اكتشف الأناقة في كل ثانية.',
    'hero-cta1':'استعرض','hero-cta2':'اتصل بنا',
    'about-title':'لماذا MY ELEGANCE','about-sub':'ما يجعلنا الخيار الأفضل',
    'about-f1-title':'ساعات أصلية','about-f1-text':'قطع استثنائية منتقاة من أفضل الماركات العالمية. الأصالة مضمونة.',
    'about-f2-title':'جودة ممتازة','about-f2-text':'حركات سويسرية ويابانية، مواد نبيلة: فولاذ مقاوم للصدأ، جلد أصلي، زجاج ياقوتي.',
    'about-f3-title':'توصيل وطني','about-f3-text':'توصيل سريع وآمن إلى جميع أنحاء الجزائر. تتبع الطلب في الوقت الفعلي.',
    'about-f4-title':'دفع آمن','about-f4-text':'الدفع عند الاستلام أو بالبطاقة المصرفية. معلوماتك محمية.',
    'about-f5-title':'خدمة العملاء','about-f5-text':'فريق متخصص تحت تصرفكم لإرشادكم ومساعدتكم في اختياركم.',
    'gallery-title':'المعرض','gallery-sub':'اكتشف مجموعتنا',
    'contact-title':'اتصل بنا','contact-sub':'تواصل معنا',
    'contact-address-title':'العنوان','contact-phone-title':'الهاتف','contact-email-title':'البريد الإلكتروني','contact-hours-title':'ساعات العمل','contact-hours-text':'السبت-الخميس 9ص-6م · الجمعة 2م-6م',
    'testimonials-title':'الشهادات','testimonials-sub':'ماذا يقول عملاؤنا عنا',
    'testimonial1-text':'اشتريت ساعتي Classic Chronograph من My Elegance. خدمة لا تشوبها شائبة، ساعة أصلية وتوصيل سريع. أوصي بشدة!',
    'testimonial1-info':'عميل راضٍ',
    'testimonial2-text':'مجموعة رائعة وخدمة عملاء استثنائية. ساعتي Elegance Gold أجمل في الواقع. شكراً My Elegance!',
    'testimonial2-info':'عميلة وفية',
    'testimonial3-text':'أهديت ساعة Heritage Automatic لوالدي. جودة استثنائية وأناقة خالدة. أفضل قيمة في الجزائر.',
    'testimonial3-info':'عميل منذ 2025',
    'faq-title':'الأسئلة الشائعة','faq-sub':'الأسئلة المتداولة',
    'faq1-q':'ما هي أوقات التوصيل؟','faq1-a':'نقوم بالتوصيل إلى جميع أنحاء الجزائر في غضون 2-5 أيام عمل. المدن الكبرى (الجزائر، وهران، قسنطينة) في غضون 24-48 ساعة. توصيل مجاني للطلبات التي تتجاوز 50,000 د.ج.',
    'faq2-q':'هل الساعات أصلية؟','faq2-a':'بالتأكيد! جميع ساعاتنا أصلية 100% ومضمونة. نعمل مباشرة مع المصنعين والموزعين المعتمدين. كل ساعة تأتي مع صندوقها الأصلي وبطاقة الضمان.',
    'faq3-q':'هل يمكنني إرجاع الساعة؟','faq3-a':'نعم، لديك 14 يوماً لإرجاع ساعتك إذا لم تناسبك. يجب أن تكون الساعة في حالتها الأصلية، غير مرتدية، مع جميع ملحقاتها. يتم الاسترداد خلال 72 ساعة.',
    'faq4-q':'هل تقدمون النقش؟','faq4-a':'نعم، نقدم خدمة النقش الشخصي على بعض الساعات المختارة. اتصل بنا لمزيد من المعلومات حول الموديلات المؤهلة والأسعار.',
    'insta-sub':'تابعنا على إنستغرام لاكتشاف أحدث مجموعاتنا','insta-followers':'تابعنا على إنستغرام','insta-btn':'تابع',
    'footer-desc':'ساعات فاخرة في الجزائر. اكتشف الأناقة في كل ثانية.',
    'footer-links-title':'روابط','footer-contact-title':'اتصل','footer-social-title':'تابعنا','footer-rights':'جميع الحقوق محفوظة.',
    'cart-title':'سلة التسوق','cart-empty':'سلة التسوق فارغة','cart-total':'المجموع','cart-checkout':'اطلب الآن',
    'checkout-title':'معلومات التوصيل','checkout-name':'الاسم الكامل','checkout-phone':'الهاتف','checkout-wilaya':'الولاية','checkout-delivery-type':'نوع التوصيل','delivery-stop-desk':'نقطة الاستلام (Stop Desk)','delivery-home':'توصيل إلى المنزل','delivery-cost-label':'رسوم التوصيل','checkout-address':'العنوان الكامل','checkout-submit':'تأكيد الطلب','checkout-back':'العودة إلى السلة',
    'delivery-fee':'التوصيل','cart-grand-total':'المجموع مع التوصيل',
    'success-title':'تم إرسال الطلب!','success-text':'شكراً! تم إرسال طلبك. سنتصل بك قريباً.','success-close':'إغلاق'
  }
};'''

# Replace the i18n object (from "const i18n={" to the matching "};" before setLang)
html = html[:lang_obj_start] + new_i18n + html[closing_end:]

with open(r'C:\Users\n1\AppData\Local\Temp\opencode\my-elegance\index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("i18n replacement complete!")
