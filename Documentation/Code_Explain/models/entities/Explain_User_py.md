# User.py

Fuente destinada a la definición de la clase usuario, para la creación de la tabla relacionada a la base de datos.

### Cabecera

Todo el conjunto de librerias o referencias empleadas en la creación de la clase 'User'.

```python

        from werkzeug.security import check_password_hash, generate_password_hash
        from sqlalchemy.orm import relationship, backref
        from sqlalchemy import Column, Integer, String
        from flask_login import UserMixin
        import db    

```
* __werkzeug.security:__ esta libreria nos permite añadir funciones de seguridad a nuestro proyecto. Para este proyecto, lo que nos inteeresa es el uso de la función *check_password_hash*, que nos permite convertir el texto que pasemos como parametro en un hash, codificado. Especialemete útil, para mantener seguro las contraseñas de los usuarios.
* __sqlalchemy.orm:__ librería propia del ORM de SQLALCHEMY. Des esta librería lo que nos interesa son los métodos *relationship* y *backref*, empleados para el uso de relación entre bases de datos relacionales y referencias entre sí, respectivamente. Más adelante se explacará el contenido.
* __sqlalchemy:__ libreria de SLQLACHEMY. De este librería, utilizaremos *Column* para establecer las columnas que querramos ver reflejados en nuestra base de datos, *Integer*, para el tipo entero de datos de algunas columnas y, *String*, para el tipo de cadena de datos de el resto de columnas necesarias.
* __flask_login:__ libreria para el manejo de incios de sesión del usuario. Des esta libería lo que nos es útil es el módulo *UserMixin*, un parámetro que hereda la clase y establece el inicio y control de sesión de una cuenta.
* __db:__ importamos del archivo de configuración funciones establecidas como *db.Base*.

### Clase 'User'

Definición de la clase 'User'
```python


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

```

La clase User, cuenta con herencia múltiple, por una parte __db.Base__ se encargará de administrar la creación y manipulación de datos referentes a la base de datos, mientras que __UserMixin__, como anteriormente se mencionó, para el control de inicio de sesión.

De entre los atributos, destacamos que los que se encuentra definicmos anteriormente al constructor *__init__*, son los nombres que hemos designado a las columnas de la base de datos, siendo el *__tablename__*, el nombre que reflejará en la base de datos, y el resto, los nombres que tendran las columnas. Haciendo un énfasis en ellos, observamos, que siguen un patron similar; se especifica el tipo de dato que almacenará y si se requiere que ese dato sea introducido con *nullabel=False*, es decir, si no se introduce un dato, se considerará como NULL. Sin embargo, de entre uno de ellos, vemos uno que es diferente, ya que no sigue el mismo patrón, y es debido a que, éste es el relacional, el cual permite enlazar la otra tabla de la base de datos con esta, tomando referencia directa a la hora de obtener datos. Ésta, especifica a qué tabla está relacionada (nombre la clase en minúscula), y como identificará la otra a ésta.

En cuanto al constructor, es necesario conocer simplemente los atributos necesarios para identificar una tarea:
* __Username:__ nombre de usuario del cliente. Tomando un valor único controlado en la función de registro, para evitar que exista más de un usuario con el mismo nombre de usuario o *nick*.
* __email:__ correo de electrónico del cliente. Tomando un valor único, controlado en la función de registro, para evitar que exista más de un usuario con el mismo correo.
* __Fullname:__ nombre completo del usuario requerido para el registro.
* __Password:__ contraseña requerida, que posteriormente será hasheada por temas de seguridad.

En cuanto a las funciones de __repr__ y __str__, las empleamos para mostrar información por terminal a la hora de desarrollo, según nuestras necesidades.

```python

            @classmethod
            def CheckPassword(cls, pwd, password_hashed):
                return check_password_hash(password_hashed, pwd)


            @classmethod
            def GeneratePassword_hash(cls, password):
                return generate_password_hash(password)

```
* __CheckPassword:__ función para comprobar la contraseña con la guardada en la base de datos hasheada.
* __GeneratePassword_hash:__ función para generar una contraseña hasheada una vez el nuevo usuario haya cumplido el registro perfectamente.