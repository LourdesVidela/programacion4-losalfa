from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models.doctor import db, Doctor
from functools import wraps

# Asegúrate de que el nombre del Blueprint sea único
admin_doctor_bp = Blueprint('admin_doctor_v2', __name__)

# Decorador para restringir acceso solo a administradores
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session or session.get('role') != 'admin':
            flash("Acceso no autorizado", "error")
            return redirect(url_for('auth.login'))  # Redirigir al login si no es admin
        return f(*args, **kwargs)
    return decorated_function

# Ruta para el panel de administración de doctores (solo admin)
@admin_doctor_bp.route('/admin_dashboard')
@admin_required  # Solo los administradores pueden acceder a esta ruta
def admin_dashboard():
    doctors = Doctor.query.all()  # Obtiene todos los doctores
    return render_template('admin-dashboard.html', doctors=doctors)

# Ruta para crear un nuevo doctor (solo admin)
@admin_doctor_bp.route('/create', methods=['GET', 'POST'])
@admin_required  # Solo los administradores pueden crear doctores
def create_doctor():
    if request.method == 'POST':
        nombre = request.form['nombre']
        especialidad = request.form['especialidad']
        numero_matricula = request.form['numero_matricula']
        obra_social = request.form['obra_social']

        # Crear un nuevo doctor
        new_doctor = Doctor(nombre=nombre, especialidad=especialidad,
                            numero_matricula=numero_matricula, obra_social=obra_social)
        db.session.add(new_doctor)
        db.session.commit()

        flash('Doctor creado exitosamente', 'success')
        return redirect(url_for('admin_doctor.admin_dashboard'))  # Redirige al panel de doctores

    return render_template('create_doctor.html')

# Ruta para editar un doctor (solo admin)
@admin_doctor_bp.route('/edit/<int:doctor_id>', methods=['GET', 'POST'])
@admin_required  # Solo los administradores pueden editar doctores
def edit_doctor(doctor_id):
    doctor = Doctor.query.get_or_404(doctor_id)

    if request.method == 'POST':
        doctor.nombre = request.form['nombre']
        doctor.especialidad = request.form['especialidad']
        doctor.numero_matricula = request.form['numero_matricula']
        doctor.obra_social = request.form['obra_social']

        db.session.commit()
        flash('Doctor actualizado exitosamente', 'success')
        return redirect(url_for('admin_doctor.admin_dashboard'))  # Redirige al panel de doctores

    return render_template('edit_doctor.html', doctor=doctor)

# Ruta para eliminar un doctor (solo admin)
@admin_doctor_bp.route('/delete/<int:doctor_id>', methods=['POST'])
@admin_required  # Solo los administradores pueden eliminar doctores
def delete_doctor(doctor_id):
    doctor = Doctor.query.get_or_404(doctor_id)

    db.session.delete(doctor)
    db.session.commit()
    flash('Doctor eliminado exitosamente', 'danger')
    return redirect(url_for('admin_doctor.admin_dashboard'))  # Redirige al panel de doctores
