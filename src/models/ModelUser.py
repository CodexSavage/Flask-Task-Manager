from ctypes import resize
from multiprocessing.sharedctypes import Value
from operator import and_, or_
from sqlalchemy import text, or_, and_

#from models.entities.Tarea import Tarea
from .entities.User import User
from .entities.Tarea import Tarea
from werkzeug.security import generate_password_hash, check_password_hash
#import db

class ModelUser():

    @classmethod
    def login(cls, db, user): # User es una instancia de la clase User
        try:
            #sql = "SELECT username, email, fullname, password FROM user WHERE username = '{}' OR email = '{}'".format(user.username,user.email)
            #result = db.session.execute(text(sql)).first() # <class 'sqlalchemy.engine.row.Row'>
            result = db.session.query(User).filter( or_(User.username == user.username, User.email == user.email)).first()
            #print("Resultado ->", result)
            if result:
                #print("Contraseña introducida -> ", user.password)
                usuario = User(username = result.username, email = result.email, fullname = result.fullname, password = User.CheckPassword(user.password, result.password))
                #print("Contraseña hasheada", result.password)
                #print("Contraseña estado -> ", usuario.password)
                return usuario
            else:
                return None

        except Exception as e:
            raise Exception(e)

    
    @classmethod
    def get_by_id(cls, db, id): # User es una instancia de la clase User
        try:
            """
            sql = "SELECT username, fullname FROM user WHERE id = '{}'".format( id )
            result = db.session.execute(text(sql)).first() # <class 'sqlalchemy.engine.row.Row'>
            
            if result:
                usuario = User(result[0], " ", result[2], 0)
                return usuario
            else:
                return None"""
            
            #
            currentUser = db.session.query(User).filter(User.id == id)

            return currentUser

        except Exception as e:
            raise Exception(e)


    @classmethod
    def GetID(cls,db, currentUser):
        userId = db.session.query(User).filter(and_(User.username == currentUser.username, User.email == currentUser.email, User.fullname == currentUser.fullname)).first()
        return userId.id

    @classmethod
    #def AddUser(cls, db, name_, email_, fullname_, pwd):
    def AddUser(cls, db):

        usuario = User( username='Joel', email='Joel@hotmail.com', fullname='Joel Tipan', password='pbkdf2:sha256:260000$PJAArK3FWUtSIwvi$93208c534564ff5d6f57c61090699f3a14498c10201a0550d5367c69e48db279')
        usuario1 = User( username='Marta', email='marta@gmail.com', fullname='Marta Narbona', password='pbkdf2:sha256:260000$Kr91bJNiqBLid4DY$a85e302b3390d6ccad3dfe2c605f3e79cdfad83b6bf100a2c6502cdf14e8f728')
        #user = User(username=name_, email=email_, fullname=fullname_, password=pwd)
        db.session.add_all([usuario, usuario1])
        db.session.commit()
        db.session.close()

        """
        el siguiente codigo es una versió alternativa al código de arriba en caso de que no funcione.


        password = User.GeneratePassword_hash(pwd, method='pbkdf2:sha256')
        pwd_ = "pbkdf2:sha256:260000$PJAArK3FWUtSIwvi$93208c534564ff5d6f57c61090699f3a14498c10201a0550d5367c69e48db279"
        #sql = "INSERT INTO user( username, email, fullname, password) values('{}', '{}', '{}', '{}')".format( name, email, fullname, password)
        user = User( username='Joel', email="Joel@gmail.com", fullname="Joel Tipan", password=pwd)
        db.session.execute(text(sql))
        db.session.commit() """

    @classmethod
    def Registration(cls,db, username_, email_, fullname_, password_):
        # Comprobación si usuraio ya existe:
        value = False
        try:
            
            name = db.session.query(User).filter(User.username == username_).first()
            if name:
                raise ValueError
            else: pass
            correo = db.session.query(User).filter(User.email == email_).first()
            if correo:
                raise ValueError
            else: pass
            
        except ValueError as e:
            print("Usuario ya registrado")

        else:     
            # Conversión a sh256 password:  
            contr = User.GeneratePassword_hash(password=password_)
            newUser = User(username=username_, email=email_, fullname=fullname_, password=contr)
            db.session.add(newUser)
            db.session.commit()
            db.session.close()
            value = True 

        return value
            
    

