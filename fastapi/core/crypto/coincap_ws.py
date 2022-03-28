from fastapi import FastAPI, WebSocket
import json
from websocket import create_connection
import time
from elasticsearch import Elasticsearch

class CoincapWSHandler():
    coincapUrl = "wss://ws.coincap.io"
    symbols = ["bitcoin"]
    
    def get_crypto_price(self):
        for symbol in self.symbols:
            self.send_ws(symbol)

    def send_ws(self, symbol):
        ws = create_connection(f"{self.coincapUrl}/prices?assets={symbol}")
        while True:
            ws.send(None)
            result = ws.recv()
            print(result)
            time.sleep(2)
        ws.close()

if __name__ == "__main__":
    wsHandler = CoincapWSHandler()
    wsHandler.get_crypto_price()




# @app.websocket("/ws")
# async def websocket_endpoint(websocket: WebSocket):
#     # 1、ws 連線
#     await websocket.accept()
#     while True:
#         # 2、接收客戶端傳送的內容
#         data = await websocket.receive_text()

#         # 3、服務端傳送內容
#         await websocket.send_text(f"小菠蘿收到的訊息是: {data}")