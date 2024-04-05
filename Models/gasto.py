from pydantic import BaseModel


class Gasto(BaseModel):
    id: str | None
    nombre:str
    descripcion:str
    caracteristica:str | None
    fecha:str
    cantidad:int
