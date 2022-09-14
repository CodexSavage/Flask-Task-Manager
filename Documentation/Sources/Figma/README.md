# FIGMA

Para el desarrollo de esta aplicación web, he empleado FIGMA como software para el desarrollo de la parte de diseño previo de mi aplicación. 

En este repositorio podremos observar los siguientes diseños de cada una de las pantallas que componen la aplicación:

* '/login' : Pantalla donde procederemos a iniciar sesión, com nuestro usuaio/correo y contraseña. También dispone de la opción de registro.
* '/register' : Pantalla para el registro del nuevo usuario.
* '/home' : Pantalla que nos mostrará el contenido relacionado con las tareas.
* '/page-not-found : Pantalla para el manejo de error 404, personalizado para nuestra página.


# Home

La ventana de 'Home' continua con la misma paleta de colores. No obstante, cuenta con degradado de colores más formal y amiga que la ventana de 'Login', manteniendo los colores primarios para la web.<br>

La ventana está compuesta por 4 elementos principales:

* Header
Elemento constante en toda la web, pero que al mantener la sesión en estado activo, permitirá cerrar sesión en cualquier momento.

* Búsqueda
Elemento que permitirá realizar la búsqueda de tareas. (El objetivo es que se pueda llegar a realizar una búsqueda con palabras que contengan dichas letras o palabras, en el caso de no llegar a realizarse, quedará pendiente de realización.

* Tareas
Conjunto de elementos/tarjetas que se visualizaran de forma lineal con un scroll horizontal, cada una de las tareas establecidas. <br>

Las tareas son conformadas por 5 elementos:
		* Tarjeta : elemento que de forma a la targeta.
		* Imagen: elemento que tiene la finalidad de especificar el tipo de tarea que se va a realizar.
		* Nombre: elemento que describe la tarea a realizar.
		* Estado: elemento formado por un toggle, donde el mod off, indica no hecho, y On, donde sí.
		* Eliminar: elemento que permite eliminar la tarea, independientemente de si está acabada o no.

* Añadir Tarea
Elemento que permite al usuario poder acceder a una ventana donde podrá especificar ciertas atributos de la tarjeta de creación de la tarea.
