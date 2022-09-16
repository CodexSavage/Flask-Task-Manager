# Tarea.py

### Cabecera
Librerias empleadas:
```python

        from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Date
        import db

```
* __sqlalchemy:__  librería empleada para utilizar metodos como Column, Integer, Strin g, Boolean, ForeignKey y Date.
* __db:__ para importar funciones de la configuracion de la base de datos como *db.Base*

### Clase Tarea

```python

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

```

Clase Tarea que hereda funciones de *db.Base* para la gestión de creación y manulación de datos de la base de datos. Dicha clase recibirá el nombre de la tabla de la base de datos como "tarea", con los atributos especificados, siendo:
* __id_tarea:__ el identificador de la tarea, único.
* __content:__ contenido del nombre de la tarea.
* __done:__ estado de la tarea, siendo False, no hecho y True, hecho.
* __user_id:__ el identificador del usuario al cual la tarea estará relacionado con el identificador de la tabla/clase 'id'.
* __category:__ el tipo de categoria la tarea.
* __limit_date:__ la fehca limite para realizar la tarea.

En cuanto al constructor, cuenta con los parémtros básicos para identificar una tarea, como lo son: contenido, hecho, identificador del usuario, categoria y fehca límite.

El resto, las funsiones *__repr__*  y *__str__*, nos servirán para mostrar informacción relevante por terminal en momentos concretos.
