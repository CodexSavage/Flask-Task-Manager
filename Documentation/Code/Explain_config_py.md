# config.py


La implementación de este archivo es debido a la necesidad de implementar funciones y características con la inteción de mejorar la propuesta de proyecto.

A continuación procederé a explicar cuáles son los atributos y finalidad de ellos.

#### Cabecera

```python

		from os import environ, path, usrandom

```

De la libreria 'os' importamos los módulos de environ path y usrandom.
* environ: para obtener valores del entorno en el que trabajamos. Esto es útil para establecer una llave secreta que permita obtener más seguridad en el proyecto.
* path: esta función nos permite obtener la dirección actual en el que se aloja el arhivo actual.
*  usrandom: nos permite crear una cadena de texto de lonitud especificada, con valores alfanuméricos alternos.

#### Cuerpo

```python

		
		class config:

			SECRET_KEY = os.urandom(70)
			TEMPLATES_FOLDER = 'templates'
			STATIC_FOLDER = 'static'
			MODELS_FOLDER = 'models'
			SQLALCHEYM_DATABASE_URI = 'sqlite:///src/database/data.db'
			SQLALCHEMY_TRACK_MODIFICATIONS = False

```
Creamos esta clase 'config' ya que esta manera podemos almacenar valores de personalización de ciertos parámetros para nuestro proyecto.

* SECRET_KEY : llave secreta que nos permite adminstrar la seguridad de nuestro proyecto.
* TEMPLATES_FOLDER : especificamos donde se encuentra la carpeta de 'templates'.
* STATIC_FOLDER: especificamos donde se encuentra la carpeta de 'static'.
* MODELS_FOLDER: especificamos donde se encuentra la carpeta de 'models'.
* SQLALCHEMY_DATABASE_URI: especificamos la dirección donde de halla la base de datos, la cual trataremos y el entorno que emplearemos (en nuestro caso sqlite).
* SQLALCHEMY_TRACK_MODIFICATIONS: para poder hacer seguimiento de las modificaciones.

```python


			class ConfigDevelopment(Config):
				
				FLASK_ENV = 'development'
				DEBUG = True
				Testing = True

				"""

				SQLITE_HOST = localhost
				SQLITE_USER = 'root'
				SQLITE:PASSWORD = '123345'
	
				"""

```

Clase cuyo orientación esta enfocada para un entorno de desarrollo con parámetros específicos.

* FLASK_ENV : determinamos el tipo entorno de desarrollo.
* DEBUG : para la búsqueda de errores en el software.
* TESTING : para funciones de test.

El resto de atributos están comentados porque no encontré docuementación sobre ellos, y a base de que se podía emplear para MySQL, con atributos adaptados a él, no quise añadirlos, hasta cerciorarme.

```python

			config = {
				'development' = ConfigDevelopment
			}

```

Creo un diccionario, para complicar al acceso a los atributos de la clase en caso de intrusión.<br>

El obejtivo de hacerlo de esta manera es evitar compremeter cierta información relevane a un usuario externo sin acreditación que intente acceder al sistema sin autorización alguna.

