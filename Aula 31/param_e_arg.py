def somar_dois(n):
    return n + 2

x = 10

resultado = somar_dois(x)
print(resultado)

def adicionar_final(texto, final="!!!"):
    return texto + final

print(adicionar_final('Olá'))
print(adicionar_final('Olá', "!"))

def dividir(a, b):
    if b == 0:
        print("Erro: Divisão por zero!")
        return None
    return a / b

print(dividir(10, 5))
print(dividir(a=10, b=5))

def funcao_complexa(
    param_1=0, 
    param_2=0, 
    param_3=0,
):
    return param_1 + param_2 + param_3

print(funcao_complexa(param_3=10))