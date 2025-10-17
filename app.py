import mysql.connector
import os
import streamlit as st

# Obtener las credenciales de las variables de entorno (seguridad)
host = os.getenv("DB_HOST", "bvi8kse5resdmgnhwhas-mysql.services.clever-cloud.com")
user = os.getenv("DB_USER", "uf1upeugsrw8g67z")
password = os.getenv("DB_PASSWORD", "NjCVNlurnppxc4VFyTiC")
database = os.getenv("DB_NAME", "bvi8kse5resdmgnhwhas")

# Intentar establecer la conexión
try:
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    
    # Verificar si la conexión fue exitosa
    if conn.is_connected():
        st.success("Conexión exitosa a la base de datos MySQL.")
    else:
        st.error("No se pudo conectar a la base de datos.")
        
except mysql.connector.Error as err:
    # Mostrar el error si la conexión falla
    st.error(f"Error al conectar con la base de datos: {err}")

finally:
    if conn.is_connected():
        # Cerrar la conexión
        conn.close()
