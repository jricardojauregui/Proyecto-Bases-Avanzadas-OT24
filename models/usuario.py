from database import mysql
import MySQLdb.cursors
import hashlib

class Usuario:
    @staticmethod
    def insertUsuario(): ### FALTA TABLA
        cur = mysql.connection.cursor()
        cur.execute() ### FALTA PROCEDURE INSERT
        mysql.connection.commit()
        cur.close

    @staticmethod
    def updateUsuario(): ### FALTA TABLA
        cur = mysql.connection.cursor()
        cur.execute() ### FALTA PROCEDURE UPDATE
        mysql.connection.commit()
        cur.close

    @staticmethod
    def deleteUsuario(): ### FALTA TABLA
        cur = mysql.connection.cursor()
        cur.execute() ### FALTA PROCEDURE DELETE
        mysql.connection.commit()
        cur.close

    @staticmethod
    def get_all():
        cur = mysql.connection.cursor()
        cur.callproc('') ### FALTA PROCEDURE MOSTRAR
        usuarios = cur.fetchall()
        cur.close()
        return usuarios
    
    @staticmethod
    def get_by_id(usuarios):
        cur = mysql.connection.cursor()
        cur.execute("", ()) ### FALTA PROCEDURE MOSTRAR , checar si mejor cambiarlo a callproc
        usuarios = cur.fetchone()
        cur.close()
        return usuarios