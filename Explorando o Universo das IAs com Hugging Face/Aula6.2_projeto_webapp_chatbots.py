import os

import dotenv
import requests
import streamlit as st
from transformers import AutoTokenizer

dotenv.load_dotenv()
token = os.environ['HF_TOKEN']

modelos = {
    'mistralai/Mixtral-8x7B-Instruct-v0.1': '[/INST]',
    'google/gemma-7b-it': '<start_of_turn>model\n',
}

nome_modelo = st.selectbox('Selecione um modelo:', options=modelos)
token_modelo = modelos[nome_modelo]

url = f"https://api-inference.huggingface.co/models/{nome_modelo}"
tokenizer = AutoTokenizer.from_pretrained(nome_modelo)

if (
    'modelo_atual' not in st.session_state  # Primeira execução do programa
    or st.session_state['modelo_atual'] != nome_modelo  # Outro modelo escolhido
):
    # Reiniciar o chat e redefinir o nome do modelo atual
    st.session_state['mensagens'] = []
    st.session_state['modelo_atual'] = nome_modelo

mensagens = st.session_state['mensagens']

area_chat = st.empty()
pergunta_usuario = st.chat_input('Faça sua pergunta aqui: ')

if pergunta_usuario:
    mensagens.append({'role': 'user', 'content': pergunta_usuario})
    inputs = tokenizer.apply_chat_template(mensagens, tokenize=False, add_generation_prompt=True)
    json = {
        'inputs': inputs,
        'parameters': {'max_new_tokens': 1_000},
        'options': {'use_cache': False, 'wait_for_model': True},
    }
    headers = {
        'Authentication': f'Bearer {token}',
    }
    response = requests.post(url, json=json, headers=headers).json()
    resposta_chatbot = response[0]['generated_text'].split(token_modelo)[-1]
    print(resposta_chatbot)
    mensagens.append({'role': 'assistant', 'content': resposta_chatbot})

with area_chat.container():
    for mensagem in mensagens:
        chat = st.chat_message(mensagem['role'])
        chat.markdown(mensagem['content'])
