from fastapi import APIRouter
from cliente import db
from Models.gasto import Gasto
from schemas.gasto import esquema_gastos

router= APIRouter(prefix="/gastos")

@router.get("/")
async def inicio():
    return "Este es el apartado de gastos"

@router.post("/crearGasto")
async def nuevo(gasto:Gasto):
    
    diccionario_gasto=dict(gasto)
    del diccionario_gasto["id"]

    id= db.local.gastos.insert_one(diccionario_gasto).inserted_id
    
    gasto_nuevo= esquema_gastos(db.local.gastos.find_one({"_id":id}))

    return Gasto(**gasto_nuevo) 
