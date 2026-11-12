# INSTITUTO SUPERIOR TECNOLÓGICO YAVIRAC
## CARRERA DE DESARROLLO DE SOFTWARE
### ASIGNATURA: Tendencias Actuales de Programación

---

# GUÍA DE TALLER PRÁCTICO EVALUATORIO
## Despliegue de Servicios Contenedorizados con Docker en Servidor Remoto (v1 y v2)

- **Servidor Remoto:** `161.97.140.245`
- **Modalidad:** Taller Práctico Individual / Parejas (según indicación docente)
- **Documento editable para entrega:** [Taller_Practico_Docker_Servidor_Remoto.docx](file:///d:/YAVIRAC/tendencias/Taller_Practico_Docker_Servidor_Remoto.docx)

---

## 1. Datos Informativos

| Campo | Detalle |
|---|---|
| **Estudiante:** | `[Nombres y Apellidos del Estudiante]` |
| **Fecha de Realización / Entrega:** | `____ / ____ / 2026` |
| **Nivel / Paralelo / Jornada:** | `________________________` |
| **Asignatura:** | Tendencias Actuales de Programación |
| **Docente:** | Cátedra de Tendencias Actuales de Programación |
| **Servidor Destino:** | `161.97.140.245` (Linux Ubuntu Server) |
| **Calificación:** | `______ / 10.00 pts` |

---

## 2. Objetivo del Taller

Desplegar un microservicio o servicio web desarrollado en el lenguaje de su preferencia (**Python, Node.js, Java, Go, PHP, etc.**) empaquetado en un **único contenedor Docker** dentro del servidor remoto `161.97.140.245`, utilizando las credenciales asignadas en clase.

El estudiante debe registrar y documentar detalladamente el flujo completo:
1. Declaración de dependencias.
2. Construcción del `Dockerfile`.
3. Transferencia de archivos al servidor (`scp`, `rsync` o `git`).
4. Conexión segura por `ssh`.
5. Compilación de la imagen Docker etiquetada (`docker build`).
6. Despliegue del contenedor con mapeo de puertos (`docker run`).
7. Comprobación y demostración del servicio activo con sus **Nombres Completos**.
8. **Reto Evaluatorio de Versionamiento (v2):** Modificar el código para agregar el mensaje **"Yo estudio en Yavirac"**, compilar una nueva imagen `:v2`, desplegar el servicio actualizado y demostrar el nuevo estado.

> [!IMPORTANT]
> **Requisito del Código de la App:** No es necesario documentar exhaustivamente cómo programó la aplicación línea por línea. Sin embargo, en la respuesta del servicio web (página web o JSON en el navegador/curl) **DEBEN figurar de forma obligatoria y clara sus Nombres Completos**.

---

## 3. Datos del Entorno y Parámetros del Servidor

- **Host / IP Pública:** `161.97.140.245`
- **Puerto SSH:** `22` (por defecto o el indicado en el aula)
- **Credenciales:** Usuario y contraseña proporcionados por el docente.
- **Puerto de Aplicación en el Servidor:** Cada estudiante debe usar el puerto asignado para no colisionar con sus compañeros (ejemplo: `5001`, `5002`, `8081`, etc.).
- **Motor Docker:** Docker Engine instalado en el servidor remoto.

---

## 4. Estructura del Informe Paso a Paso (Versión 1)

Cada paso del documento de Word cuenta con tres bloques esenciales:
- 📝 **Explicación del Estudiante:** Redacción técnica propia justificando decisiones y funcionamiento.
- 💻 **Comandos Utilizados:** Sintaxis exacta de los comandos ejecutados en terminal local y remota.
- 📷 **Evidencia Gráfica:** Captura de pantalla de la terminal o navegador demostrando el resultado.

### 4.1 Selección Tecnológica y Definición de Dependencias
- Elección del lenguaje y framework (ej. Python + Flask, Node.js + Express, Java + Spring Boot, etc.).
- Definición del archivo de dependencias (`requirements.txt`, `package.json`, etc.).
- Comprobación de que la salida del servicio contendrá sus **Nombres Completos**.

### 4.2 Creación y Configuración del Dockerfile
- Explicación de cada instrucción utilizada:
  - `FROM`: Imagen base seleccionada y justificación (versión específica, ej: `python:3.12-slim`, `node:20-alpine`).
  - `WORKDIR`: Directorio de trabajo dentro del contenedor.
  - `COPY`: Transferencia de artefactos hacia el contexto de la imagen.
  - `RUN`: Instalación de paquetes y dependencias en tiempo de compilación.
  - `EXPOSE`: Documentación del puerto interno de escucha.
  - `CMD` / `ENTRYPOINT`: Comando de arranque del servicio.

### 4.3 Transferencia de Archivos al Servidor Remoto (161.97.140.245)
- Comando de transferencia desde la máquina local hacia el servidor:
  ```bash
  scp -r ./mi-proyecto usuario@161.97.140.245:/home/usuario/
  # o alternativamente:
  rsync -avz ./mi-proyecto/ usuario@161.97.140.245:/home/usuario/mi-proyecto/
  ```
- Conexión vía SSH al servidor:
  ```bash
  ssh usuario@161.97.140.245
  ```
- Verificación del árbol de archivos en el servidor:
  ```bash
  cd /home/usuario/mi-proyecto
  ls -la
  ```

### 4.4 Construcción de la Imagen Docker en el Servidor (Versión 1 - v1)
- Compilación de la imagen en el servidor remoto utilizando etiquetado de versión:
  ```bash
  docker build -t mi-servicio-estudiante:v1 .
  ```
- Verificación en el registro local de Docker:
  ```bash
  docker images | grep mi-servicio-estudiante
  ```

### 4.5 Despliegue y Ejecución del Contenedor (Servicio v1)
- Ejecución en segundo plano con mapeo de puertos y política de reinicio:
  ```bash
  docker run -d -p 5001:5000 --name contenedor-servicio-v1 --restart unless-stopped mi-servicio-estudiante:v1
  ```
- Inspección de estado y logs:
  ```bash
  docker ps
  docker logs --tail 20 contenedor-servicio-v1
  ```

### 4.6 Verificación y Demostración del Servicio en Funcionamiento (v1)
- Acceso desde navegador web cliente o cliente HTTP:
  ```text
  http://161.97.140.245:5001
  ```
- O mediante curl:
  ```bash
  curl -i http://161.97.140.245:5001
  ```
- **Evidencia requerida:** Captura de pantalla donde se visualice la IP `161.97.140.245:PUERTO` y los **Nombres Completos del Estudiante**.

---

## 5. Reto Evaluatorio: Versionamiento y Actualización (Versión 2 - v2)

> [!WARNING]
> **RETO OBLIGATORIO DE ACTUALIZACIÓN:**
> Una vez comprobada la Versión 1, el estudiante debe:
> 1. Modificar el código fuente de la aplicación para agregar de manera visible el mensaje:
>    ### **"Yo estudio en Yavirac"**
>    *(Manteniendo también sus nombres completos).*
> 2. Construir una **nueva versión de la imagen Docker** con el tag `:v2`.
> 3. Desplegar el **nuevo servicio actualizado** en el servidor remoto.
> 4. Documentar los comandos de parada/reemplazo del contenedor y evidenciar la salida de la Versión 2.

### Tareas a completar por el estudiante en esta sección:
1. **Explicación del cambio:** Indicar el archivo modificado y la lógica agregada.
2. **Construcción de la imagen v2:**
   ```bash
   docker build -t mi-servicio-estudiante:v2 .
   docker images | grep mi-servicio-estudiante
   ```
3. **Estrategia de reemplazo del contenedor:**
   ```bash
   # Detener y remover contenedor v1 para liberar el puerto
   docker stop contenedor-servicio-v1
   docker rm contenedor-servicio-v1

   # Desplegar el nuevo contenedor con la versión 2
   docker run -d -p 5001:5000 --name contenedor-servicio-v2 --restart unless-stopped mi-servicio-estudiante:v2
   docker ps
   ```
4. **Evidencia del servicio v2 activo:**
   - Captura del navegador / curl mostrando:
     - `http://161.97.140.245:PUERTO`
     - Mensaje: **"Yo estudio en Yavirac"**
     - Nombres Completos del Estudiante.

---

## 6. Cuestionario de Fundamentación Técnica

1. **Mapeo de Puertos (`-p Host:Contenedor`):**
   ¿Cuál es la diferencia entre el primer puerto y el segundo puerto en `-p 8080:5000`? ¿Qué error arrojaría Docker si dos estudiantes intentan usar el mismo puerto en el host?
2. **Buenas Prácticas de Versionamiento:**
   ¿Por qué en producción no debe usarse el tag `:latest` y qué ventaja ofrece tener imágenes con etiquetas `:v1` y `:v2` al momento de hacer un rollback?
3. **Políticas de Resiliencia (`--restart`):**
   ¿Qué función cumple `--restart unless-stopped` ante un reinicio del sistema operativo del servidor `161.97.140.245`?
4. **Comparación Arquitectónica:**
   ¿Qué ventajas aportó desplegar este servicio con Docker frente a instalar manualmente las dependencias directamente en el sistema operativo del servidor?

---

## 7. Rúbrica de Evaluación

| Criterio | Descripción | Puntaje |
|---|---|:---:|
| **1. Dockerfile y Dependencias** | Correcta configuración del archivo de dependencias y explicación técnica de las directivas del Dockerfile. | 2.00 pts |
| **2. Transferencia y Acceso SSH** | Uso adecuado de comandos de transferencia remota (`scp`/`rsync`/`git`) y conexión SSH al servidor `161.97.140.245`. | 1.50 pts |
| **3. Despliegue de Versión 1** | Compilación de imagen v1, ejecución del contenedor en segundo plano y verificación del servicio con nombres completos. | 2.50 pts |
| **4. Reto de Actualización (v2)** | Inclusión del mensaje *"Yo estudio en Yavirac"*, construcción de imagen `:v2`, reemplazo del contenedor y evidencia del servicio v2. | 2.50 pts |
| **5. Cuestionario y Conclusiones** | Calidad de las respuestas técnicas, sintaxis precisa de comandos y conclusiones con criterio profesional. | 1.50 pts |
| **TOTAL** | **Calificación Final sobre 10** | **10.00 pts** |
