# app/routes/medico_routes.py

from flask import Blueprint

medico_bp = Blueprint('medico_bp', __name__)

@medico_bp.route('/medico')
def medico():
    return "Página del Médico"
