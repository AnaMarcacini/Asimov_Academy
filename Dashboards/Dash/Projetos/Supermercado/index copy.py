# Bibliotecas DASH
import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template

# __________________________________________________________________________________________________________________________
# dcc - dash core components
#     interagir com os dados -> grande formulario ex slider dropdown menu etc - elementos | componentes para iteragir com o conjunto de dados
# __________________________________________________________________________________________________________________________
# dcc - dash HTML components
#     utilizar blocos de HTML para desenvolver

# Bibliotecas de tratamento de dados
import pandas as pd
import numpy as np

#from app import *
# Bibliotecas de graficos
import plotly.express as px
import plotly.graph_objects as go

load_figure_template("minty")

df_data = pd.read_csv("supermarket_sales.csv")
# formatando em formato de data
df_data["Date"] = pd.to_datetime(df_data["Date"])




app = dash.Dash(
    external_stylesheets=[dbc.themes.MINTY]
)
server = app.server

# df_data["City"].value_counts().index
# df_data["City"].index


# =========  Layout  =========== #
app.layout = html.Div(children=[
    dbc.Row([
        dbc.Col([
            dbc.Card([
                html.H2("Meu primeiro Dashboard ", style={"font-family":"Voltaire","font-size":"60px"}),
                html.H5("Cidades:"),
                dcc.Checklist(df_data["City"].value_counts().index,  # valores
                              # valores preveamente marcados
                              df_data["City"].value_counts().index,
                              id="check_city",
                              inputStyle={"margin-right":"5px","margin-left":"20px"}
                              ),
                html.H5("Variavel de analise:", style={"margin-top":"10px"}),

                dcc.RadioItems(["gross income", "Rating"],  # valores
                               "gross income",  # marcado por padrão
                               id="main_variable"
                               ) 
                    ],style={"height" : "90vh", "margin" : "20px", "pading":"20px"}),
        ], sm=2),
        dbc.Col([

            dbc.Row([
                dbc.Col([dcc.Graph(id="city_fig"),],sm=4),
                dbc.Col([dcc.Graph(id="gender_fig"),],sm=4),
                dbc.Col([dcc.Graph(id="pay_fig"),],sm=4),
            ]),
            dbc.Row([dcc.Graph(id="income_per_product_fig")]),
            dbc.Row([dcc.Graph(id="income_per_date_fig")]),
            
            
            
        ], sm=10),
    ])



])
# =========  Callbacks  =========== #


@app.callback(
    [
        Output("city_fig", "figure"),
        Output("pay_fig", "figure"),
        Output("gender_fig", "figure"),
        Output("income_per_date_fig", "figure"),
        Output("income_per_product_fig", "figure"),
    ],
    [
        Input("check_city", "value"),
        Input("main_variable", "value")
    ]
)
def render_graphs(cities, main_variable):
    # cities = ["Yangon",'Mandalay']
    # main_variable = "gross income"
    operation = np.sum if main_variable == "gross income" else np.mean
    df_filtered = df_data[df_data["City"].isin(cities)]
    df_city = df_filtered.groupby("City")[main_variable].apply(
        operation).to_frame().reset_index()
    df_gender = df_filtered.groupby(["Gender","City"])[main_variable].apply(
        operation).to_frame().reset_index()
    
    df_payment = df_filtered.groupby("Payment")[main_variable].apply(
        operation).to_frame().reset_index()
    df_product_income = df_filtered.groupby(["Product line", "City"])[
        main_variable].apply(operation).to_frame().reset_index()
    df_date_income = df_filtered.groupby("Date")[
        main_variable].apply(operation).to_frame().reset_index()

    fig_city = px.bar(df_city, x="City", y=main_variable)
    fig_gender = px.bar(df_gender, x="Gender", y=main_variable, color="City",barmode="group")
    fig_payment = px.bar(df_payment, y="Payment", x=main_variable)
    fig_product_income = px.bar(
        df_product_income, x=main_variable, y="Product line", color="City", orientation="h")
    fig_date_income = px.bar(df_date_income, x="Date", y=main_variable)


    for fig in [fig_city, fig_payment, fig_gender,fig_product_income,fig_date_income
]:
        fig.update_layout(margin=dict(l=0, r=0, t=20, b=20),                   height=200, template = "minty")
    return fig_city, fig_payment, fig_gender,fig_product_income,fig_date_income


# =========  Run server  =========== #

if __name__ == "__main__":
    app.run_server(port=8050, host='0.0.0.0', debug=True)


# Dash is running on http://0.0.0.0:8050/
