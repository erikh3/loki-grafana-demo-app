import logging
import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from fastapi.responses import PlainTextResponse
from utilities import log_and_return

disable_existing_loggers_string = os.getenv('DISABLE_EXISTING_LOGGERS', 'True')
disable_existing_loggers = True
if disable_existing_loggers_string.lower() == "false":
  disable_existing_loggers = False

# setup loggers
logging.config.fileConfig('logging.conf', disable_existing_loggers=disable_existing_loggers)

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

logging.info("INFO: BOOTSTRAP: Started logger demo application!")

@app.get("/", response_class=HTMLResponse)
async def show_demo_page(request: Request):
  return templates.TemplateResponse("index.html", {"request": request, "root_path": request.scope.get("root_path")})

@app.get("/log", response_class=PlainTextResponse)
async def log_message_and_return(msg: str = "Raw message from application"):
  return log_and_return(msg)
