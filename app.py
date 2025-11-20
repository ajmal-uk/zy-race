from flask import Flask, render_template, send_from_directory, make_response, abort
import os
from datetime import datetime
import pytz

app = Flask(__name__, static_folder='static')

# Configure blog posts if needed (placeholder for RSS)
app.config['BLOG_POSTS'] = []  # Add your blog posts here as a list of dicts

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/start')
def start():
    return render_template('game.html')

@app.route('/cookies')
def cookies():
    return render_template('cookies.html')

@app.route('/gdpr')
def gdpr():
    return render_template('gdpr.html')

@app.route('/dmca')
def dmca():
    return render_template('dmca.html')

@app.route('/security')
def security():
    return render_template('security.html')

@app.route('/refund-policy')
def refund_policy():
    return render_template('refund-policy.html')

@app.route('/pricing')
def pricing():
    return render_template('pricing.html')

@app.route('/testimonials')
def testimonials():
    return render_template('testimonials.html')

@app.route('/use-cases')
def use_cases():
    return render_template('use-cases.html')

@app.route('/partners')
def partners():
    return render_template('partners.html')

@app.route('/press')
def press():
    return render_template('press.html')

@app.route('/help')
def help_():
    return render_template('help.html')

@app.route('/troubleshoot')
def troubleshoot():
    return render_template('troubleshoot.html')

@app.route('/og-images')
def og_images():
    return render_template('og-images.html')

@app.route('/documentation')
def documentation():
    return render_template('documentation.html')

@app.route('/embed')
def embed():
    response = make_response(render_template('embed.html'))
    # Placeholder for allow_iframe function - implement CORS if needed
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

@app.route('/embed-widget')
def embed_widget():
    return render_template('embed-widget.html')

@app.route('/use')
def direct_use():
    return render_template('direct-use.html')

@app.route('/feed.xml')
def rss_feed():
    try:
        last_build_date = datetime.now(pytz.UTC).strftime("%a, %d %b %Y %H:%M:%S GMT")
        response = make_response(render_template('feed.xml',
                                              posts=app.config['BLOG_POSTS'],
                                              last_build_date=last_build_date))
        response.headers['Content-Type'] = 'application/rss+xml'
        return response
    except Exception as e:
        app.logger.error(f'RSS feed generation error: {str(e)}')
        abort(500, description="Error generating RSS feed")

@app.route('/opensearch.xml')
def opensearch():
    response = make_response(render_template('opensearch.xml'))
    response.headers['Content-Type'] = 'application/opensearchdescription+xml'
    return response

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/download')
def download_page():
    return render_template('download.html')

@app.route('/guide')
def guide():
    return render_template('guide.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/disclaimer')
def disclaimer():
    return render_template('disclaimer.html')

@app.route('/features')
def features():
    return render_template('features.html')

@app.route('/robots.txt')
def robots():
    return send_from_directory('assets', 'robots.txt')

@app.route('/llms.txt')
def llms():
    return send_from_directory('assets', 'llms.txt')

@app.route('/ads.txt')
def ads():
    return send_from_directory('assets', 'ads.txt')

@app.route('/logo.png')
def logo():
    return send_from_directory('assets', 'logo.png')

@app.route('/og-image.jpg')
def og_image():
    return send_from_directory('assets', 'og-image.jpg')

@app.route('/twitter-image.jpg')
def twitter_image():
    return send_from_directory('assets', 'twitter-image.jpg')

@app.route('/favicon.ico')
def favicon_ico():
    return send_from_directory('assets/favicon', 'favicon.ico')

@app.route('/favicon.svg')
def favicon_svg():
    return send_from_directory('assets/favicon', 'favicon.svg')

@app.route('/favicon-96x96.png')
def favicon_96():
    return send_from_directory('assets/favicon', 'favicon-96x96.png')

@app.route('/web-app-manifest-192x192.png')
def web_app_manifest_192():
    return send_from_directory('assets/favicon', 'web-app-manifest-192x192.png')

@app.route('/web-app-manifest-512x512.png')
def web_app_manifest_512():
    return send_from_directory('assets/favicon', 'web-app-manifest-512x512.png')

@app.route('/apple-touch-icon.png')
def apple_icon():
    return send_from_directory('assets/favicon', 'apple-touch-icon.png')

@app.route('/site.webmanifest')
def webmanifest():
    return send_from_directory('assets/favicon', 'site.webmanifest')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)