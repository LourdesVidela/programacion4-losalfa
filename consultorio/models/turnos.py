from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Turno(db.Model):
    __tablename__ = 'turnos'

    id = db.Column(db.Integer, primary_key=True)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'), nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    hora_inicio = db.Column(db.Time, nullable=False)
    hora_fin = db.Column(db.Time, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "doctor_id": self.doctor_id,
            "fecha": self.fecha.strftime('%Y-%m-%d'),
            "hora_inicio": self.hora_inicio.strftime('%H:%M'),
            "hora_fin": self.hora_fin.strftime('%H:%M')
        }

    def __repr__(self):
        return f"<Turno Doctor ID {self.doctor_id} - {self.fecha} {self.hora_inicio} - {self.hora_fin}>"
