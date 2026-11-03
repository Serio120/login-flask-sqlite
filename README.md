# Inicio de sesión con Flask y SQLite

Aplicación educativa de autenticación con Flask, SQLite y sesiones.

## Requisitos

- Python 3.10 o superior
- pip

## Instalación

```bash
git clone https://github.com/Serio120/login-flask-sqlite.git
cd login-flask-sqlite
python -m venv .venv
```

Activa el entorno virtual:

```bash
# Linux / macOS
source .venv/bin/activate

# Windows PowerShell
.venv\\Scripts\\Activate.ps1
```

Instala dependencias:

```bash
pip install -r requirements.txt
```

## Configuración

Define una clave secreta propia para firmar las sesiones. No uses una clave fija en el código ni compartas el valor:

```bash
# Linux / macOS
export FLASK_SECRET_KEY="$(python -c 'import secrets; print(secrets.token_hex(32))')"

# Windows PowerShell
$env:FLASK_SECRET_KEY = python -c "import secrets; print(secrets.token_hex(32))"
```

Opcionalmente, configura la ruta de la base de datos mediante `DATABASE_PATH`. Por defecto se utiliza `usuarios.db` en el directorio actual.

## Inicializar y crear un usuario

La aplicación crea la tabla si no existe. Para crear un usuario de prueba sin almacenar contraseñas en texto plano:

```bash
# Linux / macOS
export APP_USERNAME="usuario_prueba"
export APP_PASSWORD="elige-una-contraseña"
python agre_usu.py

# Windows PowerShell
$env:APP_USERNAME = "usuario_prueba"
$env:APP_PASSWORD = "elige-una-contraseña"
python agre_usu.py
```

El script guarda el hash de la contraseña, no la contraseña original.

## Ejecutar

```bash
python app.py
```

Abre [http://127.0.0.1:5000/login](http://127.0.0.1:5000/login).

Rutas disponibles:

- `GET /login`: muestra el formulario.
- `POST /login`: valida las credenciales.
- `GET /bienvenido`: requiere una sesión iniciada.
- `GET /logout`: cierra la sesión.

## Tests

```bash
python -m unittest discover -v
```

Las pruebas usan una base SQLite temporal y no modifican la base de datos local.

## Seguridad y limitaciones

- Las contraseñas nuevas se almacenan mediante hashes de Werkzeug.
- Las contraseñas heredadas en texto plano se convierten a hash después de un inicio de sesión correcto.
- La clave de sesión se obtiene de `FLASK_SECRET_KEY`; la aplicación no arranca si falta.
- El modo debug está desactivado.
- Este repositorio es un ejemplo didáctico, no una solución de autenticación lista para producción. Antes de desplegarlo, añade protección CSRF, limitación de intentos, HTTPS, gestión de usuarios y revisión de configuración.
