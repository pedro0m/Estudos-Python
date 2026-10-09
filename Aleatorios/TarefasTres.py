"""
Exercício 1
Escreva um programa que receba a temperatura em graus Celsius de uma cidade e exiba
uma mensagem segundo os critérios:
● Menor que 15 °C: "Frio"
● De 15 °C a 25 °C (inclusive): "Agradável"
● Maior que 25 °C: "Quente"

graus = int(input('Quantos graus está?: '))
if graus <= 15:
    print('Frio')
elif graus > 15 and graus <= 25:
    print('Agradável')
else:
    print('Quente')
"""
"""
Exercício 2
Dado o código abaixo escrito com a estrutura tradicional if/else, reescreva-o em uma única
linha utilizando o operador ternário:
Python
status_conta = "Ativa"
pontos = 120
if pontos >= 100:
nivel = "VIP"
else:
nivel = "Padrão"

status_conta = "Ativa"
pontos = 120
nivel = "VIP" if pontos >= 100 else "Padrão"

print(nivel)
"""
"""
Exercício 3
Crie um programa que leia uma letra referente ao turno em que um aluno estuda: M
(Matutino), V (Vespertino) ou N (Noturno). Exiba a mensagem correspondente ("Bom Dia!",
"Boa Tarde!", "Boa Noite!") ou "Valor Inválido!" caso seja inserida qualquer outra letra.

periodo = input('Qual perido você estuda?: ')

if periodo == "m":
    print('Bom dia!')
elif periodo == "v":
    print('Boa Tarde!')
elif periodo == "n":
    print('Boa noite!')
else:
    print('Valor inválido')
"""
"""
Exercício 4
Desenvolva um programa que receba três valores numéricos referentes aos lados A, B e C.
1. Primeiro, verifique se os lados formam um triângulo válido (A + B > C, A + C > B e
B + C > A).
2. Caso seja um triângulo válido, classifique-o em:
○ Equilátero: Todos os três lados iguais.
○ Isósceles: Quaisquer dois lados iguais.
○ Escaleno: Todos os três lados diferentes.
3. Se não formar um triângulo, exiba "Os lados não formam um triângulo válido".

a = int(input('Digite um número: '))
b = int(input('Digite um número: '))
c = int(input('Digite um número: '))

if (a + b > c and a + c > b and b + c > a):

    if a == b == c:
        print('Equilátero')
    elif a == b or a == c or b == c:
        print('Isóloceles')
    else:
        print('Escaleno')

else:
    print("Os lados não formam um triângulo válido")
"""
"""
Exercício 5
Um sistema de folha de pagamento aplica alíquotas de imposto sobre o salário bruto
segundo as faixas:
● Até R$ 2.112,00: Isento (0%)
● De R$ 2.112,01 até R$ 2.826,65: 7,5%
● De R$ 2.826,66 até R$ 3.751,05: 15,0%
● De R$ 3.751,06 até R$ 4.664,68: 22,5%
● Acima de R$ 4.664,68: 27,5%
Escreva um script em Python que calcule e exiba o valor do desconto do imposto e o salário
líquido final.

salario = float(input('Qual seu sálario?: '))

if salario <= 2112.00:
    print(f'Isento {salario} R$ ')
elif salario > 2112.00 <= 2826.66:
    calculo = salario * 0.075
    print(f'Seu sálario recebeu o desconto de {calculo} R$ e passou a ser {salario + calculo} R$ ')
elif salario > 2826.66 <= 3751.05:
    calculo = salario * 0.075
    print(f'Seu sálario recebeu o desconto de {calculo} R$ e passou a ser {salario + calculo} R$ ')
elif salario > 3751.05 <= 4664.68:
    calculo = salario * 0.225
    print(f'Seu sálario recebeu o desconto de {calculo} R$ e passou a ser {salario + calculo} R$ ')
else:
    calculo = salario * 0.275
    print(f'Seu sálario recebeu o desconto de {calculo} R$ e passou a ser {salario + calculo} R$ ')
"""
"""
Exercício 6
Um posto está vendendo combustíveis com a seguinte tabela de descontos:
● Álcool ('A'):
○ Até 20 litros: desconto de 3% por litro.
○ Acima de 20 litros: desconto de 5% por litro.
● Gasolina ('G'):
○ Até 20 litros: desconto de 4% por litro.
○ Acima de 20 litros: desconto de 6% por litro.

Considere o preço fixo de R$ 4,00 para o litro do Álcool e R$ 5,50 para a Gasolina. Escreva
um programa que leia a quantidade de litros e o tipo de combustível ('A' ou 'G') e informe o
valor total a ser pago.
"""
"""
tipo = input('Digite Combustivel: ').lower()
litros = int(input('Digite quantos Litros: '))

if tipo == 'a':
    preco = 4
    desconto = 0.03 if litros <= 20 else 0.05
elif tipo == 'g':
    preco = 5.5
    desconto = 0.04 if litros <= 20 else 0.06
else:
    preco = 0
    desconto = 0

if preco > 0:
    subtotal = litros * preco
    total = subtotal - desconto
    print(f'R${total:.2f}')

else:
    print('Tipo Inválido')
"""