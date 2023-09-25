24/09/2023
# flask-platzi
Curso básico de flask de Platzi

## Requerimiento inicial

* Instalar python 
    https://www.python.org/downloads/
* Instalar pip 
    https://www.neoguias.com/como-instalar-pip-python/
* Instalar virtualenv 
    pip install virtualenv
* Crear una ambiente virtual con virtualenv
    virtualenv venv
* Activar el ambiente virtual source venv/bin/activate
    source venv/bin/activate
* Instalar flask
    pip install flask
* Comprobar la instalación de flask
    pip freeze
* Crear requirements
    pip freeze > requirements.txt
* Crar la variable app
    export FLASK_APP=main.py
* Activamos el servidor
    flask run
* Activar debug solo para trabajar en producción o desarrollador, desactivarlo al momento del despliegue
    export FLASK_DEBUG=1