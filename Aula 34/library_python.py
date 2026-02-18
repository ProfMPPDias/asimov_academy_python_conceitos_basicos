import math
import datetime
import random
import os
import time

print(datetime.datetime.now())

agora = datetime.datetime.now()

ano_2000 = datetime.datetime(2000, 1, 1)

print(agora - ano_2000)

print(math.pi)
print(math.log(16, 2))

for _ in range(5):
    n = random.randint(1, 10)
    print(f'Número escolhido: {n}')

nomes = ['Ana', 'Bia', 'Carlos', 'Daniel', 'Elisa']

for _ in range(5):
    nome = random.choice(nomes)
    print(f'Nome escolhido: {nome}')

print(os.getcwd())
print(os.listdir())

inicio = time.time()

print('Primeira Linha')
time.sleep(3)
print('Segunda Linha')

final = time.time()

tempo_execucao = final - inicio
print(f'O programa levou {tempo_execucao:.3f} segundos para executar')