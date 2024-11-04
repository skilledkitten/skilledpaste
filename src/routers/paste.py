from fastapi import APIRouter, HTTPException, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from src.core.data.redis_client import get_redis_client
from fastapi.templating import Jinja2Templates
import random, string
import redis

router = APIRouter()
redis_client = get_redis_client()
templates = Jinja2Templates(directory="src/templates")

def generate_random_endpoint(length=6):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.post("/create/")
async def create_paste(content: str = Form(...), custom_endpoint: str = Form(None)):
    endpoint = custom_endpoint or generate_random_endpoint()

    if redis_client.exists(endpoint):
        raise HTTPException(status_code=400, detail="Endpoint already taken")

    redis_client.set(endpoint, content)
    return RedirectResponse(url=f"/{endpoint}", status_code=302)

@router.get("/{endpoint}", response_class=HTMLResponse)
async def get_paste(request: Request, endpoint: str):
    content = redis_client.get(endpoint)
    if not content:
        raise HTTPException(status_code=404, detail="Paste not found")
    return templates.TemplateResponse("paste.html", {"request": request, "content": content})
