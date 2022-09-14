from email.policy import default
from enum import Flag
from turtle import done
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Date
import db


class Tarea(db.Base):
    __tablename__ = "tarea"
    id_tarea = Column(Integer, primary_key=True)
    content = Column(String(100), nullable=False)
    done = Column(Boolean, default=0, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    category = Column(String, default="domestico", nullable=False)
    limit_date = Column(Date, nullable=False)

    def __init__(self, content, done, user_id, category, limit_date) :
        self.content = content
        self.done = done
        self.user_id = user_id
        self.category = category
        self.limit_date = limit_date

    def __repr__(self): # imprime por defecto esto el contenido que queramos de la base de datos específico
        return "{} {} {} {} {}".format( self.content, self.done, self.user_id, self.category, self.limit_date)

    def __str__(self):
        return "{} {} {} {} {}".format(self.content, self.done, self.user_id, self.category, self.limit_date)
