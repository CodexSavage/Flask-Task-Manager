# APP.py

El siguiente fragmento de código muestra la estructura del desarrollo de la aplicación web llevada a cabo, con su respectiva explicación, puesto que en el código no se reflejan dichas explicaciones.

## Encabezado

Para poder hacer uso de algunas funciones definidas en otras librerias y aplicaciones anteriormente creadas, importamos dichas funciones para aplicar aquellas que consideremos imponecesarias.

```python
		#from crypt import methods
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
* crypt: importamos esta libreria para poder emplear la función method, para poder poder determinar el mótodo de consulta a la pa´gina web. En este caso, está comentada, ya que luego de iniciarlo por primer vez esta función queda registrada en el sistema y ya no es necesario su uso, no obstante, en caso des error, simplemente sería necesaraio descomentarlo.
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

Al principio lo que nos interesa en comprobar que el usuario existe, eso lo comprobamos con la variable </em>user_logged_web</em>, cuyo valor puede ser _None_ o una clase. En el caso de retornar un valor _None_, querrá decir que el usurio no existe en la base de datos, en caso contrario, de sí existir, comprobará la contraseña con la condición <em>"if user_logged_web.password"</em>. Si prestamos atención, para esta condición estamos accediendo al atributo del resultado de la clase creada para por parámetro, y es que, anteriormente definimos que sería una contraseña, pero en la llamada a la función <em>user_logged_web = ModelUser.login( db, user )</em>, al recibir la clase, el atributo password, a su vez toma el valor de una función, la cual devolverá True si la contraseña coincide con el de la base de datos, o False si no, todo esto en la función <em>login</em> de <em>ModelUser</em>.

Una vez comprobado que coincide, tanto usuario como contraseña mediante <em>login_user( user_logged_web )</em> confirmamos el inicio de sesión. En caso de cumplir con las condiciones se lanzarán las respectivas alertas como, "usuario no encontrado" o "Contraseña incorrecta".

Para cada condición se tiene que retornar algo, en el caso de haber algún fallo vuelve a renderizar la plantilla de "home.htmml" hasta que se introduzcan correctamente las credenciales de autenticación, en cuyo cayo nos redireccionará a la ruta de 'home' donde ya encontramos aplicación en sí.

#### Home

#### Logout

#### Register

#### Delete task

#### if __name__ == '__main__':
