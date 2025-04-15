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

# Exponer el puerto que usará tu aplicación (por ejemplo, 8000)
EXPOSE 8000

# Comando para ejecutar la aplicación (en este caso, usando uvicorn para FastAPI)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
