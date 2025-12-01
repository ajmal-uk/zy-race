from flask import Blueprint, render_template

legal_bp = Blueprint('legal', __name__)

@legal_bp.route('/terms')
def terms():
    return render_template('legal/terms.html')

@legal_bp.route('/privacy')
def privacy():
    return render_template('legal/privacy.html')

@legal_bp.route('/cookies')
def cookies():
    return render_template('legal/cookies.html')

@legal_bp.route('/dmca')
def dmca():
    return render_template('legal/dmca.html')

@legal_bp.route('/disclaimer')
def disclaimer():
    return render_template('legal/disclaimer.html')

@legal_bp.route('/refund-policy')
def refund_policy():
    return render_template('legal/refund-policy.html')

@legal_bp.route('/security')
def security():
    return render_template('legal/security.html')

@legal_bp.route('/gdpr')
def gdpr():
    return render_template('legal/gdpr.html')
