import random

# Escolhe um número secreto entre 1 e 100
numero_secreto = random.randint(1, 100)

# Número de tentativas permitidas
tentativas_restantes = 3

print("=" * 50)
print("BEM-VINDO AO JOGO: ACERTE O NÚMERO!")
print("=" * 50)
print("\nTente adivinhar o número secreto entre 1 e 100")
print(f"Você tem {tentativas_restantes} tentativas!\n")

# Loop principal do jogo
while tentativas_restantes > 0:
    print(f"Tentativas restantes: {tentativas_restantes}")
    
    # Solicita o palpite do usuário
    try:
        palpite = int(input("Digite seu palpite: "))
    except ValueError:
        print("Por favor, digite um número válido!\n")
        continue
    
    # Verifica se o usuário acertou
    if palpite == numero_secreto:
        print("\n" + "=" * 50)
        print("🎉 PARABÉNS! VOCÊ ACERTOU! 🎉")
        print(f"O número secreto era {numero_secreto}")
        print("=" * 50)
        break
    else:
        tentativas_restantes -= 1
        
        # Fornece dicas se ainda houver tentativas
        if tentativas_restantes > 0:
            if palpite < numero_secreto:
                print(f"❌ Errado! O número secreto é MAIOR que {palpite}\n")
            else:
                print(f"❌ Errado! O número secreto é MENOR que {palpite}\n")
        else:
            # Game Over
            print("\n" + "=" * 50)
            print("💀 GAME OVER! 💀")
            print(f"Suas tentativas acabaram!")
            print(f"O número secreto era {numero_secreto}")
            print("=" * 50)
