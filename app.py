import hmac
import os
from contextlib import closing

from flask import Flask, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

from conexion import obtener_conexion

app = Flask(__name__)
secret_key = os.environ.get("FLASK_SECRET_KEY")
if not secret_key:
    raise RuntimeError("Define FLASK_SECRET_KEY antes de iniciar la aplicación.")

app.config.update(
    SECRET_KEY=secret_key,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="Lax",
)


def inicializar_base_de_datos():
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


inicializar_base_de_datos()


def verificar_contrasena(stored_password, password):
    """Verify modern hashes and migrate legacy plaintext passwords on success."""
    try:
        if check_password_hash(stored_password, password):
            return True, False
    except (ValueError, TypeError):
        pass

    if hmac.compare_digest(stored_password, password):
        return True, True
    return False, False


@app.route("/login", methods=["GET", "POST"])
def login():
    mensaje = ""
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        with closing(obtener_conexion()) as conexion:
            usuario = conexion.execute(
                "SELECT id, username, password FROM usuarios WHERE username = ?",
                (username,),
            ).fetchone()

            if usuario:
                valido, necesita_migracion = verificar_contrasena(usuario[2], password)
                if valido:
                    if necesita_migracion:
                        conexion.execute(
                            "UPDATE usuarios SET password = ? WHERE id = ?",
                            (generate_password_hash(password), usuario[0]),
                        )
                        conexion.commit()

                    session.clear()
                    session["usuario"] = usuario[1]
                    return redirect(url_for("bienvenido"))

        mensaje = "Usuario o contraseña incorrectos"

    return render_template("login.html", mensaje=mensaje)


@app.route("/bienvenido")
def bienvenido():
    if "usuario" in session:
        return f"Bienvenido, {session['usuario']}!"
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=False)
