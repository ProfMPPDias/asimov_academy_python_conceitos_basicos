capitais = {
    'Brasil': 'Brasilia',
    'Argentina': 'Buenos Aires',
    'Uruguai': 'Montevideo'
}

pais = 'Brasil'

if pais in capitais:
    print(f'A capital de {pais} é {capitais[pais]}')
else:
    print(f'Não sei a capital de {pais}')