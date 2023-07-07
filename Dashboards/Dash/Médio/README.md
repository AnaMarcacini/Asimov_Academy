https://dash-bootstrap-components.opensource.faculty.ai/


pip install dash-bootstrap-components


# EXEMPLO
import dash
import dash_bootstrap_components as dbc

app = dash.Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)

app.layout = dbc.Alert(
    "Hello, Bootstrap!", className="m-5"
)

if __name__ == "__main__":
    app.run_server()


https://dash.plotly.com/dash-core-components 

















