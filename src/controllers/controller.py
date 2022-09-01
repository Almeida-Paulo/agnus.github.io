from flask.views import MethodView
from flask import request,render_template,redirect,flash
from src.db import mysql

class IndexController(MethodView):
    def get(self):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM clientes")
            data = cur.fetchall()
        return render_template('public/index.html', data=data)
    
    def post(self):
        name = request.form['name']
        phone = request.form['phone']
        business = request.form['business']
        email = request.form['email']
        message = request.form['message']

        with mysql.cursor() as cur:
            cur.execute("INSERT INTO clientes VALUES (%s, %s, %s, %s, %s)", (name, phone, business, email, message))
            cur.connection.commit()
            return redirect('/')