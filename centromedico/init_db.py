from app.models import Usuario
from app import db

def create_default_users():
    # Crea un usuario admin si no existe
    if not Usuario.query.filter_by(username='admin').first():
        admin = Usuario(username='admin', password='admin123', role='admin')
        db.session.add(admin)
        db.session.commit()

    # Crea un usuario secretario si no existe
    if not Usuario.query.filter_by(username='secretario').first():
        secretario = Usuario(username='secretario', password='secretario123', role='secretario')
        db.session.add(secretario)
        db.session.commit()
