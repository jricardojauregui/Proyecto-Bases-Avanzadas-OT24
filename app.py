from flask import Flask, render_template, request, redirect, url_for, flash, session
from config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB, SECRET_KEY
from database import mysql, init_app

from controllers.adminController import loginAdmin, logoutAdmin, mostrarEmpresas, editarEmpresas, eliminarEmpresas
from controllers.usuarioController import loginU, registerU, updateU, logoutU, delete_account, view_and_manage_cart, order_history, view_wishlist, producto, productos, productos_por_categoria

app = Flask(__name__)

app.config['MYSQL_HOST'] = MYSQL_HOST
app.config['MYSQL_USER'] = MYSQL_USER
app.config['MYSQL_PASSWORD'] = MYSQL_PASSWORD
app.config['MYSQL_DB'] = MYSQL_DB
app.secret_key = SECRET_KEY

init_app(app)

### RUTA LANDING
@app.route('/')
def inicio():
    return redirect(url_for('inicio'))

### RUTAS ADMIN
app.add_url_rule('/loginAdmin', view_func=loginAdmin, methods=['GET', 'POST'])
app.add_url_rule('/logoutAdmin', view_func=logoutAdmin)
app.add_url_rule('/empresas', view_func=mostrarEmpresas)
app.add_url_rule('/editarEmpresas/<int:id>', view_func=editarEmpresas, methods=['GET', 'POST'])
app.add_url_rule('/eliminarEmpresas/<int:id>', view_func=eliminarEmpresas, methods=['GET', 'POST'])

### RUTAS USUARIO
app.add_url_rule('/login', view_func=loginU, methods=['GET', 'POST'])
app.add_url_rule('/register', view_func=registerU, methods=['GET', 'POST'])
app.add_url_rule('/update', view_func=updateU, methods=['GET', 'POST'])
app.add_url_rule('/logout', view_func=logoutU)
app.add_url_rule('/deleteAccount', view_func=delete_account, methods=['GET', 'POST'])
app.add_url_rule('/cart', view_func=view_and_manage_cart, methods=['GET', 'POST'])
app.add_url_rule('/orderHistory', view_func=order_history, methods=['GET', 'POST'])
app.add_url_rule('/wishlist', view_func=view_wishlist, methods=['GET', 'POST'])
app.add_url_rule('/product/<int:id_producto>', view_func=producto, methods=['GET', 'POST'])
app.add_url_rule('/productos', view_func=productos, methods=['GET'])
app.add_url_rule('/productos/categoria/<int:id_categoria>', view_func=productos_por_categoria, methods=['GET'])
