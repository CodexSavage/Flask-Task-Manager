# APP.py

El siguiente fragmento de código muestra la estructura del desarrollo de la aplicación web llevada a cabo, con su respectiva explicación, puesto que en el código no se reflejan dichas explicaciones.

## Encabezado

Para poder hacer uso de algunas funciones definidas en otras librerias y aplicaciones anteriormente creadas, importamos dichas funciones para aplicar aquellas que consideremos imponecesarias.

```python
		#from crypt import methods
		from datetime import datetime
		from pickle import GET
		from flask import FLASK, render_template, request, redirect, url_for, flash, session
		fromflask_login import LoginManager, login_user, logout_user
		from config import config
		from sqlalchemy import and_
		import db
		# Models
		from models.ModelUser import ModelUser
		from models.ModelTarea import ModelTarea
		# Entities
		from models.entities,Tarea import Tarea
		from models.entities.User import User

```
<strong>Explicación</strong>
* __crypt__: importamos esta libreria para poder emplear la función method, para poder poder determinar el mótodo de consulta a la pa´gina web. En este caso, está comentada, ya que luego de iniciarlo por primer vez esta función queda registrada en el sistema y ya no es necesario su uso, no obstante, en caso des error, simplemente sería necesaraio descomentarlo.
* __datetime:__ de esta librería importaremos el módulo 'datetime' para poder convertir valores de tipo str a date, aceptados para la base de datos.
* __flask:__ esta librería es la tradicional y necesaria para poder trabajar con Flask, de ntre muchs de sus funciones, para este proyecto empleamos las sigueintes funciones:
	* __Flask:__ para el flujo de trabajo del sistema y motor de funcionamiente de FLASK.
	* <strong>render_template:</strong> Para el uso de renderizado de plantillas.
	* __request:__ para la realización de consultas a la página web.
	* <strong>url_for:</strong> para especificar un dirección de trabajo.
	* __flash:__ empleado para lanzar mensajes. Útil para mostrar alertas en caso de cumplirse condiones, como fallo de credenciales.
	* __session:__ empleado para almacenar en una instancia de memoria una consulta llevada a cabo, para posteriormente ser utilizada en alguna parte del código. Una anañogía similar, sería una tienda, la marca proporciona un producto a una tienda, y la persona que quiera ducho producto la comprará.<br>
	Si alguna función la necesita estará 100% disponible para su manipulación (más adelante hablaremos más al respecto).
* <strong>flask_login:</strong> esta libreria se emplea para el manejo del login.
	* __LoginManager:__ empleado para la gestión del "inicio de sesión".
	* <strong>login_user:</strong> emplado para el incio de sesión del usuario.
	* <strong>logout_user:</strong> empleado para el cierre de sessión del usuario.

* __config:__ esta no es una libreria propia de python, si no, es una propia, en la cual hemos configurado ciertos parámetros de Flask y SQLALCHEMY (Especificado en "Explain_config_py.md").
* __db:__ importamos el código perteneciente a la fuente "db.py", así como las funciones que la componen.
* __models.ModelUser:__ empleado para utilizar algunas funciones realizadas en ella.
* __models.ModelTarea:__ empleado para utilizar algunas funciones realizadas en ella.
* __models.entities.Tarea:__ empleado para utilizar algunas funciones realizadas en ella, especificamente de la clase Tarea.
* __models.eniitities.User:__ empleado para utilizar algunas funciones realizadas en ellas, específicamente de la clase User.

## Configuración inicial

```python

		app = Flask(__name__)
		login_manager_app = LoginManager(app)
		
		@login_manager_app.user_loder
		def load_user( id ):
		return modelUser.get_by_id( db, id )

```

* __app:__ inicio de Flask en nuestra aplicación.
* <strong>login_manager_app:</strong> manejo de las sesiones para el usuario.

## Estructura de la página

#### Raíz

```python

		@app.route('/')
		def index():
			return redirect( url_for('login') )

```

Ruta raiz designada a '/' la cual nos redirige a la ventana de 'login'.

