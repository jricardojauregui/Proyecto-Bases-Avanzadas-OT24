from flask import Flask, render_template, request, redirect, url_for, flash, session
from models.usuario import login_user, register_user, update_user, confirm_purchase, get_user_cart, add_to_cart, usr_order_history, get_cart_items, remove_from_cart, clear_cart, confirm_purchase, get_user_cards, get_wishlist
import hashlib

### HACER loginU, registerU, logoutU, compra

def loginU():
    if request.method == 'POST':
        username = request.form.get('username')  
        password = request.form.get('clave')  

        if not username or not password:
            flash('Por favor, ingresa usuario y contraseña.', 'error')
            return redirect(url_for('login'))

        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        
        user = login_user(username, hashed_password)

        if user:
            session['loggedin'] = True
            session['usuario'] = user['username']  
            flash('Acceso exitoso', 'success')
            return redirect(url_for('vista_principal')) ### checar esto
        else:
            flash('Usuario o contraseña incorrectos, intenta nuevamente.', 'error')
    
    return render_template('login.html') ### checar html

def registerU():
    if request.method == 'POST':
        try:
            username = request.form['username']
            clave = request.form['clave']
            nom_usr = request.form['nom_usr']
            apellido_usr = request.form['apellido_usr']
            correo_usr = request.form['correo_usr']
            tel_usr = request.form['tel_usr']
            tel_domicilio = request.form['tel_domicilio']
            direccion = request.form['direccion']
        except KeyError:
            flash('Faltan datos obligatorios en el formulario. Por favor verifica tus datos.', 'error')
            return redirect(url_for('register'))
        foto_usuario = request.form.get('foto_usuario', '') 

        hashed_clave = hashlib.sha256(clave.encode()).hexdigest()

        success, message = register_user(hashed_clave, username, nom_usr, apellido_usr, correo_usr, tel_usr, tel_domicilio, direccion, foto_usuario)
        if success:
            flash('Registro exitoso.', 'success')
            return redirect(url_for('login'))
        else:
            flash(message, 'error')
            return redirect(url_for('register')) ### checar tambien esto
    return render_template('registro.html') ### Checar html si es el correcto

def updateU():
    if request.method == 'POST':
        id_usr = session.get('id_usr') 

        if not id_usr:
            flash('No se puede identificar al usuario.', 'error')
            return redirect(url_for('login'))  # checar tmb esto

        username = request.form.get('username')
        clave = request.form.get('clave')
        nom_usr = request.form.get('nom_usr')
        apellido_usr = request.form.get('apellido_usr')
        correo_usr = request.form.get('correo_usr')
        tel_usr = request.form.get('tel_usr')
        tel_domicilio = request.form.get('tel_domicilio')
        direccion = request.form.get('direccion')
        foto_usuario = request.form.get('foto_usuario', '')  

        hashed_clave = hashlib.sha256(clave.encode()).hexdigest() if clave else None

        success, message = update_user(id_usr, username, hashed_clave, nom_usr, apellido_usr, correo_usr, tel_usr, tel_domicilio, direccion, foto_usuario)

        if success:
            flash(message, 'success')
            return redirect(url_for('perfil'))  # checar esto
        else:
            flash(message, 'error')
            return redirect(url_for('editar_perfil')) ### checar tambien esto
    
    return render_template('editar_perfil.html')  # checar esto

def logoutU():
    session.clear()  
    flash('Has cerrado sesión correctamente.', 'success')  
    return redirect(url_for('inicio'))  ### checar esto

def view_and_manage_cart():
    id_usr = session.get('id_usr') 

    if not id_usr:
        flash("Debes iniciar sesión para modificar tu carrito.", "error")
        return redirect(url_for('login'))  ### checar esto

    if request.method == 'POST':
        if 'id_producto' in request.form:
            id_producto = request.form.get('id_producto')
            success, message = remove_from_cart(id_usr, id_producto)
            flash(message, "success" if success else "error")
            return redirect(url_for('cart'))   ### checar esto

        if 'clear_cart' in request.form:
            success, message = clear_cart(id_usr)
            flash(message, "success" if success else "error")
            return redirect(url_for('cart'))   ### checar esto

        if 'card_number' in request.form:
            card_number = request.form.get('card_number')
            if not card_number:
                flash("Por favor, selecciona una tarjeta para confirmar la compra.", "error")
                return redirect(url_for('cart'))  ### checar esto

            success, message = confirm_purchase(id_usr, card_number)
            flash(message, "success" if success else "error")
            return redirect(url_for('perfil'))    ### checar esto

    cart_items = get_cart_items(id_usr)
    user_cards = get_user_cards(id_usr)

    if not cart_items:
        flash("Tu carrito está vacío.", "info")

    return render_template('cart.html', cart_items=cart_items, user_cards=user_cards)  ### checar esto


def add_product_to_cart():
    if request.method == 'POST':
        id_usr = session.get('id_usr')  
        if not id_usr:
            flash("Debes iniciar sesión para agregar productos al carrito.", "error")
            return redirect(url_for('login')) ## checar esto
        
        id_producto = request.form.get('product_id')
        cantidad = int(request.form.get('cantidad', 1)) 

        if not id_producto:
            flash("Faltan datos para agregar al carrito.", "error")
            return redirect(url_for('carrito')) ## checar esto

        success, message = add_to_cart(id_usr, id_producto, cantidad)

        if success:
            flash(message, "success")
        else:
            flash(message, "error")
        return redirect(url_for('carrito')) ## checar esto

def order_history():
    if request.method == 'POST':
        id_usr = session.get('id_usr')  

        if not id_usr:
            flash("Debes iniciar sesión para ver tu historial de pedidos.", "error")
            return redirect(url_for('login')) ### checar esto

        orders = usr_order_history(id_usr)

        if not orders:
            flash("No tienes pedidos registrados en tu historial.", "info")
            return render_template('order_history.html', orders=[]) ### checar este template

        return render_template('order_history.html', orders=orders) ### checar este template
    
def view_wishlist():
    if request.method == 'POST':
        id_usr = session.get('id_usr')  

        if not id_usr:
            flash("Debes iniciar sesión para ver tu lista de deseos.", "error")
            return redirect(url_for('login'))  

        wishlist_items = get_wishlist(id_usr)

        if not wishlist_items:
            flash("Tu lista de deseos está vacía.", "info")

        return render_template('wishlist.html', wishlist_items=wishlist_items)