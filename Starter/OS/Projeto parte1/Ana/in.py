import os

PastaAtual = os.getcwd()

tipos = set()
listaArquivos = os.listdir()


for item in listaArquivos:

    if item != "in.py" and item != "out.py":
        #print(item)
        tipo_Atual = item.split(".")[-1]
        tipos.add(tipo_Atual)
        #os.rename(item,tipo_Atual + "/" + item)

for tipo in tipos:
    print(tipo.upper())
    if tipo.upper() not in listaArquivos:
        os.mkdir(tipo.upper())

print(tipos)



for item in listaArquivos:
    retirar_Pastas = item.split(".")

    if len(retirar_Pastas)!= 1 and item != "in.py" and item != "out.py":
        print(item)
        tipo_Atual = item.split(".")[-1]
        tipo_Atual = tipo_Atual.upper()
        os.rename(item,tipo_Atual + "/" + item)
