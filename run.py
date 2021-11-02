# from gevent import monkey
# monkey.patch_all()
import uvicorn
from fastapi import FastAPI


# ==========initial app=============
app = FastAPI()
# ========app configure=============
#TODO
# =========regiter router===========
#TODO
import sys
sys.path.append('./fastapi')
from view import crypto
app.include_router(crypto.cryptoRouter)




def root():
    return {"message": "Hello World!"}

if __name__ == "__main__":
    uvicorn.run("run:app", host="0.0.0.0", port=5000, reload=True)
