# app/routes.py
from flask import Blueprint

# Definir los blueprints
home_bp = Blueprint('home', __name__)
auth_bp = Blueprint('auth', __name__)
admin_bp = Blueprint('admin', __name__)
medico_bp = Blueprint('medico', __name__)
paciente_bp = Blueprint('paciente', __name__)
secretario_bp = Blueprint('secretario', __name__)

# Aquí agregarías las rutas para cada blueprint


@auth_bp.route('/login')
def login():
    return "Página de login"
