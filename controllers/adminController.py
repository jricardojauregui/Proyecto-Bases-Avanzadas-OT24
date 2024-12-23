from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from models.admin import get_promedio_calificacion_productos, get_cantidad_categorias_productos, get_cantidad_stock_productos, get_pedidos_por_mes, get_usuarios_por_mes, get_productos_estado, get_ganancias_por_mes, is_admin, update_user_field, update_product_field, get_all_users, delete_user_by_id, delete_product_by_id, update_order_status, delete_order_by_id, get_all_orders, update_discount_field, delete_discount_by_id, get_all_discounts, insertar_producto, insert_user, insertar_promocion
from models.usuario import login_user, get_all_products
import hashlib

def login_all():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('clave')

        if not username or not password:
            flash('Por favor, ingresa usuario y contraseña.', 'error')
            return redirect(url_for('login_all'))

        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        user = login_user(username, hashed_password)

        if user:
            session['loggedin'] = True
            session['id_usr'] = user['id_usr']
            session['username'] = user['username']

            if is_admin(user['id_usr']):  
                session['is_admin'] = True
                flash('Acceso como administrador exitoso', 'success')
                return redirect(url_for('admin_view_dash'))  
            else:
                session['is_admin'] = False
                flash('Acceso como usuario exitoso', 'success')
                return redirect(url_for('inicio'))  

        else:
            flash('Usuario o contraseña incorrectos, intenta nuevamente.', 'error')
            return redirect(url_for('login_all'))

    return render_template('login.html') 


def admin_logout():
    session.clear()
    flash('Sesión cerrada correctamente.', 'success')
    return redirect(url_for('login_all'))


def admin_view_dash():
    if 'loggedin' in session and session.get('is_admin'):
        return render_template('dashboard.html')
    else:
        flash('Debes iniciar sesión como administrador para acceder a esta página.', 'error')
        return redirect(url_for('login_all'))


def promedio_calificacion_productos():
    if 'loggedin' in session and session.get('is_admin'):
        resultado = get_promedio_calificacion_productos()
        return jsonify([{"name": row[0], "y": float(row[1])} for row in resultado if row[1] is not None])
    else:
        flash('Debes iniciar sesión como administrador para acceder a esta página.', 'error')
        return redirect(url_for('login_all'))


def cantidad_categorias_productos():
    if 'loggedin' in session and session.get('is_admin'):
        resultado = get_cantidad_categorias_productos()
        return jsonify([{"name": row[0], "y": float(row[1])} for row in resultado if row[1] is not None])
    else:
        flash('Debes iniciar sesión como administrador para acceder a esta página.', 'error')
        return redirect(url_for('login_all'))


def admin_manage_users():
    if 'loggedin' in session and session.get('is_admin'):
        if request.method == 'POST':
            if 'field' in request.form:
                id_usr = request.form.get('id_usr')
                field = request.form.get('field')
                value = request.form.get('value')

                if not id_usr or not field or value is None:
                    return jsonify({"success": False, "message": "Datos incompletos."})

                success, message = update_user_field(id_usr, field, value)
                return jsonify({"success": success, "message": message})

            if 'delete_user' in request.form:
                id_usr = request.form.get('delete_user')

                if not id_usr:
                    return jsonify({"success": False, "message": "No se especificó el usuario a eliminar."})

                success, message = delete_user_by_id(id_usr)
                return jsonify({"success": success, "message": message})

        users = get_all_users()
        return render_template('manage_users.html', users=users)
    else:
        flash('Debes iniciar sesión como administrador para acceder a esta página.', 'error')
        return redirect(url_for('login_all'))

