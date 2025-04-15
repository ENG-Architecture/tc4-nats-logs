# 📘 Event Logs API

Una API REST desarrollada en **FastAPI** para registrar y consultar logs de eventos, almacenados en **MongoDB**. Ideal para aplicaciones que requieren monitoreo de eventos personalizados, con almacenamiento flexible y rápido.

---

## 🚀 Tecnologías

- 🐍 Python 3.12
- ⚡ FastAPI
- 🍃 MongoDB
- 🐋 Docker & Docker Compose
- 🔗 PyMongo
- 📦 Pydantic

---

## 🛠️ Estructura del proyecto

project_root/
├── app/
│   ├── __init__.py
│   ├── domain/
│   │   ├── __init__.py
│   │   └── models.py          
│   ├── application/
│   │   ├── __init__.py
│   │   └── services.py        
│   ├── infrastructure/
│   │   ├── __init__.py
│   │   └── mongo_repository.py
│   └── entrypoints/
│       ├── __init__.py
│       └── api.py    
├── main.py           
├── requirements.txt
├── Dockerfile        
├── docker-compose.yml
└── .env

## ⚙️ Variables de entorno

Crear un archivo `.env` en la raíz del proyecto con el siguiente contenido:

🔐 No incluyas tu `.env` en el control de versiones (`.gitignore` debe excluirlo).


## 🐳 Levantar el entorno con Docker

docker-compose up --build

La API estará disponible en: http://localhost:8000

La base de datos MongoDB escuchará en: mongodb://localhost:27017

## 📚 Endpoints disponibles
🔸 POST /log
Registrar un nuevo evento de log.

Request Body:
{
  "environment": "dev",
  "event_type": "LOGIN_SUCCESS",
  "timestamp": "2025-04-15T22:45:00.799Z",
  "trace_id": "1234567890",
  "payload": "{ \"username\": \"user123\", \"tenant\": \"tenant456\" }"
}
 
🔹 GET /logs
Consultar los últimos 100 logs. Se puede pasar un query con filtros:

Ejemplo: /logs?environment=dev&event_type=LOGIN_SUCCESS