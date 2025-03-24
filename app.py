from flask import Flask, render_template, request
from modelo import analizar_sentimiento
from db_config import obtener_conexion
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    porcentaje = None
    comentario = ""

    if request.method == "POST":
        comentario = request.form["comentario"]
        resultado, porcentaje = analizar_sentimiento(comentario)

        # Guardar en la base de datos
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO comentarios (comentario, resultado, porcentaje) VALUES (%s, %s, %s)",
            (comentario, resultado, float(porcentaje))
        )
        conexion.commit()
        cursor.close()
        conexion.close()

    return render_template("index.html", comentario=comentario, resultado=resultado, porcentaje=porcentaje)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # Railway usa esta variable
    app.run(host="0.0.0.0", port=port)
