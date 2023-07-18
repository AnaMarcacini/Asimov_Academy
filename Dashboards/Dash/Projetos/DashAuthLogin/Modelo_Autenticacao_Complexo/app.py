import dash
import dash_bootstrap_components as dbc
import sqlite3
from sqlalchemy import Table, create_engine
from sqlalchemy.sql import select

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin
import os
# import configparser

conn = sqlite3.connect('data.sqlite')
engine = create_engine('sqlite:///data.sqlite')
db = SQLAlchemy()
# config = configparser.ConfigParser()

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))
Users_tbl = Table('users', Users.metadata)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.QUARTZ])
server = app.server
app.config.suppress_callback_exceptions = True # retira erros de callback

server.config.update( # configurando o server de dash
    SECRET_KEY=os.urandom(12), # gernado uma chave aleatoria - segurança secret key - servidor ter informação de criptografia 
    SQLALCHEMY_DATABASE_URI='sqlite:///data.sqlite', # banco de dados
    SQLALCHEMY_TRACK_MODIFICATIONS=False) # não monitore as modificações SQLALCHEMY

db.init_app(server) # inicia o servidor

class Users(UserMixin, Users): # criando uma classe mais simples para interagir com o flask_login que herda as duas classes UserMixin - classe do flask_login (feita para que tudo funcione corretamente) e o nosso usuario
    pass

# Setup the LoginManager for the server
