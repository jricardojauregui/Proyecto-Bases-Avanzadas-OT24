from database import mysql
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