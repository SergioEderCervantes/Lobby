# Lobby Restaurant Bar

Este proyecto es un sistema para gestionar un restaurante/bar llamado Lobby.

## Creación del entorno virtual

Para crear el entorno virtual fuera del proyecto, sigue los siguientes pasos:

1. Sal del directorio del proyecto:

   ```bash
   cd ..
   ```

2. Crea el entorno virtual:

   ```bash
   virtualenv nombre_de_tu_entorno_virtual
   ```

3. Activa el entorno virtual:

   - En Windows:

     ```bash
     .\nombre_de_tu_entorno_virtual\Scripts\activate
     ```

   - En macOS/Linux:

     ```bash
     source nombre_de_tu_entorno_virtual/bin/activate
     ```

4. Regresa al directorio del proyecto:

## Instalación de requisitos

Instala los requisitos Python del proyecto ejecutando el siguiente comando:

```bash
 pip install -r local.txt
```

Aparte, instala los requisitos JavaScript del proyecto ejecutando el siguiente comando:

```bash
 npm install
```

# Ejecutando el proyecto

Realiza las migraciones necesarias:

````bash
python manage.py migrate

Inicia el servidor con el siguiente comando:

```bash
python manage.py runserver

````

# Reseteo de base de datos

Cuando se hacen cambios grandes e importantes en el proyecto y no hay aun datos importantes que se quieran conservar en la base de datos,
es recomendable hacer un reset de la base de datos y las migraciones para que funcione de manera adecuada.
Pasos para resetear la base de datos:

1. Borra la base de datos:
   En mySQL workbench, borra la base de datos, esta es la manera mas rapida y sencilla de resetearla

```sql
DROP DATABASE lobby;
```

2. Crea nuevamente la base de datos:
   Igualmente en mySQL workbench, crea la base de datos

```sql
CREATE DATABASE lobby;
```

3. Borra las migraciones antiguas

Ahora, abre una terminal powershell en el proyecto de lobby (con el entorno virtual encendido) y ejecuta este comando

```powershell
Get-ChildItem -Recurse -File -Include "*.py" | Where-Object { $_.Name -ne "__init__.py" -and $_.DirectoryName -match "migrations" } | Remove-Item -Force

```

O si es en linux/MacOS:

```bash
find . -path "*/migrations/*.py" ! -name "__init__.py" -delete
```

Esto borrara todas las migraciones exepto el init.py, ya que es necesaria, sin embargo no pasa nada con los cambios que hayas hecho a tus
modelos, ya que con el siguiente comando se crearan todas las migraciones necesarias mas aparte tus migraciones propias de tus modelos

4. Crea las migraciones limpias

En la misma terminal del panel anterior, ejecuta el siguiente comando para crear todas las migraciones del proyecto

```bash
python manage.py makemigrations
```

5. Realiza la migracion

Por ultimo, ejecuta las migraciones recien creadas:

```bash
python manage.py migrate
```

Con estos pasos, la base de datos queda limpia y actualizada con la estructura necesaria

# Entorno

1. Crear una carpeta llamada .django en el directorio raiz del proyecto

2. Pegar el archivo .env en donde pondremos las variables del entorno

3. Pegar el archivo secret y lobby dentro de la carpeta .django

4. Crear una carpeta tmp en C:/

5. Ejecutar el comando

```bash
python manage.py runserver_plus --cert-file /tmp/cert
```
