from flask import Blueprint, send_from_directory, current_app
import os

assets_bp = Blueprint('assets', __name__)

@assets_bp.route('/ads/<path:filename>')
def serve_ads(filename):
    return send_from_directory(os.path.join(current_app.root_path, 'ads'), filename)

@assets_bp.route('/robots.txt')
def robots():
    return send_from_directory('assets', 'robots.txt')

@assets_bp.route('/llms.txt')
def llms():
    return send_from_directory('assets', 'llms.txt')

@assets_bp.route('/google83f8616f6a5b1974.html')
def google():
    return send_from_directory('assets', 'google83f8616f6a5b1974.html')

@assets_bp.route('/ads.txt')
def ads():
    return send_from_directory('assets', 'ads.txt')

@assets_bp.route('/logo.png')
def logo():
    return send_from_directory('assets', 'logo.png')

@assets_bp.route('/og-image.jpg')
def og_image():
    return send_from_directory('assets', 'og-image.jpg')

@assets_bp.route('/twitter-image.jpg')
def twitter_image():
    return send_from_directory('assets', 'twitter-image.jpg')

@assets_bp.route('/favicon.ico')
def favicon_ico():
    return send_from_directory('assets/favicon', 'favicon.ico')

@assets_bp.route('/favicon.svg')
def favicon_svg():
    return send_from_directory('assets/favicon', 'favicon.svg')

@assets_bp.route('/favicon-96x96.png')
def favicon_96():
    return send_from_directory('assets/favicon', 'favicon-96x96.png')

@assets_bp.route('/web-app-manifest-192x192.png')
def web_app_manifest_192():
    return send_from_directory('assets/favicon', 'web-app-manifest-192x192.png')

@assets_bp.route('/web-app-manifest-512x512.png')
def web_app_manifest_512():
    return send_from_directory('assets/favicon', 'web-app-manifest-512x512.png')

@assets_bp.route('/apple-touch-icon.png')
def apple_icon():
    return send_from_directory('assets/favicon', 'apple-touch-icon.png')

@assets_bp.route('/site.webmanifest')
def webmanifest():
    return send_from_directory('assets/favicon', 'site.webmanifest')

@assets_bp.route('/app.apk')
def serve_apk():
    return send_from_directory('assets', 'app.apk', as_attachment=True)
