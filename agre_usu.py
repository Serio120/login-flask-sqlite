import os
from contextlib import closing

from werkzeug.security import generate_password_hash

from conexion import obtener_conexion


def agregar_usuario(username, password):
    if not username or not password:
        raise ValueError("El usuario y la contraseña son obligatorios.")

    with closing(obtener_conexion()) as conexion:
        conexion.execute(
            "INSERT INTO usuarios (username, password) VALUES (?, ?)",
            (username, generate_password_hash(password)),
        )
        conexion.commit()


if __name__ == "__main__":
    username = os.environ.get("APP_USERNAME")
    password = os.environ.get("APP_PASSWORD")
    if not username or not password:
        raise SystemExit("Define APP_USERNAME y APP_PASSWORD en el entorno.")
    agregar_usuario(username, password)
