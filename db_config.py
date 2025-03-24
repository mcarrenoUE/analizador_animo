import mysql.connector

def obtener_conexion():
    return mysql.connector.connect(
        host="crossover.proxy.rlwy.net",
        port=11217,
        user="root",
        password="KCIFXNUBDLfUcarzcqUjbBWTaIFmPOQc",
        database="railway"
    )

