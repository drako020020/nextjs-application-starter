from flask import Blueprint, request, render_template, make_response
from weasyprint import HTML
from ..models import ScanResult, LoginAttempt
import json

reporting_bp = Blueprint('reporting', __name__, template_folder='templates')

@reporting_bp.route('/generate', methods=['GET'])
def generate_report():
    # Fetch data for report
    scans = ScanResult.query.order_by(ScanResult.timestamp.desc()).limit(10).all()
    logins = LoginAttempt.query.order_by(LoginAttempt.timestamp.desc()).limit(10).all()

    # Prepare data for template
    scan_data = [{
        'host_ip': s.host_ip,
        'hostname': s.hostname,
        'open_ports': json.loads(s.open_ports) if s.open_ports else [],
        'os': s.os,
        'timestamp': s.timestamp
    } for s in scans]

    login_data = [{
        'email': l.email,
        'success': l.success,
        'timestamp': l.timestamp
    } for l in logins]

    html = render_template('report.html', scans=scan_data, logins=login_data)

    pdf = HTML(string=html).write_pdf()

    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=report.pdf'

    return response
