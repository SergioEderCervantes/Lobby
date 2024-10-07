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

Instala los requisitos del proyecto ejecutando el siguiente comando:

```bash
 pip install -r local.txt
```

# Ejecutando el proyecto

Realiza las migraciones necesarias:

```bash
python manage.py migrate
```

Inicia el servidor con el siguiente comando:

```bash
python manage.py runserver

```
