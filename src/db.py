from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
#from config import config
#from sqlalchemy.ext.declarative import declarative_base

#from config import config
engine = create_engine('sqlite:///src/database/data.db', connect_args={"check_same_thread": False})
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


""" 
Importa del fichero config.py como libreria config el diccionario 
establecido ahí como config el cual tiene como clave, el nombre -> 
'development',y como valor, una clase denominada ConfigDevelopment,
la cual es una clase heredada de la clase Config. Dichas clases, 
tinen definidas parámetros que definen el comportamiento/funcionamiento
de las variables de entorno. 

Puesto que lo que nos instersa en estas circunstcias para crear el 
engine es el tipo de sistema de gestion de base de datos, así como el 
path de dicha base de datos, la obtenemos mediante la instanciación de 
la clase ConfigDevelopment, por lo que para tener el parámetro deseado
lo obtenemos de ahí.

El objetivo de hacerlo de esta manera es evitar comprometer cierta 
información relevante a un usuario externo sin acreditación que intente
entrar en el sistema sin autorización. 

"""