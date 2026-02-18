minusculas = "abcdefghijklmnopqrstuvwxyz"
maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def cifra_cesar(texto, chave):
    resultado = ""
    for letra in texto:
        if letra in minusculas:
            indice = (minusculas.index(letra) + chave) % 26
            resultado += minusculas[indice]
        elif letra in maiusculas:
            indice = (maiusculas.index(letra) + chave) % 26
            resultado += maiusculas[indice]
        else:
            resultado += letra
    return resultado


texto = input("Digite o texto: ")
chave = int(input("Digite a chave: "))

print(f"Texto cifrado: {cifra_cesar(texto, chave)}")