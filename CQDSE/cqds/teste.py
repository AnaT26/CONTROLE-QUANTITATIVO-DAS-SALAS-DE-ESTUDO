'''from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from .model import User, NewUser
from . import te
from view import app'''
from flask import Blueprint, render_template, redirect, url_for, request, flash

import sqlite3
import sqlite3 as sql

email = "catarina@gmail.com"
senha = "cata"
conn = sqlite3.connect('te.db') 
c = conn.cursor()
j = c.execute("SELECT * FROM user where email = '"+email+"' and senha ='"+senha+"'").fetchall()

class User():
    def ___init___(self, email, senha):
        self.email = email
        self.senha = senha
    def valida_senha(email,senha):
        conn = sqlite3.connect('te.db') 
        c = conn.cursor()
        j = c.execute("SELECT * FROM user where email = '"+email+"' and senha ='"+senha+"'").fetchall()
                            
        conn.commit()
        
        print(j)
        
        if j:
            return render_template("salas.html")
        else:
            return render_template("home.html", erro="Login Incorreto")




con = sql.connect("te.db")
cur = con.cursor()
statement = f"SELECT email from user WHERE email='{email}' AND senha = '{senha}';"
cur.execute(statement)
if not cur.fetchone():  # An empty result evaluates to False.
    print("Login failed")
else:
    print("Welcome")

'''import sqlite3

conn = sqlite3.connect('te.db') 
c = conn.cursor()

j = c.execute("SELECT * FROM user").fetchall()
                     
conn.commit()

print(j)'''

'''@app.route('/cadastro')
def signup():
    return render_template('cadastro.html')


@app.route('/fcadastro', methods=['POST'])
def signup_post():
    nome = request.form.get('nome')
    dre = request.form.get('dre')
    curso = request.form.get('curso')
    email = request.form.get('email')
    senha = request.form.get('senha')

    # if this returns a user, then the email already exists in database
    key = User.query.filter_by(email=email).first()

    if key:  # if a user is found, we want to redirect back to signup page so user can try again
        flash('Email ja cadastrado')
        return redirect(url_for('view.cadastro'))

    # create new user with the form data. Hash the password so plaintext version isn't saved.
    new_user = NewUser(email=email, nome=nome, senha=senha, dre=dre, curso=curso)

    # add the new user to the database
    te.session.add(new_user)
    te.session.commit()

    return redirect(url_for('view.f_cadastro'))
'''

'''def login_post():
    email = request.form.get('email')
    senha = request.form.get('senha')

    user = User.query.filter_by(email=email).first()

    # check if user actually exists
    # take the user supplied password, hash it, and compare it to the hashed password in database
    if not user or not check_password_hash(user.senha, senha): 
        flash('Email ou senha incorreto.')
        return redirect(url_for('cqds.home')) # if user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    login_user(user)
    return redirect(url_for('cqds.sala'))'''
