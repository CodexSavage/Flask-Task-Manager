# db.py


#### cabecera

```python

		from sqlachemy import create_engine
		from sqlalchemy.orm import sessionmaker, declarative_base


```

Importamos de las librerias sqlalchemy y sqlalchemy.prm los módulos create y sessionmaker, declarative, respectivamente, para crear el motor que nos permita manejar la conexión a la base de datos y el lenguaje (dialecto) que emplea.

```python

		engine = create_engine('sqlite:///src/database/data.db', connect_args={"check_same_thread":False} )
		Session = sessionmaker(bind=engine)
		session = Session()
		Base = declarative_base()

```

* engine : motor de la conexión de la base a la base de datos
* Session : para el manejo de las sesiones de la conexión
* session : instancia de la sesión.
* Base : función que construye una base de datos a partir de una clase definida.




