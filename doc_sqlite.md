> [!NOTE]
> Useful information that users should know, even when skimming content.
> 
> [!TIP]
> Helpful advice for doing things better or more easily.

> [!IMPORTANT]
> Key information users need to know to achieve their goal.

> [!WARNING]
> Urgent info that needs immediate user attention to avoid problems.

> [!CAUTION]
> Advises about risks or negative outcomes of certain actions.

```diff
diff --git a/filea.extension b/fileb.extension
index d28nd309d..b3nu834uj 111111
--- a/filea.extension
+++ b/fileb.extension
@@ -1,6 +1,6 @@
-oldLine
+newL
```

<h1 align="center">SQLite in SERVER</h1>

## Instalar Apache2

```
1 sudo apt update
2 sudo apt install apache2
```

## Instalar Gestor Base de Datos
```
1 sudo apt install sqlite3
2 sqlite3 –version
```

## Directorio en el que crear Base de Datos
```
1 cd ~		(directorio home del usuario actual) (AQUÍ SI TIENES PERMISOS)
```

## Si la has creado en otro directorio
```
1 mkdir ~/mydb
2 cp example.db ~/mydb/
3 cd ~/mydb
```

## Crear la base de datos y entrar dentro de ella
```
1 sqlite3 example.db
```

## Ejemplo de creación de una tabla
```
sqlite> CREATE TABLE mujeres (
id INTEGER PRIMARY KEY AUTOINCREMENT,
 vestido TEXT NOT NULL,
 zapatos TEXT NOT NULL UNIQUE
);
```

## Ejemplo de insertar registros
```
sqlite> INSERT INTO mujeres (vestido, zapatos) VALUES ('Traje', 'Zapato Verde');
 INSERT INTO mujeres (vestido, zapatos) VALUES ('Falda', 'Zapato Azul');
```

## Consulta de Registros
```diff
diff sqlite> SELECT * FROM mujeres;
```

<h1>Resumen rápido</h1>

```diff

diff ACCIÓN	                    COMANDO
--------------------------------------------------

+ Entrar a la BD	          sqlite3 example.db
+ Ver tablas	                .tables
+ Crear tabla	                CREATE TABLE ...
+ Insertar datos	           INSERT INTO ...
+ Ver datos	                 SELECT * FROM ...
+ Salir	                         .quit

```

----------------------------------------------
