from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

# Inicialización de la app
app = FastAPI()


# Modelo de datos para manejar entradas (POST)
class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


# Método GET en la raíz
@app.get("/")
def read_root():
    return {"message": "Bienvenido a mi API"}


# Método GET para consultar un ítem
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


# Método POST para crear un nuevo ítem
@app.post("/items/")
def create_item(item: Item):
    return {"message": "Item creado exitosamente", "item": item}
