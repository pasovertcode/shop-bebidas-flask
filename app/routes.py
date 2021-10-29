from werkzeug.utils import redirect
from app import app

from flask import render_template, request, url_for, session
from app.controller import user_controller
from app.controller import product_controller
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


#sign up
@app.route("/logup", methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        pass

# sign in
@app.route("/login", methods=['GET', 'POST'])
def sign_in():
    form = user_controller.LoginForm()
    if form.validate_on_submit():
        username = request.form['username']
        password = request.form['password']
        if user_controller.LoginUsuario(username, password):
            return redirect(url_for('index'))
        form.username.errors.append("datos incorrectos.")
    elif request.method == 'POST':
        if request.form['submit'] == "add-user":
            user_data = {
                "username": request.form['user-add-name'],
                "password": request.form['user-add-password'],
                "email": request.form['user-add-email']
            }
            user_controller.registerUser(user_data)
    return render_template('public/login.html', form=form)

@app.route("/logout")
def logout():
    session.pop('username')
    session.pop('id')
    session.pop('type')
    session.pop('logged_in', None)
    return redirect(url_for('sign_in'))

@app.route("/search", methods=['GET'])
def search():
    if request.method == 'GET':
        if request.args.get('value') != None and request.args.get('value') != "" and request.args != 'value' :
            datasearch = request.args.get('value')
            encontrados = product_controller.buscarProductos(datasearch)
            return render_template('public/search.html', data=encontrados)
    return render_template('public/error.html', error = "Error 404 not found")