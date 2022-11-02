from tkinter import E
from flask_login import UserMixin
#from .view import te
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
import sqlite3

from flask_sqlalchemy import SQLAlchemy
import os


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'te.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

te = SQLAlchemy(app)

print(te.MetaData())

#from .model import User, NewUser



'''''''''class User(UserMixin, te.Model):
    id_u = te.Column(te.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = te.Column(te.String(100), unique=True)
    senha = te.Column(te.String(100))
    nome = te.Column(te.String(1000))

class NewUser(User):
    dre = te.Column(te.String(100)) #, primary_key=True)
    curso = te.Column(te.String(1000))
    #pass'''''''''

class Sala:
    def __init__(self):
        pass
    def inserir_sala(self):
        self.nome = input("Insira o nome da sala (ex:d206):\n")
        self.np = input("Insira o numero de pessoas na sala:\n")
        conn = sqlite3.connect(os.path.join(basedir, 'te.db'))
        c = conn.cursor()
        c.executescript("INSERT INTO sala(nome, np) VALUES('"+self.nome+"','"+self.np+"')")
        conn.commit()
    def entrar(self, id_s):
        conn = sqlite3.connect(os.path.join(basedir, 'te.db'))
        c = conn.cursor()
        n = c.execute("SELECT np FROM sala WHERE id_s=?",[str(id_s)])
        rows = n.fetchone()
        linha = rows[0]
        soma1 = int(linha) + 1
        c.execute("UPDATE sala SET np = ? WHERE id_s = ?",[int(soma1), str(id_s)])
        conn.commit()
        print(linha, soma1)
    def sair(self, id_s):
        conn = sqlite3.connect(os.path.join(basedir, 'te.db'))
        c = conn.cursor()
        n = c.execute("SELECT np FROM sala WHERE id_s=?",[str(id_s)])
        rows = n.fetchone()
        linha = rows[0]
        sub1 = int(linha) - 1
        c.execute("UPDATE sala SET np = ? WHERE id_s = ?",[int(sub1), str(id_s)])
        conn.commit()
        print(linha, sub1)
        return render_template("vs.html")
    def buscar(self, id_s):
        conn = sqlite3.connect(os.path.join(basedir, 'te.db'))
        post = conn.execute('SELECT * FROM sala WHERE id_s = ?',(id_s,)).fetchone()
        conn.commit()
    def buscar_np(self, id_s):
        conn = sqlite3.connect(os.path.join(basedir, 'te.db'))
        c = conn.cursor()
        n = c.execute("SELECT np FROM sala WHERE id_s=?",[str(id_s)])
        rows = n.fetchone()
        linha = rows[0]
        conn.commit()
        print(linha)
        return linha
        

#Sala().buscar(2)

#Sala().inserir_sala() 
#A função acima atualiza os bancos de dados das salas de estudo
#Sala().entrar(2)
 
#atualizar o valor do bd e fazer essa função somar no valor de uma sala especifica, e mostrar valor no html


