# ModelTarea.py

### Cabecera

```python
        from datetime import datetime
        from sqlalchemy import text, delete, and_
        from models.entities.Tarea import Tarea     

```

* __datetime:__ libreria para emplear la función datetime para convertir un fehca en formato str a tipo Date, aceptable para la base de datos.
* __sqlalchemy:__ libreria para importar funciones de ejecución de
* __models.entities.Tarea:__ el uso de esta llamada es para la obtención de la clase de Tarea.

### Clase ModelTarea

```python
        class ModelTarea():
             @classmethod
            def AddTarea(cls, db ): 
                try:

                    task = Tarea(content="Lavar los platos", done=False, user_id = 1, category="domestico", limit_date=datetime.strptime('04/09/2001', "%d/%m/%Y"))
                    task1 = Tarea(content="Jugar a la play", done=True, user_id = 2,category="domestico", limit_date=datetime.strptime('04/09/2002', "%d/%m/%Y"))
                    task2 = Tarea(content="ver la película", done=False, user_id=2, category="domestico", limit_date=datetime.strptime('04/09/2003', "%d/%m/%Y"))
                    task3 = Tarea(content="salir a pasear", done=True, user_id=1, category="domestico", limit_date=datetime.strptime('04/09/2004', "%d/%m/%Y"))
                    task4 = Tarea(content="Comprar", done=False, user_id=1, category="domestico", limit_date=datetime.strptime('04/09/2005', "%d/%m/%Y"))
                    db.session.add_all([task, task1, task2, task3, task4])
                    db.session.commit()
                    db.session.close()
                except Exception as e:
                    raise Exception(e)
                else:
                    print("[+] Tasks added succesfully")
e".

```
 El uso de la definción de una clase es para agrupar de mejor manera funciones y contenido de dicah clase. y de esta forma, emplerarlas sin ningún tipo de restricción.

 Para esta *classmethod*, *Addtarea*, lo que hacemos es crear registros con todos los datos pertinentes para añadirlos a la base de datos y, el manejo de error, es para comprobar que todos los datos fueron introducidos de forma correcta.

 ```python
 
                @classmethod
                def Task_to_Done(cls,db, id_task, id_user):
                    task = db.session.query(Tarea).filter(Tarea.id_tarea == id_task, Tarea.user_id == id_user).first()
                    task.done = True
                    db.session.commit()
                    db.session.close()


                @classmethod
                def Task_to_Undone(cls,db, id_task, id_user): 
                    task = db.session.query(Tarea).filter(and_(Tarea.id_tarea == id_task, Tarea.user_id == id_user)).first()
                    task.done = False
                    db.session.commit()
                    db.session.close()
 
 ```

 Ambas funciones tienen el propósito de cambiar el estado de las tareas, de hecho a no hecho y viceversa, pasando por parámetros el identificador del usuario y de la tarea.

```python
                    @classmethod
                    def getTask_byID(cls, db, userId): 
                        task = db.session.query(Tarea).filter(Tarea.user_id == userId) # Obtenemos las 
                        return task
o

```
Empleamos esta función para obtener todas las tareas pertenecientes a un usuario con una consulta a la base de datos. Todas a aquellas que pertenezcan al usuario, se guardaran en la vairable en forma de lista, que finalmente, será devuelto.

```python

                    @classmethod
                    def Add_new_task(cls, db, new_task): 
                        db.session.add(new_task)
                        db.session.commit()
                        db.session.close()


```

Funcion para guardar la nueva tarea creda en la base de datos. El código podría haberse hecho en 'app.py', pero de esta forma queda mejor organizado.

```python

                    @classmethod
                    def Edit_task_byID( cls,db, tarea_id ):
                        tarea = db.session.query(Tarea).filter(Tarea.id_tarea == tarea_id).first() 
                        return tarea

```

Función para obtener la información de la tarea recibiendo como único atributo el identificador de la tarea.

```python
                    @classmethod
                    def edit(cls, db, task):
                        db.session.add(task)
                        db.session.commit()
                        db.session.close()

```

Función para guardar los cambios en la base de datos, respecto a la edición de los parámetros de una tarea.