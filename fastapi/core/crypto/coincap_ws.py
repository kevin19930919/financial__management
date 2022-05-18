import json
from websocket import create_connection
import time


class CoincapWSHandler():
    coincapUrl = "wss://ws.coincap.io"
    symbols = ["bitcoin","ethereum"]
    
    def construct_assets(self):
        symbol_string = ""
        for index in range(len(symbols)):
            symbol_string+=symbols[index] + ","
        symbol_string.strip(",")
        
        return  symbol_string      
    
    def get_crypto_price(self):
        symbol_string = self.construct_assets()
        if symbol_string:
            self.send_ws(symbol)
        else:
            print("assign target please")

    def send_ws(self, symbol_string):
        ws = create_connection(f"{self.coincapUrl}/prices?assets={symbol_string}")
        while True:
            ws.send(None)
            result = ws.recv()
            time.sleep(2)
        ws.close()
    
    def insert_prices_in_elastic(self, data):




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