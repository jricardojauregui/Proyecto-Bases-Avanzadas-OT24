from flask import Flask, render_template, request, redirect, url_for, flash, session
from config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB, SECRET_KEY
from database import mysql, init_app

from controllers.adminController import admin_login, admin_logout, admin_view_dashboard, admin_edit_products, admin_edit_users
from controllers.usuarioController import user_login, user_register, user_update, user_logout, user_delete_account, user_profile, user_view_and_manage_cart, user_order_history, user_view_wishlist, user_view_product, user_view_all_products, user_view_products_by_category
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

### RUTAS USUARIO
app.add_url_rule('/login', view_func=user_login, methods=['GET', 'POST'])
app.add_url_rule('/register', view_func=user_register, methods=['GET', 'POST'])
app.add_url_rule('/update', view_func=user_update, methods=['GET', 'POST'])
app.add_url_rule('/logout', view_func=user_logout)
app.add_url_rule('/deleteAccount', view_func=user_delete_account, methods=['GET', 'POST'])
app.add_url_rule('/profile', view_func=user_profile, methods=['GET'])
app.add_url_rule('/cart', view_func=user_view_and_manage_cart, methods=['GET', 'POST'])
app.add_url_rule('/orderHistory', view_func=user_order_history, methods=['GET', 'POST'])
app.add_url_rule('/wishlist', view_func=user_view_wishlist, methods=['GET', 'POST'])
app.add_url_rule('/product/<int:id_producto>', view_func=user_view_product, methods=['GET', 'POST'])
app.add_url_rule('/products', view_func=user_view_all_products, methods=['GET'])
app.add_url_rule('/products/category/<int:id_categoria>', view_func=user_view_products_by_category, methods=['GET'])
