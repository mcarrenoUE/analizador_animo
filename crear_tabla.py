from db_config import obtener_conexion

conexion = obtener_conexion()
cursor = conexion.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS comentarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    comentario TEXT NOT NULL,
    resultado VARCHAR(20),
    porcentaje FLOAT,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conexion.commit()
cursor.close()
conexion.close()

print("✅ Tabla creada en Railway")
