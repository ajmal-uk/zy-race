from flask import Blueprint, render_template, make_response, current_app, request, jsonify
import requests

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    # Get latest 3 blog posts (reverse order to show newest first)
    blog_posts = current_app.config.get('BLOG_POSTS', [])[::-1][:3]
    return render_template('pages/home.html', posts=blog_posts)

@main_bp.route('/start')
def start():
    return render_template('pages/game.html')

@main_bp.route('/about')
def about():
    return render_template('pages/about.html')

@main_bp.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        try:
            data = request.get_json()
            
            # Google Apps Script URL (Updated)
            script_url = "https://script.google.com/macros/s/AKfycbxac6NfjLV2hf8goEYZVR8y4t0RhIBqWjTblr1KR2nSBHgdorHY62V6xzMNh27efAk/exec"
            
            # Forward the data to Google Apps Script
            response = requests.post(script_url, json=data)
            
            return jsonify(response.json())
        except Exception as e:
            return jsonify({'success': False, 'error': str(e)}), 500
            
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

    # Add static pages
    for url, priority, changefreq in static_urls:
        pages.append({
            'loc': f"https://zyrace.com{url}",
            'lastmod': datetime.now().strftime('%Y-%m-%d'),
            'changefreq': changefreq,
            'priority': priority
        })

    # Add blog posts
    from flask import current_app
    blog_posts = current_app.config.get('BLOG_POSTS', [])
    for post in blog_posts:
        pages.append({
            'loc': f"https://zyrace.com/blog/{post['slug']}",
            'lastmod': post.get('date', datetime.now().strftime('%Y-%m-%d')), # Fallback to current date if not set
            'changefreq': 'monthly',
            'priority': 0.6
        })

    response = make_response(render_template('seo/sitemap.xml', pages=pages))
    response.headers['Content-Type'] = 'application/xml'
    return response

@main_bp.route('/robots.txt')
def robots():
    response = make_response(render_template('seo/robots.txt'))
    response.headers['Content-Type'] = 'text/plain'
    return response
