from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from app.config import Config

# Inicializa la base de datos y Flask-Login sin asignarlos a una app todavía
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar extensiones con la app
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'  # Configura la vista de login por defecto

    with app.app_context():
        from app.models.user_model import Usuario
        from app.models.doctor_model import Doctor  # Agregado para evitar problemas con la tabla
        db.create_all()  # Asegura que las tablas se creen si no existen

    # Registrar Blueprints de rutas
    from app.routes.home import home_bp
    from app.routes.auth import auth_bp
    from app.routes.admin import admin_bp
    from app.routes.medicos import medico_bp  # Cambio a un nombre más coherente
    from app.routes.paciente_panel import paciente_bp
    from app.routes.secretario import secretario_bp

    # Registra los Blueprints
    app.register_blueprint(home_bp, url_prefix='/')
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(medico_bp, url_prefix='/doctores')  # Cambié a /doctores para mayor claridad
    app.register_blueprint(paciente_bp, url_prefix='/paciente')
    app.register_blueprint(secretario_bp, url_prefix='/secretario')

    return app

# Cargar el usuario por ID
@login_manager.user_loader
def load_user(user_id):
    from app.models.user_model import Usuario  # Importación aquí para evitar errores circulares
    return Usuario.query.get(int(user_id))