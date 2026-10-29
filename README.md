# Material de Clase: Docker Desktop en Windows y Despliegue con Python & Flask

Este repositorio contiene el material didáctico completo para impartir el taller de **2 horas (120 minutos)** sobre virtualización ligera con Docker en entornos Windows, diseñado para la materia de **Tendencias Actuales de Programación**.

---

## 📁 Estructura del Material

| Archivo / Carpeta | Destinatario | Descripción |
|---|---|---|
| [**CLASE_DOCENTE.md**](file:///d:/YAVIRAC/tendencias/CLASE_DOCENTE.md) | **Docente** | Plan de clase estructurado (120 min), guión pedagógico, dinámicas para romper el hielo, analogías didácticas, preguntas clave y rúbrica de evaluación (25 pts). |
| [**GUIA_ESTUDIANTE.md**](file:///d:/YAVIRAC/tendencias/GUIA_ESTUDIANTE.md) | **Estudiantes** | Manual de laboratorio paso a paso: instalación de WSL 2, comandos con explicación visual, código explicado, resolución de problemas y reto práctico. |
| [**CHEAT_SHEET_DOCKER.md**](file:///d:/YAVIRAC/tendencias/CHEAT_SHEET_DOCKER.md) | **Ambos** | Hoja de referencia rápida con los comandos de Docker más utilizados en Windows (PowerShell/CMD). |
| [**hola-flask/**](file:///d:/YAVIRAC/tendencias/hola-flask/) | **Proyecto Demo** | Código fuente listo para probar: `app.py`, `requirements.txt`, `Dockerfile` y `.dockerignore`. |

---

## ⏱️ Resumen del Cronograma de Clase (120 min)

```
[00-10m] El problema "en mi PC sí funciona" (Debate)
   ↓
[10-30m] Conceptos: Docker vs VMs, Imagen vs Contenedor
   ↓
[30-45m] Verificación de Docker Desktop & WSL 2 (`docker run hello-world`)
   ↓
[45-60m] Comandos esenciales (`ps`, `images`, `logs`, `rm`, `rmi`)
   ↓
[60-90m] Práctica central: Crear app Flask y redactar Dockerfile
   ↓
[90-110m] Desafío práctico: Modificar código, reconstruir imagen y nueva ruta `/saludo`
   ↓
[110-120m] Evaluación con lista de cotejo y preguntas de cierre
```

---

## 🚀 Inicio Rápido para el Docente

Para probar todo el entorno antes de iniciar la sesión de clase, abre PowerShell en esta carpeta y ejecuta:

```powershell
cd d:\YAVIRAC\tendencias\hola-flask
docker build -t hola-flask .
docker run -d --name hola-flask -p 5000:5000 hola-flask
```

Abre tu navegador en: [http://localhost:5000](http://localhost:5000)
