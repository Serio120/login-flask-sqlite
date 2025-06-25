from flask import Flask, render_template, request, redirect, url_for, session
from conexion import obtener_conexion

app = Flask(__name__)
app.secret_key = 'clave_secreta'  # Necesaria para manejar sesiones

# Crear la base de datos y la tabla de usuarios (se ejecuta una vez)
def inicializar_base_de_datos():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    ''')
    conexion.commit()
    conexion.close()

inicializar_base_de_datos()

@app.route('/login', methods=['GET', 'POST'])
def login():
    mensaje = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute('SELECT * FROM usuarios WHERE username = ? AND password = ?', (username, password))
        usuario = cursor.fetchone()
        conexion.close()
        if usuario:
            session['usuario'] = usuario[1]  # Guarda el nombre de usuario en la sesión
            return redirect(url_for('bienvenido'))
        else:
            mensaje = 'Usuario o contraseña incorrectos'
    return render_template('login.html', mensaje=mensaje)

@app.route('/bienvenido')
def bienvenido():
    if 'usuario' in session:
        return f"Bienvenido, {session['usuario']}!"
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
