"""
Aplicação Terminal - Desafios de Iteração
Autor: ASIMOV Academy - Curso Python
Aula 19 - Desafio
"""

def calcular_soma_e_media(numeros):
    """
    Calcula a soma e média de uma sequência de números sem usar sum()
    
    Args:
        numeros: lista de números
    
    Returns:
        tuple: (soma, media)
    """
    soma = 0
    for numero in numeros:
        soma += numero
    
    quantidade = len(numeros)
    media = soma / quantidade if quantidade > 0 else 0
    
    return soma, media


def encontrar_maior_valor(numeros):
    """
    Encontra o maior valor em uma sequência sem usar max()
    
    Args:
        numeros: lista de números
    
    Returns:
        float/int: maior valor da sequência
    """
    if len(numeros) == 0:
        return None
    
    maior = numeros[0]
    for numero in numeros:
        if numero > maior:
            maior = numero
    
    return maior


def filtrar_palavras_longas(palavras, tamanho_minimo=5):
    """
    Filtra e imprime palavras com pelo menos N caracteres
    
    Args:
        palavras: lista de palavras
        tamanho_minimo: quantidade mínima de caracteres (padrão: 5)
    """
    print(f"\nPalavras com pelo menos {tamanho_minimo} caracteres:")
    print("-" * 50)
    
    palavras_filtradas = []
    for palavra in palavras:
        if len(palavra) >= tamanho_minimo:
            palavras_filtradas.append(palavra)
            print(f"  • {palavra} ({len(palavra)} caracteres)")
    
    if len(palavras_filtradas) == 0:
        print(f"  Nenhuma palavra encontrada com {tamanho_minimo}+ caracteres")
    
    return palavras_filtradas


def menu_principal():
    """
    Exibe o menu principal e gerencia a navegação
    """
    while True:
        print("\n" + "=" * 60)
        print("  APLICAÇÃO DE ITERAÇÃO - DESAFIOS PYTHON")
        print("=" * 60)
        print("\n[1] Calcular Soma e Média de Números")
        print("[2] Encontrar Maior Valor")
        print("[3] Filtrar Palavras com 5+ Caracteres")
        print("[0] Sair")
        print("-" * 60)
        
        opcao = input("\nEscolha uma opção: ").strip()
        
        if opcao == "1":
            desafio_soma_e_media()
        elif opcao == "2":
            desafio_maior_valor()
        elif opcao == "3":
            desafio_filtrar_palavras()
        elif opcao == "0":
            print("\n👋 Encerrando aplicação. Até logo!")
            break
        else:
            print("\n❌ Opção inválida! Tente novamente.")


def desafio_soma_e_media():
    """
    Desafio 1: Calcular soma e média
    """
    print("\n" + "=" * 60)
    print("  DESAFIO 1: SOMA E MÉDIA")
    print("=" * 60)
    print("\nDigite os números separados por espaço (ex: 10 20 30 40)")
    
    entrada = input("Números: ").strip()
    
    try:
        numeros = [float(n) for n in entrada.split()]
        
        if len(numeros) == 0:
            print("\n⚠️  Nenhum número foi digitado!")
            return
        
        soma, media = calcular_soma_e_media(numeros)
        
        print("\n" + "-" * 60)
        print(f"📊 Sequência: {numeros}")
        print(f"➕ Soma: {soma}")
        print(f"📈 Média: {media:.2f}")
        print("-" * 60)
        
    except ValueError:
        print("\n❌ Erro! Digite apenas números válidos separados por espaço.")


def desafio_maior_valor():
    """
    Desafio 2: Encontrar maior valor
    """
    print("\n" + "=" * 60)
    print("  DESAFIO 2: MAIOR VALOR")
    print("=" * 60)
    print("\nDigite os números separados por espaço (ex: 15 42 8 23)")
    
    entrada = input("Números: ").strip()
    
    try:
        numeros = [float(n) for n in entrada.split()]
        
        if len(numeros) == 0:
            print("\n⚠️  Nenhum número foi digitado!")
            return
        
        maior = encontrar_maior_valor(numeros)
        
        print("\n" + "-" * 60)
        print(f"📊 Sequência: {numeros}")
        print(f"🏆 Maior valor: {maior}")
        print("-" * 60)
        
    except ValueError:
        print("\n❌ Erro! Digite apenas números válidos separados por espaço.")


def desafio_filtrar_palavras():
    """
    Desafio 3: Filtrar palavras com 5+ caracteres
    """
    print("\n" + "=" * 60)
    print("  DESAFIO 3: FILTRAR PALAVRAS")
    print("=" * 60)
    print("\nDigite as palavras separadas por espaço")
    print("(ex: Python programação código lista função)")
    
    entrada = input("\nPalavras: ").strip()
    
    if not entrada:
        print("\n⚠️  Nenhuma palavra foi digitada!")
        return
    
    palavras = entrada.split()
    
    print(f"\n📝 Total de palavras digitadas: {len(palavras)}")
    palavras_filtradas = filtrar_palavras_longas(palavras, 5)
    print(f"\n✅ Total de palavras filtradas: {len(palavras_filtradas)}")


if __name__ == "__main__":
    menu_principal()
