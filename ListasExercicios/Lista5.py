'''
Exercício 1 - Escreva um programa que exiba os múltiplos de 5 no intervalo de 5 a 50

for i in range(5,51,5):
    print(i)
'''
'''
Exercício 2 - Escreva um programa que some de 1 a 100.

conta = 0
for i in range(1,101,1):
    conta += 1
    print(f"{i} + {conta} = {i+conta}")
'''
'''
Exercício 3 - Escreva um programa que conte as vogais de uma palavra

palavra = input("Digite uma palavra: ")
vogais = "aeiouAEIOU"
contador = 0

for letra in palavra:
    if letra in vogais:
        contador += 1
print(f"a palavra {palavra} tem {contador} vogais.")
'''
'''
Exercício 4 - Escreva um programa que exiba a tabuada do 7

conta = 0
for i in range(1,11):
    conta = 7
    print(f"{conta} x {i} = {i*conta}")
'''
'''
Exercício 5 - Escreva um programa que Inverta o texto de uma string usando o for.
Obs.: Não usar comandos prontos.

texto = input("Digite um texto: ")
inverte = ""
for i in texto:
    inverte = i + inverte
print(inverte)
'''
'''
Exercício 6 - Escreva um programa que exiba os números de 1 a 30 (exceto múltiplos de
3).

for i in range(1,31):
    if i % 3 == 0:
        print(i)
'''
'''
Exercício 7 - Usando o for escreva uma programa que procure um numero em uma lista e
exiba a posição onde o número foi encontrado ou exiba “o numero não foi encontrado”.
Obs.: Não usar comandos prontos.

lista = [1,2,3,4,5,6,7,8,9,10]
numero = int(input("Qual numero deseja procurar?: "))

for i in range(len(lista)):
    if lista[i] == numero:
        print(f"O numero {numero} está na posição {i}")
    else:
        print(f"O numero {numero} não foi encontrado.")
        break
'''
'''
Exercício 9 - Escreva um programa que exiba as tabuadas completas de 1 a 5 (usando
laços aninhados)

for i in range(1,6):
    for n in range(1,11):
        print(f"{i} x {n} = {i * n}")
    print("")
'''