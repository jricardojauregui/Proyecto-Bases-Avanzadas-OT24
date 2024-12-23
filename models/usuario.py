from database import mysql
import MySQLdb.cursors
from flask import Flask, session

def login_user(username, hashed_password):
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    try:
        cur.execute('SELECT * FROM usuarios WHERE username = %s AND clave = %s', (username, hashed_password))
        user = cur.fetchone() 

        if user:
            session['loggedin'] = True 
            session['id_usr'] = user['id_usr'] 
            session['username'] = user['username']  
            return user  
    except MySQLdb.Error as e:
        print(f"Error en la consulta SQL: {e}")
    finally:
        cur.close()
    return None  


def register_user(username, clave, nom_usr, apellido_usr, correo_usr, tel_usr, tel_domicilio, direccion, foto_usuario):
    cur = mysql.connection.cursor()
    try:
        cur.callproc('InsertUsuario', [username, clave, nom_usr, apellido_usr, correo_usr, tel_usr, tel_domicilio, direccion, foto_usuario])
        mysql.connection.commit()
        return True, 'Registro exitoso.'
    except MySQLdb.exceptions.OperationalError as e:
        return False, str(e)
    finally:
        cur.close()

def update_user(id_usr, username, clave, nom_usr, apellido_usr, correo_usr, tel_usr, tel_domicilio, direccion, foto_usuario):
    cur = mysql.connection.cursor()
    try:
        cur.execute('SELECT * FROM usuarios WHERE id_usr = %s', (id_usr,))
        current_user = cur.fetchone()
        if not current_user:
            return False, "Usuario no encontrado."
        username = username or current_user['username']
        clave = clave or current_user['clave']
        nom_usr = nom_usr or current_user['nom_usr']
        apellido_usr = apellido_usr or current_user['apellido_usr']
        correo_usr = correo_usr or current_user['correo_usr']
        tel_usr = tel_usr or current_user['tel_usr']
        tel_domicilio = tel_domicilio or current_user['tel_domicilio']
        direccion = direccion or current_user['direccion']
        foto_usuario = foto_usuario or current_user['foto_usuario']
        cur.callproc('UpdateUsuario', [id_usr, username, clave, nom_usr, apellido_usr, correo_usr, tel_usr, tel_domicilio, direccion, foto_usuario])
        mysql.connection.commit()
        return True, "Usuario actualizado correctamente."
    except MySQLdb.Error as e:
        return False, str(e)
    finally:
        cur.close()


def get_user_profile(id_usr):
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    try:
        cur.callproc('MostrarUsuarioPorID', [id_usr])
        result = cur.fetchone()
        return result  
    except MySQLdb.Error as e:
        print(f"Error al obtener el perfil del usuario: {e}")
        return None
    finally:
        cur.close()


def get_product_info(id_producto):
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    try:
        cur.execute("SELECT * FROM productos WHERE id_producto = %s", (id_producto,))
        return cur.fetchone()
    except MySQLdb.Error as e:
        return False, str(e)
    finally:
        cur.close()


def add_to_cart(id_usr, id_producto, cantidad):
    cur = mysql.connection.cursor()
    try:
        cur.callproc('anadirCarrito', [id_usr, id_producto, cantidad])
        mysql.connection.commit()
        return True, "Producto agregado al carrito."
    except MySQLdb.Error as e:
        return False, str(e)
    finally:
        cur.close()


def direct_purchase(id_usr, id_producto, cantidad, tarjeta_usr):
    cur = mysql.connection.cursor()
    try:
        cur.callproc('CompraDirecta', [id_usr, id_producto, cantidad, tarjeta_usr])
        mysql.connection.commit()
        return True, "Compra directa realizada exitosamente."
    except MySQLdb.Error as e:
        return False, str(e)
    finally:
        cur.close()


def toggle_wishlist(id_usr, id_producto):
    cur = mysql.connection.cursor()
    try:
        cur.callproc('ToggleProductoWishList', [id_usr, id_producto])
        mysql.connection.commit()
        return True, "Operación realizada exitosamente."
    except MySQLdb.Error as e:
        return False, str(e)
    finally:
        cur.close()


def get_wishlist_status(id_usr, id_producto):
    cur = mysql.connection.cursor()
    try:
        cur.callproc('checarWishlist', [id_usr, id_producto])
        result = cur.fetchone() 
        return result is not None
    except MySQLdb.Error as e:
        print(f"Error al verificar estado de wishlist: {e}")
        return False
    finally:
        cur.close()


def get_product_ratings(id_producto):
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    try:
        cur.callproc('VerCalificacionesPorProducto', [id_producto])
        return cur.fetchall()
    except MySQLdb.Error as e:
        print(f"Error al obtener calificaciones: {e}")
        return []
    finally:
        cur.close()


def submit_rating(id_usr, id_producto, calificacion, comentario):
    cur = mysql.connection.cursor()
    try:
        cur.callproc('CrearCalificacion', [id_usr, id_producto, calificacion, comentario])
        mysql.connection.commit()
        return True, "Calificación enviada exitosamente."
    except MySQLdb.Error as e:
        return False, str(e)
    finally:
        cur.close()


def get_last_purchase_date(id_usr, id_producto):
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    try:
        cur.callproc('UltimaCompra', [id_usr, id_producto])
        result = cur.fetchone()
        if result and 'last_purchase_date' in result:
            return result['last_purchase_date']
        else:
            return None 
    except MySQLdb.Error as e:
        print(f"Error al obtener la fecha del último pedido: {e}")
        return None
    finally:
        cur.close()


def get_all_products():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    try:
        cur.callproc('todosProductos')
        products = cur.fetchall()
        return products
    except MySQLdb.Error as e:
        print(f"Error al obtener los productos: {e}")
        return []
    finally:
        cur.close()


