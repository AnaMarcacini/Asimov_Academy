from dash import Dash, dash_table
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')

app = Dash(__name__)

app.layout = dash_table.DataTable(df.to_dict('records'), [{"name": i, "id": i} for i in df.columns])
# df.to_dict('records') - transforma o data frame numa lista de dicionarios

if __name__ == '__main__':
    app.run(debug=True)
