import os

PastaAtual = os.getcwd()

Pastas = set()
listaArquivos = os.listdir()


for item in listaArquivos:
    arquivos = item.split(".")
    #if item != "in.py" and item != "out.py":
    if len(arquivos)== 1:
        print(item)
        Pastas.add(item)

print(Pastas)

for pasta in Pastas:
    Conteudo_Pastas = os.listdir(PastaAtual + "/" + pasta)
    #print(Conteudo_Pastas)
    for arquivo in Conteudo_Pastas:
        endereco = os.path.join(PastaAtual, pasta)
        os.rename(os.path.join(endereco, arquivo),os.path.join(PastaAtual, arquivo))
    os.rmdir(pasta)



