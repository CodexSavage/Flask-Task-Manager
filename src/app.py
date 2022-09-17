#from crypt import methods
from dataclasses import replace
from datetime import datetime
from pickle import GET
from unicodedata import category
from flask import Flask, render_template, request, redirect, url_for, flash,session
from flask_login import LoginManager, login_user, logout_user
from config import config
from sqlalchemy import and_
import db
# Models
from models.ModelUser import ModelUser
from models.ModelTarea import ModelTarea
# Entities
from models.entities.Tarea import Tarea
from models.entities.User import User

app = Flask(__name__)
login_manager_app=LoginManager(app)


@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db,id)


@app.route('/')
def index(): #Done
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login(): # Done
    if request.method == 'POST':
        user = User(request.form['email'], request.form['email'], 0 , request.form['pwd'])
        user_logged_web = ModelUser.login( db, user) # <models.entities.User.User object at ...>
        if user_logged_web:
            if user_logged_web.password:
                login_user(user_logged_web)
                id = ModelUser.GetID(db,user_logged_web)
                session['id'] = id
                return redirect(url_for('home'))
            else:
                flash("Invalid password...")
                return render_template('auth/login.html')
        else:
            flash("User not found...")
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')


@app.route('/home', methods=['GET', 'POST'])
def home():
    id_ = 0
    if 'id' in session:
        id_ = session['id']
    userTasks = ModelTarea.getTask_byID(db=db, userId=id_)
    if request.method == 'POST':
        find = False
        if 'send' in request.form :
            if 'task' in request.form:
                search_task = request.form['task'] 
                # print("la tarea es: ",search_task, " de longitud: ", len(search_task))
                for task in userTasks:
                    if task.content in search_task:
                        # print("tarea coincidente: {} {}".format(task.content, task.id_tarea))
                        find = True
                        convert_to_list_task = []
                        convert_to_list_task.append(task)
                        return render_template('home.html', tareas = convert_to_list_task)
                if find is not True and search_task != "":
                    flash("Task doesn't exist")
                    #print("Tarea no encontrada")
                    return render_template('home.html', tareas=userTasks)
            else:
                
                return render_template('home.html', tareas=userTasks)
        else:
            for value in userTasks:
                
                if request.form.get('boton_switch{}'.format(value.id_tarea)) == '{}'.format(value.id_tarea):
                    if request.form['verify-value'] == 'Verify{}'.format(value.id_tarea):
                        ModelTarea.Task_to_Done(db, value.id_tarea, id_)
                        #print("activate" )
                        return render_template('home.html', tareas = userTasks)
                else:
                    if request.form['verify-value'] == 'Verify{}'.format(value.id_tarea):
                        ModelTarea.Task_to_Undone(db, value.id_tarea, id_)
                        #print("No hecho")
                        return render_template('home.html', tareas = userTasks)
    return render_template('home.html', tareas = userTasks)


@app.route('/add_new_task', methods = ['GET', 'POST']) # Ruta para añadir una nueva tarea con todos los atributos relacionados
def add_new_task():
    id_ = 0
    try:
        if 'id' in session:
            id_ = session['id']
            # print("Identificador de nueva tarea ", id_)
    except Exception as e:
        raise Exception(e)
    if request.method == 'POST':
        task = request.form['task']
        task = task.lower()
        #print("la tarea en minuscula", task)
        category = request.form['category']
        fecha  = request.form['date-limit']
        fecha = fecha.replace("-","/")
        # print(task,category,fecha)
        if task and category and fecha:
            new_add_task = Tarea( content= task, done=False, user_id=id_, category=category, limit_date=datetime.strptime( fecha, "%Y/%m/%d" ))
            ModelTarea.Add_new_task(db=db, new_task= new_add_task)
            return redirect( url_for('home'))
    else:
        return render_template('add_new_task.html')
    # Falta comprobar si la tarea que se va a añadir ya existe.


@app.route('/edit_task/<tarea_id>/', methods=['GET' ,'POST'])
def edit_task( tarea_id):
    task = ModelTarea.Edit_task_byID(db,tarea_id)
    # print("La tarea a editar es: ",task)
    if request.method == 'POST':
        task.category = request.form['category']
        fecha  = request.form['date-limit']
        fecha = fecha.replace("-","/")
        task.limit_date = datetime.strptime( fecha, "%Y/%m/%d")
        # print("Tarea modificada con nuevos cambios --> ", task)
        ModelTarea.edit(db, task=task)
        return redirect( url_for('home'))
    else:
        return render_template('edit.html', tarea = task)


@app.route('/logout') # Redirección desde dentro de home como "path"
def logout(): # Done
    logout_user()
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register(): # Done
    
    if request.method == 'POST':
        username = request.form['uname']
        email = request.form['email']
        fullname = request.form['fname']
        pwd = request.form['pwd']
        confirm_pwd = request.form['confirm-pwd']
        if confirm_pwd != pwd:
            flash("Password is not correct")
            # print("Contraseeña no igual")
            return render_template('register.html')
        # print("{} {} {} {}".format(username, email, fullname, pwd))
        else:
            validateUser = ModelUser.Registration(db, username_= username, email_ = email, fullname_ = fullname, password_= pwd)
        # print(validateUser)
            if validateUser:
            # print("Registro completado")
                return redirect('login')
            else:
                # print("Usuario o correo ya existente")
                flash("User or email already exist...")
                return render_template('register.html')
    else:
        return render_template('register.html')


@app.route('/delete_task/<idTarea>/<userId>')
def delete_task(idTarea, userId):
    taskDelete = db.session.query(Tarea).filter(and_(Tarea.id_tarea == idTarea, Tarea.user_id == userId)).first()
    db.session.delete(taskDelete)
    db.session.commit()
    db.session.close()
    return redirect(url_for('home'))


"""@app.errorhandler(404)
def not_found(error):
    return render_template('page_not_found.html'),404"""


if __name__ == '__main__':
    
    db.Base.metadata.drop_all( bind=db.engine, checkfirst=True)
    app.config.from_object(config['development']) # Cargamos la configuración establecida en al archivo 'config.py'
    db.Base.metadata.create_all(db.engine) # Creamos las tablas establecidas en los ficheros de las clases)
    ModelUser.AddUser(db)
    ModelTarea.AddTarea(db)
    app.run()
