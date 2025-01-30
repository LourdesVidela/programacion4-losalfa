import os

class Config:
    # URL de conexión a la base de datos
    SQLALCHEMY_DATABASE_URI = "postgresql://neondb_owner:npg_Gf8YFrz4ghEI@ep-muddy-mode-a872v159-pooler.eastus2.azure.neon.tech/neondb?sslmode=require"
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Deshabilitar el seguimiento de modificaciones (opcional)
    SECRET_KEY = os.urandom(24)  # Asegúrate de usar una clave secreta para sesiones y cookies
