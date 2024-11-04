from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from src.routers import paste

app = FastAPI()
templates = Jinja2Templates(directory="src/templates")

# Mount the static files directory
app.mount("/static", StaticFiles(directory="src/static"), name="static")

# Include your routers
app.include_router(paste.router)