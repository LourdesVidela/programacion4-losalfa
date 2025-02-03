# app/routes/secretario_routes.py

from flask import Blueprint

# Importamos el blueprint de admin.py para usar sus rutas
from app.routes.admin import admin_bp

secretario_bp = Blueprint('secretario_bp', __name__)

# Aquí simplemente registramos las rutas de admin para que los secretarios puedan acceder a ellas
secretario_bp.register_blueprint(admin_bp, url_prefix='/secretario')

# Puedes añadir más rutas o personalizaciones si son necesarias para el secretario,
# pero en este caso, las rutas para administrar doctores son las mismas que las del admin.
