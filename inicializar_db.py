from conexion import obtener_conexion
def crear_tabla_usuarios():
    """Crear la tabla 'usuarios' si no existe."""
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
    ''')
    conexion.commit()
    conexion.close()
if __name__ == '__main__':
    crear_tabla_usuarios()