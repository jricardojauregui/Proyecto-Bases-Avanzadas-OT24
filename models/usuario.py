from database import mysql
from flask import request
import MySQLdb.cursors
import hashlib

class Usuario:
    @staticmethod
    def insertUsuario(clave, nom_usr, apellido_usr, correo_usr, tel_usr, tel_domicilio, direccion, foto_usuario): 
        cur = mysql.connection.cursor()
        cur.callproc('InsertUsuario', (clave, nom_usr, apellido_usr, correo_usr, tel_usr, tel_domicilio, direccion, foto_usuario)) 
        mysql.connection.commit()
        cur.close

    @staticmethod
    def updateUsuario(id_usr, clave, nom_usr, apellido_usr, correo_usr, tel_usr, tel_domicilio, direccion, foto_usuario): 
        cur = mysql.connection.cursor()
        cur.callproc('UpdateUsuario', (id_usr, clave, nom_usr, apellido_usr, correo_usr, tel_usr, tel_domicilio, direccion, foto_usuario)) 
        mysql.connection.commit()
        cur.close

    @staticmethod
    def deleteUsuario(id_usr): 
        cur = mysql.connection.cursor()
        cur.callproc('DeleteUsuario', (id_usr,)) 
        mysql.connection.commit()
        cur.close

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
    
def login_user(nom_usr, clave):
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    hashed_clave = hashlib.sha256(clave.encode()).hexdigest()

    cur.callproc('MostrarUsuarioPorID', (nom_usr,)) 
    user = cur.fetchone()

    if user:
        stored_clave = user['clave']  
        print(f"Contraseña ingresada (hash): {hashed_clave}")
        print(f"Contraseña almacenada: {stored_clave}")

        if stored_clave == hashed_clave:
            return user

    return None


def register_user(nom_usr, clave):
    cur = mysql.connection.cursor()
    hashed_clave = hashlib.sha256(clave.encode()).hexdigest()

    try:
        cur.callproc('registrarUsuario', [nom_usr, hashed_clave])
        mysql.connection.commit()
        return True, 'Registro exitoso.'
    except MySQLdb.exceptions.OperationalError as e: 
        return False, str(e)