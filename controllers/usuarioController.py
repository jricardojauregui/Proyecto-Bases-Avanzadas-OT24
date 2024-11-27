from flask import Flask, render_template, request, redirect, url_for, flash, session
from models.usuario import login_user, register_user, update_user, get_user_profile, confirm_purchase, get_user_cart, add_to_cart, cancel_order, usr_order_history, remove_from_cart, clear_cart, get_user_cards, get_wishlist, delete_user_account, get_product_info, toggle_wishlist, get_wishlist_status, direct_purchase, get_product_ratings, submit_rating, get_last_purchase_date, get_product_category, get_all_products, get_products_by_category, add_credit_card, remove_credit_card, validate_user_credentials, get_most_requested_products, get_newest_products, get_products_on_promotion, get_recommended_products
import hashlib

def user_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['clave']

        if not username or not password:
            flash('Por favor, ingresa usuario y contraseña.', 'error')
            return redirect(url_for('login'))

        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        
        user = login_user(username, hashed_password)

        if user:
            session['loggedin'] = True
            session['usuario'] = user['username']  
            flash('Acceso exitoso', 'success')
            return redirect(url_for('inicio')) ### checar esto
        else:
            flash('Usuario o contraseña incorrectos, intenta nuevamente.', 'error')
    
    return render_template('login.html') ### checar html

def user_register():
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

def user_update():
    if 'loggedin' in session:
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

            hashed_clave = hashlib.sha256(clave.encode()).hexdigest() if clave else None
            id_usr = session['id_usr']   

            success, message = update_user(id_usr, username, hashed_clave, nom_usr, apellido_usr, correo_usr, tel_usr, tel_domicilio, direccion, foto_usuario)

            if success:
                flash(message, 'success')
                return redirect(url_for('profile'))  # checar esto
            else:
                flash(message, 'error')
                return redirect(url_for('update')) ### checar tambien esto
    
        return render_template('editar_perfil.html')  # checar esto
    else:
        flash('Primero debe de ingresar.', 'error')
        return redirect(url_for('login'))

def user_profile():
    if 'loggedin' in session:
        id_usr = session['id_usr'] 

        user_profile = get_user_profile(id_usr) 

        if not user_profile:
            flash("No se pudo cargar el perfil. Intenta nuevamente.", "error")
            return redirect(url_for('logout')) 

        return render_template('perfil.html', user=user_profile)  
    else:
        flash("Debes iniciar sesión para ver tu perfil.", "error")
        return redirect(url_for('login'))  
    
def user_logout():
    if 'loggedin' not in session:  
        flash('No hay sesión activa.', 'error')
        return redirect(url_for('login')) 
    
    session.clear()  
    flash('Has cerrado sesión correctamente.', 'success')  
    return redirect(url_for('inicio'))  ### checar esto

def user_delete_account():
    if 'loggedin' in session:
        if request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')

            if not username or not password:
                flash("Por favor, proporciona tu nombre de usuario y contraseña.", "error")
                return redirect(url_for('deleteAccount'))
            
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            
            user_id = validate_user_credentials(username, hashed_password)
            
            if not user_id:
                flash("Nombre de usuario o contraseña incorrectos, o el usuario no existe.", "error")
                return redirect(url_for('deleteAccount'))

            success, message = delete_user_account(user_id)
            if success:
                session.clear()  
                flash(message, "success")
                return redirect(url_for('inicio'))  
            else:
                flash(message, "error")
                return redirect(url_for('deleteAccount')) 

        return render_template('delete_account.html') 

    else:
        flash("Debes iniciar sesión para eliminar tu cuenta.", "error")
        return redirect(url_for('login')) 

def user_view_and_manage_cart():
    if 'loggedin' in session:
        id_usr = session['id_usr']  

        if request.method == 'POST':
            if 'id_producto' in request.form:
                id_producto = request.form.get('id_producto')
                success, message = remove_from_cart(id_usr, id_producto)
                flash(message, "success" if success else "error")
                return redirect(url_for('cart'))  

            if 'clear_cart' in request.form:
                success, message = clear_cart(id_usr)
                flash(message, "success" if success else "error")
                return redirect(url_for('cart'))  

            if 'card_number' in request.form:
                card_number = request.form.get('card_number')
                if not card_number:
                    flash("Por favor, selecciona una tarjeta para confirmar la compra.", "error")
                    return redirect(url_for('cart'))  

                success, message = confirm_purchase(id_usr, card_number)
                flash(message, "success" if success else "error")
                return redirect(url_for('profile'))  

        cart_items = get_user_cart(id_usr)
        user_cards = get_user_cards(id_usr)

        if not cart_items:
            flash("Tu carrito está vacío.", "info")

        return render_template('cart.html', cart_items=cart_items, user_cards=user_cards)

    else:
        flash("Debes iniciar sesión para modificar tu carrito.", "error")
        return redirect(url_for('login'))  # Si no está logueado, redirige al login



