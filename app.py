from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB, SECRET_KEY
from database import mysql, init_app

from controllers.adminController import admin_login, admin_logout, admin_view_dashboard, admin_edit_products, admin_edit_users
from controllers.usuarioController import user_login, user_register, user_update, user_logout, user_delete_account, user_profile, user_view_and_manage_cart, user_order_history, user_view_wishlist, user_view_product, user_view_all_products, user_view_products_by_category, user_view_credit_cards, user_manage_credit_cards
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
    return render_template('inicio.html') ### checar html

### RUTAS ADMIN
app.add_url_rule('/adminLogin', view_func=admin_login, methods=['GET', 'POST'])
app.add_url_rule('/adminLogout', view_func=admin_logout)
app.add_url_rule('/dashboard', view_func=admin_view_dashboard)
app.add_url_rule('/editProducts/<int:id_producto>', view_func=admin_edit_products, methods=['GET', 'POST'])
app.add_url_rule('/editUsers/<int:id_usr>', view_func=admin_edit_users, methods=['GET', 'POST'])

### RUTAS DASHBOARD
@app.route('/dashboard')
def inicio():
    return render_template('dashboard.html')

@app.route('/data/Promedio_calificacion_Productos', methods=['GET'])
def Promedio_calificacion_Productos():
    cur = mysql.connection.cursor()
    cur.callproc('promedioCalifProductos')
    resultado = cur.fetchall()
    cur.close()
    return jsonify([{"name": row[0], "y": float(row[1])} for row in resultado if row[1] is not None])

@app.route('/data/Cantidad_categorias_Productos', methods=['GET'])
def Cantidad_categorias_Productos():
    cur = mysql.connection.cursor()
    cur.callproc('cantProductosCategorias')
    resultado = cur.fetchall()
    cur.close()
    return jsonify([{"name": row[0], "y": float(row[1])} for row in resultado if row[1] is not None])

@app.route('/data/Cantidad_stock_Productos', methods=['GET'])
def Cantidad_stock_Productos():
    cur = mysql.connection.cursor()
    cur.callproc('cantProductosStock')
    resultado = cur.fetchall()
    cur.close()
    return jsonify([{"name": row[0], "y": float(row[1])} for row in resultado if row[1] is not None])

@app.route('/data/pedidos_por_mes', methods=['GET'])
def pedidos_por_mes():
    cur = mysql.connection.cursor()
    cur.callproc('pedidosPorMes')
    resultado = cur.fetchall()
    cur.close()
    return jsonify([{"name": row[0], "y": float(row[1])} for row in resultado if row[1] is not None])

@app.route('/data/usuarios_por_mes', methods=['GET'])
def usuarios_por_mes():
    cur = mysql.connection.cursor()
    cur.callproc('UsuariosPorMes')
    resultado = cur.fetchall()
    cur.close()
    return jsonify([{"name": row[0], "y": float(row[1])} for row in resultado if row[1] is not None])

@app.route('/data/productos_entregados', methods=['GET'])
def productos_entregados():
    cur = mysql.connection.cursor()
    cur.callproc('verCompletados')
    resultado = cur.fetchone()
    cur.close()
    return jsonify([{"total": resultado[0]}])

@app.route('/data/productos_EnProceso', methods=['GET'])
def productos_EnProceso():
    cur = mysql.connection.cursor()
    cur.callproc('verEnProceso')
    resultado = cur.fetchone()
    cur.close()
    return jsonify([{"total": resultado[0]}])

@app.route('/data/productos_cancelados', methods=['GET'])
def productos_Cancelados():
    cur = mysql.connection.cursor()
    cur.callproc('verCancelados')
    resultado = cur.fetchone()
    cur.close()
    return jsonify([{"total": resultado[0]}])

@app.route('/data/ganancias_por_mes', methods=['GET'])
def ganancias_por_mes():
    cur = mysql.connection.cursor()
    cur.callproc('gananciasPorMes')
    resultado = cur.fetchall()
    cur.close()
    return jsonify([{"name": row[0], "y": float(row[1])} for row in resultado if row[1] is not None])


### RUTAS USUARIO
app.add_url_rule('/login', view_func=user_login, methods=['GET', 'POST'])
app.add_url_rule('/register', view_func=user_register, methods=['GET', 'POST'])
app.add_url_rule('/update', view_func=user_update, methods=['GET', 'POST'])
app.add_url_rule('/creditCards', view_func=user_view_credit_cards, methods=['GET'])
app.add_url_rule('/editCreditCards', view_func=user_manage_credit_cards, methods=['GET', 'POST'])
app.add_url_rule('/logout', view_func=user_logout)
app.add_url_rule('/deleteAccount', view_func=user_delete_account, methods=['GET', 'POST'])
app.add_url_rule('/profile', view_func=user_profile, methods=['GET'])
app.add_url_rule('/cart', view_func=user_view_and_manage_cart, methods=['GET', 'POST'])
app.add_url_rule('/orderHistory', view_func=user_order_history, methods=['GET', 'POST'])
app.add_url_rule('/wishlist', view_func=user_view_wishlist, methods=['GET', 'POST'])
app.add_url_rule('/product/<int:id_producto>', view_func=user_view_product, methods=['GET', 'POST'])
app.add_url_rule('/products', view_func=user_view_all_products, methods=['GET'])
app.add_url_rule('/products/category/<int:id_categoria>', view_func=user_view_products_by_category, methods=['GET'])