#### Login
```python

		@app.route('/login', methods=['GET', 'POST'] )
		def login():
			if request.method == 'POST':
				user = User( request.form['email'], request.form['email'], 0, request.form['pwd'])
				user_logged_web = ModelUser.login( db, user )
				if user_logged_web:
					if user_logged_web.password:
						login_user( user_logged_web )
						id = ModelUser.GetID( db, user_logged_web )
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

```
Ruta '/login'. Ésta cuenta con los parámetros 'GET' y 'POST' para la transmisión de información.

Como nota, empleando el parámetro 'GET', la posibilidad de tener un problema de seguridad será mayor puesto que la informacción se encontraría visible en la URL.

Para solucionar el problema anterior definimos la condición "_if request.method == 'POST'_", con esto decimos que si se recibe algún tipo de información realizará la siguiente condición.

Una vez detectado algo, pasamos a rellenar los valores de los atributos, con los que se nos pasa. En este caso, el formulario para iniciar sesión, requiere del nombre de usuario o correo y la contraseña. Al proponer la opción de introducir nombre de usuario o correo electrónico( con el que se registró), rellenamos los valores de la clase "User" con aquellos que se nos proporcione, teniendo, la clase "User", los siguientes atributos: nombre de usuario, email, nombre completo y contraseña.

Al principio lo que nos interesa en comprobar que el usuario existe, eso lo comprobamos con la variable </em>user_logged_web</em>, cuyo valor puede ser _None_ o una clase. En el caso de retornar un valor _None_, querrá decir que el usuario no existe en la base de datos, en caso contrario, de sí existir, comprobará la contraseña con la condición <em>"if user_logged_web.password"</em>. Si prestamos atención, para esta condición estamos accediendo al atributo del resultado de la clase creada para por parámetro, y es que, anteriormente definimos que sería una contraseña, pero en la llamada a la función <em>user_logged_web = ModelUser.login( db, user )</em>, al recibir la clase, el atributo password, a su vez toma el valor de una función, la cual devolverá True si la contraseña coincide con el de la base de datos, o False si no, todo esto en la función <em>login</em> de <em>ModelUser</em>.

Una vez comprobado que coincide, tanto usuario como contraseña mediante <em>login_user( user_logged_web )</em> confirmamos el inicio de sesión. En caso de no cumplir con las condiciones se lanzarán las respectivas alertas como, "usuario no encontrado" o "Contraseña incorrecta".

Para cada condición se tiene que retornar algo, en el caso de haber algún fallo vuelve a renderizar la plantilla de "home.htmml" hasta que se introduzcan correctamente las credenciales de autenticación, en cuyo caso, nos redireccionará a la ruta de 'home' donde ya encontramos aplicación en sí.

#### Home

```python

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
						
						for task in userTasks:
							if task.content in search_task:
								
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

```
Anteriormente, mencionamos el uso de las sesiones en Flask, para enviar información interna, y es que al tener problemas al enviar el identificador como un parámetro más a la hora de redirigir nuetra plantilla de *Login* a *Home*, la alternativa más eficiente era mediante las sesiones, ya que en vista a futuras necesidades de mantener este valor, permitiá reutilizar código y no sobrecargar tanta información irrelevante. El principal motivo es que, en el momento de renderizar o redirigir a otra plantilla, en la terminal de consultas, se podía apreciar que la infromación que se transmitía como parámetros se mostraban en la URL de la página por lo que el único valor que podía englobar el resto era el identificador, ya que al ser único, teniendo solo este podía obtener cualquier infromacióndel resto de sus atributos, por ello la importancia de mantener este identificador(id), es importante, como he dicho antes, para su reutilización. Desconozco aún si realmente puede contribuir a una futuro fallo de seguridad, no obstante es algo que investigaré.

Un vez obtenido el valor del identificador( id_ ), obtendremos todas las tareas pertenecientes a dicho identidficador, en este caso, el identificador, pertenece al usuario, no a las tareas, y ya que las tablas de usuarios y tareas se encuentran relacionadas, siendo su relación 1 a muchos, mediante el identificador de usuario puedo obtener todas la tareas que pertenezcan a dicho usuario, a partir de la función __ModelTarea.getTask_byID( db=db, userId=id_)__.

