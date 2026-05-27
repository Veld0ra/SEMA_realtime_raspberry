import websockets

from core.config import URL, API_KEY


async def conectar():

    ws = await websockets.connect(
        URL,
        extra_headers={
            "Authorization": f"Bearer {API_KEY}"
        }
    )

    return ws
