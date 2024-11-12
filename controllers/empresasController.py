from flask import Flask, render_template, request, redirect, url_for, flash, session
from models.empresa import Empresa

### HACER loginEmp, registerEmp, logoutEmp, editarEmp