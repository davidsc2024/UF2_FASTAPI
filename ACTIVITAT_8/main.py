from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import HTTPException

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None
    description: Union[str, None] = None  # Campo opcional
    stock: int  # Cantidad disponible
    category: str  # Categoría del producto


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    if item_id > 100:  # Ejemplo de condición para un ID inexistente
        raise HTTPException(status_code=404, detail="Item no encontrado")
    return {"item_id": item_id, "q": q}


@app.post("/items/")
def create_item(item: Item):
    return {"name": item.name, "price": item.price, "category": item.category}
