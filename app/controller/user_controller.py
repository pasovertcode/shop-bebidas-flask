from app import database

def obtenerProductos():
    db = database.get_db()
    cursor = db.cursor()
    sql = "SELECT id_producto, nombre_producto, codigo_producto, info_producto, precio_producto, estado_producto from productos"
    cursor.execute(sql)
    return cursor.fetchall()