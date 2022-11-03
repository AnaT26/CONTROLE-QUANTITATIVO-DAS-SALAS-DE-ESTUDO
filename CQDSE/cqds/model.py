from tkinter import E
from flask_login import UserMixin
from flask import Flask, render_template, redirect, url_for, request, flash
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
    #metodo que insere uma nova classe no DB
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
    #metodo que soma um no numero de pessoas armazenado no banco de dados
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
    #metodo que subtrai um do numero de pessoas armazenado no bd
    def buscar_np(self, id_s):
        conn = sqlite3.connect(os.path.join(basedir, 'te.db'))
        c = conn.cursor()
        n = c.execute("SELECT np FROM sala WHERE id_s=?",[str(id_s)])
        rows = n.fetchone()
        linha = rows[0]
        conn.commit()
        print(linha)
        return linha
    #metodo que busca no DB o numero de pessoas na sala
        



