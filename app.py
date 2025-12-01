from flask import Flask, render_template
from datetime import datetime
import pytz
import os

# Import blueprints
from routes.main_routes import main_bp
from routes.legal_routes import legal_bp
from routes.blog_routes import blog_bp
from routes.asset_routes import assets_bp

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev_key_please_change_in_prod')

# Blog Configuration
app.config['BLOG_POSTS'] = [
    {
        'title': 'The Physics Behind ZyRace',
        'slug': 'physics-behind-zyrace',
        'description': 'Dive deep into how we use Matter.js to simulate realistic car physics.',
        'date': 'Nov 2025'
    },
    {
        'title': 'The Indie Dev Journey',
        'slug': 'indie-dev-journey',
        'description': 'Ajmal U K shares the story of building ZyRace as a solo developer.',
        'date': 'Nov 2025'
    }
]

# Register Blueprints
app.register_blueprint(main_bp)
app.register_blueprint(legal_bp)
app.register_blueprint(blog_bp)
app.register_blueprint(assets_bp)

# Context Processor for Year
@app.context_processor
def inject_year():
    return {'current_year': datetime.now().year}

# Security Headers
@app.after_request
def add_security_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    return response

# Error Handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.html'), 500

if __name__ == '__main__':
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(debug=debug_mode, host='0.0.0.0', port=5000)