# Pega Inputs do Usuário
nome = input("Qual seu nome?\nDigite aqui: ")
idade = input("Qual a sua idade?\nDigite aqui: ")

# Variáveis Usuais
qntd_nome = len(nome)
idade_futuro = int(idade) + 5

# Exibe resultados do código
print('-' * 30)
print(f"Olá,{nome}! Você tem {idade} anos.")
print(f"Seu nome tem {str(qntd_nome)} letras.")
print(f"Em 5 anos, você terá {str(idade_futuro)} anos.")
print('-' * 30)