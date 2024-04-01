from fastapi import FastAPI
from routes import gastos

app=FastAPI()

app.include_router(gastos.router)

@app.get("/")
async def inicio():
    return "Bienvenido a la aplicacion de gestion de gastos"