import dash_bootstrap_components as dbc

from dash import html

import dash

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

server = app.server

app.layout = html.Div([
    dbc.Row([
        dbc.Button("Primary", color="primary", className="me-1"),
        dbc.Button("Secondary", color="secondary", className="me-1"),
        dbc.Button("Success", color="success", className="me-1"),
        dbc.Button("Warning", color="warning", className="me-1"),
        dbc.Button("Danger", color="danger", className="me-1"),
        # dbc.Button("Info", color="info", className="me-1"),
        dbc.Button("Light", color="light", className="me-1"),
        dbc.Button("Dark", color="dark", className="me-1"),
        dbc.Button("Link", color="link"),
        html.H1("Outline"),
        dbc.Button("Primary", outline=True, color="primary", className="me-1"),
        dbc.Button(
            "Secondary", outline=True, color="secondary", className="me-1"
        ),
        dbc.Button("Success", outline=True, color="success", className="me-1"),
        dbc.Button("Warning", outline=True, color="warning", className="me-1"),
        dbc.Button("Danger", outline=True, color="danger", className="me-1"),
        # dbc.Button("Info", outline=True, color="info", className="me-1"),
        dbc.Button("Light", outline=True, color="light", className="me-1"),
        dbc.Button("Dark", outline=True, color="dark"),
        dbc.Card(
            [
                dbc.CardImg(
                    src="https://s3.static.brasilescola.uol.com.br/be/2020/12/girassol.jpg",
                    top=True,
                    style={"opacity": 0.3},
                ),
                dbc.CardImgOverlay(
                    dbc.CardBody(
                        [
                            html.H4("Card title", className="card-title"),
                            html.P(
                                "An example of using an image in the background of "
                                "a card.",
                                className="card-text",
                            ),
                            dbc.Button("Go somewhere", color="primary"),
                        ],
                    ),
                ),
            ],
            style={"width": "18rem"},
        )
    ])


])

if __name__ == "__main__":
    app.run_server(port=8051, debug=True)


# https://dash-bootstrap-components.opensource.faculty.ai/docs/components/button/
