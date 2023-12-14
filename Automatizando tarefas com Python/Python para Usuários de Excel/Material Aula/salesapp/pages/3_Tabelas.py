from pathlib import Path

import streamlit as st
import pandas as pd

from utilidades import leitura_de_dados

leitura_de_dados()

df_vendas = st.session_state['dados']['df_vendas']
df_filiais = st.session_state['dados']['df_filiais']
df_produtos = st.session_state['dados']['df_produtos']


def mostra_tabela_produtos():
    st.dataframe(df_produtos)

def mostra_tabela_filiais():
    st.dataframe(df_filiais)

def mostra_tabela_vendas():
    st.sidebar.divider()
    st.sidebar.markdown('### Filtrar tabela')
    colunas_selecionadas = st.sidebar.multiselect('Selecione as colunas da tabela:',
                                                  list(df_vendas.columns),
                                                  list(df_vendas.columns))
    col1, col2 = st.sidebar.columns(2)
    filtro_selecionada = col1.selectbox('Filtrar coluna',
                                        list(df_vendas.columns))
    valores_unicos_coluna = list(df_vendas[filtro_selecionada].unique())
    valor_filtro = col2.selectbox('Valor do filtro',
                                  valores_unicos_coluna)
    filtrar = col1.button('Filtrar')
    limpar = col2.button('Limpar')

    if filtrar:
        st.dataframe(df_vendas.loc[df_vendas[filtro_selecionada] == valor_filtro, colunas_selecionadas], height=800)
    elif limpar:
        st.dataframe(df_vendas[colunas_selecionadas], height=800)
    else:
        st.dataframe(df_vendas[colunas_selecionadas], height=800)




st.sidebar.markdown('## Seleção de Tabelas')
tabelas_selecionada = st.sidebar.selectbox('Selecione a tabela que você deseja ver:',
                                           ['Vendas', 'Produtos', 'Filiais'])

if tabelas_selecionada == 'Produtos':
    mostra_tabela_produtos()
elif tabelas_selecionada == 'Filiais':
     mostra_tabela_filiais()
elif tabelas_selecionada == 'Vendas':
     mostra_tabela_vendas()

