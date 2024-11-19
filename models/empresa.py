from database import mysql
import MySQLdb.cursors
import hashlib

class Empresa:
    @staticmethod
    def insertEmpresa(): ### FALTA TABLA
        cur = mysql.connection.cursor()
        cur.execute() ### FALTA PROCEDURE INSERT
        mysql.connection.commit()
        cur.close

    @staticmethod
    def updateEmpresa(): ### FALTA TABLA
        cur = mysql.connection.cursor()
        cur.execute() ### FALTA PROCEDURE UPDATE
        mysql.connection.commit()
        cur.close

    @staticmethod
    def deleteEmpresa(): ### FALTA TABLA
        cur = mysql.connection.cursor()
        cur.execute() ### FALTA PROCEDURE DELETE
        mysql.connection.commit()
        cur.close

    @staticmethod
    def get_all():
        cur = mysql.connection.cursor()
        cur.callproc('') ### FALTA PROCEDURE MOSTRAR
        empresas = cur.fetchall()
        cur.close()
        return empresas
    
    @staticmethod
    def get_by_id(empresa):
        cur = mysql.connection.cursor()
        cur.execute("", ()) ### FALTA PROCEDURE MOSTRAR , checar si mejor cambiarlo a callproc
        empresa = cur.fetchone()
        cur.close()
        return empresa