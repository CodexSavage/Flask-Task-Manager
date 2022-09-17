from asyncio import tasks
from datetime import datetime
from sqlalchemy import text, delete, and_
from models.entities.Tarea import Tarea
from models.entities.User import User

class ModelTarea():
    
    @classmethod
    def VerifyChanges( db, Name_tarea,New_name_tarea ):# Función para modificar la tarea. Empleado para uso de test.
        try :
            sql = """
                    UPDATE tarea
                    SET content = {} 
                    WHERE content = {}""".format(Name_tarea, New_name_tarea)
            db.session.execute(text(sql)).execution_options(autocommit=True)
        except Exception as e:
            raise Exception(e)
    

    @classmethod
    def AddTarea(cls, db ): # Para inicializar la base de datos de Usuario.
        try:
            #sql = """INSERT INTO tarea(content, doit) values('{}', '{}')""".format(content, done)
            #db.session.execute(text(sql))
            task = Tarea(content="modificar datos", done=False, user_id = 1, category="domestico", limit_date=datetime.strptime('04/09/2022', "%d/%m/%Y"))
            task1 = Tarea(content="asistir conferencia", done=True, user_id = 2,category="ocio", limit_date=datetime.strptime('04/09/2022', "%d/%m/%Y"))
            task2 = Tarea(content="terminar proyecto", done=False, user_id=2, category="docio", limit_date=datetime.strptime('04/09/2022', "%d/%m/%Y"))
            task3 = Tarea(content="salir a pasear", done=True, user_id=1, category="salud", limit_date=datetime.strptime('04/09/2022', "%d/%m/%Y"))
            task4 = Tarea(content="comprar biberes", done=False, user_id=1, category="tarea", limit_date=datetime.strptime('04/09/2022', "%d/%m/%Y"))
            db.session.add_all([task, task1, task2, task3, task4])
            db.session.commit()
            db.session.close()
        except Exception as e:
            raise Exception(e)
        else:
            print("[+] Tasks added succesfully")

        # El uso de manejo de errores esra pora comprobar que la fecha se guardara tipo "Date".


    @classmethod
    def deleteTarea(db, name_tarea): # Perteneciente para uso de test no para la aplicación web.
        try: 
            sql_del = (
                delete(Tarea).
                where(Tarea.content == name_tarea)
            )
            db.session.execute(text(sql_del))
            db.session.commit()

            """
            sql = " DELETE FROM Tarea WHERE content = '{}' ".format(name_tarea)
            db.session.execute(text(sql))
            db.session.commit()
            """
            
        except Exception as e:
            raise Exception(e)
        else: 
            print("Tarea eliminada...")
        finally:
            print("Process finished")


    @classmethod
    def Task_to_Done(cls,db, id_task, id_user): # Corregido. Convertir una tarea no hecha a hecha.
        task = db.session.query(Tarea).filter(Tarea.id_tarea == id_task, Tarea.user_id == id_user).first()
        task.done = True
        db.session.commit()
        db.session.close()


    @classmethod
    def Task_to_Undone(cls,db, id_task, id_user): # Corregido. Convertir una tarea hecha a no hecha.
        task = db.session.query(Tarea).filter(and_(Tarea.id_tarea == id_task, Tarea.user_id == id_user)).first()
        task.done = False
        db.session.commit()
        db.session.close()


    @classmethod
    def getTask_byID(cls, db, userId): # Terminado. Obtenemos todas la tareas pertenecientes a un usuario al iniciar la sesión
        task = db.session.query(Tarea).filter(Tarea.user_id == userId) # Obtenemos las tareas pertenecientes al usuario de la base de datos
        return task
        #Devuleve una lista de todos los registros/Tareas pertenecientes al usuario


    @classmethod
    def Add_new_task(cls, db, new_task): # Añadimos la tarea a la base de datos teneindo en cuenta el usuario que lo ha añadido.
        # Pasamos la clase creada directmanete y aquí sólo hacemos el commit.
        db.session.add(new_task)
        db.session.commit()
        db.session.close()
        # Se podría heber hecho en "app.py" pero de esta forma queda un código más ordenado y estéticamente mejor.


    @classmethod
    def Edit_task_byID( cls,db, tarea_id ): # Terminado. # Recibo un string tipo objecto de tarea y la longitud de la cadena de contenido
        tarea = db.session.query(Tarea).filter(Tarea.id_tarea == tarea_id).first() # Teniendo sólo el id de la tarea obtenemos el resto de la información de la tarea
        return tarea
 
        
    @classmethod
    def edit(cls, db, task):
        #task = db.session.query(Tarea).filter(and_(Tarea.content == contenido, Tarea.user_id == tarea[1], Tarea.category == tarea[2], Tarea.limit_date == datetime.strptime(tarea[3].replace("-","/"), "%Y/%m/%d"))).first()
        db.session.add(task)
        db.session.commit()
        db.session.close()
