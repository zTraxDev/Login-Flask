from flask import Flask, Blueprint, render_template, redirect, request, session, url_for, flash, abort
from db import DataBase


login = Blueprint("Na", __name__)


@login.route('/login', methods =['GET','POST'])
def login_():
    if request.method == "POST":
        userName = request.form['txtUse']
        password = request.form['txtContra']

        conexion = DataBase()
        cursor = conexion.cursor()
        cursor.execute('SELECT * FROM user WHERE name = %s AND password = %s', (userName, password, ))
        users = cursor.fetchone()
        a = session["Sesion_ID"] = users[1]
        error = None

        if users == None:
            return ("Error: Usuario o Contraseñas son Incorrectas")
        elif error is None:
            session.accessed = True
            return redirect("/home")
    return render_template("templates/login.html")

@login.route("/register", methods =['GET','POST'])
def register():
    if request.method == 'POST':
        #------
        user = request.form['txtName']
        password = request.form['txtPassword']
        email = request.form['txtCorreo']
         
        conexion = DataBase()
        cursor = conexion.cursor()
        sql = 'INSERT INTO user (name, password, email) VALUES (%s, %s, %s)'
        data = (user, password, email)
        cursor.execute(sql, data)
        conexion.commit()
        session.clear()
        return redirect("/login")
    return render_template('templates/register.html')

@login.route("/home")
def inde():
   conexion = DataBase()
   cursor = conexion.cursor()
   cursor.execute("SELECT * FROM user")
   users = cursor.fetchall()
   conexion.commit()
   return render_template("templates/home.html", user = users)

@login.route("/logout", methods=["GET"])
def cerrar():
  session.clear()
  return redirect("/login")