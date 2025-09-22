from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from .routes import router

app = FastAPI()
app.include_router(router)

# Templates
app.templates = Jinja2Templates(directory="templates")

# Static
app.mount("/static", StaticFiles(directory="static"), name="static")
