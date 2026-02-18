def dizer_ola():
    print("Olá!")

dizer_ola()

produtos = {
    'banana': 1.50,
    'maçã': 2.00,
    'laranja': 1.00,
    'manga': 3.00,
    'uva': 4.00,
}

print(produtos.get('banana'))
print(produtos.get('maçã'))
print(produtos.get('laranja'))
print(produtos.get('manga'))
print(produtos.get('uva'))
print(produtos.get('pera'))