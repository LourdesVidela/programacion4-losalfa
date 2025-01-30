from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash
from models.usuario import db, Usuario, Rol
from models.paciente import Paciente

# Crear el Blueprint de paciente
paciente_bp = Blueprint('paciente', __name__)

# Ruta para registrar un nuevo paciente
@paciente_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Obtener datos del formulario
        dni = request.form['dni']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        edad = request.form['edad']
        sexo = request.form['sexo']
        obra_social = request.form['obra-social']
        domicilio = request.form['domicilio']
        telefono = request.form['telefono']
        correo = request.form['correo']
        usuario = request.form['usuario']
        contraseña = request.form['contraseña']

        # Verifica si el usuario ya existe
        if Usuario.query.filter_by(usuario=usuario).first():
            flash("El usuario ya existe", "danger")
            return redirect(url_for('paciente.register'))

        # Obtener el rol 'paciente' desde la base de datos
        rol_paciente = Rol.query.filter_by(nombre='paciente').first()

        if not rol_paciente:
            flash("Rol 'paciente' no encontrado", "danger")
            return redirect(url_for('paciente.register'))

        # Crear nuevo usuario con el rol 'paciente'
        nuevo_usuario = Usuario(
            usuario=usuario,
            contraseña=generate_password_hash(contraseña),
            rol_id=rol_paciente.id  # Asignar el ID del rol 'paciente'
        )
        db.session.add(nuevo_usuario)
        db.session.commit()

        # Crear paciente vinculado al usuario
        nuevo_paciente = Paciente(
            dni=dni,
            nombre=nombre,
            apellido=apellido,
            edad=int(edad),
            sexo=sexo,
            obra_social=obra_social,
            domicilio=domicilio,
            telefono=telefono,
            correo=correo,
            usuario_id=nuevo_usuario.id  # Relacionar el paciente con el usuario
        )
        db.session.add(nuevo_paciente)
        db.session.commit()

        # Mostrar mensaje de éxito y redirigir al login
        flash("Paciente registrado exitosamente", "success")
        return redirect(url_for('auth.login'))

    return render_template('register.html')

