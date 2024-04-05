def esquema_gastos(gasto) -> dict:
        
    return{
        "id":str(gasto["_id"]),
        "nombre":(gasto["nombre"]),
        "descripcion":(gasto["descripcion"]),
        "caracteristica":(gasto["caracteristica"]),
        "fecha":(gasto["fecha"]),
        "cantidad":(gasto["cantidad"])
    }
def esquemas_gastos(gastos)-> list:
    return [esquema_gastos(gasto) for  gasto in gastos]

