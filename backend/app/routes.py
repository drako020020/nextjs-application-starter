from flask import Flask
from .auth.routes import auth_bp
from .network_discovery.routes import network_bp
from .ai_planner.routes import ai_bp
from .dashboard.routes import dashboard_bp
from .reporting.routes import reporting_bp
from .remote_control.routes import remote_bp
from .vulnerability_ai.routes import vulnerability_bp
from .privilege_escalation.routes import privilege_bp
from .integration_tools.routes import integration_bp
from .trace_hiding.routes import trace_bp

def register_blueprints(app: Flask):
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(network_bp, url_prefix='/network')
    app.register_blueprint(ai_bp, url_prefix='/ai_planner')
    app.register_blueprint(dashboard_bp, url_prefix='/dashboard')
    app.register_blueprint(reporting_bp, url_prefix='/reporting')
    app.register_blueprint(remote_bp, url_prefix='/remote_control')
    app.register_blueprint(vulnerability_bp, url_prefix='/vulnerability_ai')
    app.register_blueprint(privilege_bp, url_prefix='/privilege_escalation')
    app.register_blueprint(integration_bp, url_prefix='/integration_tools')
    app.register_blueprint(trace_bp, url_prefix='/trace_hiding')
