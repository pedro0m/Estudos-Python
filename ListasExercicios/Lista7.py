'''
Exercício 1 - Crie uma lista com os 7 dias da semana. Imprima o primeiro dia, o último dia
(usando índice negativo) e o dia do meio (4º dia).

semana = ["Domingo","Segunda","Terça","Quarta","Quinta","Sexta","Sabado"]
print(semana[0])
print(semana[-1])
print(semana[len(semana)//2])
'''
'''
Exercício 2 - Dada a lista numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], crie uma nova lista
contendo os elementos na ordem inversa utilizando slicing.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
inverter = numeros[::-1]
print(inverter)
'''
'''
Exercício 3 - Crie uma lista vazia chamada tarefas. Adicione três tarefas com append(). Em
seguida, remova a última tarefa inserida utilizando pop() e exiba a lista resultante.

tarefa = []
for indice in range(1,4):
    tarefa.append(input("Digite uma tarefa: "))
p = tarefa[-1]
tarefa.pop(tarefa.index(p))
print(tarefa)
'''
'''
Exercício 4 - Dada a lista vogais = ['a', 'e', 'i', 'o', 'u', 'a', 'a', 'e'],
use o método .count() para exibir quantas vezes a letra 'a' aparece.

vogais = ['a', 'e', 'i', 'o', 'u', 'a', 'a', 'e']
print(vogais.count('a'))
'''
'''
Exercício 5 - Dada a lista animais = ["gato", "cachorro", "pássaro"],
altere o valor de "pássaro" para "peixe" acessando seu índice diretamente.
'''
'''
Exercício 6 - Crie duas listas de números inteiros. Escreva um programa 
com laço for que gere uma terceira lista
contendo apenas os elementos que estão presentes em ambas as listas (sem duplicatas).

num1 = [1,2,3]
num2 = [3,4,5]

for i in num1:
    if i in num2:
        num3 = []
        num3.append(i)
print(num3)
'''