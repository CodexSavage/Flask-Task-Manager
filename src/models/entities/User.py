#from enum import unique
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, Integer, String
from flask_login import UserMixin
import db

class User(db.Base, UserMixin):
    __tablename__ = "user"
    id = Column(Integer,primary_key=True, autoincrement=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    fullname = Column(String)
    password = Column(String, nullable=False)
    tasks = relationship('Tarea', backref='user')

    def __init__(self, username, email,fullname, password):
        self.username = username
        self.email = email
        self.fullname = fullname
        self.password = password


    def __repr__(self) :
        return "{} {} {} {}".format(self.id, self.username, self.email, self.fullname)


    def __str__(self):
        return "{} {} {} {}".format(self.id, self.username, self.email, self.fullname)


    @classmethod
    def CheckPassword(cls, pwd, password_hashed):
        return check_password_hash(password_hashed, pwd)


    @classmethod
    def GeneratePassword_hash(cls, password):
        return generate_password_hash(password)

"""

password_hashed -> contraseña que se obtiene de la base de datos hasheada

pwd -> contraseña que introduce el usuario


"""