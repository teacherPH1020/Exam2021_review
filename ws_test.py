import websockets

# print(dir(websockets))

import asyncio

async def echo():
    #uri = "wss://echo.websocket.org"
    uri = "ws://127.0.0.1:8765/test"
    async with websockets.connect(uri) as ws:
        text = input("cry some words: ")

        await ws.send(text)
        print(f"outgoing:{text}")

        answer = await ws.recv()
        print(f"incoming:{answer}")


asyncio.get_event_loop().run_until_complete(echo())
