from flask import Flask, render_template
from datetime import datetime
import os

# Import blueprints
from routes.main_routes import main_bp
from routes.legal_routes import legal_bp
from routes.blog_routes import blog_bp
from routes.asset_routes import assets_bp

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'ajmaluk')

# Blog Configuration
app.config['BLOG_POSTS'] = [
    {
        'title': 'Launch Day Success!',
        'slug': '#',
        'description': "We are live! ZyRace is now available for everyone to play for free. Check out what's new in version 1.0.",
        'date': 'Oct 2025',
        'image': 'launch-day.jpg',
        'category': 'Update'
    },
    {
        'title': 'The Physics Behind ZyRace',
        'slug': 'physics-behind-zyrace',
        'description': 'Dive deep into how we use Matter.js to simulate realistic car physics, suspension, and terrain interactions.',
        'date': 'Nov 2025',
        'image': 'physics-engine.jpg',
        'category': 'Engineering'
    },
    {
        'title': 'The Indie Dev Journey',
        'slug': 'indie-dev-journey',
        'description': 'Ajmal U K shares the story of building ZyRace as a solo developer in Kerala. The challenges, the wins, and the vision.',
        'date': 'Nov 2025',
        'image': 'indie-dev.jpg',
        'category': 'Story'
    },
    {
        'title': 'Top 5 Strategies for Hill Climb Racing',
        'slug': 'strategies-hill-climb',
        'description': 'Master the tracks with these pro tips. Learn when to brake, when to boost, and how to maintain momentum for the best times.',
        'date': 'Dec 2025',
        'image': 'strategies-hill-climb.png',
        'category': 'Guide'
    },
    {
        'title': 'Why Browser Games are Making a Comeback',
        'slug': 'browser-games-comeback',
        'description': 'With WebGL and WebAssembly, browser gaming is entering a new golden age. See why ZyRace is leading the pack in innovation.',
        'date': 'Dec 2025',
        'image': 'browser-games-comeback.png',
        'category': 'Tech'
    },
    {
        'title': 'ZyRace Garage: Unlockable Cars Guide',
        'slug': 'unlockable-cars',
        'description': 'From the Scout to the Titan. A complete breakdown of every vehicle\'s stats and cost in ZyRace.',
        'date': 'Dec 2025',
        'image': 'zyrace-vehicles.png',
        'category': 'Guide'
    },
    {
        'title': 'Speedrun Guide: Conquer the Tracks',
        'slug': 'speedrun-guide',
        'description': 'Want to top the leaderboards? Learn advanced techniques like "Sonic Start" and "Wall Riding" from the pros.',
        'date': 'Dec 2025',
        'image': 'strategies-hill-climb.png',
        'category': 'Advanced'
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