def get_products_by_category(id_categoria):
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    try:
        cur.callproc('productosPorCategoria', [id_categoria])
        return cur.fetchall()
    except MySQLdb.Error as e:
        print(f"Error al obtener productos por categoría: {e}")
        return []
    finally:
        cur.close()


def get_product_category(id_producto):
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    try:
        cur.callproc('productoCategoria', [id_producto])
        result = cur.fetchone()
        return result['categoria'] if result else None
    except MySQLdb.Error as e:
        print(f"Error al obtener la categoría del producto: {e}")
        return None
    finally:
        cur.close()


def get_user_cart(id_usr):
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    try:
        cur.callproc('MostrarCarritoDeUsuario', [id_usr])
        cart = cur.fetchall()
        return cart
    except MySQLdb.Error as e:
        return False, str(e)
    finally:
        cur.close()


def clear_cart(id_usr):
    cur = mysql.connection.cursor()
    try:
        cur.callproc('QuitarTodoCarrito', [id_usr])
        mysql.connection.commit()
        return True, "Carrito vaciado exitosamente."
    except MySQLdb.Error as e:
        return False, str(e)
    finally:
        cur.close()


def remove_from_cart(id_usr, id_producto):
    cur = mysql.connection.cursor()
    try:
        cur.callproc('QuitarProductoCarrito', [id_usr, id_producto])
        mysql.connection.commit()
        return True, "Producto eliminado del carrito."
    except MySQLdb.Error as e:
        return False, str(e)
    finally:
        cur.close()


def get_user_cards(id_usr):
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    try:
        cur.callproc('verTarjetasUsuario', [id_usr])
        tarjetas = cur.fetchall()
        return tarjetas
    except MySQLdb.Error as e:
        return False, str(e)
    finally:
        cur.close()


def confirm_purchase(id_usr, tarjeta_usr):
    cur = mysql.connection.cursor()
    try:
        cur.callproc('ConfirmarCompra', [id_usr, tarjeta_usr])
        mysql.connection.commit()
        return True, "Compra confirmada exitosamente."
    except MySQLdb.Error as e:
        return False, str(e)
    finally:
        cur.close()


def cancel_order(id_pedido):
    cur = mysql.connection.cursor()
    try:
        cur.callproc('CancelarPedido', [id_pedido])
        mysql.connection.commit()
        return True, "Pedido cancelado exitosamente."
    except MySQLdb.Error as e:
        return False, str(e)
    finally:
        cur.close()


def usr_order_history(id_usr):
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    try:
        cur.callproc('HistorialPedidosPorUsuario', [id_usr])
        orders = cur.fetchall()
        return orders
    except MySQLdb.Error as e:
        return False, str(e)
    finally:
        cur.close()


def get_wishlist(id_usr):
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    try:
        cur.callproc('verListaDeseos', [id_usr])
        products = cur.fetchall()
        return products
    except MySQLdb.Error as e:
        return False, str(e)
    finally:
        cur.close()

def delete_user_account(id_usr):
    cur = mysql.connection.cursor()
    try:
        cur.callproc('BorrarUsuario', [id_usr])
        mysql.connection.commit()
        return True, "Cuenta eliminada exitosamente."
    except MySQLdb.Error as e:
        print(f"Error al eliminar la cuenta: {e}")
        return False, str(e)
    finally:
        cur.close()

def add_credit_card(id_usr, tarjeta_usr, id_banco, propietario, caduci_tarjeta):
    cur = mysql.connection.cursor()
    try:
        cur.callproc('AnadirTarjeta', [id_usr, tarjeta_usr, id_banco, propietario, caduci_tarjeta])
        mysql.connection.commit()
        return True, "Tarjeta añadida exitosamente."
    except MySQLdb.Error as e:
        print(f"Error al añadir la tarjeta: {e}")
        return False, str(e)
    finally:
        cur.close()

def remove_credit_card(id_usr, tarjeta_usr):
    cur = mysql.connection.cursor()
    try:
        cur.callproc('BorrarTarjeta', [id_usr, tarjeta_usr])
        mysql.connection.commit()
        return True, "Tarjeta eliminada exitosamente."
    except MySQLdb.Error as e:
        print(f"Error al eliminar la tarjeta: {e}")
        return False, str(e)
    finally:
        cur.close()

def validate_user_credentials(username, password):
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    try:
        cur.execute("SELECT id_usr FROM usuarios WHERE username = %s AND clave = %s", (username, password))
        user = cur.fetchone()
        return user['id_usr'] if user else None
    except MySQLdb.Error as e:
        print(f"Error al validar las credenciales: {e}")
        return None
    finally:
        cur.close()

def get_products_on_promotion():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    try:
        cur.callproc('MostrarProductosEnPromocion')
        products = cur.fetchall()
        return products
    except MySQLdb.Error as e:
        print(f"Error al obtener productos en promoción: {e}")
        return []
    finally:
        cur.close()

def get_most_requested_products():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    try:
        cur.callproc('MostrarProductosMasSolicitadosParaWeb')
        products = cur.fetchall()
        return products
    except MySQLdb.Error as e:
        print(f"Error al obtener productos más solicitados: {e}")
        return []
    finally:
        cur.close()

def get_newest_products():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    try:
        cur.callproc('MostrarProductosMasNuevos')
        products = cur.fetchall()
        return products
    except MySQLdb.Error as e:
        print(f"Error al obtener productos más nuevos: {e}")
        return []
    finally:
        cur.close()

def get_recommended_products(id_usr):
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    try:
        cur.callproc('sistemaRecomendaciones', [id_usr]) 
        return cur.fetchall()
    except MySQLdb.Error as e:
        print(f"Error al obtener recomendaciones personalizadas: {e}")
        return []
    finally:
        cur.close()