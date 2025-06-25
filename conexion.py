import sqlite3
def obtener_conexion():
    """Establecer y devolver una conexión a la base de datos SQLite."""
    return sqlite3.connect('usuarios.db')