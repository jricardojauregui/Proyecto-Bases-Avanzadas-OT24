from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB, SECRET_KEY
from database import mysql, init_app

from controllers.adminController import login_all, admin_logout, admin_manage_products, admin_manage_users, admin_manage_orders, admin_manage_discounts, admin_view_dash, promedio_calificacion_productos, cantidad_categorias_productos, cantidad_stock_productos, pedidos_por_mes, usuarios_por_mes, productos_entregados, productos_cancelados, productos_en_proceso, ganancias_por_mes, admin_insert_user, admin_insert_product, admin_insert_discount
from controllers.usuarioController import user_register, user_update, user_logout, user_delete_account, user_profile, user_view_and_manage_cart, user_order_history, user_view_wishlist, user_view_product, user_view_all_products, user_view_products_by_category, user_view_credit_cards, user_manage_credit_cards, user_view_products_with_discount, user_view_most_requested_products, user_view_newest_products, user_view_recommendations
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
app.add_url_rule('/adminLogout', view_func=admin_logout)
app.add_url_rule('/manageProducts', view_func=admin_manage_products, methods=['GET', 'POST'])
app.add_url_rule('/manageUsers', view_func=admin_manage_users, methods=['GET', 'POST'])
app.add_url_rule('/manageOrders', view_func=admin_manage_orders, methods=['GET', 'POST'])
app.add_url_rule('/manageDiscounts', view_func=admin_manage_discounts, methods=['GET', 'POST'])
app.add_url_rule('/insertUser', view_func=admin_insert_user, methods=['GET', 'POST'])
app.add_url_rule('/insertProduct', view_func=admin_insert_product, methods=['GET', 'POST'])
app.add_url_rule('/insertProduct', view_func=admin_insert_discount, methods=['GET', 'POST'])

### RUTAS DASHBOARD
app.add_url_rule('/dashboard', view_func=admin_view_dash, methods=['GET'])

app.add_url_rule('/data/Promedio_calificacion_Productos', view_func=promedio_calificacion_productos, methods=['GET'])
app.add_url_rule('/data/Cantidad_categorias_Productos', view_func=cantidad_categorias_productos, methods=['GET'])
app.add_url_rule('/data/Cantidad_stock_Productos', view_func=cantidad_stock_productos, methods=['GET'])
app.add_url_rule('/data/pedidos_por_mes', view_func=pedidos_por_mes, methods=['GET'])
app.add_url_rule('/data/usuarios_por_mes', view_func=usuarios_por_mes, methods=['GET'])
app.add_url_rule('/data/productos_entregados', view_func=productos_entregados, methods=['GET'])
app.add_url_rule('/data/productos_EnProceso', view_func=productos_en_proceso, methods=['GET'])
app.add_url_rule('/data/productos_cancelados', view_func=productos_cancelados, methods=['GET'])
app.add_url_rule('/data/ganancias_por_mes', view_func=ganancias_por_mes, methods=['GET'])

### RUTAS USUARIO
app.add_url_rule('/login', view_func=login_all, methods=['GET', 'POST'])
app.add_url_rule('/register', view_func=user_register, methods=['GET', 'POST'])
app.add_url_rule('/update', view_func=user_update, methods=['GET', 'POST'])
app.add_url_rule('/creditCards', view_func=user_view_credit_cards, methods=['GET'])
app.add_url_rule('/editCreditCards', view_func=user_manage_credit_cards, methods=['GET', 'POST'])
app.add_url_rule('/logout', view_func=user_logout)
app.add_url_rule('/deleteAccount', view_func=user_delete_account, methods=['GET', 'POST'])
app.add_url_rule('/profile', view_func=user_profile, methods=['GET'])
app.add_url_rule('/cart', view_func=user_view_and_manage_cart, methods=['GET', 'POST'])
app.add_url_rule('/orderHistory', view_func=user_order_history, methods=['GET', 'POST'])
app.add_url_rule('/wishlist', view_func=user_view_wishlist, methods=['GET'])
app.add_url_rule('/product/<int:id_producto>', view_func=user_view_product, methods=['GET', 'POST'])
app.add_url_rule('/products', view_func=user_view_all_products, methods=['GET'])
app.add_url_rule('/products/category/<int:id_categoria>', view_func=user_view_products_by_category, methods=['GET'])
app.add_url_rule('/products/discount', view_func=user_view_products_with_discount, methods=['GET'])
app.add_url_rule('/products/popular', view_func=user_view_most_requested_products, methods=['GET'])
app.add_url_rule('/products/new', view_func=user_view_newest_products, methods=['GET'])
app.add_url_rule('/products/recommendations', view_func=user_view_recommendations, methods=['GET'])

