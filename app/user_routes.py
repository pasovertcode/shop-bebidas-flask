from flask.templating import render_template
from app import app
from flask import session, flash, url_for, request
from app.controller import user_controller, product_controller
from werkzeug.utils import redirect

@app.route("/user/profile", methods=['POST', 'GET'])
def user_profile():
    # if session is on, verify what type of user is and get template of .
    if session.get('logged_in') == True:
        data = user_controller.obtenerDataUsuario()
        if session['type'] == 1:
            form_product = user_controller.ProductForm()
            if request.method == 'POST':
                if request.form['submit'] == 'add-product':
                    params = [form_product.nombre.data, form_product.codigo.data, form_product.info.data, form_product.precio.data, form_product.estado.data]
                    product_controller.agregarProducto(params)
                elif request.form['submit'] == 'update-product':
                    params = [form_product.nombre.data, form_product.info.data, form_product.precio.data, form_product.estado.data]
                    product_controller.actualizarProducto(form_product.ID.data, params)
                elif request.form['submit'] == 'del-product':
                    product_controller.eliminarProducto(form_product.ID.data)
                return redirect(url_for('user_profile'))

            data_product = product_controller.obtenerProductos()
            return render_template('public/user-profile.html'
            ,user_data=data
            , product_data = data_product
            , form_product = form_product)

        elif session['type'] == 2:
            form_product = user_controller.ProductForm()
            if request.method == 'POST':
                if request.form['submit'] == 'add-product':
                    params = [form_product.nombre.data, form_product.codigo.data, form_product.info.data, form_product.precio.data, form_product.estado.data]
                    product_controller.agregarProducto(params)
                elif request.form['submit'] == 'update-product':
                    params = [form_product.nombre.data, form_product.info.data, form_product.precio.data, form_product.estado.data]
                    product_controller.actualizarProducto(form_product.ID.data, params)
                elif request.form['submit'] == 'del-product':
                    product_controller.eliminarProducto(form_product.ID.data)
                return redirect(url_for('user_profile'))
            
            data_product = product_controller.obtenerProductos()
            data_users = user_controller.obtenerUsersData()


            ## falta consulta de usuario y comentarios
            return render_template('public/user-profile.html'
            , user_data = data
            , users_data = data_users
            , product_data = data_product
            , form_product = form_product)
         
        return render_template('public/user-profile.html', user_data=data) 
    
    return render_template('public/error.html', error = "Error 404 not found")