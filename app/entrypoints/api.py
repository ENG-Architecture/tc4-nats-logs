from fastapi import APIRouter, Query
from typing import Optional
from datetime import datetime
from app.domain.models import EventLog, EventLog_Create
from app.application.services import save_event_log, get_event_logs

router = APIRouter()

@router.post("", summary="Guardar un nuevo log de evento")
async def create_log(log: EventLog_Create):
    log_save = EventLog(
    environment=log.environment,
    event_type=log.event_type,
    timestamp=log.timestamp,
    payload=log.payload
    )
    
    result = await save_event_log(log_save)
    return result

@router.get("", summary="Buscar logs por filtros")
async def read_logs(
    event_type: Optional[str] = Query(None, description="Tipo de evento"),
    environment: Optional[str] = Query(None, description="Entorno: dev, qa, prod, etc."),
    start_date: Optional[datetime] = Query(None, description="Fecha inicial (ISO8601)"),
    end_date: Optional[datetime] = Query(None, description="Fecha final (ISO8601)"),
):
    return await get_event_logs(event_type, environment, start_date, end_date)
