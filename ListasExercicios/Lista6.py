'''
Exercício 1: Menu Interativo com Validação
Dicas:
1. Manter o programa rodando até o usuário decidir sair (while True).
2. Exibir o menu e ler a opção.
3. Decidir a ação com base no número inserido (if/elif/else).

while True:
    print("[1] Ver um numero\n[2] Sair")
    opcao = int(input(":"))
    if opcao == 1:
        print("3.14 ou pi")
    elif opcao == 2:
        break
    else:
        print("Digite uma opção valida.")
'''
'''
Exercício 2: Processamento e Estatísticas de Dados
Dica:
1. Ler a quantidade de elementos.
2. Ler os números acumulando a soma e atualizando maior/menor.
3. Calcular a média ao final.

elementos = [20,30,40]
soma = 0
maior = elementos[0]
menor = 0

for i in elementos:
    soma += i
    if i > maior:
        maior = i
    else:
        menor = i

media = soma // len(elementos)
print(soma)
print(maior)
print(menor)
print(media)
'''
'''
Exercício 3: Validador de Senha
Crie um programa que peça uma senha ao usuário. Se a senha digitada for 1234, exiba
"Acesso concedido" e encerre. Caso contrário, exiba "Senha incorreta" e peça novamente
até acertar.

senha = "1234"

while True:
    tentativa = input("Digite sua senha: ")
    if tentativa == senha:
        print("Acesso concedido")
        break
    else:
        print("Senha incorreta")
'''
'''
Exercício 4: Contador de Pares e Ímpares
Solicite ao usuário 5 números inteiros. Ao final, informe quantos eram pares e quantos eram
ímpares.

numeros = []

while len(numeros) < 5:
    n = int(input("Digite um numero: "))
    numeros.append(n)

par = 0
impar = 0
for i in numeros:
    if i % 2 == 0:
        par += 1
    else:
        impar += 1

print(f"A quantidade de numeros pares é de {par} e a de numeros impares é {impar}")
'''
