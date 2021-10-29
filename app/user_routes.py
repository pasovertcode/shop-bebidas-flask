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
        

        if session['type'] == 0:
            if request.method == 'POST':
                if request.form['submit'] == 'normal-user-update':
                    data_user = {
                        "email": request.form['email'],
                        "password": request.form['password']
                    }
                    if str(data_user['password']).strip() == '':
                        user_controller.updateNormalUser(data_user, False)
                    else:
                        user_controller.updateNormalUser(data_user, True)
                    
                return redirect(url_for('user_profile'))
        elif session['type'] == 1:
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
                elif request.form['submit'] == 'user-update':
                    user_data = {
                        "user-type": request.form['user-type'],
                        "user-name": request.form['user-name'],
                        "user-password": request.form['user-password'],
                        "user-state": request.form['user-state'],
                        "user-email": request.form['user-email']
                    }
                    username = request.form['p-username']
                    if str(user_data['user-password']).strip() == '':
                        user_controller.actualizarUsuario(username, user_data, False)
                    else:
                        user_controller.actualizarUsuario(username, user_data, True)

                elif request.form['submit'] == 'user-delete':
                    username = request.form['p-username']
                    user_controller.borrarUsuario(username)
                elif request.form['submit'] == 'add-user':
                    user_data = {
                        "user-type": request.form['user-add-type'],
                        "user-name": request.form['user-add-name'],
                        "user-password": request.form['user-add-password'],
                        "user-state": request.form['user-add-state'],
                        "user-email": request.form['user-add-email']
                    }
                    user_controller.agregarUsuario(user_data)
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