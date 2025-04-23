# Usa una imagen base de Python
FROM python:3.12-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos de requisitos al contenedor
COPY requirements.txt /app/

# Instalar las dependencias desde requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el código fuente al contenedor
COPY . /app/

# 👇 Esta línea es clave
ENV PYTHONUNBUFFERED=1

# Exponer el puerto que usará tu aplicación (por ejemplo, 8000)
EXPOSE 8000

# Comando para ejecutar la aplicación (en este caso, usando uvicorn para FastAPI)
CMD ["python", "main.py"]
