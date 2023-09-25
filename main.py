"""
    Configuración inicial y básica para crear una aplicación utilizando el framework flask
"""
from flask import Flask, request, make_response, redirect, render_template

# 
app = Flask(__name__)

@app.route('/')
def index():
    # Capturamos la iP
    user_ip = request.remote_addr
    
    # redireccionamos a la ruta /hello
    response = make_response(redirect('/hello'))
    # cramos una cookie con la ip
    response.set_cookie('user_ip', user_ip)
    
    # retornamos la respuesta
    return  response


# variable con actividades
todos = ['todo 1', 'todo 2', 'todo 3']

# empleamos el decorador para indicar la rutae
@app.route('/hello')
# creamos la funcion re retorna hello world flask
def hello():
    # recuperamos le dirección IP de la cookie
    user_ip = request.cookies.get('user_ip')
    
    context = {
        'user_ip' : user_ip,
        'todos' : todos
    }
    
    
    # retornamos con render_template el html y con los argumentos
    return render_template('hello.html', **context) # se utilizan ** para expandir el diccionario, de lo caontrario se tendria que utilizar context.user_ip