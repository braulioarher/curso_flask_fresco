from crypt import methods
from flask import request
from helloapp import render_template, redirect, url_for
from helloapp import app, db
from helloapp.models import User
from .forms import UserForm


@app.route("/")
def hello():
    return render_template("index.html", title="Title Page of Hello App", user=None)

@app.route("/user/<username>/")
def hello_user(username):
    return render_template("index.html", title="User Page", user=username)

@app.route("/user/<username>/<int:age>/")
def display_age(username, age):
    return '''
<html>
    <head>
       <title>User Page</title>
    </head>
    <body>
        <h1>Hello, ''' + username + '''!!!</h1>
    </body>
</html>'''

@app.route("/home")
def home():
    return redirect("http://localhost:5000/")

@app.route("/greet/user/<uname>")
def greet_user(uname):
   return redirect(url_for('hello_user', username=uname))

@app.route("/users/")
def display_users():
    users = ['John', 'Rosy', 'Jack', 'Sammy', 'Lilly']
    return render_template('users.html', title='Users', users=users)

@app.route("/adduser/", methods=['GET', 'POST'])
def useradd():
    form = UserForm()
    if request.method == 'POST':
        user = User(fname=form.fname.data, lname=form.lname.data, email=form.email.data)
        try:
            db.session.add(user)
            db.session.commit()
        except Exception:
            db.session.rollback()
        return render_template('adduser_confirmation.html', title='Add User Confirmations', username=form.fname.data)    
    return render_template('adduser.html', title = 'User Input Form', form=form)

@app.route('/showusers/')
def showusers():
    users = User.query.all()
    users = [user.fname for user in users]
    return render_template('showusers.html', users=users)
