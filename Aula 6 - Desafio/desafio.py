nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
qntd_nome = len(nome)
idade_futuro = int(idade) + 5
print("Olá, " + nome + "! Você tem " + idade + " anos.")
print("Seu nome tem " + str(qntd_nome) + " letras.")
print("Em 5 anos, você terá " + str(idade_futuro) + " anos.")