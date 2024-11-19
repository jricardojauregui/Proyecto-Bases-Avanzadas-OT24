
from database import mysql
import MySQLdb.cursors
import hashlib

class Admin:
    @staticmethod
    def get_by_id(admins):
        cur = mysql.connection.cursor()
        cur.execute("", ()) ### FALTA PROCEDURE MOSTRAR , checar si mejor cambiarlo a callproc
        admins = cur.fetchone()
        cur.close()
        return admins