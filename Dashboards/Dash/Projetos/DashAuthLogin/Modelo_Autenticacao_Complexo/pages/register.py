from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from werkzeug.security import generate_password_hash
from dash.exceptions import PreventUpdate

from app import * # importa tudo do app - todas as importações do app.py

card_style = {
    'width': '300px',
    'min-height': '300px',
    'padding-top': '25px',
    'padding-right': '25px',
    'padding-left': '25px',
}



# =========  Layout  =========== #
def render_layout(message):
    message = "Ocorreu algum erro durante o registro." if message == "error" else message

    layout = dbc.Card([
                html.Legend("Registrar"),
                dbc.Input(id="user_register", placeholder="Username", type="text"),
                dbc.Input(id="pwd_register", placeholder="Password", type="password"),
                dbc.Input(id="email_register", placeholder="E-mail", type="email"),
                dbc.Button("Registrar", id='register-button'),
                html.Span(message, style={"text-align": "center"}),

                html.Div([
                    html.Label("Ou ", style={"margin-right": "5px"}),
                    dcc.Link("faça login", href="/login"),
                ], style={"padding": "20px", "justify-content": "center", "display": "flex"})

            ], style=card_style, className="align-self-center")
    return layout



# =========  Callbacks Page1  =========== #
@app.callback(
    Output('register-state', 'data'),
    Input('register-button', 'n_clicks'), 

    [State('user_register', 'value'), 
    State('pwd_register', 'value'),
    State('email_register', 'value')],
    )
def successful(n_clicks, username, password, email):
    if n_clicks == None: # se o botão não foi clicado - carregado na renderização da aplicação - chamada pelo dash
        raise PreventUpdate # termina a aplicação - não faz nada

    if username is not None and password is not None and email is not None:
        hashed_password = generate_password_hash(password, method='sha256') # codifica o codigo em sha256 - metodo de cryptografia
        ins = Users_tbl.insert().values(username=username,  password=hashed_password, email=email)# pega a tabela do banco de dados e insere os dados
        conn = engine.connect()# cria conexão
        conn.execute(ins)# salva no banco de dados
        conn.close() # fecha o banco de dados 
        print("TUDO OK NO REGISTRO")
        return ''
    else:
        return 'error'