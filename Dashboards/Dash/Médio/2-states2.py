from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State

app = Dash(__name__)

app.layout = html.Div([
    dcc.Input(id='input-1-state', type='text', value='Montréal'),
    dcc.Input(id='input-2-state', type='text', value='Canada'),
    html.Button(id='submit-button-state', n_clicks=0, children='Submit'),
    html.Div(id='output-state')
])

#State -> elemento utilizado no callback mas que não gera o mesmo || apenas pega o estado do elemento
@app.callback(Output('output-state', 'children'),
              Input('submit-button-state', 'n_clicks'),#botão
              State('input-1-state', 'value'),#valor input 1
              State('input-2-state', 'value'))#valor input 2
def update_output(n_clicks, input1, input2):#
    return u'''
        The Button has been pressed {} times,
        Input 1 is "{}",
        and Input 2 is "{}"
    '''.format(n_clicks, input1, input2)


if __name__ == '__main__':
    app.run_server(debug=True)