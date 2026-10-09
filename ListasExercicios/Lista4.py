'''
Exercício 1 - Escreva um programa que imprima todos os números inteiros de 1 a 15
utilizando o laço while.

numero = 0
while numero < 15:
    numero += 1
    print(numero)
'''
'''
Exercício 2 - Solicite ao usuário um número inteiro e exiba a tabuada desse número de 1 a
10 utilizando while.

numero = int(input("Digite um numero para tabuada: "))
x = 0

while x < 10:
    x += 1
    print(f"{numero} x {x} = {numero * x}")
'''
'''
Exercício 3 - Crie um programa que mantenha uma senha cadastrada python123. Peça ao
usuário para digitar a senha e continue solicitando até que a senha digitada seja igual à
cadastrada.

senha = "python123"

while True:
    acesso = input("Digite sua senha: ")
    if acesso == senha:
        break
'''
'''
Exercício 4 - Exiba todos os números pares de 2 até 20 na tela utilizando o laço while.

n = 2
while n < 20:
    n += 2
    print(n)
'''
'''
Exercício 5 - Faça um programa que leia números inteiros do usuário até que ele digite um
número negativo. Ao final, exiba a quantidade de números positivos/nulos digitados.

contador = 0

while True:
    numero = int(input("Digite um numero: "))
    contador += 1
    if numero < 0:
        print(contador-1)
        break
'''
'''
Exercício 6 - Desenvolva um programa que leia diversas notas de alunos. A leitura deve
ser encerrada quando o usuário digitar o valor -1 (sentinela). Ao final, o programa deve
exibir a quantidade total de notas lidas, a soma total e a média aritmética da turma.

contador = 0
total = 0

while True:
    nota = float(input("Digite uma nota: "))
    contador += 1
    if nota >= 0:
        total += nota
    else:
        print("Vezes:",contador-1)
        print("Soma:",total)
        print("Média:",total/contador)
        break
'''
'''
Exercício 7 - Crie um programa que comece com um saldo bancário de R$ 1.000,00.
Mostre um menu com as opções:
Verificar Saldo
Realizar Saque
Encerrar
O programa deve repetir até que a opção 3 seja escolhida. Caso o usuário tente sacar um
valor superior ao saldo disponível, exiba uma mensagem de erro e não efetue o saque.

saldo = 1000

while True:
    opcao = int(input("[1] Verificar Saldo\n[2] Realizar Saque\n[3] Encerrar\n"))
    if opcao == 1:
        print(f"R$ {saldo:.2f}")
    elif opcao == 2:
        saque = float(input("Quanto quer sacar?: "))
        if saque < 1:
            print("Digite um valor valido")
        elif saque < saldo:
            total = saldo - saque
            print("Saldo: ",total)
        else:
            print("Digite um valor que não seja superior ao saldo.")
    elif opcao == 3:
        break
    else:
        print("Digite uma opção valida\n")
'''