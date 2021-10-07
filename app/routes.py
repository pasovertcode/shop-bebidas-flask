from app import app

from flask import render_template

# indice
@app.route('/')
def index():
    return render_template('public/index.html')

# about us
@app.route("/about")
def about():
    return "about"

# menu
@app.route("/menu")
def menu():
    return "menu"

# wish-List
@app.route("/wishlist")
def wishlist():
    return "Wish List"

# store
@app.route("/store")
def store():
    return "Store"

# sign in
@app.route("/login")
def sign_in():
    return "Sign In"