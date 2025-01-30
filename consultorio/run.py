from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from routes import init_routes  # Importa la función que inicializa las rutas
from models.usuario import db, Usuario, crear_usuarios_iniciales  # Asegúrate de tener estos modelos y funciones correctamente importados
from config.config import Config  # Asegúrate de que la configuración esté correcta
from flask_migrate import Migrate  # Para manejar migraciones de base de datos

# Inicializa la aplicación Flask
app = Flask(__name__)
app.config.from_object(Config)  # Usar la configuración definida en el archivo config.py

# Inicializa la base de datos
db.init_app(app)

# Configuración de Flask-Migrate para manejar migraciones de la base de datos
migrate = Migrate(app, db)

# Inicializa Flask-Login
login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'  # Redirige al login si el usuario no está autenticado

# Función para cargar al usuario por su ID (requerido por Flask-Login)
@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))  # Obtiene el usuario desde la base de datos

# Inicializa las rutas desde el módulo 'routes'
init_routes(app)

# Ruta de inicio de la aplicación
@app.route('/')
def home():
    return render_template('home.html')  # Asegúrate de tener esta plantilla en la carpeta de templates

# Inicia la aplicación
if __name__ == '__main__':
    # Ejecutar solo si la aplicación se está ejecutando directamente
    with app.app_context():
        db.create_all()  # Crea las tablas en la base de datos si no existen
        crear_usuarios_iniciales()  # Llama a la función para crear los usuarios iniciales en la base de datos si es necesario

    # Ejecuta la aplicación en modo debug
    app.run(debug=True)
