#2 Deflnindo variáveis como funções
def soma_um (numero) :
    return numero+ 1



f1 = soma_um
f1(1)


#2 Definindo funções dentro de outras funções
def soma_um (numero):
    def adiciona_um (numero):
        return numero + 1
    return adiciona_um(numero)

soma_um(4)


#3 Passando funções como argumentos de outras funções
def soma_um (numero) :
    return numero+ 1
def function_call(function) :
    numero_to_add = 5
    return function(numero_to_add)

function_call(soma_um)

#4 Funçöes retornando outras funções
def funcao_ola():
    def diga_oi():
        return "Hi"
    return diga_oi
hello = funcao_ola()
hello()

## DECORADOR

def decorador_maiusculo ( function) :
    def wrapper () :
        func = function()
        cria_maiusculo = func. upper ()
        return cria_maiusculo
    return wrapper
def diga_oi() :
    return 'hello there'

funcao_decorada = decorador_maiusculo(diga_oi)
funcao_decorada ()

@decorador_maiusculo
def diga_oi() :
    return 'hello there'
diga_oi()