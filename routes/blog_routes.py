from flask import Blueprint, render_template, make_response, current_app, abort
from datetime import datetime
import pytz

blog_bp = Blueprint('blog', __name__)

@blog_bp.route('/blog')
def blog():
    return render_template('blog/blog.html')

@blog_bp.route('/blog/physics-behind-zyrace')
def blog_physics():
    return render_template('blog/physics-engine.html')

@blog_bp.route('/blog/indie-dev-journey')
def blog_journey():
    return render_template('blog/indie-dev-journey.html')

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
