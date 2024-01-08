# importamos las librerias
from sqlalchemy import Column, String, Integer
# importamos la relacion
from sqlalchemy.orm import relationship

# Traemos la base del archivo .declarative base.
from .declarative_base import Base

class Cancion(Base):

    __tablename__ = "cancion"
    id = Column(Integer, primary_key=True)
    titulo = Column(String)
    minutos = Column(Integer)
    segundos = Column(Integer)
    compositor = Column(String)
    albumes = relationship('Album', secondary='album_cancion')
    interpretes = relationship('Interprete', cascade='all, delete, delete-orphan')