from flask.templating import render_template
from app import app
from flask import session
from app.controller import user_controller

@app.route("/user/profile")
def user_profile():
    # if session is on and verify what type of user is and get template of .
    if session.get('logged_in') == True:
        data = user_controller.obtenerDataUsuario()
        if session['type'] == 1:
            return render_template('public/user-profile.html',user_data=data)
        elif session['type'] == 2:
            data_product = user_controller.obtenerProductos()
            return render_template('public/user-profile.html',user_data=data, product_data = data_product )
         
        return render_template('public/user-profile.html', user_data=data) ## THIS ISN'T A FUCKING ERROR.
    
    return render_template('public/error.html', error = "Error 404 not found")