def admin_insert_user():
    if 'loggedin' in session and session.get('is_admin'): 
        if request.method == 'POST':
            username = request.form.get('username')
            clave = request.form.get('clave')
            nom_usr = request.form.get('nom_usr')
            apellido_usr = request.form.get('apellido_usr')
            correo_usr = request.form.get('correo_usr')
            tel_usr = request.form.get('tel_usr')
            tel_domicilio = request.form.get('tel_domicilio')
            direccion = request.form.get('direccion')
            foto_usuario = request.form.get('foto_usuario', '')  
            
            if not foto_usuario:
                foto_usuario = ''

            success, message = insert_user(username, clave, nom_usr, apellido_usr, correo_usr, tel_usr, tel_domicilio, direccion, foto_usuario)

            if success:
                return redirect(url_for('admin_manage_users'))
            else:
                return render_template('admin_insert_user.html', error=message)

        return render_template('admin_insert_user.html')

    return redirect(url_for('login')) 

def admin_insert_product():
    if 'loggedin' in session and session.get('is_admin'):
        if request.method == 'POST':
            nom_producto = request.form['nom_producto']
            desc_producto = request.form['desc_producto']
            precio = request.form['precio']
            empresa_nom = request.form['empresa_nom']
            foto_producto = request.form.get('foto_producto', '')  

            success, message = insertar_producto(nom_producto, desc_producto, precio, empresa_nom, foto_producto)
            
            if success:
                flash(message, 'success')
                return redirect(url_for('admin_manage_products'))
            else:
                flash(message, 'error')

        return render_template('insertar_producto.html')

    else:
        flash('Debes iniciar sesión como administrador para acceder a esta página.', 'error')
        return redirect(url_for('login_all'))

def admin_insert_discount():
    if 'loggedin' in session and session.get('is_admin'):
        if request.method == 'POST':
            nom_promocion = request.form['nom_promocion']
            descuento = request.form['descuento']
            fecha_inicio = request.form['fecha_inicio']
            fecha_fin = request.form['fecha_fin']
            activo = bool(int(request.form['activo'])) 

            success, message = insertar_promocion(nom_promocion, descuento, fecha_inicio, fecha_fin, activo)
            
            if success:
                flash(message, 'success')
                return redirect(url_for('admin_manage_promotions'))
            else:
                flash(message, 'error')

        return render_template('insertar_promocion.html')

    else:
        flash('Debes iniciar sesión como administrador para acceder a esta página.', 'error')
        return redirect(url_for('login_all'))


def admin_manage_products():
    if 'loggedin' in session and session.get('is_admin'):
        if request.method == 'POST':
            if 'field' in request.form:
                id_producto = request.form.get('id_producto')
                field = request.form.get('field')
                value = request.form.get('value')

                if not id_producto or not field or value is None:
                    return jsonify({"success": False, "message": "Datos incompletos."})
                
                allowed_fields = ['nom_producto', 'desc_producto', 'precio', 'empresa_nom']
                if field not in allowed_fields:
                    return jsonify({"success": False, "message": "Campo no permitido para actualizar."})

                success, message = update_product_field(id_producto, field, value)
                return jsonify({"success": success, "message": message})

            if 'delete_product' in request.form:
                id_producto = request.form.get('delete_product')

                if not id_producto:
                    return jsonify({"success": False, "message": "No se especificó el producto a eliminar."})

                success, message = delete_product_by_id(id_producto)
                return jsonify({"success": success, "message": message})

        products = get_all_products()
        return render_template('manage_products.html', products=products)
    else:
        flash('Debes iniciar sesión como administrador para acceder a esta página.', 'error')
        return redirect(url_for('login_all'))


