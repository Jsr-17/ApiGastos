def esquema_gastos(gasto) -> dict:
        
    return{
        "id":str(gasto["_id"]),
        "nombre":(gasto["nombre"]),
        "descripcion":(gasto["descripcion"]),
        "caracteristica":(gasto["caracteristica"]),
        "fecha":(gasto["fecha"])
    }
