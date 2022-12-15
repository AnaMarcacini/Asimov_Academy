import os

PastaAtual = os.getcwd()

Pastas = set()
listaArquivos = os.listdir()


for item in listaArquivos:
    arquivos = item.split(".")
    #if item != "in.py" and item != "out.py":
    if len(arquivos)== 1:
        print(item)
        Conteudo_Pastas = os.listdir(PastaAtual + "/" + item)
        #print(Conteudo_Pastas)
        for arquivo in Conteudo_Pastas:
            endereco = os.path.join(PastaAtual, item)
            os.rename(os.path.join(endereco, arquivo),os.path.join(PastaAtual, arquivo))
        os.rmdir(item)



