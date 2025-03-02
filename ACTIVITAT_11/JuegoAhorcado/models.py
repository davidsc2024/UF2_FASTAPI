from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    puntos_totales = Column(Integer, default=0)

class Palabra(Base):
    __tablename__ = "palabras"
    id = Column(Integer, primary_key=True, index=True)
    palabra = Column(String, nullable=False)
    dificultad = Column(String, nullable=False)

class RegistroJuego(Base):
    __tablename__ = "registro_juego"
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    palabra_id = Column(Integer, ForeignKey("palabras.id"))
    intentos = Column(Integer, default=0)
