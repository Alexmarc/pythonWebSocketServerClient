import asyncio
import websockets

PORT = 443
IPAddr="127.0.0.1"

async def hello():
    uri = "ws://" + IPAddr + ":" + str(PORT)
    print(uri)
    async with websockets.connect(uri) as websocket:
        name = input("What's your name? ")
        await websocket.send(name)
        print(f">>> {name}")

        greeting = await websocket.recv()
        print(f"<<< {greeting}")

if __name__ == "__main__":
    asyncio.run(hello())