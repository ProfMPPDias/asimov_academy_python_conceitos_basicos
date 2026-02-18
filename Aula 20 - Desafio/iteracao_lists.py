"""
Aplicação Python Terminal - Comparação de Listas
Encontra elementos duplicados entre duas listas e verifica se há elementos em comum.
"""

def encontrar_duplicados(lista1, lista2):
    """
    Encontra todos os elementos que aparecem em ambas as listas.
    
    Args:
        lista1: Primeira lista
        lista2: Segunda lista
    
    Returns:
        Lista com elementos duplicados (sem repetição)
    """
    # Converte para sets e encontra a interseção
    duplicados = list(set(lista1) & set(lista2))
    return duplicados


def main():
    print("=" * 60)
    print("COMPARADOR DE LISTAS - ENCONTRAR ELEMENTOS DUPLICADOS")
    print("=" * 60)
    print()
    
    # Exemplo 1: Listas com elementos em comum
    lista1 = [1, 2, 3, 4, 5, 6, 7]
    lista2 = [5, 6, 7, 8, 9, 10]
    
    print("Exemplo 1:")
    print(f"Lista 1: {lista1}")
    print(f"Lista 2: {lista2}")
    print()
    
    duplicados = encontrar_duplicados(lista1, lista2)
    
    if duplicados:
        print(f"✓ Existem elementos em comum entre as listas!")
        print(f"Elementos duplicados: {sorted(duplicados)}")
    else:
        print("✗ Não existem elementos em comum entre as listas.")
    
    print()
    print("-" * 60)
    print()
    
    # Exemplo 2: Listas sem elementos em comum
    lista3 = [1, 2, 3, 4]
    lista4 = [5, 6, 7, 8]
    
    print("Exemplo 2:")
    print(f"Lista 1: {lista3}")
    print(f"Lista 2: {lista4}")
    print()
    
    duplicados2 = encontrar_duplicados(lista3, lista4)
    
    if duplicados2:
        print(f"✓ Existem elementos em comum entre as listas!")
        print(f"Elementos duplicados: {sorted(duplicados2)}")
    else:
        print("✗ Não existem elementos em comum entre as listas.")
    
    print()
    print("-" * 60)
    print()
    
    # Exemplo 3: Listas com strings
    lista5 = ["python", "java", "javascript", "c++"]
    lista6 = ["javascript", "ruby", "python", "go"]
    
    print("Exemplo 3 (com strings):")
    print(f"Lista 1: {lista5}")
    print(f"Lista 2: {lista6}")
    print()
    
    duplicados3 = encontrar_duplicados(lista5, lista6)
    
    if duplicados3:
        print(f"✓ Existem elementos em comum entre as listas!")
        print(f"Elementos duplicados: {sorted(duplicados3)}")
    else:
        print("✗ Não existem elementos em comum entre as listas.")
    
    print()
    print("=" * 60)
    print()
    
    # Modo interativo - permite ao usuário inserir suas próprias listas
    print("MODO INTERATIVO")
    print("=" * 60)
    resposta = input("Deseja inserir suas próprias listas? (s/n): ").strip().lower()
    
    if resposta == 's':
        print()
        print("Insira os elementos separados por vírgula (ex: 1,2,3,4)")
        
        entrada1 = input("Lista 1: ").strip()
        entrada2 = input("Lista 2: ").strip()
        
        # Tenta converter para números, se não conseguir, mantém como strings
        try:
            lista_user1 = [int(x.strip()) for x in entrada1.split(',')]
            lista_user2 = [int(x.strip()) for x in entrada2.split(',')]
        except ValueError:
            lista_user1 = [x.strip() for x in entrada1.split(',')]
            lista_user2 = [x.strip() for x in entrada2.split(',')]
        
        print()
        print(f"Lista 1: {lista_user1}")
        print(f"Lista 2: {lista_user2}")
        print()
        
        duplicados_user = encontrar_duplicados(lista_user1, lista_user2)
        
        if duplicados_user:
            print(f"✓ Existem elementos em comum entre as listas!")
            print(f"Elementos duplicados: {sorted(duplicados_user)}")
        else:
            print("✗ Não existem elementos em comum entre as listas.")
    
    print()
    print("Programa finalizado!")


if __name__ == "__main__":
    main()
