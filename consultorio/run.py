from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from routes import init_routes
from models.usuario import db, Usuario, crear_usuarios_iniciales  # Importa la función
from config.config import Config  # Para importar correctamente desde la carpeta config
from flask_migrate import Migrate  # Para manejar migraciones de base de datos

# Inicializa la aplicación
app = Flask(__name__)
app.config.from_object(Config)  # Usar la configuración del archivo config.py

# Inicializa la base de datos
db.init_app(app)
migrate = Migrate(app, db)  # Inicializa Flask-Migrate para manejar migraciones

# Inicializa Flask-Login
login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'  # Redirige al login si el usuario no está autenticado

# Cargar al usuario en base al ID (requerido por Flask-Login)
@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))  # Devuelve el usuario desde la base de datos

# Inicializa las rutas
init_routes(app)

# Ruta de inicio
@app.route('/')
def home():
    return render_template('home.html')  # Asegúrate de tener esta plantilla

# Inicia la aplicación
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Crea las tablas si no existen
        crear_usuarios_iniciales()  # Llama a la función para crear usuarios iniciales
    app.run(debug=True)
