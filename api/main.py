from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

# 🔹 Detecta la ruta base de este archivo (api/)
BASE_DIR = os.path.dirname(__file__)

# 🔹 Monta la carpeta static correctamente
app.mount(
    "/static",
    StaticFiles(directory=os.path.join(BASE_DIR, "static")),
    name="static"
)

# 🔹 Ejemplo de endpoint raíz
@app.get("/")
def read_root():
    return {"message": "Bienvenido al sistema de reservas 🚀"}

# 🔹 Importar las rutas (si tenés un archivo routes.py)
try:
    from . import routes
    app.include_router(routes.router)
except ImportError:
    pass
