<h1 align="center">
    <b>Proyecto de Inicio de Sesión con Flask y SQLite</b>
</h1>


# Estructura del Proyecto
Este es un ejemplo de la estructura de un proyecto de Flask que incluye una página de inicio de sesión y una base de datos SQLite. A continuación se muestra cómo debería organizarse el proyecto:

```plaintext
/mi_proyecto
│
├── /templates
│   └── login.html
│
├── app.py
├── conexion.py
└── inicializar_db.py
```


# Descripción de los Archivos
- `app.py`: Este es el archivo principal de la aplicación Flask donde se define la ruta
    de inicio de sesión y se configura la aplicación.
    - `conexion.py`: Este archivo contiene la lógica para conectarse a la base de datos SQLite.
    - `inicializar_db.py`: Este archivo se utiliza para inicializar la base de datos SQLite y crear la tabla de usuarios.
    - `templates/login.html`: Este es el archivo HTML que define la interfaz de usuario para la página de inicio de sesión.
    - `agre_usu.py`: Permite agregar usuarios manualmente a la base de datos, facilitando las pruebas del sistema de inicio de sesión antes de su uso en producción.
    - `login.html`: Contiene la estructura HTML de la página de inicio de sesión, permitiendo separar la lógica de la aplicación de la presentación visual.
    # Orden de Creación

1. Archivo: `app.py`
Este archivo contiene la configuración de la aplicación Flask y las rutas necesarias para el sistema de login.

2. Archivo: `conexion.py`
Este archivo maneja la conexión a la base de datos SQLite.

3. Archivo: `inicializar_db.py`
Este archivo se utiliza para crear la tabla de usuarios en la base de datos.
 
4. Archivo: `templates/login.html`
Este archivo contiene el formulario HTML para el inicio de sesión.

5. Agregar un Usuario Manualmente: `agre_usu.py`
Antes de probar el inicio de sesión, puedes agregar un usuario manualmente en la base de datos SQLite. Puedes hacerlo ejecutando el siguiente código en un script separado o en un intérprete de Python:

6. Ejecutar la Aplicación
Para ejecutar la aplicación, abre una terminal, navega a la carpeta del proyecto y ejecuta: `python app.py`
   
---
   
## Serio120: @workspace /explain 



    


