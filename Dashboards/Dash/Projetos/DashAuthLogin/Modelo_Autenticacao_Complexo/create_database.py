from sqlalchemy import Table, create_engine # conexão com o banco de dados
from sqlalchemy.sql import select
from flask_sqlalchemy import SQLAlchemy # flask backend do dash - importamos a classe SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash # senhas está correta cryptografado
import sqlite3
import warnings
import os
# import configparser
#pip3 install sqlalchemy flask_sqlalchemy flask_login werkzeug configparser

# Criando a conexão com o bd
conn = sqlite3.connect('data.sqlite')
engine = create_engine('sqlite:///data.sqlite')
db = SQLAlchemy()
# config = configparser.ConfigParser()

class Users(db.Model):# herda db.Model
    #criando a tabela de usuarios
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable = False)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))

Users_tbl = Table('users', Users.metadata)# metadata - atributo do db.model permitindo a criação da tabela pelos parametros passados a cima

#fuction to create table using Users class
def create_users_table():
    Users.metadata.create_all(engine)#cria tabela
create_users_table()



# import pandas as pd
# c = conn.cursor()
# df = pd.read_sql('select * from users', conn)
# df
