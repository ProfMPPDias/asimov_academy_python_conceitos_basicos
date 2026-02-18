produtos = {
    'banana': 2.50,
    'maçã': 3.00,
    'laranja': 2.00,
    'uva': 4.00,
    'manga': 5.00,
}

print(produtos.get('maçã'))
print(produtos.get('banana'))
print(produtos.get('laranja'))
print(produtos.get('uva'))
print(produtos.get('manga'))
print(produtos.get('abacaxi', 'Produto não encontrado'))

# resultado = produtos.get('banana', 'Produto não encontrado')
# resultado = produtos.get('arroz')

# produtos.setdefault('arroz', 100)

for produto in produtos.keys(): 
    print(produtos)

for valor in produtos.values(): 
    print(valor)

for par in produtos.items(): 
    print(par)

for k, v in produtos.items(): 
    print(f'{k} -> {v}')

produtos = {
    'banana': 2.50,
    'maçã': 3.00,
    'laranja': 2.00,
    'uva': 4.00,
    'manga': 5.00,
}

novos_produtos = {
    'abacaxi': 10.00,
    'melancia': 20.00,
    'manga': 5.00,
}

produtos.update(novos_produtos)
print(produtos)

produtos = {
    'banana': 2.50,
    'maçã': 3.00,
    'laranja': 2.00,
    'uva': 4.00,
    'manga': 5.00,
}

produtos_copia = produtos.copy()
produtos_copia['morango'] = 3.30
print(produtos_copia)