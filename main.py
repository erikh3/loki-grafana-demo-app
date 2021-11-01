import logging
from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from fastapi.responses import PlainTextResponse
from utilities import log_and_return

# setup loggers
logging.config.fileConfig('logging.conf', disable_existing_loggers=True)

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
  return templates.TemplateResponse("index.html", {"request": request})

@app.get("/example/raw", response_class=PlainTextResponse)
async def raw(msg: str = "Raw message from application"):
  return log_and_return(msg)
