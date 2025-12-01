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
    # Placeholder for allow_iframe function - implement CORS if needed
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
