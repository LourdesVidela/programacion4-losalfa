from app import db


class Doctor(db.Model):
    __tablename__ = 'doctor'  # Asegúrate de que el nombre de la tabla sea 'doctor'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    especialidad = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(20), nullable=False)
    direccion = db.Column(db.String(200), nullable=False)
    obra_social = db.Column(db.String(200), nullable=False)  # Obras sociales en formato string separadas por comas

    user_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), unique=True, nullable=False)
    usuario = db.relationship('Usuario', backref=db.backref('doctor', uselist=False))

    def __repr__(self):
        return f"<Doctor {self.nombre} - Especialidad: {self.especialidad}>"

    def get_obras_sociales(self):
        """Devuelve las obras sociales como una lista."""
        return self.obra_social.split(",")  # Convierte la cadena separada por coma en una lista