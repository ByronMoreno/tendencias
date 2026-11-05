# 1. Imagen base ligera de Python 3.12
FROM python:3.12-slim

# 2. Definir directorio de trabajo dentro del contenedor
WORKDIR /app

# 3. Copiar archivo de requerimientos
COPY requirements.txt .

# 4. Instalar librerías de Python
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiar el código fuente de la aplicación Flask
COPY app.py .

# 6. Exponer el puerto 5000
EXPOSE 5000

# 7. Ejecutar la aplicación
CMD ["python", "app.py"]
