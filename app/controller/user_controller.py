from app import database
from flask import session, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SelectField, TextAreaField
from wtforms.validators import Required
from werkzeug.security import check_password_hash, generate_password_hash


def obtenerProductos():
    db = database.get_db()
    cursor = db.cursor()
    sql = "SELECT id_producto, nombre_producto, codigo_producto, info_producto, precio_producto, estado_producto from productos"
    cursor.execute(sql)
    return cursor.fetchall()

def obtenerUsersData():
    db = database.get_db()
    cursor = db.cursor()
    users_data = cursor.execute("SELECT * from usuarios").fetchall()
    return users_data

def actualizarUsuario(username, data_user, do):
    db = database.get_db()
    cursor = db.cursor()
    if do:
        cursor.execute("""
        UPDATE usuarios set 
            tipo_usuario = :type, username = :username, password_user_hash = :password,
            estado_usuario = :state, email_usuario = :email WHERE username = :pusername
            """, {"type": data_user['user-type'], 
            "username": data_user['user-name'], 
            "password": generate_password_hash(data_user['user-password']),
            "state": data_user['user-state'],
            "email": data_user['user-email'],
            "pusername": username
            })
    else:
        cursor.execute("""
        UPDATE usuarios set 
            tipo_usuario = :type, username = :username,
            estado_usuario = :state, email_usuario = :email WHERE username = :pusername
            """, {"type": data_user['user-type'], 
            "username": data_user['user-name'],
            "state": data_user['user-state'],
            "email": data_user['user-email'],
            "pusername": username
            })
    db.commit()
        
def borrarUsuario(username):
    db = database.get_db()
    cursor = db.cursor()
    cursor.execute ("""
        DELETE FROM usuarios WHERE username = :username
    """, {"username": username})
    db.commit()



def obtenerDataUsuario():
    db = database.get_db()
    cursor = db.cursor()
    datauser = cursor.execute("SELECT * from usuarios WHERE username = :user", {"user": session['username']}).fetchone()
    return datauser

def LoginUsuario(user, password):
    db = database.get_db()
    cursor = db.cursor()
    dbuser = cursor.execute("SELECT * from usuarios WHERE username = :user", {"user": user}).fetchone()
    if dbuser != None:
        if check_password_hash(dbuser[3], password):
            session["logged_in"] = True
            session["id"] = dbuser[0]
            session["username"] = dbuser[2]
            session["type"] = dbuser[1]
            return True
    return False

def updateNormalUser(data_user, do):
    db = database.get_db()
    cursor = db.cursor()
    if do:
        cursor.execute("""
        UPDATE usuarios SET email_usuario = :email, password_user_hash = :password
        WHERE username = :username
            """, {"email": data_user['email'],
          "password": generate_password_hash(data_user['password']),
          "username": session['username']})
    else:
        cursor.execute("""
        UPDATE usuarios SET email_usuario = :email
        WHERE username = :username
            """, {"email": data_user['email'],
          "username": session['username']})
    
    db.commit()

def agregarUsuario(user_data):
    db = database.get_db()
    cursor = db.cursor()
    cursor.execute(""" 
        INSERT INTO usuarios (
            tipo_usuario,
            username,
            password_user_hash,
            fecha_creacion_usuario,
            estado_usuario,
            email_usuario
            ) VALUES (
                :type,
                :username,
                :password,
                datetime('now'),
                :state,
                :email
            )
     """, {
         "type": user_data['user-type'],
         "username": user_data['user-name'],
         "password": generate_password_hash(user_data['user-password']),
         "state": user_data['user-state'],
         "email": user_data['user-email']
     }
    )
    db.commit()
def registerUser(user_data):
    db = database.get_db()
    cursor = db.cursor()
    cursor.execute(""" 
        INSERT INTO usuarios (
            tipo_usuario,
            username,
            password_user_hash,
            fecha_creacion_usuario,
            estado_usuario,
            email_usuario
            ) VALUES (
                0,
                :username,
                :password,
                datetime('now'),
                'active',
                :email
            )
     """, {
         "username": user_data['username'],
         "password": generate_password_hash(user_data['password']),
         "email": user_data['email']
     }
    )
    db.commit()

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[Required()])
    password = PasswordField('Password', validators=[Required()])
    submit = SubmitField('Sign In')

class ProductAddForm(FlaskForm):
   
    nombre = StringField('NOMBRE', validators=[Required()])
    codigo = StringField('CODIGO', validators=[Required()])
    info = TextAreaField('INFORMACION', validators=[Required()])
    precio = IntegerField('PRECIO', validators=[Required()])
    estado = SelectField('ESTADO', choices=[('active', 'activo'),('deactive', 'desactivado')])
    submit_add_product = SubmitField('Agregar')
class ProductForm(FlaskForm):
    ID = StringField('ID', validators=[Required()])
    nombre = StringField('NOMBRE', validators=[Required()])
    codigo = StringField('CODIGO', validators=[Required()])
    info = TextAreaField('INFORMACION', validators=[Required()])
    precio = IntegerField('PRECIO', validators=[Required()])
    estado = SelectField('ESTADO', choices=[('active', 'activo'),('deactive', 'desactivado')])
    submit_update_product = SubmitField('Actualizar')
    submit_del_product = SubmitField('Eliminar')
    
