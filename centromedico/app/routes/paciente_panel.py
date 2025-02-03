# app/routes/paciente_routes.py

from flask import Blueprint, render_template
from flask_login import login_required

paciente_bp = Blueprint('paciente', __name__)

@paciente_bp.route('/panel')
@login_required
def panel():
    return render_template('paciente_panel.html')  # Asegúrate de tener una plantilla 'paciente_panel.html'
