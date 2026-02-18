tup = (0, 0, 0, 1, 0, 1, 0)
print(tup.index(1))

print(tup.count(0))

l1 = [0, 0, 1, 0, 1, 0]
l2 = l1.copy()
print(l2)

l1.clear()
print(l1)

for n in range(5):
    l1.append(n * 2)
print(l1)

l1.append('hello')
print(l1)

valores = [10, 30, -90, -1, 0, 1]
valores_positivos = []

for valor in valores:
    if valor > 0:
        valores_positivos.append(valor)
print(valores_positivos)

numeros = [1, 2, 3]
numeros.append([4, 5, 6])
print(numeros)

numeros = [1, 2, 3]
numeros.extend([4, 5, 6])
print(numeros)

numeros = [1, 2, 3]
novos_numeros = numeros + [4, 5, 6]
print(novos_numeros)

vogais = ['a', 'i', 'o', 'u']
vogais.insert(1, 'e')
print(vogais)

valores = [150, 20, 30, 40, 50]
valores_removido = valores.pop()
print(valores_removido)

valores = [150, 20, 30, 40, 50]
valores.pop(0)
print(valores)

clientes = ['xxx', 'yyy', 'zzz']
while clientes:
    cliente = clientes.pop()
    print(f'Processando cliente {cliente}')
print('Fila vazia')

valores = [150, 20, 30, 40, 50]
valores.reverse()
print(valores)

valores.sort()
print(valores)