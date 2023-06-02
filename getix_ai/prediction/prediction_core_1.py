import asyncio
import websockets
import sys
from prediction_config import * 

try:
    speech_to_text_structured = sys.argv[1]
    async def ws_client():
        uri = "ws://" + CORE_1_IP + ":" + CORE_1_PORT
        async with websockets.connect(uri, ping_interval=None) as websocket:

            list_of_params = "|".join([speech_to_text_structured])
            await websocket.send(list_of_params)
            ai_json_response = await websocket.recv()
            print(f"{ai_json_response}")

    asyncio.get_event_loop().run_until_complete(ws_client())
except Exception as e:
    print ({"error : ",str(e)})
