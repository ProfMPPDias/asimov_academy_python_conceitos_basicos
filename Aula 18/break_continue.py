n = 0

while n < 10:
    print(f'O valor de n é {n}')
    n += 1
    if n == 5:
        break

print('Acabou o Loop!')

for n in range (-5, 6):
    if n == 0:
        continue
    resultado = 1 / n
    print(f'O resultado é: {resultado}')

while True:
    entrada = input('Digite um número (Digite "q" para sair): ')
    if entrada == 'q':
        break
    print(f'Você digitou: {entrada}')

while True:
    opt = input('Digite uma opção (1, 2) | (Digite "q" para sair): ')
    if opt == 'q':
        break
    elif opt != '1' and opt != '2':
        print('Opção inválida!')
        continue
    print(f'Opção selecionada: {opt}')

print('Programa Finalizado')