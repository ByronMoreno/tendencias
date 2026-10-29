# ==========================================
# 1. Usar una imagen base oficial con Python
# ==========================================
FROM python:3.12-slim

# ==========================================
# 2. Definir el directorio de trabajo
# ==========================================
WORKDIR /app

# ==========================================
# 3. Copiar las dependencias primero (aprovecha la caché de Docker)
# ==========================================
COPY requirements.txt .

# ==========================================
# 4. Instalar las dependencias de Python
# ==========================================
RUN pip install --no-cache-dir -r requirements.txt

# ==========================================
# 5. Copiar el código fuente de la aplicación
# ==========================================
COPY app.py .

# ==========================================
# 6. Documentar el puerto que expone el servicio
# ==========================================
EXPOSE 5000

# ==========================================
# 7. Iniciar Flask cuando arranque el contenedor
# ==========================================
CMD ["python", "app.py"]
