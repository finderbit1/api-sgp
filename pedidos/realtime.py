import asyncio
import json
from typing import Any, Dict, Set

from fastapi import WebSocket

class OrdersNotifier:
    def __init__(self) -> None:
        self._connections: Set[WebSocket] = set()
        self._lock = asyncio.Lock()

    async def connect(self, websocket: WebSocket) -> None:
        await websocket.accept()
        async with self._lock:
            self._connections.add(websocket)

    async def disconnect(self, websocket: WebSocket) -> None:
        async with self._lock:
            if websocket in self._connections:
                self._connections.remove(websocket)

    async def broadcast(self, message: Dict[str, Any]) -> None:
        async with self._lock:
            recipients = list(self._connections)

        if not recipients:
            return

        payload = json.dumps(message, default=str)
        stale_connections: Set[WebSocket] = set()

        for websocket in recipients:
            try:
                await websocket.send_text(payload)
            except Exception:
                stale_connections.add(websocket)

        if stale_connections:
            async with self._lock:
                for websocket in stale_connections:
                    if websocket in self._connections:
                        self._connections.remove(websocket)


orders_notifier = OrdersNotifier()


def schedule_broadcast(message: Dict[str, Any]) -> None:
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        return

    if not loop.is_running():
        return

    loop.create_task(orders_notifier.broadcast(message))
