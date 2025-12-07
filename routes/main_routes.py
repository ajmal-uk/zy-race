from flask import Blueprint, render_template, make_response

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('blog/index.html')

@main_bp.route('/start')
def start():
    return render_template('pages/game.html')

@main_bp.route('/about')
def about():
    return render_template('pages/about.html')

@main_bp.route('/contact')
def contact():
    return render_template('pages/contact.html')

@main_bp.route('/features')
def features():
    return render_template('pages/features.html')

@main_bp.route('/pricing')
def pricing():
    return render_template('pages/pricing.html')

@main_bp.route('/testimonials')
def testimonials():
    return render_template('pages/testimonials.html')

@main_bp.route('/use-cases')
def use_cases():
    return render_template('pages/use-cases.html')

@main_bp.route('/partners')
def partners():
    return render_template('pages/partners.html')

@main_bp.route('/press')
def press():
    return render_template('pages/press.html')

@main_bp.route('/help')
def help_():
    return render_template('support/help.html')

@main_bp.route('/troubleshoot')
def troubleshoot():
    return render_template('support/troubleshoot.html')

@main_bp.route('/documentation')
def documentation():
    return render_template('support/documentation.html')

@main_bp.route('/embed')
def embed():
    response = make_response(render_template('components/embed.html'))
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

@main_bp.route('/embed-widget')
def embed_widget():
    return render_template('components/embed-widget.html')

@main_bp.route('/use')
def direct_use():
    return render_template('support/direct-use.html')

@main_bp.route('/og-images')
def og_images():
    return render_template('seo/og-images.html')

@main_bp.route('/guide')
def guide():
    return render_template('support/guide.html')

@main_bp.route('/faq')
def faq():
    return render_template('support/faq.html')

@main_bp.route('/download')
def download_page():
    return render_template('pages/download.html')

@main_bp.route('/sitemap.xml')
def sitemap():
    from datetime import datetime
    pages = []
    static_urls = [
        ('/', 1.0, 'daily'),
        ('/start', 0.9, 'weekly'),
        ('/features', 0.8, 'monthly'),
        ('/blog', 0.8, 'weekly'),
        ('/about', 0.6, 'monthly'),
        ('/contact', 0.6, 'monthly'),
        ('/pricing', 0.7, 'monthly'),
        ('/testimonials', 0.6, 'monthly'),
        ('/use-cases', 0.7, 'monthly'),
        ('/partners', 0.5, 'monthly'),
        ('/press', 0.5, 'monthly'),
        ('/help', 0.5, 'monthly'),
        ('/troubleshoot', 0.5, 'monthly'),
        ('/documentation', 0.6, 'monthly'),
        ('/guide', 0.7, 'monthly'),
        ('/faq', 0.6, 'monthly'),
        ('/download', 0.7, 'monthly'),
    ]

    for url, priority, changefreq in static_urls:
        pages.append({
            'loc': f"https://zyrace.com{url}",
            'lastmod': datetime.now().strftime('%Y-%m-%d'),
            'changefreq': changefreq,
            'priority': priority
        })

    response = make_response(render_template('seo/sitemap.xml', pages=pages))
    response.headers['Content-Type'] = 'application/xml'
    return response

@main_bp.route('/robots.txt')
def robots():
    response = make_response(render_template('seo/robots.txt'))
    response.headers['Content-Type'] = 'text/plain'
    return response
