# Semana 2: Aplicación Web Python + Base de Datos PostgreSQL con Docker Compose

Proyecto multi-contenedor para la materia de **Tendencias Actuales de Programación** (Instituto Superior Tecnológico Yavirac).

## 🚀 Inicio Rápido en Windows (PowerShell)

```powershell
# 1. Ingresar a la carpeta de la semana 2
cd "d:\YAVIRAC\tendencias\semana 2"

# 2. Construir e iniciar ambos servicios (PostgreSQL + Flask)
docker compose up --build -d

# 3. Verificar que ambos contenedores estén corriendo
docker compose ps

# 4. Probar en el navegador
Start-Process http://localhost:5000

# 5. Ver registros en tiempo real
docker compose logs -f

# 6. Detener los contenedores (los datos se mantienen guardados)
docker compose down
```

Para ver la explicación completa, diagramas de arquitectura y retos evaluados, consulta [**`GUIA_SEMANA_2.md`**](file:///d:/YAVIRAC/tendencias/semana%202/GUIA_SEMANA_2.md).
