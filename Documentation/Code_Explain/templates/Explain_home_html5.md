# Home.html
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

El cuerpo del archivo html cuenta principalmente con 6 elementos, el banner, el mensajde de bienvenida, el lanzador de alertas,el buscador de tareas, las targetas de tareas y el de a??adir nuevas tareas

Uno de los elementos primarios que se define como alert, nos permite establecer donde se crear?? la caja de mensaje, en este caso de error. En nuestro c??digo principal de python, al haber alg??n error se ejecuta una funci??n flash, la cual mostrar?? un mensaje en forma de caja conforme al error ocurrido.??sta cuenta adem??s con la opci??n de minimizar una vez observado.

Para el uso individual de las tareas, se recorre en un bucle for la lista de la tareas pasada por par??metro al renderizar la plantilla html, de esta forma, al asignar un valor individual a cada input, simplemente esperando una consulta referente al nombre propio asignado, se puede conseguir un trabajo independiente entre las targetas de tareas. A dem??s, el uso de Jinja, facilita en gran medida la gesti??n de la informaci??n.

Para las tarjetas y el dise??o en general se realiz?? incialmente en FIGMA (acceso al archivo en el PATH /Documentation/Sources/Figma). Para dar un toque moderno se pens?? en otorgar animaciones sutiles, es por ello que al __div__ llamado `container" se le dio la posibilidad de trabajar como un scroll vertical, adaptable, es decir que dependiendo de las dimensiones de la pantalla las targetas se monstraran de una forma u otra ordenada, si no hay suficiente espacio para mostrar 3 en la pantalla se mostrarn en columnas de 2 con scroll vertical, y as?? conforme las unidades que puedan aparecer en pantalla.