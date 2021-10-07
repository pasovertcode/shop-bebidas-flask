import sqlite3
from flask import g
from app import app

DATABASE = "/database/blackrockdb.db"

def get_db():
    db = getattr(g, '_database', None)

    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def getProducts():
    sql = "SELECT id_producto, nombre_producto, codigo_producto, info_producto, precio_producto, estado_producto from productos"

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()