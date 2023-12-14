from pathlib import Path

import streamlit as st
import pandas as pd

pasta_datasets = Path(__file__).parent.parent / 'datasets'
df_vendas = pd.read_csv(pasta_datasets / 'vendas.csv', decimal=',', sep=';', index_col=0)

colunas = list(df_vendas.columns)
colunas_selecionadas = st.sidebar.multiselect('Selecione as colunas:', colunas, colunas)


col1, col2 = st.sidebar.columns(2)
col_filtro = col1.selectbox('Selecione a coluna', [c for c in colunas if c not in ['id_venda']])
valor_filtro = col2.selectbox('Selecione o valor', list(df_vendas[col_filtro].unique()))

status_filtrar = col1.button('Filtrar')
status_limpar = col2.button('Limpar')

if status_filtrar:
    st.dataframe(df_vendas.loc[df_vendas[col_filtro] == valor_filtro, colunas_selecionadas], height=800)
elif status_limpar:
    st.dataframe(df_vendas[colunas_selecionadas], height=800)
else:
    st.dataframe(df_vendas[colunas_selecionadas], height=800)