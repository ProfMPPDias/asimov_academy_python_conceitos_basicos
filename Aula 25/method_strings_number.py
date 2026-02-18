x = 4.5

print(x.as_integer_ratio())

x = 38.125

print(x.as_integer_ratio())

arquivo = '2026_02_16_relatorio_vendas.csv'

print(arquivo.endswith('.csv'))

print(arquivo.endswith('.doc'))

print(arquivo.startswith('2026'))

print(arquivo.startswith('2023'))

if arquivo.startswith('2026') and arquivo.endswith('.csv'):
    print('Relatório de vendas encontrado')
else:
    print('Relatório não encontrado')

texto = 'Olá, mundo. Estou aprendendo Python na ASIMOV'

print(texto.count('a'))
print(texto.count('Python'))

seq = 'aaaaaaabaaaaaaaabbaaaaabaaa'

print(seq.find('b'))
print(seq.find('a'))
print(seq.find('c'))
print(seq.index('b'))
print(seq.index('a'))

print(seq[seq.find('b'):])

s1 = '37213213'

print(s1.isdigit())

s2 = 'ASDAASDdjisjlxz'
print(s2.isalpha())

s3 = 'Olá, 2026 Python!'
print(s3.isdigit())
print(s3.isalpha())

frase = 'Estou estudando Python!'
print(frase.replace('!', '?'))

linha = 'Item1'    'Item2'    'Item3'

print(linha.split())

linha = 'Item1;Item2;Item3'

print(linha.split(';'))

nomes = ['Maria', 'João', 'Pedro', 'Ana']

print(' ---- '.join(nomes))