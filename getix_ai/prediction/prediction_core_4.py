import asyncio
import websockets
import sys
from prediction_config import * 

try:
    callCenterId = sys.argv[1]
    deep_speech_structured = sys.argv[2]
    language = sys.argv[3]
    debit_disclosure_payment_status = sys.argv[4]
    service_name = sys.argv[5]
    async def ws_client():
        uri = "ws://" + CORE_4_IP + ":" + CORE_4_PORT
        async with websockets.connect(uri, ping_interval=None) as websocket:

            list_of_params = "|".join([callCenterId, deep_speech_structured, language, debit_disclosure_payment_status, service_name])
            await websocket.send(list_of_params)
            ai_json_response = await websocket.recv()
            print(f"{ai_json_response}")

    asyncio.get_event_loop().run_until_complete(ws_client())
except Exception as e:
    print ({"error : ",str(e)})
