from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')  # Cargar la configuración desde config.py
    db.init_app(app)
    
    # Importa las rutas
    from routes.auth import auth_bp
    from routes.paciente import paciente_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(paciente_bp)

    return app