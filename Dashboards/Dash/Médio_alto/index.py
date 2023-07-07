import dash_bootstrap_components as dbc

from dash import html

import dash

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

server = app.server

app.layout = html.Div([
    dbc.Row([
#md dá a proporção da largura das colunas -- md medium display || sm - smal
        dbc.Col(html.Div("Column"), style={"background": "#EFF912"}, md =6, sm =3), 
        dbc.Col(html.Div("Column"),style={"background": "#ff0000"},md =3, sm =2), 
        dbc.Col(html.Div("Column"),style={"background": "#912321"},md =3, sm =2 ),
    ])


])

if __name__ == "__main__":
    app.run_server(port=8051, debug = True)