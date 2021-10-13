from werkzeug.utils import redirect
from app import app

from flask import render_template, request, url_for, session
from app.controller import user_controller
# indice
@app.route('/')
def index():
    return render_template('public/index.html')

# about us
@app.route("/about")
def about():
    return render_template('public/about.html')

# menu
@app.route("/menu")
def menu():
    return render_template('public/menu.html')

# wish-List
@app.route("/wishlist")
def wishlist():
    return render_template('public/wishlist.html')

# store
@app.route("/store")
def store():
    data = user_controller.obtenerProductos()
    # load database here and send it to html
    return render_template('public/store.html', datos = data)

# sign in
@app.route("/login", methods=['GET', 'POST'])
def sign_in():
    form = user_controller.LoginForm()
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        if user_controller.LoginUsuario(username, password):
            print(session)
            return redirect(url_for('index'))
        form.username.erros.append("Usuario o contraseña incorrectos.")
    return render_template('public/login.html', form=form)

@app.route("/logout")
def logout():
    session.pop('username')
    session.pop('id')
    session.pop('type')
    return redirect(url_for('sign_in'))