En este punto si llegamos a obtener alguna interacción con el servidor, realizaremos las pertienentes instrucciones, si no, se renderizará la plabtilla *Home*. En cao afirmativo podemos distinguir principalmente 2 interacciones, la primera referente al 'buscador de tarea/s'. En caso de detectar el boton de búsqueda, comprobará si se ha introducido texto en él, en caso negativo se renderizará de nuevo la plantilla de home con toda las tareas coincidentes con el id del usuario y, en caso afirmativo, buscará entre todas las tareas, aquella que coincida, entonces sólo mostrará quellas que coincidan. Cabe destacar que en un futuro se modificrá esto para que busque tareas similares y coincidentes, es decir, conque alguna palabra esté dentro del nombre de la tarea, pueda mostrarlo libremente. A la par, como forma de boton hacia 'Home' si no se introduce nada en el input text y se da enter en buscar tareas, se nos mostraran de nuevo toda las tareas.

En caso de no ser el boton de búsqueda, el otro objeto interactivo son los switch/toggle para modificar el estado de la tare, de hecho a no hecho. No es neesario mencionar que dicha modificación no se guardará a no ser que se verifique el cambio con el input submit (verify#). 

En este punto, donde es el mismo usuario el que tiene que modificar el estado de la tarea, fue necesario individualizar cada carta de tarea para que funcionara de forma independiente, y esto se ve con más claridad en el archivo html.

```html

			{% extends './index.html' %}
			{% block title %} home {% endblock %}
			{% block customCSS %}
			<link rel="stylesheet" href="/static/css/home.css">
			{% endblock %}
			{% block body %} 
				<header>
					<h3 class="name"><a class="home-codex" href="{{ url_for('home')}}">codexsavage</a></h3>
					<a class="B" href="{{ url_for('logout') }}" >Log out</a>
				</header>

				<h1>WELCOME</h1>
				{% for message in get_flashed_messages() %}
				<div class="alert">
					<span class="closebtn" onclick="this.parentElement.style.display='none';">&times;</span>
					{{message }}
				</div>
				<br>
			{% endfor %}
				<div class="send_added_task">
					<form action="{{ url_for('home')}}" method="POST">
						
						<div class="input-field">
							<input type="text"  id="search_task" name="task"  class="input_task" placeholder=" Introduce task">
							<label class="check" for="search_task"></label>
						</div>
						<input class="send" type="submit" value="search" name="send">
					</form>
				</div>
				<div class="container">
					<form action="{{ url_for('home')}}" method="POST">
						<ul class="listas">
							{% for tarea in tareas: %} 
							<li>   
								<div class="card">
									<div class="inbox">
										<a class="del" href="/delete_task/{{tarea.id_tarea}}/{{tarea.user_id}}">
											<img class="delete_src" src="{{ url_for('static', filename='img/close.png')}}" alt="" width="19" height="19">
										</a>
									</div>
									<div class="layout_down">
										<p class="task_and_edit">
											{{tarea.content}}
											<a class="edit" href="/edit_task/{{tarea.id_tarea}}">
												<img class="edit-task" src="{{ url_for( 'static', filename='img/edit.png')}}" alt="edit" width="20" height="20">
											</a>
										</p>
										<p class="limit_day">
											Limit day: <strong>{{ tarea.limit_date }}</strong>
										</p>
										<div class="wrap-toggle" >
										{% if tarea.done %}
											<input type="checkbox" id="toggle{{tarea.id_tarea}}" name="boton_switch{{tarea.id_tarea}}" value="{{tarea.id_tarea}}" checked="checked" class="offscreen">
											<label for="toggle{{tarea.id_tarea}}" class="switch"></label>
										{% else %}
											<input type="checkbox" id="toggle{{tarea.id_tarea}}" name="boton_switch{{tarea.id_tarea}}" value="{{tarea.id_tarea}}" class="offscreen" >
											<label for="toggle{{tarea.id_tarea}}" class="switch"></label>
										{% endif %}
										</div>
										<input type="submit" name="verify-value" value="Verify{{tarea.id_tarea}}" class="verify_submit">
									</div>
								</div> 
							</li>               
							{% endfor %}
						</ul>
					</form>
				</div>
				<div class="new_task">
					<a class="C" href="{{ url_for('add_new_task') }}">Add new task</a>
				</div>
			{% endblock %}
```
Como podremos fijarnos, al pasar una lista de todas las tareas, aproveché para que, mediante un nombre propio pudiese obtener el valor de dicha tarea, asociada a su id, de forma independiente, ya que al principio todas estaban relacionadas a la primera tarea, y cualquier cambio afectaba a ésta, por lo que esta solución fue la más inteligente para la consulta de datos y obtención de información relevante.

#### Add_new_task

```python

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
			
```

Como anteriormente se mecionó el uso de la sesión era importante y, esta no es la excepción, aquí volveremos a hacer uso de ella, para asociar a la tarea con el identificador de quién está añadiendo la tarea, el cual se verá reflejado en la base de datos con el resto de la información necesaria. Y en el caso de haber algún fallo en la obtención de éste, se manejará el error con try y except.

Aquí simplemente la información que recibamos por parte de la página web, será introducida como información de complementación para los atributos de la clase 'Tarea', posteriormente se guardará en la base de datos mediante ka llamada a la función *ModelTarea.Add_new_task(db=db, new_task=new_add_task)*. Finalmente se volverá a redirigir a la plantilla de 'Home'.

Tanto en este como en la plantilla de editar tarea, en el archivo html se especificó que cada uno de los input fuese requerido, es decir, que no se podía enviar nada hasta que, todos los campos estuviesen llenos.

#### Edit_task

Código python
```python

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


```
En este apartado lo que nos interesa es cambiar datos como fecha y categoria, por lo que el cambio de nombre de tarea está bloqueado en el archivo html, por lo que los dos campos anteriormente mencionados sí son editables.

Como aporte, a la hora de editar una tarea, en la plantilla podremos visualizar los valores actuales para poder visualizar qué campos requieren de modificación. Y evidentemente todos los cambios se guardaran en la base de datos.
#### Logout

```python

		@app.route('/logout')
		def logout(): # Done
			logout_user()
			return redirect(url_for('login'))
```
Función para salir y cerrar sesión alctual del usuario registrado.

#### Register

```python

		@app.route('/register', methods=['GET', 'POST'])
		def register(): # Done
				
			if request.method == 'POST':
				username = request.form['uname']
				email = request.form['email']
				fullname = request.form['fname']
				pwd = request.form['pwd']
				confirm_pwd = request.form['confirm-pwd']
				if confirm_pwd is not pwd:
					flash("Password is not correct")
					# print("Contraseeña no igual")
					#return render_template('register.html')
				# print("{} {} {} {}".format(username, email, fullname, pwd))
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


```
Con una estructura similar a la de añadir tareas, ésta, se diferencia en que a la hora de añadir un nuevo usuario, a parte de recibir la información de nuevo resgitro de usuario, comprueba su existencia en la base de datos, tanto para nombre de usuario como para correo electrónico, dos claves consideradas únicas, para la obtención de datos. Una vez validada sus credenciales, mediante la función *ModelUser.Registration(db, username_= username, email_ = email, fullname_ = fullname, password_= pwd)*, se procederá el registro, en caso contrario, se lanzará un mensaje conforme el usuario o correo electrónico, ya existen y se volverá a pedir al usuario que lo rellene, con otra credenciales, evidentemente.

#### Delete task

```python

		@app.route('/delete_task/<idTarea>/<userId>')
		def delete_task(idTarea, userId):
			taskDelete = db.session.query(Tarea).filter(and_(Tarea.id_tarea == idTarea, Tarea.user_id == userId)).first()
			db.session.delete(taskDelete)
			db.session.commit()
			db.session.close()
			return redirect(url_for('home'))

```
Esta función permite borrar un atarea pasando como parámetros el identificador de la tarea y del usuario, valores indepensables para determinar la tarea.
#### if __name__ == '__main__':

```python
			
		if __name__ == '__main__':
				
			db.Base.metadata.drop_all( bind=db.engine, checkfirst=True)
			app.config.from_object(config['development'])
			db.Base.metadata.create_all(db.engine) 
			ModelUser.AddUser(db)
			ModelTarea.AddTarea(db)
			app.run()
```
Línea a línea, podremos realizar las sigueintes acciones:
* Borrar el contenido de la base de datos.
* Cargar los parámtros especificados en el archivo de configuración de flask.
* Crear las tablas establecidas en los ficheros de la clases, es decir, las tablas de las bases de datos.
* Añadir nuevos usuarios.
* Añadir nuevas tareas.
* Inciar la aplicación de flask.