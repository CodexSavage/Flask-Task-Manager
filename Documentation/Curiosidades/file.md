# Apuntes personales

Cuando tenemos varias tablas, a la hora de añadir registros en las tablas relacionales no existe un método por el cual debamos especificar la tabla de la base de datos o la clase a la que vayamos añadir dichos registros. Es decir no existe como tal un comanando como el siguiente:

```python

		user = User("Joel", "joel@hotmail.com", "21")
		db.session.query(User).add(user)
		db.session.commit()
		db.session.close()

		# Alternativa que no existe:

		user = User("Joel", "joel@hotmail.com", "21")
		db.session.query(User).insert(values)
		db.session.commit()
		db.session.close()


```

Para simplificar todo ello, el ORM de SQLALCHEMY, lo simplifica de la siguiente manera:

```python

		user =  User("Joel", "joel@hotmail.com", "21")
		db.session.add(user)
		db.session.commit()
		db.session.close()

```

Al principio al no conocer como funcionaba completamente el ORM de SQLALCHEMY, busqué docuemntación al respecto y no encontré nada al respecto, ya que lo intenté de esa forma al inicio, pero tenía errores que no tenían sentido, así que comencé a emplear el comando:

```python

	from sqlalchemy import text

	sql = "INSERT INTO user(username, email, age) values('Joel', 'joel@hotmail.com', '21')"
	db.essiion.execute(text(sql))
	db.session.commit()
	db.session.close()


```

Tras muchas pruebas y errores, con soluciones propuestas en foros, al error "IntegrityError: ERROR: NOT NULL constraint failed", llegué a varias soluciones que "podrían" llegar a ser útiles, como definir en la columna de la llave primaria, el parámetro "autoincrement=True", para que no existiera algún error en definir valores nulos en la definición de los atributos de la base de datos, ya que en mi caso, al contar con las siguientes clase, para Usuario y Tarea:

```python

		class User( db.Base, UserMixin ) :
			__tablename__ = "user"
			id = Column(Integer, primary_key = True, autoincrement=True)
			username = Column(String, nullable=False)
			email = Column(String, nullable=False)
			fullname = Column(String)
			password =  Column(String, nullable=Faslse)

			def __init__(self, username, email, fullname, password):
				self.username = username
				self.email = email
				self.fullname = fullname
				self.password = password


		class Tarea( db.Base ) :
			__tablename__ = "tarea"
			id = Column(Integer, primary_key=True, autoincrement=True)
			content = Column(String, nullable=False)
			doit = Column(Boolean, default=0, nullable=False)
		

```

De esta forma evitaba que los atributos no se quedarna si alfún tipo de dato relevante para su registro.


# Problemas

En un punto del desarrollo, llegué a tener alguno inconvenientes con el ORM de SQLALCHEMY. No podíaemplear algunas funciones como mencioné anteriormente. Tras buscar algunas soluciones, la solución para este tipo de problemas fue muy simple, bastó con volver a transcribir la clase afectada y elimnar la orignal, así como la base de datos. De esta manera el error cesó. 


# Acceso a los datos de tablas relacionales

Pra el acceso a los datos de dos tablas relacinadas, siendo el tipo de relacion '1 a muchos', se debe tene en cuenta que la clase creada, la que luego se añade a la base de datos, se comporta como una estructur de una estructura, pudiendo acceder a los datos de la otra tabla especificando el 'backref' y el atributo que querramos obtener. Ejemplo:

```python


		


```


