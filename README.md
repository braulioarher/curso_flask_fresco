# Notas de apoyo

## Flask-WTF

Las web forms se usan para recibir informacion de los usuarios Flask-WTF es una extension que maneja estas formas y las integra en Flask para instalar debemos hacer lo siguiente:

    pip install flask-wtf
una vez instalado la configuracion de SECRET_KEY debe ser declarado

        class Config(object):
    .....
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'

Flask-WTF usa el valor SECRET_KEY para protejer las web forms de ataques de fuerza cruzada

## Crear una base de datos y crear modelos

## Para hacer consultas directamente a la base de datos desde flask

Primero iniciamos la shell para esto;

    flask shell

Despues importamos nuestro modelo
    from helloapp.models import User

Despues importamos nuestra base de datos
    from helloapp impor db

Listo ahora podemos hacer consultas o agregar campos

### Ejemplo de agregar un campo

user1 = User(fname="James", lname="smith", email="james@abc.com")
db.session.add(user1)
db.session.commit()

### Ejemplo de hacer una consulta

User.query.all()
User.query.filter(User.fname == 'James').all()