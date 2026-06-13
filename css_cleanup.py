import re

with open(r'C:\Users\n1\AppData\Local\Temp\opencode\my-elegance\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Clean up unused CSS by replacing patterns that reference removed elements
# These rules don't cause errors but are dead code

# Remove memberships + responsive memberships from responsive section
html = html.replace(
    '  .membership-grid{grid-template-columns:1fr 1fr}\n  .social-wrap{flex-direction:column}',
    '  .social-wrap{flex-direction:column}'
)

html = html.replace(
    '  .membership-grid{grid-template-columns:1fr;gap:16px}\n  .membership-card{padding:24px 20px}\n  .membership-card .m-price{font-size:1.6rem}\n  .membership-card .m-benefits li{font-size:.85rem;padding:6px 0}\n  .gallery-grid',
    '  .gallery-grid'
)

html = html.replace(
    '  .membership-card{padding:16px 12px}\n  .cart-item-info h4',
    '  .cart-item-info h4'
)

# Remove sched-tab remnants
html = html.replace(
    '  .sched-tabs{max-width:100%;gap:4px}\n  .sched-tab{padding:12px 16px;font-size:.9rem}\n  .mobile-nav .nav-link',
    '  .mobile-nav .nav-link'
)

# Remove trainer-card-wrapper from responsive sections
html = html.replace(
    '  .trainer-card-wrapper{width:calc(75% - 8px);min-width:240px}\n  .testimonials-grid',
    '  .testimonials-grid'
)
html = html.replace(
    '  .trainer-card-wrapper{width:calc(85% - 8px);min-width:220px}\n  .trainer-initials',
    '  .trainer-initials'
)
html = html.replace(
    '  .trainer-card-wrapper{width:calc(95% - 8px);min-width:170px}\n  .schedule-card',
    '  .schedule-card'
)

# Remove wo-body from responsive
html = html.replace(
    '  .wo-body{padding:20px}\n  .wo-params',
    '  .wo-params'
)
html = html.replace(
    '  .wo-body{padding:16px}\n  .wday-grid',
    '  .wday-grid'
)
html = html.replace(
    '  .wo-body{padding:12px}\n  .wo-field',
    '  .wo-field'
)

# Remove trainer/membership schema from touch-action
html = html.replace(
    'button,a,.btn,.nav-link,.lang-btn,.hamburger,.cart-btn,.faq-q,.sched-day-header,.trainer-card,input,select,textarea{touch-action:manipulation}',
    'button,a,.btn,.nav-link,.lang-btn,.hamburger,.cart-btn,.faq-q,input,select,textarea{touch-action:manipulation}'
)

# Remove schedule-related CSS from before "/* About Features */"
# The Schedule Cards CSS block was already removed, but schedule-card still appears in responsive

# Remove trainer-card:hover references
html = html.replace(
    '  .trainer-card:hover{transform:none;box-shadow:none}\n  .trainer-card:hover .trainer-overlay,.trainer-card:focus .trainer-overlay{transform:translateY(0);opacity:1}\n  .wday-card:hover{transform:none;box-shadow:none}\n  .wday-card:hover::before{opacity:0}\n  .gallery-item:hover,.membership-card:hover{transform:none}\n  .member-card:hover{transform:none}\n',
    '  .gallery-item:hover{transform:none}\n'
)

html = html.replace(
    '  .trainer-card:active{transform:translateY(-2px)}\n  .trainer-card:active .trainer-overlay{transform:translateY(0);opacity:1}\n',
    ''
)

# Remove sched-tab references from transition
html = html.replace(
    '.contact-card,.membership-card,.gallery-item{transition:transform .3s ease}\n.btn,.btn-nav,.sched-tab,.cart-btn,.lang-btn{transition:color .3s,background .3s,border .3s,transform .3s}',
    '.contact-card,.gallery-item{transition:transform .3s ease}\n.btn,.btn-nav,.cart-btn,.lang-btn{transition:color .3s,background .3s,border .3s,transform .3s}'
)

# Remove hover effects for removed sections
html = html.replace(
    '.info-card:hover,.membership-card:hover,.testimonial-card:hover,.trainer-card:hover,.instagram-card:hover{transform:none!important}',
    '.info-card:hover,.testimonial-card:hover,.instagram-card:hover{transform:none!important}'
)

# Remove wday-card from reduced motion
html = html.replace(
    '  .wo-result .wday-card{opacity:1;transform:none;animation:none}\n  .trainer-overlay',
    '  .trainer-overlay'
)

# Also clean up any remaining schedule and coach related stuff
html = html.replace(
    '  .schedule-card{padding:16px}\n  .schedule-card .sch-title{font-size:.9rem;margin-bottom:10px;padding-bottom:8px}',
    ''
)

html = html.replace(
    '  .schedule-card{padding:10px}\n  .schedule-card .sch-title{font-size:.78rem;margin-bottom:6px}',
    ''
)

with open(r'C:\Users\n1\AppData\Local\Temp\opencode\my-elegance\index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("CSS cleanup complete!")
