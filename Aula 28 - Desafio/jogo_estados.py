"""
Jogo dos Estados - Adivinhe as Capitais do Brasil
O jogador precisa responder o nome da capital de cada Estado do Brasil.
"""

def criar_dicionario_estados():
    """Retorna um dicionário com estados e suas capitais"""
    estados_capitais = {
        "Acre": "Rio Branco",
        "Alagoas": "Maceió",
        "Amapá": "Macapá",
        "Amazonas": "Manaus",
        "Bahia": "Salvador",
        "Ceará": "Fortaleza",
        "Distrito Federal": "Brasília",
        "Espírito Santo": "Vitória",
        "Goiás": "Goiânia",
        "Maranhão": "São Luís",
        "Mato Grosso": "Cuiabá",
        "Mato Grosso do Sul": "Campo Grande",
        "Minas Gerais": "Belo Horizonte",
        "Pará": "Belém",
        "Paraíba": "João Pessoa",
        "Paraná": "Curitiba",
        "Pernambuco": "Recife",
        "Piauí": "Teresina",
        "Rio de Janeiro": "Rio de Janeiro",
        "Rio Grande do Norte": "Natal",
        "Rio Grande do Sul": "Porto Alegre",
        "Rondônia": "Porto Velho",
        "Roraima": "Boa Vista",
        "Santa Catarina": "Florianópolis",
        "São Paulo": "São Paulo",
        "Sergipe": "Aracaju",
        "Tocantins": "Palmas"
    }
    return estados_capitais


def normalizar_texto(texto):
    """Remove acentos e converte para minúsculas para comparação"""
    import unicodedata
    texto = texto.strip().lower()
    # Remove acentuação
    texto_normalizado = ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )
    return texto_normalizado


def jogar():
    """Função principal do jogo"""
    import random
    
    estados_capitais = criar_dicionario_estados()
    estados = list(estados_capitais.keys())
    random.shuffle(estados)  # Embaralha a ordem das perguntas
    
    acertos = 0
    total_perguntas = 0
    
    print("=" * 50)
    print("BEM-VINDO AO JOGO DOS ESTADOS DO BRASIL!")
    print("=" * 50)
    print("\nVocê será perguntado sobre as capitais dos estados.")
    print("Após cada pergunta, você pode escolher continuar ou parar.")
    print("\nVamos começar!\n")
    
    for estado in estados:
        capital_correta = estados_capitais[estado]
        
        # Faz a pergunta
        print(f"Qual a Capital do Estado {estado}?")
        resposta = input("Sua resposta: ")
        
        total_perguntas += 1
        
        # Verifica se a resposta está correta (comparação sem acentos)
        if normalizar_texto(resposta) == normalizar_texto(capital_correta):
            print(f"✓ CORRETO! A capital de {estado} é {capital_correta}.\n")
            acertos += 1
        else:
            print(f"✗ ERRADO! A capital de {estado} é {capital_correta}.\n")
        
        # Pergunta se quer continuar (exceto na última pergunta)
        if total_perguntas < len(estados):
            continuar = input("Deseja continuar? (s/n): ").strip().lower()
            print()
            
            if continuar != 's':
                print("Você escolheu parar o jogo.\n")
                break
    
    # Mostra o resultado final
    print("=" * 50)
    print("FIM DO JOGO!")
    print("=" * 50)
    print(f"\nVocê respondeu {total_perguntas} pergunta(s).")
    print(f"Acertos: {acertos}")
    print(f"Erros: {total_perguntas - acertos}")
    
    if total_perguntas > 0:
        percentual = (acertos / total_perguntas) * 100
        print(f"Percentual de acertos: {percentual:.1f}%")
    
    print("\nObrigado por jogar!")
    print("=" * 50)


if __name__ == "__main__":
    jogar()