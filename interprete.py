from sqlalchemy import Column, String, Integer, ForeignKey

from .declarative_base import Base

class Interprete(Base):
    __tablename__ = 'interprete'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    cancion = Column(Integer, ForeignKey('cancion.id'))
