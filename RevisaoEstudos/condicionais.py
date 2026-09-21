'''
3.1) Peça ao usuário um número inteiro. O programa deve dizer se o número é par ou ímpar,
e se é positivo, negativo ou zero. As duas informações devem aparecer separadas.

num = int(input('Digite um número: '))
impar_ou_par = 'par' if num % 2 == 0 else 'impar'
pos_ou_neg = 'positivo' if num > 0 else 'negativo'

print(f'Seu número é {impar_ou_par} e é {pos_ou_neg}')
'''

'''
3.2) Peça três números e imprima o maior deles.

num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
num3 = int(input('Terceiro número: '))

if num1 > num2 > num3:
    print(num1)
elif num2 > num3 > num1:
    print(num2)
else:
    print(num3)
'''

'''
3.3) Um cinema cobra ingressos assim:

Menores de 12 anos: R$ 15

De 12 a 17 anos: R$ 25

De 18 a 59 anos: R$ 40

60 anos ou mais: R$ 20

Peça a idade e mostre o valor do ingresso.

idade = int(input('Digite sua idade: '))
valor_ingresso = 15

if idade <= 12:
    print(f'Seu ingresso fica R$ {valor_ingresso}')
elif idade > 12 and idade <= 17:
    print(f'Seu ingresso fica R$ {valor_ingresso + 10}')
elif idade > 17 and idade <= 59:
    print(f'Seu ingresso fica R$ {valor_ingresso + 25}')
else:
    print(f'Seu ingresso fica R$ {valor_ingresso + 5}')
'''

'''
3.4) Peça o login e a senha do usuário. O sistema libera acesso se:
Login for "admin" E senha for "1234", OU
Login for "user" E senha for "abcd"
Caso contrário, nega. Mostre uma mensagem personalizada 
para cada caso ("Bem-vindo, admin!", "Bem-vindo, user!", "Acesso negado").
'''