from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from models.admin import get_promedio_calificacion_productos, get_cantidad_categorias_productos, get_cantidad_stock_productos, get_pedidos_por_mes, get_usuarios_por_mes, get_productos_estado, get_ganancias_por_mes, is_admin
from models.usuario import login_user
from functools import wraps
import hashlib

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('loggedin') or not session.get('is_admin'):
            flash('Debes iniciar sesión como administrador para acceder a esta página.', 'error')
            return redirect(url_for('admin_login'))  
        return f(*args, **kwargs)
    return decorated_function

def admin_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('clave')

        if not username or not password:
            flash('Por favor, ingresa usuario y contraseña.', 'error')
            return redirect(url_for('admin_login'))

        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        user = login_user(username, hashed_password)
        if user and is_admin(user['id_usr']):
            session['loggedin'] = True
            session['id_usr'] = user['id_usr']
            session['username'] = user['username']
            session['is_admin'] = True
            flash('Acceso como administrador exitoso', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Credenciales incorrectas o no tienes acceso como administrador.', 'error')

    return render_template('admin_login.html')

def admin_logout():
    session.clear()
    flash('Sesión cerrada correctamente.', 'success')
    return redirect(url_for('admin_login'))

@admin_required
def admin_view_dash():
    return render_template('dashboard.html')

@admin_required
def promedio_calificacion_productos():
    resultado = get_promedio_calificacion_productos()
    return jsonify([{"name": row[0], "y": float(row[1])} for row in resultado if row[1] is not None])

@admin_required
def cantidad_categorias_productos():
    resultado = get_cantidad_categorias_productos()
    return jsonify([{"name": row[0], "y": float(row[1])} for row in resultado if row[1] is not None])

@admin_required
def cantidad_stock_productos():
    resultado = get_cantidad_stock_productos()
    return jsonify([{"name": row[0], "y": float(row[1])} for row in resultado if row[1] is not None])

@admin_required
def pedidos_por_mes():
    resultado = get_pedidos_por_mes()
    return jsonify([{"name": row[0], "y": float(row[1])} for row in resultado if row[1] is not None])

@admin_required
def usuarios_por_mes():
    resultado = get_usuarios_por_mes()
    return jsonify([{"name": row[0], "y": float(row[1])} for row in resultado if row[1] is not None])

@admin_required
def productos_estado(estado):
    resultado = get_productos_estado(estado)
    return jsonify([{"total": resultado[0]}])

@admin_required
def ganancias_por_mes():
    resultado = get_ganancias_por_mes()
    return jsonify([{"name": row[0], "y": float(row[1])} for row in resultado if row[1] is not None])
