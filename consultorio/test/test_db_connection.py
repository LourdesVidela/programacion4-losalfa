# test/test_db_connection.py

import psycopg2
import pytest
from psycopg2 import OperationalError

# Configura la cadena de conexión a la base de datos
DATABASE_URL = "postgresql://neondb_owner:npg_Gf8YFrz4ghEI@ep-muddy-mode-a872v159-pooler.eastus2.azure.neon.tech/neondb?sslmode=require"

# Función para probar la conexión a la base de datos
def test_db_connection():
    try:
        # Intentamos establecer la conexión
        connection = psycopg2.connect(DATABASE_URL)
        cursor = connection.cursor()

        # Ejecutamos una simple consulta para verificar la conexión
        cursor.execute('SELECT 1')
        result = cursor.fetchone()

        # Aseguramos que el resultado de la consulta sea 1
        assert result == (1,)

        # Cerrar la conexión
        cursor.close()
        connection.close()

    except OperationalError as e:
        pytest.fail(f"Error de conexión a la base de datos: {e}")
