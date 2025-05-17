from flask import Blueprint, jsonify
from ..models import LoginAttempt, ScanResult
from ..extensions import db
from sqlalchemy import func

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/login_attempts', methods=['GET'])
def login_attempts():
    total = db.session.query(func.count(LoginAttempt.id)).scalar()
    success = db.session.query(func.count(LoginAttempt.id)).filter(LoginAttempt.success == True).scalar()
    failed = total - success
    return jsonify({'total': total, 'success': success, 'failed': failed})

@dashboard_bp.route('/scan_results', methods=['GET'])
def scan_results():
    # Return count of scan results grouped by OS
    results = db.session.query(ScanResult.os, func.count(ScanResult.id)).group_by(ScanResult.os).all()
    data = [{'os': os, 'count': count} for os, count in results]
    return jsonify({'scan_results': data})
