from app import database



def buscarProductos(value):
    db = database.get_db()
    cursor = db.cursor()
    SQL = "SELECT * FROM productos"
    cursor.execute(SQL)
    listaProductos = cursor.fetchall()
    listaEncontrados = []
    for producto in listaProductos:
        if producto[1].find(value) != -1 :
            listaEncontrados.append(producto)
    return listaEncontrados



def obtenerProductos():
    db = database.get_db()
    cursor = db.cursor()
    sql = "SELECT id_producto, nombre_producto, codigo_producto, info_producto, precio_producto, estado_producto from productos"
    cursor.execute(sql)
    return cursor.fetchall()


class producto():
    pass