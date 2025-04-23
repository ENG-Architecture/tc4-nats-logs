import json
from nats.aio.client import Client as NATS
from nats.js.client import JetStreamContext
from nats.js.errors import NotFoundError

from app.domain.models import EventLog
from app.insfrastructure.mongo_repository import save_log
from datetime import datetime

class LogEventListener:
    def __init__(self):
        print("************** start connector")
        self._nc = NATS()
        self._js: JetStreamContext = None

    async def connect(self):
        print("************** initial connection")
        await self._nc.connect(servers=["nats://192.168.0.177:4222"])
        self._js = self._nc.jetstream()

        try:
            await self._js.stream_info("teamcore_stream")
        except Exception:
            await self.js.add_stream(name="teamcore_stream", subjects=["teamcore.*"])

        print("listener started")

    async def handle_message(self, msg):
        try:
            data = json.loads(msg.data.decode())
            print(f"Mensaje recibido en {msg.subject}: {data}")

            log = EventLog(**data)  # Asegúrate que el dict tenga el formato de EventLog
            save_log(log.__dict__)
            await msg.ack()
        except Exception as e:
            print(f"Error procesando mensaje: {e}")

    async def ensure_stream_exists(self, stream_name: str, subjects: list[str]):
        try:
            stream_info = await self._js.stream_info(stream_name)
            existing_subjects = set(stream_info.config.subjects)
            new_subjects = set(subjects)
            if not new_subjects.issubset(existing_subjects):
                updated_subjects = list(existing_subjects.union(new_subjects))
                await self._js.update_stream(name=stream_name, subjects=updated_subjects)
        except NotFoundError:
            await self._js.add_stream(name=stream_name, subjects=subjects)

    async def listen(self):
        await self.connect()
        await self._js.subscribe(
        subject="teamcore.*",
        durable="reset_password_listener_logs",
        cb=self.handle_message
        )
