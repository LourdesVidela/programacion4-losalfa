from flask_sqlalchemy import SQLAlchemy
from models.usuario import db, Usuario  # Importamos la instancia de la base de datos y el modelo Usuario

db = SQLAlchemy()

class Doctor(db.Model):
    __tablename__ = 'doctor'

    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), unique=True, nullable=False)  # Relación con Usuario
    especialidad = db.Column(db.String(100), nullable=False)
    matricula = db.Column(db.String(50), unique=True, nullable=False)
    telefono = db.Column(db.String(20), nullable=False)
    correo = db.Column(db.String(120), unique=True, nullable=False)

    # Relación con Usuario (cada doctor tiene un usuario)
    usuario = db.relationship('Usuario', backref=db.backref('doctor', uselist=False))

    def __repr__(self):
        return f'<Doctor {self.usuario.usuario}>'
