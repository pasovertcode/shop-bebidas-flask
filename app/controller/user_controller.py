from app import database
from flask import session, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Required
from werkzeug.security import check_password_hash, generate_password_hash


def obtenerProductos():
    db = database.get_db()
    cursor = db.cursor()
    sql = "SELECT id_producto, nombre_producto, codigo_producto, info_producto, precio_producto, estado_producto from productos"
    cursor.execute(sql)
    return cursor.fetchall()


def LoginUsuario(user, password):
    db = database.get_db()
    cursor = db.cursor()
    dbuser = cursor.execute("SELECT * from usuarios WHERE username = :user", {"user": user}).fetchone()
    if dbuser != None:
        if password == dbuser[3]:
            session["logged_in"] = True
            session["id"] = dbuser[0]
            session["username"] = dbuser[2]
            session["type"] = dbuser[1]
            return True
    return False


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[Required()])
    password = PasswordField('Password', validators=[Required()])
    submit = SubmitField('Sign In')
