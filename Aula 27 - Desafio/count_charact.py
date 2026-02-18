# Programa para contar vogais em um texto

# Texto de exemplo
texto = """
Python é uma linguagem de programação de alto nível, interpretada de script, 
imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte. 
Foi lançada por Guido van Rossum em 1991.
"""

# Define as vogais (maiúsculas e minúsculas, incluindo acentuadas)
vogais = "aeiouAEIOUáéíóúÁÉÍÓÚàèìòùÀÈÌÒÙâêîôûÂÊÎÔÛãõÃÕäëïöüÄËÏÖÜ"

# Contador de vogais
contador = 0

# Percorre cada caractere do texto
for caractere in texto:
    if caractere in vogais:
        contador += 1

# Exibe o resultado
print(f"Texto analisado:")
print(texto)
print(f"\nNúmero total de vogais: {contador}")
