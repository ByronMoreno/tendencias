# Material de Clases: Docker y Despliegue de Aplicaciones

Repositorio de contenidos y laboratorios prácticos para la materia de **Tendencias Actuales de Programación** (Instituto Superior Tecnológico Yavirac).

---

## 📚 Módulos y Semanas de Clase

| Módulo | Tema Principal | Tecnologías | Recursos Clave |
|---|---|---|---|
| **Semana 1** | Introducción a Docker Desktop y Despliegue Web | Docker, Python 3.12, Flask, WSL 2 | [Plan Docente](file:///d:/YAVIRAC/tendencias/CLASE_DOCENTE.md) \| [Guía Estudiante](file:///d:/YAVIRAC/tendencias/GUIA_ESTUDIANTE.md) \| [Cheat Sheet](file:///d:/YAVIRAC/tendencias/CHEAT_SHEET_DOCKER.md) \| [Código Demo](file:///d:/YAVIRAC/tendencias/hola-flask/) |
| **Semana 2** | Aplicación Web Multi-contenedor con Base de Datos Persistente | Docker Compose, Python, Flask, PostgreSQL 16, Volúmenes | [Guía Completa Semana 2](file:///d:/YAVIRAC/tendencias/semana%202/GUIA_SEMANA_2.md) \| [Código y Compose](file:///d:/YAVIRAC/tendencias/semana%202/) |

---

## 📁 Estructura del Repositorio

```text
tendencias/
├── CLASE_DOCENTE.md            # Plan de clase docente - Semana 1
├── GUIA_ESTUDIANTE.md          # Manual de laboratorio estudiante - Semana 1
├── CHEAT_SHEET_DOCKER.md       # Hoja de atajos y comandos de Docker
├── hola-flask/                 # Proyecto práctico Semana 1 (Hola Mundo con Flask)
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── README.md
└── semana 2/                   # Proyecto práctico Semana 2 (Flask + PostgreSQL)
    ├── app.py                  # Web Flask con CRUD y reconexión a Postgres
    ├── requirements.txt        # Flask y psycopg2-binary
    ├── Dockerfile              # Empaquetado de la aplicación Python
    ├── docker-compose.yml      # Orquestación de app web + base de datos
    ├── .dockerignore           # Exclusiones de construcción
    ├── README.md               # Comandos de ejecución rápida
    └── GUIA_SEMANA_2.md        # Guía paso a paso, arquitectura y reto evaluado
```

---

## 🚀 Inicio Rápido para Semana 2

```powershell
cd "d:\YAVIRAC\tendencias\semana 2"
docker compose up --build -d
Start-Process http://localhost:5000
```
