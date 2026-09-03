lines = 50 * "="

print(f"{lines}\n Calculo de cagada remunerada \n{lines}")

horas = int(input('\nvc trabalha quantas horas por dia?: '))
escala = input('\nem qual escala vc trabalha?: ').lower()
tempo = int(input('\nquantos minutos foi sua cagada?: '))
salario = float(input('\nqual o seu salario?: '))

seisporum = 26
seteporzero = 30
cincopordois = 15

if escala == '6x1':
    v1 = horas * seisporum
    v2 = salario / v1
    v3 = v2 / 60
    v4 = v3 * tempo
    print(f'\nO valor da sua cagada foi de: R${v4:.2f}')

elif escala == '7x0':
    v1 = horas * seteporzero
    v2 = salario / v1
    v3 = v2 / 60
    v4 = v3 * tempo
    print(f'\nO valor da sua cagada foi de: R${v4:.2f}')

elif escala == '5x2':
    v1 = horas * cincopordois
    v2 = salario / v1
    v3 = v2 / 60
    v4 = v3 * tempo
    print(f'\nO valor da sua cagada foi de: R${v4:.2f}')

else:
    print('\nEscala invalida, tente novamente')