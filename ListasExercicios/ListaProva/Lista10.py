'''
Exercício 1 Crie um dicionário representando um
livro com as chaves: "titulo", "autor" e "ano". Imprima o título e o ano acessando suas chaves

livro = {
    "titulo": "a volta dos que não foram",
    "autor": "joaozinho",
    "ano": 1989
}

print(livro["titulo"], livro["ano"])
'''
'''
Exercício 2 Dado o dicionário contato = {"nome": "Beatriz", "telefone": "9999-8888"}, 
adicione a chave "email" e altere o número de telefone para "9777-6666".

contato = {
    "nome": "Beatriz",
    "telefone": "9999-8888"
}
print(contato)

contato["email"] = "bea@email.com"
print(contato)
contato["telefone"] = "9777-6666"
print(contato)
'''
'''
Exercício 3 Dada a tabela de preços precos = {"arroz": 5.50, "feijao": 8.00}, 
verifique se a chave "café" existe. Se não existir, adicione-a com o valor 12.00.

precos = {"arroz": 5.50, "feijao": 8.00}

if "cafe" in precos:
    print(f"valor {precos["cafe"]}")
else:
    precos["cafe"] = 12.00
    print(precos)
'''
'''
Exercício 4 Dado o dicionário aluno = {"nome": "Pedro", "nota1": 8.0, "nota2": 6.5, "status": "Em curso"}, 
remova a chave "status" utilizando .pop() e imprima o valor removido.

aluno = {"nome": "Pedro", "nota1": 8.0, "nota2": 6.5, "status": "Em curso"}

remover = aluno.pop("status")

print(aluno)
print(remover)
'''
'''
Exercício 5 Dado o dicionário carro = {"marca": "Ford", "modelo": "Mustang", "ano": 1969}, 
imprima separadamente todas as chaves em uma linha e todos os valores em outra.

carro = {"marca": "Ford", "modelo": "Mustang", "ano": 1969}

for chave, valor in carro.items():
    print(chave, end=" ")

print()

for chave, valor in carro.items():
    print(valor, end=" ")
'''
'''
Exercício 6 Escreva um programa que receba um dicionário 
contendo nomes de alunos como chaves e listas de 3 notas como valores. 
O programa deve calcular e exibir a média final de cada aluno no formato "Aluno: Média".

alunos = {
    "Pedro": [7,9,5],
    "João": [5,6,10],
    "Maria": [9,2,7]    
}

for nome, nota in alunos.items():
    soma = nota[0] + nota[1] + nota[2]
    media = soma / 3
    print(f"Aluno: {nome}, Média: {media}")
'''
'''
Exercício 7  Dada a lista de tuplas
compras = [("fruta", "maçã"), ("limpeza", "sabão"), ("fruta", "banana"), ("limpeza", "detergente")], 
crie um dicionário onde as chaves sejam as categorias e os valores sejam listas contendo os 
produtos de cada categoria.

compras = [("fruta", "maçã"), ("limpeza", "sabão"), ("fruta", "banana"), ("limpeza", "detergente")]

dicionario = {}
lista1 = []
lista2 = []

for categoria, produto in compras:
    if categoria == "fruta":
        item = lista1.append(produto)
        dicionario[categoria] = lista1
    elif categoria == "limpeza":
        item = lista2.append(produto)
        dicionario[categoria] = lista2
    else:
        print("Inválido")
print(dicionario)
'''
'''
Exercício 8 Dado o dicionário codigos = {"BR": "Brasil", "US": "Estados Unidos", "FR": "França"}, 
crie um novo dicionário invertendo as chaves com os valores (ex.: {"Brasil": "BR", ...}).

codigos = {"BR": "Brasil", "US": "Estados Unidos", "FR": "França"}
novo_codigos = {}

for chave, valor in codigos.items():
    novo_codigos[valor] = chave
print(novo_codigos)
'''
'''
Exercício 9 Dada uma lista de funcionários representados por 
dicionários [{"nome": "Ana", "salario": 3500}, {"nome": "João", "salario": 1800}, ...], 
crie um programa que filtre e exiba apenas o nome dos funcionários com salário acima de 2500.

funcionarios = [{"nome": "Ana", "salario": 3500}, {"nome": "João", "salario": 1800}]

for funcionario in funcionarios:
    if funcionario["salario"] > 2500:
        print(funcionario["nome"])
'''
'''
Exercício 10 Escreva uma função em Python que receba um texto (string) 
qualquer e retorne uma tupla contendo dois dicionários:
O primeiro contendo a frequência de cada caractere individual (desconsiderando espaços).
O segundo contendo a frequência de cada palavra (convertida para minúsculas).
Ao final, o programa principal deve usar o resultado da função para 
imprimir a letra e a palavra mais frequentes do texto lido.

texto = input(": ")

caracteres = {}
palavras = {}
completo = (caracteres, palavras)

for caractere in texto:
    if caractere != " ":
        if caractere in caracteres:
            caracteres[caractere] += 1
        else:
            caracteres[caractere] = 1

for palavra in texto.split():
    palavra = palavra.lower()
    if palavra in palavras:
        palavras[palavra] += 1
    else:
        palavras[palavra] = 1

letras_quantidade = 0
letras_frequente = ""
for letra, qtd in caracteres.items():
    if qtd > letras_quantidade:
        letras_quantidade = qtd
        letras_frequente = letra

print(letras_frequente, letras_quantidade)

palavras_quantidade = 0
palavras_frequente = ""
for palavra, qtd in palavras.items():
    if qtd > palavras_quantidade:
            palavras_quantidade = qtd
            palavras_frequente = palavra

print(palavras_frequente, palavras_quantidade)
'''