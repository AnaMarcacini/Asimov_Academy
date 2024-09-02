from bs4 import BeautifulSoup  
# !pip install lxml
# !pip3 install beautifulsoup4
with open('asimov_ex.html', 'r') as file:
    conteudo = file.read()
    print(conteudo)                      
    
    # ex = BeautifulSoup(conteudo, 'lxml')    # O segundo elemento é o parse que nada mais é do que transformar de um tipo 1 para outro tipo 2 Nesse caso estamos transformando o código HTML para string, utilizando uma lxml
ex = BeautifulSoup(conteudo,  "html.parser")
print(ex)

print(ex.prettify())      # Aqui temos a identação exata

tags = ex.find('p') # Esse código só vai retornar a primeira situação do 'p'

all_tags = ex.find_all('p') # retorna todos os ps
print(all_tags)
    
print("______________________")

for p in all_tags:
        print(p.text)