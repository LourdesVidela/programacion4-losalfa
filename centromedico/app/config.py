import os

class Config:
    # URL de conexión a la base de datos PostgreSQL
    SQLALCHEMY_DATABASE_URI = "postgresql://neondb_owner:npg_Pul1nec6gGhR@ep-sweet-hill-a8xmighl-pooler.eastus2.azure.neon.tech/neondb?sslmode=require"
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Deshabilitar el seguimiento de modificaciones (opcional)
    SECRET_KEY = os.urandom(24)  # Asegúrate de usar una clave secreta para sesiones y cookies
