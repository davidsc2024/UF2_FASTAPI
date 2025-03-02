from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, index=True)
    partidas = relationship("Partida", back_populates="usuario")

class Partida(Base):
    __tablename__ = "partidas"
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    palabra = Column(String)
    intentos = Column(Integer, default=0)
    estado = Column(String)  # "ganado" o "perdido"
    usuario = relationship("Usuario", back_populates="partidas")
