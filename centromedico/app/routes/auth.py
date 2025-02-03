# app/routes/auth.py
from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.user_model import Usuario

from app import db
from datetime import datetime
from flask_login import login_user, current_user, logout_user, login_required

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Obtener los datos del formulario
        username = request.form['usuario']  # Corregido para que coincida con el nombre del campo en el formulario HTML
        password = request.form['contraseña']  # Corregido para que coincida con el nombre del campo en el formulario HTML
        
        # Buscar al usuario por el nombre de usuario
        user = Usuario.query.filter_by(username=username).first()
        
        if user and user.check_password(password):  # Verificar la contraseña
            login_user(user)  # Iniciar la sesión del usuario
            
            # Redirigir al panel correspondiente según el rol del usuario
            if user.role == 'admin' or user.role == 'secretario':
                return redirect(url_for('admin.panel_admin'))  # Panel de admin/secretario
            elif user.role == 'paciente':
                return redirect(url_for('paciente.panel'))  # Panel de paciente
            
        else:
            flash('Credenciales inválidas', 'danger')  # Mensaje de error si las credenciales no son correctas
            return redirect(url_for('auth.login'))  # Volver al login en caso de error

    return render_template('login.html')


@auth_bp.route('/register', methods=['GET', 'POST']) 
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        role = request.form['role']  # El rol puede ser paciente, admin o secretario
        
        # Verificar si el nombre de usuario ya existe en la base de datos
        existing_user = Usuario.query.filter_by(username=username).first()
        if existing_user:
            flash('El nombre de usuario ya está en uso. Por favor elige otro.', 'danger')
            return redirect(url_for('auth.register'))  # Volver a la página de registro
        
        # Crear el nuevo usuario
        new_user = Usuario(username=username, role=role)
        new_user.set_password(password)  # Asegúrate de que 'set_password' encripte la contraseña
        
        # Añadir el nuevo usuario a la base de datos
        db.session.add(new_user)
        db.session.commit()  # Confirmar los cambios
        
        flash('Usuario registrado correctamente', 'success')
        
        # Redirigir al panel correspondiente según el rol del usuario
        if role in ['admin', 'secretario']:
            return redirect(url_for('admin.panel_admin'))  # Redirigir al panel de admin/secretario
        elif role == 'paciente':
            return redirect(url_for('paciente.panel'))  # Redirigir al panel de paciente

    return render_template('register.html')

@auth_bp.route('/logout')
@login_required  # Esto asegura que el usuario debe estar autenticado para cerrar sesión
def logout():
    logout_user()  # Cierra la sesión
    flash('Has cerrado sesión correctamente', 'success')  # Mensaje de éxito
    return redirect(url_for('auth.login'))  # Redirige al login después de cerrar sesión