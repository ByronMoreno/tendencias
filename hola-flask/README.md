# Proyecto de Demostración: Hola Mundo con Flask en Docker

Este es el proyecto base listo para la clase de **Docker Desktop en Windows**.

## Estructura de archivos

- `app.py`: Aplicación Flask con la ruta principal `/` y la ruta reto `/saludo/<nombre>`.
- `requirements.txt`: Dependencia fija `Flask==3.1.2`.
- `Dockerfile`: Especificación para construir la imagen ligera con Python 3.12-slim.
- `.dockerignore`: Evita que archivos temporales y entornos virtuales locales se copien a la imagen.

## Ejecución Rápida en Windows (PowerShell)

```powershell
# 1. Construir la imagen
docker build -t hola-flask .

# 2. Correr el contenedor
docker run -d --name hola-flask -p 5000:5000 hola-flask

# 3. Abrir en el navegador
Start-Process http://localhost:5000
Start-Process http://localhost:5000/saludo/Estudiante

# 4. Detener y limpiar cuando termine la prueba
docker stop hola-flask
docker rm hola-flask
```
