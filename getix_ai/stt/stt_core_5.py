#!/usr/bin/env python

import asyncio
import websockets
import sys
from stt_config import * 

try:
    file_name = str(sys.argv[1])

    async def ws_client():
        uri = "ws://" + CORE_5_IP + ":" + CORE_5_PORT
        async with websockets.connect(uri, ping_interval=None) as websocket:
            await websocket.send(file_name)
            text = await websocket.recv()
            print(f"{text}")

    asyncio.get_event_loop().run_until_complete(ws_client())
except Exception as e:
    print ({"error : ",str(e)})
