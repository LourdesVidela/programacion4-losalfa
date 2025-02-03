#user_model.py
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db

class Usuario(db.Model, UserMixin):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Usuario {self.username}>'

    def set_password(self, password):
        """Encripta la contraseña antes de almacenarla."""
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """Verifica que la contraseña proporcionada coincida con la almacenada (hashed)."""
        return check_password_hash(self.password, password)

    def get_id(self):
        """Requiere ser implementado por Flask-Login."""
        return str(self.id)  # Devuelve el ID del usuario como una cadena