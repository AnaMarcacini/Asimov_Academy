import dash_bootstrap_components as dbc

from dash import html

import dash

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

card_content = [
    dbc.CardHeader("Card header"),
    dbc.CardBody(
        [
            html.H5("Card title", className="card-title"),
            html.P(
                "This is some card content that we'll reuse",
                className="card-text",
            ),
        ]
    ),
]

server = app.server

app.layout = html.Div([
    dbc.Row([
#md dá a proporção da largura das colunas -- md medium display || sm - smal
        dbc.Col([
            dbc.Card(card_content,color="primary",inverse=True, style={"height" : "90vh", "margin":"10px"}),]
            , sm =3), 
        dbc.Col([
            dbc.Row([
                dbc.Col(dbc.Card(card_content,color="info",inverse=True,style={"height" : "40vh"}),md =4),
                dbc.Col(dbc.Card(card_content,color="info",inverse=True,style={"height" : "40vh"}), md =4)
            ]),
            dbc.Row([
                dbc.Col( dbc.Card(card_content,color="erro"),md=4),
                dbc.Col( dbc.Card(card_content,color="erro"),md=4),
                dbc.Col( dbc.Card(card_content,color="erro"),md=4),
            ])
    ]), 
    ])


])

if __name__ == "__main__":
    app.run_server(port=8051, debug = True)