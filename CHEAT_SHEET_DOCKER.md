# 🐳 Docker Cheat Sheet para Windows (PowerShell / CMD)

Referencia rápida de comandos fundamentales para la clase de **Tendencias Actuales de Programación**.

---

## 1. Verificación del Sistema

| Comando | Descripción |
|---|---|
| `docker --version` | Muestra la versión del cliente de Docker. |
| `docker compose version` | Muestra la versión de Docker Compose. |
| `docker info` | Información detallada del sistema, motor y configuración de WSL 2. |
| `docker run hello-world` | Descarga y ejecuta el contenedor de prueba oficial. |

---

## 2. Gestión de Imágenes (`Images`)

| Comando | Descripción |
|---|---|
| `docker images` | Lista todas las imágenes almacenadas localmente. |
| `docker pull <imagen>:<tag>` | Descarga una imagen desde Docker Hub (ej: `docker pull python:3.12-slim`). |
| `docker build -t <nombre> .` | Construye una imagen a partir del `Dockerfile` en el directorio actual (`.`). |
| `docker rmi <nombre-o-id>` | Elimina una imagen local (no debe tener contenedores asociados). |
| `docker rmi -f <nombre-o-id>` | Fuerza la eliminación de una imagen. |
| `docker image prune -a` | Limpia y elimina todas las imágenes que no estén siendo usadas. |

---

## 3. Ciclo de Vida de Contenedores (`Containers`)

| Comando | Descripción |
|---|---|
| `docker ps` | Lista únicamente los contenedores **en ejecución**. |
| `docker ps -a` | Lista **todos** los contenedores (activos, detenidos y fallidos). |
| `docker run -d --name <nombre> -p <host>:<cont> <imagen>` | Crea y arranca un contenedor en segundo plano (`-d`) con mapeo de puertos (`-p`). |
| `docker stop <nombre-o-id>` | Detiene de forma segura un contenedor en marcha. |
| `docker start <nombre-o-id>` | Inicia un contenedor previamente detenido. |
| `docker restart <nombre-o-id>` | Reinicia el contenedor. |
| `docker rm <nombre-o-id>` | Elimina un contenedor detenido. |
| `docker rm -f <nombre-o-id>` | **Fuerza la detención y eliminación** inmediata de un contenedor. |
| `docker container prune` | Elimina todos los contenedores detenidos del sistema. |

---

## 4. Diagnóstico, Logs e Inspección

| Comando | Descripción |
|---|---|
| `docker logs <nombre>` | Muestra la salida estándar y errores registrados por la aplicación. |
| `docker logs -f <nombre>` | Monitorea los logs en **tiempo real** (modo interactivo, salir con `Ctrl + C`). |
| `docker inspect <nombre>` | Muestra un JSON con la configuración técnica completa (redes, IP, volúmenes, puertos). |
| `docker top <nombre>` | Muestra los procesos en ejecución dentro del contenedor. |
| `docker exec -it <nombre> sh` | Abre una terminal interactiva dentro del contenedor en ejecución. |

---

## 5. El Flujo de Trabajo en Nuestra Clase (Paso a Paso)

```powershell
# 1. Posicionarse en la carpeta del proyecto
cd d:\YAVIRAC\tendencias\hola-flask

# 2. Construir la imagen con el tag "hola-flask"
docker build -t hola-flask .

# 3. Correr el contenedor en segundo plano en el puerto 5000
docker run -d --name hola-flask -p 5000:5000 hola-flask

# 4. Verificar que esté activo
docker ps

# 5. Revisar logs si algo no carga
docker logs hola-flask

# 6. Cuando modifiques el código: Reconstruir y Reemplazar
docker build -t hola-flask .
docker rm -f hola-flask
docker run -d --name hola-flask -p 5000:5000 hola-flask
```
