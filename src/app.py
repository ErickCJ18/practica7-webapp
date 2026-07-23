from flask import Flask
import mysql.connector
import time

app = Flask(__name__)

@app.route("/")
def inicio():
    try:
        conexion = mysql.connector.connect(
            host="db",
            user="root",
            password="root123",
            database="practica"
        )

        if conexion.is_connected():
            conexion.close()
            return "<h1>Hola Mundo</h1><h2>Conexión exitosa a MySQL</h2>"

    except Exception as e:
        return f"<h1>Hola Mundo</h1><p>Error al conectar: {e}</p>"

if __name__ == "__main__":
    time.sleep(10)  # Espera a que MySQL termine de iniciar
    app.run(host="0.0.0.0", port=5000)
