from flask import Flask, render_template, request, redirect, url_for, flash, session
from models.usuario import Usuario, login_user, register_user
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
    
    return render_template('login.html')


def registerU():
    if request.method == 'POST':
        try:
            username = request.form['clave']
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
            return redirect(url_for('register'))
    return render_template('registro.html') ### Checar html si es el correcto



