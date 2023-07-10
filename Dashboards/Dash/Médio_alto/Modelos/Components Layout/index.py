from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from app import app

from _components.component1 import *

app.layout = dbc.Container(
        children=[
            component1
        ], fluid=True, )



if __name__ == '__main__':
    app.run_server(debug=True)