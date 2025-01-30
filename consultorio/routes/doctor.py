from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Doctor(db.Model):
    __tablename__ = 'doctors'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    especialidad = db.Column(db.String(100), nullable=False)
    numero_matricula = db.Column(db.String(50), nullable=False, unique=True)
    obra_social = db.Column(db.String(100), nullable=False)
    
    turnos = db.relationship('Turno', backref='doctor', lazy=True)  # Relación con Turno

    def __repr__(self):
        return f"<Doctor {self.nombre}>"
