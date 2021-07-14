import websockets

# print(dir(websockets))

import asyncio

async def echo(ws, path):
    data = await ws.recv()
    print(f"got data {data} path {path}")
    print(ws.remote_address)
    await ws.send(data)
    print(f"complete sending data {data}")


start_server = websockets.serve(echo,"127.0.0.1",8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()