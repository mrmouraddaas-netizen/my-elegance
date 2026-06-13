# My Elegance — Watches Store

## Brand
- **Name**: My Elegance
- **Tagline**: Montres de Luxe en Algérie / Luxury Watches in Algeria
- **Colors**: Black (`#0a0a0a`) + Gold (`#D4AF37`)
- **Logo**: `assets/images/logo.jpg`
- **Currency**: DZD (د.ج)
- **Languages**: EN, FR, AR

## Products
10 luxury watches stored in `assets/images/watches/` with placeholder images. Replace with actual product photos.

## Delivery
Yalidine pricing zones (Stop Desk + Home Delivery across all 58 wilayas). Fee auto-calculated in checkout.

## Email Notifications
- **Google Apps Script URL**: `https://script.google.com/macros/s/AKfycbyiXRCyY5U-rwq4lILdD4oMULid1uB5UjHTTm5Lz9WZ4OaoUS0rFAo7wSi-yzpjOXR3/exec`
- **Secret Key**: `myelegance2024`
- Sends name, phone, wilaya, deliveryType, deliveryFee, address, items, total

## Sections
- Hero, About, Shop (10 watches), Gallery, Testimonials, FAQ, Contact, Social
- **Removed**: Schedule, Memberships, Workout Builder, Coaches (fitness-specific)

## To Deploy
1. Upload all files to a web server or GitHub Pages
2. Deploy the Google Apps Script (in `email-gas.txt`) and update the URL in `index.html`
3. Replace placeholder watch images with real product photos
4. Update contact info, social links, and any pricing
