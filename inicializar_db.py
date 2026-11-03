from contextlib import closing

from conexion import obtener_conexion


def crear_tabla_usuarios():
    """Crear la tabla de usuarios si no existe."""
    with closing(obtener_conexion()) as conexion:
        conexion.execute(
            """
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
            """
        )
        conexion.commit()


if __name__ == "__main__":
    crear_tabla_usuarios()