def user_view_product(id_producto):
    if 'loggedin' in session:  
        id_usr = session['id_usr'] 

        if request.method == 'POST':
            if 'add_to_cart' in request.form:
                cantidad = int(request.form.get('cantidad'))
                success, message = add_to_cart(id_usr, id_producto, cantidad)
                flash(message, "success" if success else "error")

            elif 'confirm_purchase' in request.form:
                tarjeta_usr = request.form.get('tarjeta_usr')
                if not tarjeta_usr:
                    flash("Selecciona una tarjeta para confirmar la compra.", "error")
                else:
                    success, message = direct_purchase(id_usr, id_producto, 1, tarjeta_usr)
                    flash(message, "success" if success else "error")

            elif 'toggle_wishlist' in request.form:
                success, message = toggle_wishlist(id_usr, id_producto)
                flash(message, "success" if success else "error")

            elif 'submit_rating' in request.form:
                calificacion = int(request.form.get('calificacion'))
                comentario = request.form.get('comentario')
                success, message = submit_rating(id_usr, id_producto, calificacion, comentario)
                flash(message, "success" if success else "error")

            return redirect(url_for('product', id_producto=id_producto))

        wishlist_status = get_wishlist_status(id_usr, id_producto)
        tarjetas = get_user_cards(id_usr)
        last_purchase_date = get_last_purchase_date(id_usr, id_producto)

    else:
        wishlist_status = None
        tarjetas = None
        last_purchase_date = None

    product_info = get_product_info(id_producto)
    ratings = get_product_ratings(id_producto)
    category = get_product_category(id_producto)

    return render_template('producto.html', product=product_info, category=category, ratings=ratings, wishlist_status=wishlist_status, tarjetas=tarjetas, last_purchase_date=last_purchase_date)


def user_view_all_products():
    all_products = get_all_products()
    return render_template('productos.html', productos=all_products)

def user_view_products_by_category(id_categoria):
    productos = get_products_by_category(id_categoria)
    categoria = get_product_category(id_categoria)  

    if not categoria:
        flash("Categoría no encontrada.", "error")
        return redirect(url_for('products')) 
    
    return render_template('productos_categoria.html', productos=productos, categoria=categoria)

def user_order_history():
    if 'loggedin' not in session: 
        flash("Debes iniciar sesión para ver tu historial de pedidos.", "error")
        return redirect(url_for('login'))  

    id_usr = session['id_usr']  

    if request.method == 'POST':
        if 'id_pedido' in request.form:
            id_pedido = request.form.get('id_pedido')
            success, message = cancel_order(id_pedido)
            flash(message, "success" if success else "error")
            return redirect(url_for('orderHistory')) 

    orders = usr_order_history(id_usr)

    pending_orders = [order for order in orders if order['estado_pedido'] == 'En proceso']
    completed_orders = [order for order in orders if order['estado_pedido'] == 'Completado']

    return render_template('order_history.html', pending_orders=pending_orders, completed_orders=completed_orders)

def user_view_wishlist():
    if 'loggedin' not in session:  
        flash("Debes iniciar sesión para ver tu lista de deseos.", "error")
        return redirect(url_for('login')) 

    id_usr = session['id_usr']  

    wishlist_items = get_wishlist(id_usr)  

    if not wishlist_items:
        flash("Tu lista de deseos está vacía.", "info")  

    return render_template('wishlist.html', wishlist_items=wishlist_items)  
    
def user_view_credit_cards():
    if 'loggedin' not in session:  
        flash("Debes iniciar sesión para ver tus tarjetas.", "error")
        return redirect(url_for('login'))  

    id_usr = session['id_usr'] 

    user_cards = get_user_cards(id_usr) 
    if not user_cards:
        flash("No tienes tarjetas registradas.", "info") 

    return render_template('view_cards.html', user_cards=user_cards)  

    
def user_manage_credit_cards():
    if 'loggedin' not in session:  
        flash("Debes iniciar sesión para gestionar tus tarjetas.", "error")
        return redirect(url_for('login'))  

    id_usr = session['id_usr'] 

    if request.method == 'POST':
        if 'add_card' in request.form:  
            tarjeta_usr = request.form.get('tarjeta_usr')
            id_banco = request.form.get('id_banco')
            propietario = request.form.get('propietario')
            caduci_tarjeta = request.form.get('caduci_tarjeta')

            if not (tarjeta_usr and id_banco and propietario and caduci_tarjeta):
                flash("Todos los campos son obligatorios para añadir una tarjeta.", "error")
            else:
                success, message = add_credit_card(id_usr, tarjeta_usr, id_banco, propietario, caduci_tarjeta)
                flash(message, "success" if success else "error")

        elif 'remove_card' in request.form:  
            tarjeta_usr = request.form.get('tarjeta_usr')

            if not tarjeta_usr:
                flash("No se seleccionó ninguna tarjeta para eliminar.", "error")
            else:
                success, message = remove_credit_card(id_usr, tarjeta_usr)
                flash(message, "success" if success else "error")

    user_cards = get_user_cards(id_usr)  
    return render_template('manage_cards.html', user_cards=user_cards)  


def user_view_products_with_discount():
    products = get_products_on_promotion()
    return render_template('promotion_products.html', products=products)

def user_view_most_requested_products():
    products = get_most_requested_products()
    return render_template('most_requested_products.html', products=products)

def user_view_newest_products():
    products = get_newest_products()
    return render_template('newest_products.html', products=products)

def user_view_recommendations():
    if 'loggedin' in session:  
        id_usr = session['id_usr']
        recommended_products = get_recommended_products(id_usr) 
        return render_template('recommendations.html', recommended_products=recommended_products)
    else:
        flash("Inicia sesión para ver tus recomendaciones personalizadas.", "warning")
        return redirect(url_for('products'))  