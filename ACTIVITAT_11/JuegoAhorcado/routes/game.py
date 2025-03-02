from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Usuario, Palabra, RegistroJuego
from schemas import UsuarioSchema, PalabraSchema, RegistroJuegoSchema

router = APIRouter()

@router.post("/usuarios/")
def crear_usuario(usuario: UsuarioSchema, db: Session = Depends(get_db)):
    nuevo_usuario = Usuario(nombre=usuario.nombre, email=usuario.email)
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario

@router.get("/usuarios/")
def obtener_usuarios(db: Session = Depends(get_db)):
    return db.query(Usuario).all()

@router.put("/usuarios/{usuario_id}")
def actualizar_usuario(usuario_id: int, usuario: UsuarioSchema, db: Session = Depends(get_db)):
    usuario_db = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not usuario_db:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    usuario_db.nombre = usuario.nombre
    usuario_db.email = usuario.email
    db.commit()
    return usuario_db

@router.delete("/usuarios/{usuario_id}")
def eliminar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario_db = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not usuario_db:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    db.delete(usuario_db)
    db.commit()
    return {"mensaje": "Usuario eliminado"}

@router.post("/palabras/")
def crear_palabra(palabra: PalabraSchema, db: Session = Depends(get_db)):
    nueva_palabra = Palabra(palabra=palabra.palabra, dificultad=palabra.dificultad)
    db.add(nueva_palabra)
    db.commit()
    db.refresh(nueva_palabra)
    return nueva_palabra

@router.get("/palabras/")
def obtener_palabras(db: Session = Depends(get_db)):
    return db.query(Palabra).all()

@router.put("/palabras/{palabra_id}")
def actualizar_palabra(palabra_id: int, palabra: PalabraSchema, db: Session = Depends(get_db)):
    palabra_db = db.query(Palabra).filter(Palabra.id == palabra_id).first()
    if not palabra_db:
        raise HTTPException(status_code=404, detail="Palabra no encontrada")
    palabra_db.palabra = palabra.palabra
    palabra_db.dificultad = palabra.dificultad
    db.commit()
    return palabra_db

@router.delete("/palabras/{palabra_id}")
def eliminar_palabra(palabra_id: int, db: Session = Depends(get_db)):
    palabra_db = db.query(Palabra).filter(Palabra.id == palabra_id).first()
    if not palabra_db:
        raise HTTPException(status_code=404, detail="Palabra no encontrada")
    db.delete(palabra_db)
    db.commit()
    return {"mensaje": "Palabra eliminada"}

@router.post("/registro_juego/")
def crear_registro_juego(registro: RegistroJuegoSchema, db: Session = Depends(get_db)):
    nuevo_registro = RegistroJuego(
        usuario_id=registro.usuario_id, palabra_id=registro.palabra_id, intentos=registro.intentos
    )
    db.add(nuevo_registro)
    db.commit()
    db.refresh(nuevo_registro)
    return nuevo_registro

@router.get("/registro_juego/")
def obtener_registros_juego(db: Session = Depends(get_db)):
    return db.query(RegistroJuego).all()

@router.put("/registro_juego/{registro_id}")
def actualizar_registro_juego(registro_id: int, registro: RegistroJuegoSchema, db: Session = Depends(get_db)):
    registro_db = db.query(RegistroJuego).filter(RegistroJuego.id == registro_id).first()
    if not registro_db:
        raise HTTPException(status_code=404, detail="Registro de juego no encontrado")
    registro_db.intentos = registro.intentos
    db.commit()
    return registro_db

@router.delete("/registro_juego/{registro_id}")
def eliminar_registro_juego(registro_id: int, db: Session = Depends(get_db)):
    registro_db = db.query(RegistroJuego).filter(RegistroJuego.id == registro_id).first()
    if not registro_db:
        raise HTTPException(status_code=404, detail="Registro de juego no encontrado")
    db.delete(registro_db)
    db.commit()
    return {"mensaje": "Registro de juego eliminado"}
