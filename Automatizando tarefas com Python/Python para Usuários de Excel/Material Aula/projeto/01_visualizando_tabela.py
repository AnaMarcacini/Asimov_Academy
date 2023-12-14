 from pathlib import Path

import streamlit as st
import pandas as pd

pasta_datasets = Path(__file__).parent.parent / 'datasets'
caminho_vendas = pasta_datasets / 'vendas.csv'
#st.write('qualquer coisa')
df_vendas = pd.read_csv(caminho_vendas, sep=';', decimal=',')

st.dataframe(df_vendas)


#streamlit run .\projeto\01_visualizando_tabela.py