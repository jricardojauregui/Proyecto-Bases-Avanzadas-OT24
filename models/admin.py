
from database import mysql
import MySQLdb.cursors

def is_admin(id_usr):
    cur = mysql.connection.cursor()
    try:
        cur.callproc('VerificarRolAdmin', [id_usr])
        return cur.fetchone() is not None 
    except MySQLdb.Error as e:
        print(f"Error al verificar rol de administrador: {e}")
        return False
    finally:
        cur.close()


def get_promedio_calificacion_productos():
    cur = mysql.connection.cursor()
    try:
        cur.callproc('promedioCalifProductos')
        return cur.fetchall()
    except MySQLdb.Error as e:
        print(f"Error al obtener el promedio de calificaciones: {e}")
        return []
    finally:
        cur.close()

def get_cantidad_categorias_productos():
    cur = mysql.connection.cursor()
    try:
        cur.callproc('cantProductosCategorias')
        return cur.fetchall()
    except MySQLdb.Error as e:
        print(f"Error al obtener la cantidad de categorías: {e}")
        return []
    finally:
        cur.close()

def get_cantidad_stock_productos():
    cur = mysql.connection.cursor()
    try:
        cur.callproc('cantProductosStock')
        return cur.fetchall()
    except MySQLdb.Error as e:
        print(f"Error al obtener el stock de productos: {e}")
        return []
    finally:
        cur.close()

def get_pedidos_por_mes():
    cur = mysql.connection.cursor()
    try:
        cur.callproc('pedidosPorMes')
        return cur.fetchall()
    except MySQLdb.Error as e:
        print(f"Error al obtener pedidos por mes: {e}")
        return []
    finally:
        cur.close()

def get_usuarios_por_mes():
    cur = mysql.connection.cursor()
    try:
        cur.callproc('UsuariosPorMes')
        return cur.fetchall()
    except MySQLdb.Error as e:
        print(f"Error al obtener usuarios por mes: {e}")
        return []
    finally:
        cur.close()

def get_productos_estado(estado):
    cur = mysql.connection.cursor()
    try:
        procedure_map = {
            'completados': 'verCompletados',
            'en_proceso': 'verEnProceso',
            'cancelados': 'verCancelados'
        }
        if estado in procedure_map:
            cur.callproc(procedure_map[estado])
            return cur.fetchone()
        else:
            raise ValueError("Estado no válido")
    except (MySQLdb.Error, ValueError) as e:
        print(f"Error al obtener productos por estado: {e}")
        return [0]
    finally:
        cur.close()

def get_ganancias_por_mes():
    cur = mysql.connection.cursor()
    try:
        cur.callproc('gananciasPorMes')
        return cur.fetchall()
    except MySQLdb.Error as e:
        print(f"Error al obtener ganancias por mes: {e}")
        return []
    finally:
        cur.close()


def get_all_users():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    try:
        cur.callproc('MostrarTodosUsuarios')
        users = cur.fetchall()
        return users
    except MySQLdb.Error as e:
        print(f"Error al obtener usuarios: {e}")
        return None
    finally:
        cur.close()

def update_user_field(id_usr, field, value):
    cur = mysql.connection.cursor()
    try:
        cur.callproc('ActualizarCampoUsuario', [id_usr, field, value])
        mysql.connection.commit()
        return True, "Campo actualizado correctamente."
    except MySQLdb.Error as e:
        print(f"Error al actualizar el campo del usuario: {e}")
        return False, str(e)
    finally:
        cur.close()

def delete_user_by_id(id_usr):
    cur = mysql.connection.cursor()
    try:
        cur.callproc('BorrarUsuario', [id_usr])
        mysql.connection.commit()
        return True, "Usuario eliminado correctamente."
    except MySQLdb.Error as e:
        print(f"Error al borrar usuario: {e}")
        return False, str(e)
    finally:
        cur.close()

def delete_product_by_id(id_producto):
    cur = mysql.connection.cursor()
    try:
        cur.callproc('BorrarProducto', [id_producto])
        mysql.connection.commit()
        return True, "Producto eliminado correctamente."
    except MySQLdb.Error as e:
        print(f"Error al borrar el producto: {e}")
        return False, str(e)
    finally:
        cur.close()