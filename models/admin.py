
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

