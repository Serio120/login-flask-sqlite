import os
import sqlite3


def obtener_conexion():
    """Open the configured SQLite database."""
    database_path = os.environ.get("DATABASE_PATH", "usuarios.db")
    return sqlite3.connect(database_path)
