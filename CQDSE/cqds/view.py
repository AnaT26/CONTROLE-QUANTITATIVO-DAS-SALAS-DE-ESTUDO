from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
import sqlite3
from cqds.model import Sala

from flask_sqlalchemy import SQLAlchemy
import os


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'te.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

te = SQLAlchemy(app)


@app.route("/")
def home():
    return render_template("home.html")
# pagina inicial do site



@app.route("/home", methods=["POST"])
def voltar():
    return render_template("home.html")
# direciona para a home do site


@app.route("/login", methods=["POST"])
def login():

    if request.method == "POST":
        email = request.form["email"]
        senha = request.form["senha"]
        return valida_senha(email, senha)

    else:
        print("Deu ruim")
        return "RUIM"
# pega as informações de login e redireciona para o valida senha


def valida_senha(email, senha):

    conn = sqlite3.connect(os.path.join(basedir, 'te.db'))
    c = conn.cursor()
    j = c.execute("SELECT * FROM user where email = '" +
                  email+"' and senha ='"+senha+"'").fetchall()

    conn.commit()

    print(j)

    if j:
        return render_template("salas.html")
    else:
        return render_template("home.html", erro="Login Incorreto")
# se email e a senha forem verificados retorna uma mensagem de erro ou a lista com as salas


@app.route("/f_cadastro", methods=["POST"])
def f_cadastro():
    dre = request.form["dre"]
    nome = request.form["nome"]
    curso = request.form["curso"]
    senha = request.form["senha"]
    email = request.form["email"]
    repetesenha = request.form["repetesenha"]
    return cadastrar(nome, dre, curso, email, senha, repetesenha)
# depois de coletar os dados de cadastro, retorna para a função cadastrar


def cadastrar(nome, dre, curso, email, senha, repetesenha):
    conn = sqlite3.connect(os.path.join(basedir, 'te.db'))
    c = conn.cursor()
    e = c.execute("SELECT * FROM user where email = '"+email+"'").fetchall()
    conn.commit()
    if e:
        return render_template("cadastro.html", erro2="usuario ja cadastrado")
    else:
        if senha == repetesenha:
            conn = sqlite3.connect(os.path.join(basedir, 'te.db'))
            c = conn.cursor()
            c.executescript("INSERT INTO pessoa(dre, nome, curso, senha, email) VALUES('" +
                            dre+"','"+nome+"','"+curso+"','"+senha+"','"+email+"')")
            c.executescript(
                "INSERT INTO user(email, senha) VALUES('"+email+"','"+senha+"')")
            conn.commit()
            return render_template("home.html", cr="cadastro realizado")
        else:
            return render_template("cadastro.html", erro1="Senhas não correspondentes")
'''verifica se o email não é cadastrado e se as senhas são iguais se estas condições forem 
satisfeitas retorna para a pagina de login com uma mensagem de cadastro realizado, se não retorna uma mensagem de acordo com 
o erro
'''

@app.route("/voltars", methods=["POST"])
def voltars():
    return render_template("salas.html")
#rota que retorna para a lista com as salas

@app.route("/cadastro", methods=["POST"])
def cadastro():
    return render_template("cadastro.html")
# direciona para a pagina para realizar o cadastro

@app.route("/sh323", methods=["POST"])
def salaH323():
    np = Sala().buscar_np(1)
    return render_template("sh323.html", n=np)
# retorna para o html da sala h323

@app.route("/sd206", methods=["POST"])
def salaD206():
    np = Sala().buscar_np(2)
    return render_template("sd206.html", n=np)
# retorna para o html da sala d206


@app.route("/sd216", methods=["POST"])
def salaD216():
    np = Sala().buscar_np(3)
    return render_template("sd216.html", n=np)
# retorna para o html da sala d216


@app.route('/sai/<int:id_s>', methods=('POST',))
def sai(id_s):
    temp = Sala().sair(id_s)
    print(temp)
    return render_template("vs.html")
#esta rota direciona para o html com uma mensagem de volte sempre e subtrai um do nùmero de pessoas da sala correspondente


@app.route('/entra/<int:id_s>', methods=('POST',))
def entra(id_s):
    temp = Sala().entrar(id_s)
    print(temp)
    return render_template("bv.html")
#esta rota direciona para o html com uma mensagem de bem vindo e soma um no nùmero de pessoas da sala correspondente

