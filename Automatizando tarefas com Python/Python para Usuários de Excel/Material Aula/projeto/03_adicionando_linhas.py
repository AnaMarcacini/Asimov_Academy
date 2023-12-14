from pathlib import Path
from datetime import datetime

import streamlit as st
import pandas as pd

pasta_datasets = Path(__file__).parent.parent / 'datasets'
df_vendas = pd.read_csv(pasta_datasets / 'vendas.csv', decimal=',', sep=';', index_col=0)
df_filiais = pd.read_csv(pasta_datasets / 'filiais.csv', decimal=',', sep=';')
df_produtos = pd.read_csv(pasta_datasets / 'produtos.csv', decimal=',', sep=';')

df_filiais['cidade/estado'] = df_filiais['cidade'] + '/' + df_filiais['estado']
lista_filiais = df_filiais['cidade/estado'].to_list()
filial_selecionada = st.sidebar.selectbox('Selecione a filial:',
                                            lista_filiais)

lista_vendedores = df_filiais.loc[df_filiais['cidade/estado'] == filial_selecionada, 'vendedores'].iloc[0]
lista_vendedores = lista_vendedores.strip('][').replace("'", '').split(', ')
vendedor_selecionado = st.sidebar.selectbox('Selecione o vendedor:',
                                            lista_vendedores)

lista_produtos = df_produtos['nome'].to_list()
produto_selecionado = st.sidebar.selectbox('Selecione o produto:',
                                            lista_produtos)

nome_cliente = st.sidebar.text_input('Nome do cliente')

genero_selecionado = st.sidebar.selectbox('Genêro do cliente:',
                                            ['masculino', 'feminino'])

forma_pag_selecionado = st.sidebar.selectbox('Forma de pagamento',
                                                ['credito', 'pix', 'boleto'])

if st.sidebar.button('Adicionar nova venda'):
    lista_adicionar = [df_vendas['id_venda'].max() + 1,
                       filial_selecionada,
                       vendedor_selecionado,
                       produto_selecionado,
                       nome_cliente,
                       genero_selecionado,
                       forma_pag_selecionado]
    df_vendas.loc[datetime.now()] = lista_adicionar
    df_vendas.to_csv(pasta_datasets / 'vendas.csv', decimal=',', sep=';')
    st.success('Venda adicionada')

st.dataframe(df_vendas, height=800)
