import dotenv #pip install python-dotenv
import os
#dotenv.find_dotenv() # retorna o endereço do .env
dotenv.load_dotenv(dotenv.find_dotenv())# carregando para a memoria as variaveis ||| como se fosse uma variavel de ambiente

print(os.getenv("senha"))
print(f'Minha senha é {os.getenv("senha")}')
print(f'postgresql://postgres:{os.getenv("senha")}@localhost:5432/asimov_academy')


# no arquivo .env localizado na raiz do projeto
#senha = "COLOQUE_A_SENHA"
