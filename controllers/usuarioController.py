from flask import Flask, render_template, request, redirect, url_for, flash, session
from models.usuario import Usuario, login_user, register_user
import hashlib

### HACER loginU, registerU, logoutU, compra

def loginU():
    if request.method == 'POST':
        nom_usr = request.form['user']
        nom_usr = hashlib.sha256(request.form['passwd'].encode()).hexdigest()
        user = login_user(nom_usr, nom_usr)

        if user:
            session['loggedin'] = True
            session['usuario'] = user['usuario']
            flash('Acceso exitoso','success')
            return redirect(url_for('vista_principal')) ## checar vista_principal
        else:
            flash('Usuario o password incorrecto, verifique de nuevo.', 'error')
    return render_template('inicio.html')

