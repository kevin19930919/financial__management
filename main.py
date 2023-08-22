from src.crypto import router
# from view import cryptoView
import uvicorn
from fastapi import FastAPI
# from fastapi.staticfiles import StaticFiles

# ==========initial app=============
app = FastAPI()
# app.mount("/static", StaticFiles(directory="./fastapi/static"), name="static")

# ========app configure=============
#TODO
# =========regiter router===========
#TODO

app.include_router(router.cryptoAPIRouter)
# app.include_router(cryptoView.CryptoTradeListRouter)




if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=1219)
