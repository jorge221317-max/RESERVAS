from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from .routes import router

app = FastAPI(title="API de Reservas 🚀")

# Carpeta static
app.mount("/static", StaticFiles(directory="api/static"), name="static")

# Carpeta templates
templates = Jinja2Templates(directory="templates")

# Incluir rutas de API
app.include_router(router)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
