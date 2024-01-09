# Importamos 
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Creamos el motor con la direccion de la base de datos
                             #   ↓ aqui agregamos la direccion
engine = create_engine('sqlite:///baseDeDatos.sqlite')

# Creamos la sesion que interactua con el motor
Session = sessionmaker(bind=engine)

# Creamos la clase Base la cual hereda las clases del diagramaS
Base = declarative_base()

session = Session()