# models/usuario.py
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model, UserMixin):
    __tablename__ = 'usuario'

    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(50), unique=True, nullable=False)
    contraseña = db.Column(db.String(200), nullable=False)
    rol = db.Column(db.String(20), nullable=False)  # admin, doctor, paciente, secretario

    def verificar_contraseña(self, contraseña):
        return check_password_hash(self.contraseña, contraseña)

    def set_contraseña(self, contraseña):
        """Hash de la contraseña antes de guardarla"""
        self.contraseña = generate_password_hash(contraseña)

    def get_id(self):
        return str(self.id)  # Flask-Login requiere que get_id retorne el ID del usuario como cadena

# Crear los usuarios admin y secretario si no existen
def crear_usuarios_iniciales():
    # Verificar si el usuario admin ya existe
    admin = Usuario.query.filter_by(usuario='admin').first()
    if not admin:
        admin = Usuario(usuario='admin', rol='admin')
        admin.set_contraseña('admin123')  # Establecer la contraseña por defecto para el admin
        db.session.add(admin)
    
    # Verificar si el usuario secretario ya existe
    secretario = Usuario.query.filter_by(usuario='secretario').first()
    if not secretario:
        secretario = Usuario(usuario='secretario', rol='secretario')
        secretario.set_contraseña('secretario123')  # Establecer la contraseña por defecto para el secretario
        db.session.add(secretario)
    
    # Confirmar los cambios en la base de datos
    db.session.commit()
