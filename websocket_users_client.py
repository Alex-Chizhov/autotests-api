import websockets
import asyncio

async def client():
    async with websockets.connect(uri="ws://localhost:8765") as websocket:

        await websocket.send("Привет, сервер!")

        for _ in range(5):
            response = await websocket.recv()
            print(response)

asyncio.run(client())
