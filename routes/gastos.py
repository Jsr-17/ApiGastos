from fastapi import APIRouter,HTTPException
from cliente import db
from clienteOnline import db_online
from Models.gasto import Gasto
from schemas.gasto import esquema_gastos,esquemas_gastos
from bson import ObjectId

router= APIRouter(prefix="/gastos")

@router.get("/")
async def inicio():
    return "Este es el apartado de gastos"

@router.post("/crearGastoOnline")
async def nuevo(gasto:Gasto):
    
    diccionario_gasto=dict(gasto)
    del diccionario_gasto["id"]

    id= db_online.coleccion.insert_one(diccionario_gasto).inserted_id
    
    gasto_nuevo= esquema_gastos(db_online.coleccion.find_one({"_id":id}))

    return Gasto(**gasto_nuevo) 


@router.post("/crearGastoLocal")
async def nuevo(gasto:Gasto):
    
    diccionario_gasto=dict(gasto)
    del diccionario_gasto["id"]

    id= db.local.gastos.insert_one(diccionario_gasto).inserted_id
    
    gasto_nuevo= esquema_gastos(db.local.gastos.find_one({"_id":id}))

    return Gasto(**gasto_nuevo) 

@router.get("/obtenerGastos")
async def ObtenerGastos():
    try:
        return esquemas_gastos(db_online.coleccion.find())
    except:
        raise HTTPException(status_code=404)


@router.get("/obtenerGastos")
async def ObtenerGastos():
    try:
        return esquemas_gastos(db_online.coleccion.find())
    except:
        raise HTTPException(status_code=404)
    

@router.get("/obtenerNombre/{nombre}")
async def obtenerNombre(nombre:str):
    try:
        return buscarPorPersonalizado("nombre",nombre)
    except:
        raise HTTPException(status_code=404)
 
@router.get("/obtenerPrecio/{precio}")
async def obtenerPrecio(precio:int):
    try:
        return buscarPorPersonalizado("cantidad",precio)
    except:
        raise HTTPException(status_code=404)
 

@router.get("/obtenerId/{id}")
async def buscarPorId(id:str):
    datos = db_online.coleccion.find_one({"_id": ObjectId(id)})
    if datos:
        registro = Gasto(**esquema_gastos(datos))
        return registro
    else:
        return None

@router.get("/obtenerDescripcion/{descripcion}")
async def buscarDescripcion(descripcion:str):
    try:
        return buscarPorPersonalizado("descripcion",descripcion)
    except:
        raise HTTPException(status_code=404)
    
@router.get("/obtenerTodosPrecio")
async def buscarTodosPrecio():
    try:
        return esquemas_gastos(buscarPorPersonalizado("ca"))
    except:
        raise HTTPException(status_code=404)

@router.get("/obtenerTodosNombre/{nombre}")
async def buscarTodosNombre(nombre:str):
        try:
            return esquemas_gastos(buscarPorPersonalizadoD("nombre",nombre))
        except:
            raise HTTPException    
        
@router.get("/obtenerTodosPrecio/{precio}")
async def buscarTodosNombre(precio:int):
        try:
            return esquemas_gastos(buscarPorPersonalizadoD("cantidad",precio))
        except:
            raise HTTPException(status_code=404)


@router.get("/calcularGastosTotales")
async def buscarTodosNombre():
        try:
            almacen=esquemas_gastos(db_online.coleccion.find())
            total=0
            for valor in almacen:
                total+=valor["cantidad"]

            return   {"total":total}
        except:
            raise HTTPException(status_code=404)



def buscarPorPersonalizado(tipo,dato):
    datos=db_online.coleccion.find_one({str(tipo):dato})
    registro=Gasto(**esquema_gastos(datos))

    return registro

def buscarPorPersonalizadoD(tipo,dato):

    datos=db_online.coleccion.find({str(tipo):dato})
    registro=[]

    for dato in datos:
        registro.append(dato) 

    #registro=[dato for dato in datos]

    return registro
    