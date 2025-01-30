
from flask_sqlalchemy import SQLAlchemy
from models.usuario import db, Usuario  # Importamos la instancia de la base de datos y el modelo Usuario

db = SQLAlchemy()

class Paciente(db.Model):
    __tablename__ = 'paciente'

    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), unique=True, nullable=False)  # Relación con Usuario
    dni = db.Column(db.String(20), unique=True, nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    sexo = db.Column(db.String(1), nullable=False)
    obra_social = db.Column(db.String(100))
    domicilio = db.Column(db.String(255), nullable=False)
    telefono = db.Column(db.String(20), nullable=False)
    correo = db.Column(db.String(120), unique=True, nullable=False)

    # Relación con Usuario (cada paciente tiene un usuario)
    usuario = db.relationship('Usuario', backref=db.backref('paciente', uselist=False))

    def __repr__(self):
        return f'<Paciente {self.nombre} {self.apellido}>'
