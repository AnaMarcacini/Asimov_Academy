from dash import html
import dash_bootstrap_components as dbc

from components import modal

layout = dbc.Container([
    dbc.Row([
    modal.layout,# pop up
        dbc.Col([
            dbc.Button("Home", href='/home', className='header_icon')
        ], md=1,xs=4), # ocupa 1 de 12 ---> extra small xs = 4 de 12
        dbc.Col([
            dbc.Button("Wallet", href='/wallet', className='header_icon')
        ], md=1,xs=4),
        dbc.Col([
            dbc.Button("Add", href='', id='add_button', className='header_icon')
        ], md=1,xs=4),
        html.Hr(style={'color' : 'rgba(255, 255, 255, 0.6)'})# linha divisora da linha do menu
    ], className='g-2 my-auto'),# do bootrap deixa os elementos espaçados e não se sobrepõem 

], fluid=True)# ocupar toda a tela