def admin_manage_orders():
    if 'loggedin' in session and session.get('is_admin'):
        if request.method == 'POST':
            if 'estado_pedido' in request.form:
                id_pedido = request.form.get('id_pedido')
                estado_pedido = request.form.get('estado_pedido')

                if not id_pedido or not estado_pedido:
                    return jsonify({"success": False, "message": "Datos incompletos."})

                success, message = update_order_status(id_pedido, estado_pedido)
                return jsonify({"success": success, "message": message})

            if 'delete_order' in request.form:
                id_pedido = request.form.get('delete_order')

                if not id_pedido:
                    return jsonify({"success": False, "message": "No se especificó la orden a eliminar."})

                success, message = delete_order_by_id(id_pedido)
                return jsonify({"success": success, "message": message})

        orders = get_all_orders()
        return render_template('manage_orders.html', orders=orders)
    else:
        flash('Debes iniciar sesión como administrador para acceder a esta página.', 'error')
        return redirect(url_for('login_all'))

def admin_manage_discounts():
    if 'loggedin' in session and session.get('is_admin'):
        if request.method == 'POST':
            if 'field' in request.form:
                id_promocion = request.form.get('id_promocion')
                field = request.form.get('field')
                value = request.form.get('value')

                if not id_promocion or not field or value is None:
                    return jsonify({"success": False, "message": "Datos incompletos."})

                success, message = update_discount_field(id_promocion, field, value)
                return jsonify({"success": success, "message": message})

            if 'delete_discount' in request.form:
                id_promocion = request.form.get('delete_discount')

                if not id_promocion:
                    return jsonify({"success": False, "message": "No se especificó el descuento a eliminar."})

                success, message = delete_discount_by_id(id_promocion)
                return jsonify({"success": success, "message": message})

        discounts = get_all_discounts()
        return render_template('manage_discounts.html', discounts=discounts)
    else:
        flash('Debes iniciar sesión como administrador para acceder a esta página.', 'error')
        return redirect(url_for('login_all'))


def promedio_calificacion_productos():
    if 'loggedin' in session and session.get('is_admin'):
        resultado = get_promedio_calificacion_productos()
        return jsonify([{"name": row[0], "y": float(row[1])} for row in resultado if row[1] is not None])
    else:
        return jsonify({"error": "Acceso no autorizado"}), 403  


def cantidad_categorias_productos():
    if 'loggedin' in session and session.get('is_admin'):
        resultado = get_cantidad_categorias_productos()
        return jsonify([{"name": row[0], "y": float(row[1])} for row in resultado if row[1] is not None])
    else:
        return jsonify({"error": "Acceso no autorizado"}), 403


def cantidad_stock_productos():
    if 'loggedin' in session and session.get('is_admin'):
        resultado = get_cantidad_stock_productos()
        return jsonify([{"name": row[0], "y": float(row[1])} for row in resultado if row[1] is not None])
    else:
        return jsonify({"error": "Acceso no autorizado"}), 403


def pedidos_por_mes():
    if 'loggedin' in session and session.get('is_admin'):
        resultado = get_pedidos_por_mes()
        return jsonify([{"name": row[0], "y": float(row[1])} for row in resultado if row[1] is not None])
    else:
        return jsonify({"error": "Acceso no autorizado"}), 403


def usuarios_por_mes():
    if 'loggedin' in session and session.get('is_admin'):
        resultado = get_usuarios_por_mes()
        return jsonify([{"name": row[0], "y": float(row[1])} for row in resultado if row[1] is not None])
    else:
        return jsonify({"error": "Acceso no autorizado"}), 403


def productos_estado(estado):
    if 'loggedin' in session and session.get('is_admin'):
        resultado = get_productos_estado(estado)
        return jsonify([{"total": resultado[0]}])
    else:
        return jsonify({"error": "Acceso no autorizado"}), 403
    
def productos_entregados():
    return productos_estado('completados')

def productos_en_proceso():
    return productos_estado('en_proceso')

def productos_cancelados():
    return productos_estado('cancelados')


def ganancias_por_mes():
    if 'loggedin' in session and session.get('is_admin'):
        resultado = get_ganancias_por_mes()
        return jsonify([{"name": row[0], "y": float(row[1])} for row in resultado if row[1] is not None])
    else:
        return jsonify({"error": "Acceso no autorizado"}), 403
