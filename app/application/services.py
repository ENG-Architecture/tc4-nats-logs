from app.domain.models import EventLog
from app.insfrastructure.mongo_repository import save_log, search_logs
from typing import Optional
from datetime import datetime

async def save_event_log(log: EventLog):
    try:
        save_log(log.dict())
        return {"message": "Log saved successfully", "trace_id": log.trace_id}
    except Exception as e:
        print(f"error al insertar el log {e}")

async def get_event_logs(event_type: Optional[str], environment: Optional[str], start_date: Optional[datetime], end_date: Optional[datetime]):
    print("start query")
    query = {}
    if event_type:
        query["event_type"] = event_type
    if environment:
        query["environment"] = environment
    if start_date or end_date:
        query["timestamp"] = {}
        if start_date:
            query["timestamp"]["$gte"] = start_date
        if end_date:
            query["timestamp"]["$lte"] = end_date
    
    print(query)

    try:
        result = search_logs(query)
    except Exception as e:
        print(f"error al leer query {e}")

    return result
