from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import pandas as pd

app = Dash(__name__)

df = pd.DataFrame({
  'student_id' : range(1, 11),
  'score' : [1, 5, 2, 5, 2, 3, 1, 5, 1, 5]
})

app.layout = html.Div([
	dcc.Dropdown(list(range(1, 6)), 1, id='score'),
	'Foi pontuado pela seguinte quantidade de estudantes:',
	html.Div(id='output'),
    dcc.Store(id='store')#div invisivel - guarda por sessão dataframes e variaveis 
])

@app.callback(Output('store', 'data'), Input('score', 'value'))
def update_output(value):
	global df
	#df = df[df['score'] == value] - não faça alteração de variaveis globais dentro de funções ou callbacks
	filtered_df = df[df['score'] == value]

	return filtered_df.to_dict()# dado pertinente apenas para o usuario - guardar informação
#to_dict - para dicionario

@app.callback(Output('output', 'children'), Input('store', 'data'))
def update_output(data):
	filtered_df = pd.DataFrame(data)#transfoma de volta em dataframe
	return len(filtered_df)


if __name__ == "__main__":
    app.run_server(debug=True)
    
	