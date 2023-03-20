import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)#criando a instancia de classe
app.layout=html.Div([
])

if __name__ == '__main__':
    app.run_server (debug=True)