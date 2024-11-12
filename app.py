from flask import Flask, render_template, request, redirect, url_for, flash, session
from config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB, SECRET_KEY
from database import mysql, init_app

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
app.add_url_rule('/registerAdmin', view_func=registerAdmin, methods=['GET', 'POST'])
app.add_url_rule('/logoutAdmin', view_func=logoutAdmin)
app.add_url_rule('/empresas', view_func=mostrarEmpresas)
app.add_url_rule('/editarEmpresas/<int:id>', view_func=editarEmpresas, methods=['GET', 'POST'])
app.add_url_rule('/eliminarEmpresas/<int:id>', view_func=eliminarEmpresas, methods=['GET', 'POST'])

### RUTAS EMPRESAS
app.add_url_rule('/loginEmp', view_func=loginEmp, methods=['GET', 'POST'])
app.add_url_rule('/registrarEmp', view_func=registerEmp, methods=['GET', 'POST'])
app.add_url_rule('/logoutEmp', view_func=logoutEmp)
app.add_url_rule('/editarEmp/<int:id>', view_func=editarEmp, methods=['GET', 'POST'])

### RUTAS USUARIO
app.add_url_rule('/login', view_func=loginU, methods=['GET', 'POST'])
app.add_url_rule('/registrar', view_func=registerU, methods=['GET', 'POST'])
app.add_url_rule('/logoutEmp', view_func=logoutU)
app.add_url_rule('/compra', view_func=compra, methods=['GET', 'POST'])
