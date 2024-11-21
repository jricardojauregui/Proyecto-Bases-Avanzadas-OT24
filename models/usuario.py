from database import mysql
from flask import request
import MySQLdb.cursors
import hashlib

class Usuario:
    @staticmethod
    def get_all():
        cur = mysql.connection.cursor()
        cur.callproc('MostrarUsuarios') 
        usuarios = cur.fetchall()
        cur.close()
        return usuarios
    
    @staticmethod
    def get_by_id(usuarios):
        cur = mysql.connection.cursor()
        cur.callproc('MostrarUsuarioPorID', (id_usr,)) 
        usuarios = cur.fetchone()
        cur.close()
        return usuarios
    
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
