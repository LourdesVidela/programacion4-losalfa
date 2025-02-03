from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.doctor_model import Doctor
from app.models.user_model import Usuario
from app import db
from werkzeug.security import generate_password_hash
from flask_login import current_user, login_required
from functools import wraps  # Import necesario para evitar errores con Flask-Login

admin_bp = Blueprint('admin', __name__)

# Decorador para verificar permisos de administrador
def admin_required(f):
    @wraps(f)  # Evita errores con Flask-Login
    def wrapper(*args, **kwargs):
        if not hasattr(current_user, "role") or current_user.role not in ['admin', 'secretario']:
            flash('No tienes permiso para acceder a esta sección', 'danger')
            return redirect(url_for('main.index'))
        return f(*args, **kwargs)
    return login_required(wrapper)

# Ruta para el panel de administración
@admin_bp.route('/panel_admin')
def panel_admin():
    return render_template('panel_admin.html')

# Ruta para ver la lista de doctores
@admin_bp.route('/panel/doctores')
@admin_required
def doctores():
    doctores = Doctor.query.all()  # Consulta para obtener todos los doctores
    return render_template('doctores.html', doctores=doctores)

@admin_bp.route('/crear_doctor', methods=['GET', 'POST'])
def crear_doctor():
    if request.method == 'POST':
        # Obtener los datos del formulario
        nombre = request.form.get('nombre')
        username = request.form.get('username')
        password = request.form.get('password')
        especialidad = request.form.get('especialidad')
        telefono = request.form.get('telefono')
        direccion = request.form.get('direccion')
        obras_sociales = request.form.getlist('obras_sociales')  # Obtener lista de obras sociales seleccionadas

        # Validaciones básicas
        if not nombre or not username or not password or not especialidad or not telefono or not direccion:
            flash('Todos los campos son obligatorios.', 'error')
            return redirect(url_for('admin.crear_doctor'))

        # Verificar si el nombre de usuario ya existe
        existing_user = Usuario.query.filter_by(username=username).first()
        if existing_user:
            flash('El nombre de usuario ya está en uso. Por favor, elige otro.', 'error')
            return redirect(url_for('admin.crear_doctor'))

        try:
            # Crear el nuevo usuario
            new_user = Usuario(
                username=username,
                password=generate_password_hash(password),
                role='doctor'  # Suponiendo que 'doctor' es el rol para los doctores
            )

            # Agregar el nuevo usuario a la base de datos
            db.session.add(new_user)
            db.session.commit()  # Commit para generar el ID del usuario.

            # Crear el nuevo doctor
            new_doctor = Doctor(
                nombre=nombre,
                especialidad=especialidad,
                telefono=telefono,
                direccion=direccion,
                obra_social=','.join(obras_sociales),  # Guardar las obras sociales como una cadena separada por comas
                user_id=new_user.id  # Asociamos el doctor con el usuario
            )

            # Agregar el doctor a la base de datos
            db.session.add(new_doctor)
            db.session.commit()  # Commit para agregar el doctor a la base de datos.

            flash('Doctor creado exitosamente.', 'success')
            return redirect(url_for('admin.panel_admin'))  # Redirigir al panel de administración

        except Exception as e:
            db.session.rollback()  # Rollback para revertir la transacción si ocurre un error
            flash(f'Hubo un error al crear el doctor: {e}', 'error')
            return redirect(url_for('admin.crear_doctor'))

    return render_template('crear_doctor.html')  # Asegúrate de que la plantilla esté en la ruta correcta
   
# Ruta para editar un doctor
@admin_bp.route('/panel/doctores/editar/<int:doctor_id>', methods=['GET', 'POST'])
@admin_required
def editar_doctor(doctor_id):
    doctor = Doctor.query.get_or_404(doctor_id)  # Busca al doctor por ID

    if request.method == 'POST':
        # Obtén los datos del formulario
        doctor.nombre = request.form['nombre']
        doctor.especialidad = request.form['especialidad']
        doctor.telefono = request.form['telefono']
        doctor.direccion = request.form['direccion']
        doctor.obra_social = request.form['obra_social']

        # Guarda los cambios
        db.session.commit()
        return redirect(url_for('admin.doctores'))  # Redirige a la lista de doctores

    return render_template('editar_doctor.html', doctor=doctor)  # Muestra el formulario con los datos del doctor

# Ruta para eliminar un doctor
@admin_bp.route('/panel/doctores/eliminar/<int:doctor_id>', methods=['GET', 'POST'])
@admin_required
def eliminar_doctor(doctor_id):
    doctor = Doctor.query.get_or_404(doctor_id)  # Busca al doctor por ID

    # Elimina el doctor
    db.session.delete(doctor)
    db.session.commit()

    return redirect(url_for('admin.doctores'))  # Redirige a la lista de doctores
