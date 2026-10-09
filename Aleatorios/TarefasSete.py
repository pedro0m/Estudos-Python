'''Exercício 1 - Crie uma lista com os 7 dias da semana. Imprima o primeiro dia, o último dia
(usando índice negativo) e o dia do meio (4º dia).

semana = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado']
print(f' {semana[0], semana[-1], semana[3]} ')
'''

'''Exercício 2 - Dada a lista numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], crie uma nova lista
contendo os elementos na ordem inversa utilizando slicing.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros = numeros[::-1]
print(numeros)
'''

'''Exercício 3 - Crie uma lista vazia chamada tarefas. Adicione três tarefas com append(). Em
seguida, remova a última tarefa inserida utilizando pop() e exiba a lista resultante.

tarefas = []
for i in range (1,4,1):
    addtarefa = input('Digite uma tarefa: ')
    tarefas.append(addtarefa)
tarefas.pop(-1)
print(tarefas)
'''

'''Exercício 4 - Dada a lista vogais = ['a', 'e', 'i', 'o', 'u', 'a', 'a', 'e'],
 use o método .count() para exibir quantas vezes a letra 'a' aparece.

vogais = ['a', 'e', 'i', 'o', 'u', 'a', 'a', 'e']
print(f'Tem {vogais.count('a')} Ás ')
'''

'''Exercício 5 - Dada a lista animais = ["gato", "cachorro", "pássaro"],
 altere o valor de "pássaro" para "peixe" acessando seu índice diretamente.

animais = ["gato", "cachorro", "pássaro"]
pos = animais.index('pássaro')
animais[pos] = 'peixe'
print(animais)
'''

