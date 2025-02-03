# app/test/test_connection.py

from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
import os

def test_db_connection():
    # URL de la base de datos PostgreSQL (asegúrate de que sea la correcta)
    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://neondb_owner:npg_Pul1nec6gGhR@ep-sweet-hill-a8xmighl-pooler.eastus2.azure.neon.tech/neondb?sslmode=require")
    
    # Crear el motor de conexión
    engine = create_engine(DATABASE_URL)
    
    try:
        # Intentar conectar
        connection = engine.connect()
        print("Conexión exitosa a la base de datos.")
        connection.close()
    except SQLAlchemyError as e:
        # Si ocurre un error, mostrar el mensaje de error
        print(f"Error de conexión: {e}")
    except Exception as e:
        # Capturar otros posibles errores
        print(f"Error inesperado: {e}")

# Llamar a la función de prueba de conexión
if __name__ == "__main__":
    test_db_connection()
