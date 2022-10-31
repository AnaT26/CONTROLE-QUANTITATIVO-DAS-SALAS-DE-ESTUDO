from tkinter import E
from flask_login import UserMixin
from .view import te
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
print("basedir:", basedir)


'''''''''class User(UserMixin, te.Model):
    id_u = te.Column(te.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = te.Column(te.String(100), unique=True)
    senha = te.Column(te.String(100))
    nome = te.Column(te.String(1000))

class NewUser(User):
    dre = te.Column(te.String(100)) #, primary_key=True)
    curso = te.Column(te.String(1000))
    #pass'''''''''

class Sala():
    def __init__(self, nome, np):
        self.nome = nome
        self.np = np
    def inserir_sala(self, nome, np):
        self.nome = input("Insira o nome da sala (ex:d206):")
        self.np = input("Insira o numero de pessoas na sala:/n")
        conn = sqlite3.connect(os.path.join(basedir, 'te.db'))
        c = conn.cursor()
        c.executescript("INSERT INTO sala(nome, np) VALUES('"+nome+"','"+np+"')")
        conn.commit()
    
 
    


