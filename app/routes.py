from app import app

from flask import render_template
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
    for data in user_controller.obtenerProductos():
        print(data)
    # load database here and send it to html
    return render_template('public/store.html')

# sign in
@app.route("/login")
def sign_in():
    return "Sign In"