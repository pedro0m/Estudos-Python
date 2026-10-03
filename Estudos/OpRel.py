'''
BLOCO 1
'''
'''
1.1) Sem rodar, diga o resultado:

print(5 > 3 > 1) = False
print(1 < 2 < 3 < 4) = True
print(10 > 5 > 20) = False
print(3 < 5 == True) = False
print(2 == 2 == 2) = True
'''
'''
1.2) Sem rodar, diga o resultado:

print(1 == 1.0) = True
print("1" == 1) = False
print(True == 1) = True
print(True + True) = 2
print(False == 0) = True
print(True == 2) = False
'''
'''
1.3) Sem rodar, diga o resultado:

print("a" < "b") = True
print("A" < "a") = True
print("abc" < "abd") = False
print("Z" < "a") = True
print("banana" < "Banana") = False
'''
'''
1.4) Sem rodar, diga o resultado:

print(3 < 5 == True) = False
print((3 < 5) == True) = True
print(3 < (5 == True)) = False
'''

'''
BLOCO 2
'''

'''
2.1) Peça um número ao usuário e mostre True se ele estiver fora do intervalo [10, 20].
Restrição: use apenas uma comparação encadeada com or ou not.


numero = int(input('Digite um numero: '))

entreIntervalo = (numero >= 10 or numero <= 20)
print(entreIntervalo)
'''
'''
2.2) Peça três números e diga se o primeiro é o maior dos três.
Restrição: use só operadores relacionais (sem and/or explícito, se possível).

a = int(input('Digite um numero: '))
b = int(input('Digite outro numero: '))
c = int(input('Digite mais um numero: '))

eMaior = a > b > c
print(eMaior)
'''
'''
2.3) Peça uma string. Mostre True se a string estiver em ordem alfabética crescente (ex: "abc", "amor", "bcd").
Ex: "abc" → True, "acb" → False.
Restrição: não use sorted(). Compare caractere por caractere.

texto = input('Digite algo: ')

for i in range(len(texto)):
    ordem = texto[i] > texto[i-1]
print(ordem)
'''
'''
2.4) Peça uma data no formato dia, mês, ano (três inputs). Diga se a data é válida considerando:

Dia entre 1 e 31

Mês entre 1 e 12

Ano entre 1900 e 2100

Mostre apenas True ou False.
Restrição: use encadeamento de comparações (ex: 1 <= dia <= 31). entregou o exercicio kkkk

dia = int(input('Digite o dia: '))
mes = int(input('Digite o mes: '))
ano = int(input('Digite o ano: '))

validoDia = 1 <= dia <= 31
validoMes = 1 <= mes <= 12
validoAno = 1900 <= ano <= 2100

print(validoDia, validoMes, validoAno)
'''
'''
2.5) Peça a hora, minuto e segundo (três inteiros). Diga se é um horário válido (00:00:00 até 23:59:59).
'''