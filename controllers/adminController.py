from flask import Flask, render_template, request, redirect, url_for, flash, session
from models.admin import Admin

## HACER loginAdmin, registerAdmin, logoutAdmin, mostrarEmpresas, editarEmpresas, eliminarEmpresas