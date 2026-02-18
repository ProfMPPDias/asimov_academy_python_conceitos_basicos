print('----- INÍCIO -----\n')

resposta1 = input('Estou com fome? (Digite "S" para SIM)')
if resposta1 == 'S':
    resposta2 = input('Tenho comida? (Digite "S" para SIM)')
    if resposta2 != 'S':
        print('Ir ao mercado')
        print('Voltar para casa')
    print('Preparar uma refeição')
    print('Comer a comida')

print('\n----- FIM -----\n')