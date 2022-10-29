from tkinter import E
from flask_login import UserMixin
from .view import te


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


