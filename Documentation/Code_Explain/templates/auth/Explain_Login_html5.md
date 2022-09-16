# Login html

```html

        {% extends './index.html' %}
{% block title %} Login User {% endblock %}
{% block customCSS %}
<link rel="stylesheet" href="/static/css/login.css">
{% endblock %}
{% block body %}
<header>
    <h3 class="name"><a class="login-codex" href="{{ url_for('login')}}">codexsavage</a></h3>
</header>
<div class="card">
    <form  action="/login" method="POST">
        <img class="logo" src="{{ url_for('static', filename='img/logo.png')}}" alt="" width="110" height="110">
        <h5>PLEASE SIGN IN</h5>
        {% for message in get_flashed_messages() %}
            <div class="alert">
                <span class="closebtn" onclick="this.parentElement.style.display='none';">&times;</span>
                {{message }}
            </div>
            <br>
        {% endfor %}
        <div class="input-field">
            <input type="text"  id="email" name="email" required>
            <label class="check" for="email">Email or username</label>
        </div>
        <div class="input-field">
            <input type="password" id="pwd" name="pwd" required >
            <label class="check" for="pwd" >Password</label>
        </div>
        <div class="input-check">
            <label>
                <input type="checkbox">Remember me
            </label>
        </div>
        <button class="signIn" type="submit">Sign in</button>
    </form>
</div>
<p class="register">Don't have an account yet? <a href="/register"> Register now</a></p>
{% endblock %}

```

La plantilla de Login, nos permite iniciar sesión con nuestra cuenta. Más allá de introducri datos y enviarlos al servidor, permite dos cosas, emplear el nombre, para cargar de nuevo la ventana, y utilizar el link de registrarse para acceder a una nueva ventana para registrarnos pro primera vez.