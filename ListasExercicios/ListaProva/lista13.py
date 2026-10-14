'''
Exercício 1: gere uma lista contendo o quadrado de todos os 
números ímpares entre 1 e 15 usando List Comprehension.

lista = [impar ** 2 for impar in range(1, 16) if impar % 2 != 0]
print(lista)
'''
'''
Exercício 2: dada a lista linguagens = ["Python", "C", "JavaScript", "Java", "Go"], 
crie um dicionário usando Dict Comprehension no formato {nome_da_linguagem: tamanho_da_string}.

linguagens = ["Python", "C", "JavaScript", "Java", "Go"]

dicionario = {linguagem: len(linguagem) for linguagem in linguagens}
print(dicionario)
'''
'''
Exercício 3: dada a lista notas = [4.5, 8.0, 6.5, 9.0, 3.0], 
crie uma nova lista onde notas maiores ou iguais a 6.0 viram "Aprovado" e menores viram "Reprovado".

notas = [4.5, 8.0, 6.5, 9.0, 3.0]

maiores_notas = ["Aprovado" if nota >= 6 else "Reprovado" for nota in notas]
print(maiores_notas)
'''
'''
Exercício 4: dada uma lista nomes = ["Ana", "João", "Amanda", "Carlos", "Alberto"], 
filtre apenas os nomes que começam com a letra "A".

nomes = ["Ana", "João", "Amanda", "Carlos", "Alberto"]

nomes_a = [nome for nome in nomes if nome[0].lower() == 'a']
print(nomes_a)
'''
'''
Exercício 5: crie um dicionário para os números de 1 a 5 onde a 
chave é o próprio número e o valor é a string "Par" ou "Ímpar".

dicionario = {numero: "Par" if numero % 2 == 0 else "Impar" for numero in range(1,6)}
print(dicionario)
'''
'''
Exercício 6: dada a matriz [[1, 2, 3], [4, 5, 6], [7, 8, 9]], 
utilize uma comprehension aninhada para extrair 
todos os números pares em uma única lista unidimensional.

matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

pares = [item for linha in matriz for item in linha if item % 2 == 0]
print(pares)
'''
'''
Exercício 7: dada uma lista produtos = [{"nome": "Mouse", "preco": 80, "em_estoque": True}, 
{"nome": "Teclado", "preco": 150, "em_estoque": False}, 
{"nome": "Monitor", "preco": 900, "em_estoque": True}], 
gere uma lista apenas com o nome dos produtos que estão em estoque e custam mais de R$ 100.

produtos = [{"nome": "Mouse", "preco": 80, "em_estoque": True}, 
            {"nome": "Teclado", "preco": 150, "em_estoque": False}, 
            {"nome": "Monitor", "preco": 900, "em_estoque": True}]

lista = [item["nome"] for item in produtos if item["em_estoque"] and item["preco"] > 100]
print(lista)
'''
'''
Exercício 8: dado o dicionário paises = {"BR": "brasil", "US": "estados unidos", "FR": "frança"}, 
crie um novo dicionário invertendo chaves e valores, 
garantindo que o nome do país fique com a primeira letra maiúscula (.capitalize()).

Fiz na lista 10
novo_codigos = {}

for chave, valor in codigos.items():
    novo_codigos[valor] = chave
print(novo_codigos)

paises = {"BR": "brasil", "US": "estados unidos", "FR": "frança"}

novo = {chave.capitalize(): valor for valor,chave in paises.items()}
print(novo)
'''
'''
Exercício 9: dada a frase "Python é uma linguagem sensacional", 
crie uma lista com todas as consoantes presentes na frase 
(desconsiderando espaços e convertendo para minúsculas).

frase = "Python é uma linguagem sensacional"

lista = [letras for letras in frase.lower() if letras != " " if letras not in "aeéiou"]
print(lista)
'''
'''
Exercício 10: você recebeu uma matriz representando uma 
tabela de medições de sensores em 3 estações ao longo de 4 horários do dia:
medicoes = [
    [22.5, 25.0, 28.1, 21.0],  # Estação 1
    [18.0, 19.5, 21.2, 17.8],  # Estação 2
    [30.2, 31.5, 33.0, 29.8]   # Estação 3
]
Escreva um programa em Python usando exclusivamente comprehensions que:
Calcule a matriz transposta (trocando linhas por colunas, resultando em 4 linhas de 3 sensores cada).
Crie um dicionário no formato {"Horario_1": [temp1, temp2, temp3], ...} a partir da matriz transposta.
Filtre o dicionário gerando um novo 
dicionário contendo apenas os horários em que a temperatura média das 3 estações foi superior a 24°C.

medicoes = [
    [22.5, 25.0, 28.1, 21.0],  # Estação 1
    [18.0, 19.5, 21.2, 17.8],  # Estação 2
    [30.2, 31.5, 33.0, 29.8]   # Estação 3
]

transposta = [[linha[coluna] for linha in medicoes] for coluna in range(4)]
horarios = {f"Horario_{i + 1}": transposta[i] for i in range(len(transposta))}
filtar = {horario: temperaturas for horario, temperaturas in horarios.items()
            if (temperaturas[0] + temperaturas[1] + temperaturas[2]) / len(temperaturas) > 24}
'''