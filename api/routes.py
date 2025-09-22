from fastapi import APIRouter, Request, Form
from fastapi.responses import RedirectResponse

router = APIRouter()

# Lista simple de turnos en memoria
turnos = []

@router.post("/reservar")
async def reservar_turno(nombre: str = Form(...), fecha: str = Form(...), hora: str = Form(...)):
    turnos.append({"nombre": nombre, "fecha": fecha, "hora": hora})
    return RedirectResponse(url="/", status_code=303)

@router.get("/turnos")
async def listar_turnos():
    return {"turnos": turnos}
