valores = [10, 20, 30, 3, -2, 20]

for valor in valores:
    print(f'O valor é {valor}')

print('Acabou o Loop!')

clientes = [
    ('Ana', 'xxx', 'xxx@gmail.com'), 
    ('Marcos', 'yyyy', 'yyyy@gmail.com')
] 

for cliente in clientes:
    nome = cliente[0]
    telefone = cliente[1]
    email = cliente[2]
    print(f'Nome: {nome}\n Telefone: {telefone}\n Email: {email}')
print('Acabou o Loop!')