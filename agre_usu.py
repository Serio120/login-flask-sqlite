from conexion import obtener_conexion
conexion = obtener_conexion()
cursor = conexion.cursor()
cursor.execute('INSERT INTO usuarios (username, password) VALUES (?, ?)', ('usuario_prueba', 'contraseña123'))
conexion.commit()
conexion.close()