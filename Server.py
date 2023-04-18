import asyncio
import websockets

PORT = 443
IPAddr = "127.0.0.1"
print("Server is listening port : " + str(PORT) + " on ip : " + IPAddr)

async def hello(websocket):
    name = await websocket.recv()
    print(f"<<< {name}")

    greeting = f"Hello {name}!"
    await websocket.send(greeting)
    print(f">>> {greeting}")

async def main():
    async with websockets.serve(hello, IPAddr, PORT):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())