from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from models.usuario import Usuario, db
from models.paciente import Paciente
from models.doctor import db, Doctor

# Crear el blueprint de autenticación
auth_bp = Blueprint('auth', __name__)

# Ruta de login
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('auth.patient_dashboard'))  # Redirige al panel de paciente si ya está logueado
    
    if request.method == 'POST':
        usuario = request.form.get('usuario', None)
        contraseña = request.form.get('contraseña', None)

        # Verifica si los campos están vacíos
        if not usuario or not contraseña:
            flash('Por favor, complete todos los campos', 'error')
            return render_template('login.html')

        # Verifica que los valores de usuario y contraseña estén siendo recibidos
        print(f'Usuario: {usuario}, Contraseña: {contraseña}')

        # Buscar al usuario en la base de datos
        user = Usuario.query.filter_by(usuario=usuario).first()

        if user and user.verificar_contraseña(contraseña):  # Verificación de la contraseña
            # Login con Flask-Login
            login_user(user)

            # Redirigir según el rol del usuario
            if user.rol == 'paciente':
                return redirect(url_for('auth.patient_dashboard'))  # Panel del paciente
            elif user.rol == 'doctor':
                return redirect(url_for('doctor_dashboard'))  # Panel del doctor
            elif user.rol == 'admin':
                return redirect(url_for('auth.admin_dashboard'))  # Panel del administrador
            elif user.rol == 'secretary':
                return redirect(url_for('secretary_dashboard'))  # Panel del secretario
        else:
            flash('Credenciales incorrectas', 'error')  # Mostrar mensaje de error

    return render_template('login.html')  # Renderizamos la plantilla de login

# Ruta para el registro de usuarios
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('auth.patient_dashboard'))  # Redirige al dashboard si ya está logueado
    
    if request.method == 'POST':
        # Recoger datos del formulario
        usuario = request.form['usuario']
        contraseña = request.form['contraseña']
        confirm_contraseña = request.form['confirm_contraseña']
        dni = request.form['dni']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        edad = request.form['edad']
        sexo = request.form['sexo']
        obra_social = request.form.get('obra_social', '')  # Puede ser opcional
        domicilio = request.form['domicilio']
        telefono = request.form['telefono']
        correo = request.form['correo']

        # Validación de las contraseñas
        if contraseña != confirm_contraseña:
            flash('Las contraseñas no coinciden', 'error')
            return redirect(url_for('auth.register'))
        
        # Verificar si el usuario ya existe
        existing_user = Usuario.query.filter_by(usuario=usuario).first()
        if existing_user:
            flash('El usuario ya está registrado', 'error')
            return redirect(url_for('auth.register'))
        
        # Verificar si el paciente ya está registrado por su DNI
        existing_paciente = Paciente.query.filter_by(dni=dni).first()
        if existing_paciente:
            flash('El paciente ya está registrado con ese DNI.', 'error')
            return redirect(url_for('auth.register'))

        # Encriptar la contraseña
        hashed_password = generate_password_hash(contraseña)

        # Crear un nuevo usuario
        new_user = Usuario(usuario=usuario, contraseña=hashed_password, rol='paciente')

        try:
            db.session.add(new_user)
            db.session.commit()  # Se debe confirmar primero el usuario para obtener su ID

            # Crear el paciente asociado
            new_paciente = Paciente(
                usuario_id=new_user.id,
                dni=dni,
                nombre=nombre,
                apellido=apellido,
                edad=int(edad),
                sexo=sexo,
                obra_social=obra_social,
                domicilio=domicilio,
                telefono=telefono,
                correo=correo
            )

            db.session.add(new_paciente)
            db.session.commit()  # Confirmar la creación del paciente

            flash('Registro exitoso. Ahora puedes iniciar sesión.', 'success')
            return redirect(url_for('auth.login'))
        
        except Exception as e:
            db.session.rollback()
            flash('Hubo un error al registrar el usuario. Intenta nuevamente.', 'error')

    return render_template('register.html')


# Ruta para cerrar sesión
@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

# Ruta para el panel de paciente
@auth_bp.route('/dashboard/paciente')
@login_required
def patient_dashboard():
    if current_user.rol != 'paciente':
        return redirect(url_for('auth.login'))  # Redirige a login si no es paciente
    return render_template('patient-dashboard.html')  # Renderiza la plantilla del panel de paciente

# Ruta para el panel de administración
@auth_bp.route('/admin_dashboard')
def admin_dashboard():
    doctors = Doctor.query.all()  # Obtiene todos los doctores de la base de datos
    return render_template('admin-dashboard.html', doctors=doctors)

