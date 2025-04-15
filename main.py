from fastapi import FastAPI
from app.entrypoints.api import router as log_router

app = FastAPI(
    title="Event Logger Microservice",
    description="Microservicio para guardar y consultar logs de eventos del sistema.",
    version="1.0.0",
    contact={
        "name": "Equipo de Arquitectura",
        "email": "soporte@teamcore.cl"
    },
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

app.include_router(log_router, prefix="/logs", tags=["Logs"])