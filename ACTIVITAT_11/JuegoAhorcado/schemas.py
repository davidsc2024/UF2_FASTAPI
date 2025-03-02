from pydantic import BaseModel

class UsuarioSchema(BaseModel):
    nombre: str
    email: str

class PalabraSchema(BaseModel):
    palabra: str
    dificultad: str

class RegistroJuegoSchema(BaseModel):
    usuario_id: int
    palabra_id: int
    intentos: int
