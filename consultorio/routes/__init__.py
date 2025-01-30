from routes.auth import auth_bp
from routes.doctor import admin_doctor_bp

def init_routes(app):
    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_doctor_bp)