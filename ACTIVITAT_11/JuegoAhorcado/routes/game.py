from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Usuario, Partida

router = APIRouter()

@router.post("/usuarios/")
def crear_usuario(nombre: str, db: Session = Depends(get_db)):
    usuario = Usuario(nombre=nombre)
    db.add(usuario)
    db.commit()
    return {"mensaje": "Usuario creado"}

@router.post("/partidas/")
def iniciar_partida(nombre: str, palabra: str, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.nombre == nombre).first()
    if not usuario:
        return {"error": "Usuario no encontrado"}
    
    partida = Partida(usuario_id=usuario.id, palabra=palabra, intentos=0, estado="jugando")
    db.add(partida)
    db.commit()
    return {"mensaje": "Partida iniciada"}

@router.get("/estadisticas/")
def obtener_estadisticas(nombre: str, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.nombre == nombre).first()
    if not usuario:
        return {"error": "Usuario no encontrado"}
    
    total = len(usuario.partidas)
    ganadas = sum(1 for p in usuario.partidas if p.estado == "ganado")
    return {"total_partidas": total, "partidas_ganadas": ganadas}
