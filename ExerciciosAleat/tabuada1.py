"""
t = int(input("Digite um número para ver a tabuada: "))
cont = 0

while cont != 10:
    cont += 1
    print(f'{cont} x {t} = {cont * t}'  )
"""

t = int(input("Digite um número para ver a tabuada: "))
cont = 0
cont2 = 11

while cont != 10 and cont2 != 1:
    cont += 1
    print(f'{cont} x {t} = {cont * t}')
    cont2 -= 1
    print(f'{cont2} x {t} = {cont2 * t}')      