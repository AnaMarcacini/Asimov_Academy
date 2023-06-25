#variavel como função

def soma_um(n):
    return n+1
f1 = soma_um

f1(1)

#função dentro de função

def soma_dois(n):
    def adiciona2(n):
        return n+2
    return adiciona2(n)


soma_dois(4)

#Funções como argumento
def devolve_funcao(funcao):
    numero_add = 5
    return funcao(numero_add)

devolve_funcao(soma_dois)

#funções retornando funções
def chama_funcao(p):
    def soma_um(n):
        return n+1
    def soma_dois(n):
        return n+2
    #match p:
    #    case 1:
    if p==1:
        return soma_um
    if p==2:
        return soma_dois
    
mais1 = chama_funcao(1)
mais2 = chama_funcao(2)

mais1 = chama_funcao(1)(1)
mais2 = chama_funcao(2)(1)


# decorador

def decorador_maiușculo(function):
    def wrapper():
        func = function ()
        cria_maiusculo = func.upper()
        return cria_maiusculo
    return wrapper
def diga_oi():
    return 'hello there'

funcao_decorada = decorador_maiușculo(diga_oi)
funcao_decorada()

#Maneira enxuta------------------
@decorador_maiușculo
def diga_tchau():
    return 'tchau there'
diga_tchau()