valores = list(range(10))

maiores_que_cinco = []

for valor in valores:
    if valor > 5:
        maiores_que_cinco.append(valor + 10)

maiores_que_cinco = [
    valor + 10     # Resultado
    for valor in valores # Para cada ELEMENTO in SEQUÊNCIA
    if valor > 5] # Se CONDIÇÃO

print(valores)
print(maiores_que_cinco)
