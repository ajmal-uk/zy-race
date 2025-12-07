from flask import Blueprint, render_template, make_response, current_app, abort
from datetime import datetime
import pytz

blog_bp = Blueprint('blog', __name__)

@blog_bp.route('/blog')
def blog():
    return render_template('blog/blog.html', posts=current_app.config['BLOG_POSTS'])

@blog_bp.route('/blog/<slug>')
def post(slug):
    # Map slugs to template files
    # Only 'physics-behind-zyrace' differs from its filename.
    # We can default to slug.html if not found in the map.
    template_map = {
        'physics-behind-zyrace': 'blog/physics-engine.html',
        'indie-dev-journey': 'blog/indie-dev-journey.html',
        'strategies-hill-climb': 'blog/strategies-hill-climb.html',
        'browser-games-comeback': 'blog/browser-games-comeback.html',
        'unlockable-cars': 'blog/unlockable-cars.html',
        'speedrun-guide': 'blog/speedrun-guide.html'
    }
    
    template = template_map.get(slug)
    if template:
        return render_template(template)
    else:
        # Fallback or 404
        return render_template('errors/404.html'), 404


@blog_bp.route('/feed.xml')
def rss_feed():
    try:
        last_build_date = datetime.now(pytz.UTC).strftime("%a, %d %b %Y %H:%M:%S GMT")
        response = make_response(render_template('blog/feed.xml',
                                              posts=current_app.config['BLOG_POSTS'],
                                              last_build_date=last_build_date))
        response.headers['Content-Type'] = 'application/rss+xml'
        return response
    except Exception as e:
        current_app.logger.error(f'RSS feed generation error: {str(e)}')
        abort(500, description="Error generating RSS feed")

@blog_bp.route('/opensearch.xml')
def opensearch():
    response = make_response(render_template('seo/opensearch.xml'))
    response.headers['Content-Type'] = 'application/opensearchdescription+xml'
    return response
