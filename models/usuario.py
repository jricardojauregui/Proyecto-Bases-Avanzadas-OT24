from database import mysql
from flask import request
import MySQLdb.cursors
import hashlib

class Usuario:  
    def login_user(username, hashed_password):
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        try:
            cur.execute('SELECT * FROM usuarios WHERE username = %s AND clave = %s', (username, hashed_password))
            user = cur.fetchone()  
            if user:
                stored_password = user['clave']
                print(f"Contraseña ingresada (hash): {hashed_password}")
                print(f"Contraseña almacenada: {stored_password}")
                if stored_password == hashed_password:
                    return user
        except MySQLdb.Error as e:
            return False, str(e)
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
            if result:
                return result[0] 
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
            cur.callproc('MostrarWishList', [id_usr])
            wishlist = cur.fetchall()
            return wishlist
        except MySQLdb.Error as e:
            return False, str(e)
        finally:
            cur.close()

    def validate_user_credentials(username, password):
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        try:
            hashed_password = hashlib.sha256(password.encode()).hexdigest() 
            cur.callproc('autenticarUser', [username, hashed_password])
            user = cur.fetchone()
            if not user:
                return None 
            id_usr = user['id_usr']
            cur.callproc('VerificarUsuario', [id_usr])
            return id_usr 
        except MySQLdb.Error as e:
                return False, str(e)
        finally:
            cur.close()

    def delete_user_account(id_usr):
        cur = mysql.connection.cursor()
        try:
            cur.callproc('DeleteUsuario', [id_usr])  
            mysql.connection.commit()
            return True, "Cuenta eliminada exitosamente."
        except MySQLdb.Error as e:
            return False, str(e)
        finally:
            cur.close()