from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Body-Fields: Modelo de usuario básico
class User(BaseModel):
    name: str
    age: int
    email: str

@app.post("/user/")
async def create_user(user: User):
    return {"message": "User created", "user": user}

# Body-Nested Models: Modelo con dirección anidada
class Address(BaseModel):
    street: str
    city: str
    country: str

class UserWithAddress(BaseModel):
    name: str
    age: int
    email: str
    address: Address  # Campo anidado

@app.post("/user-with-address/")
async def create_user_with_address(user: UserWithAddress):
    return {"message": "User with address created", "user": user}
