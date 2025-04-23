from fastapi import FastAPI
from app.entrypoints.api import router as log_router
from app.application.natsservice import LogEventListener  # Importá tu listener
import asyncio
import logging

logger = logging.getLogger(__name__)

async def main():
    logger.info("************** start listener")
    listener = LogEventListener()
    await listener.listen()

    # Bloquea el proceso para que no termine
    await asyncio.Event().wait()

if __name__ == "__main__":
    print("start")
    asyncio.run(main())