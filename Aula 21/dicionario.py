capitais = {
    'Brasil': 'Brasilia',
    'Argentina': 'Buenos Aires',
    'Uruguai': 'Montevideo'
}

for pais in capitais:
    capital = capitais[pais]
    print(f'A capital de {pais} é {capital}')

d = dict()

d[10] = 'abc'
d['CHAVE'] = 5
d[3.15] = True

for k in d:
    v = d[k]
    print(f'Chave: {k} | Valor: {v}')