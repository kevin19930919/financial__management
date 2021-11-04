from fastapi import FastAPI, Request, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="./fastapi/templates")

cryptoInfoRouter = APIRouter(prefix="/cryptoInfo",tags=["cryptoInfo"])

@cryptoInfoRouter.get("/", response_class=HTMLResponse)
async def render_crypto(request: Request):
    return templates.TemplateResponse("crypto.html", {"request": request})