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


def agregarProducto(params):
    db = database.get_db()
    cursor = db.cursor()
    cursor.execute("""INSERT INTO productos (
                          nombre_producto,
                          codigo_producto,
                          info_producto,
                          precio_producto,
                          estado_producto)
                      VALUES (
                          :name,
                          :code,
                          :info,
                          :price,
                          :state
                      );""", {"name": params[0], "code": params[1], "info": params[2], "price": params[3], "state": params[4]})
    db.commit()

def eliminarProducto(id):
    db = database.get_db()
    cursor = db.cursor()
    cursor.execute("""
        DELETE FROM productos WHERE id_producto = :id
    """, {"id": id})
    db.commit()

def actualizarProducto(id, params):
    db = database.get_db()
    cursor = db.cursor()
    cursor.execute("UPDATE productos SET nombre_producto = :name, info_producto = :info, precio_producto = :precio, estado_producto = :estado where id_producto = :id", {"name": params[0], "info": params[1], "precio": params[2],"id": id, "estado": params[3]})
    db.commit()

def obtenerProductos():
    db = database.get_db()
    cursor = db.cursor()
    sql = "SELECT id_producto, nombre_producto, codigo_producto, info_producto, precio_producto, estado_producto from productos"
    cursor.execute(sql)
    return cursor.fetchall()


class producto():
    pass