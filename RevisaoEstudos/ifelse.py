'''
# Classificação de aluno

nota1 = float(input("Digite aqui a primeira nota: "))
nota2 = float(input("Digite aqui a segunda nota: "))
nota3 = float(input("Digite aqui a terceira nota: "))

faltas = int(input("Digite aqui quantas faltas: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 6 and faltas < 10:
    print("Aprovado")

elif media >= 5 and faltas < 5:
    print("Recuperação")

else:
    print("Reprovado")
'''
'''
# Caixa eletronico

valor_disponivel = 4000

print(f"Esse é o valor disponivel na sua conta: {valor_disponivel:.2f}")
valor_saque = float(input("Quanto deseja sacar?: "))

if valor_saque < 1:
    print("Digite um valor valido!")
elif valor_saque > valor_disponivel:
    print("Digite um valor valido!")
else:
    valor_sobra = valor_disponivel - valor_saque
    print(f"O saque de R$ {valor_saque:.2f} foi realizado com sucesso!")
    print(f"seu saldo atualizado é de R$ {valor_sobra:.2f}")
'''
'''
# Sistema de desconto

valor_compra = float(input("Qual o valor da compra?: "))
tipo_cliente = "VIP"

if tipo_cliente == "VIP":
    if valor_compra >= 200:
        desconto = 0.15 # 15%
        sub_total = desconto * valor_compra
        total = valor_compra - sub_total
    elif valor_compra >= 100:
        desconto = 0.1 # 10%
        sub_total = desconto * valor_compra
        total = valor_compra - sub_total
    else:
        desconto = 0
        sub_total = desconto * valor_compra
        total = valor_compra - sub_total

elif tipo_cliente == "Comum":
    if valor_compra >= 250:
            desconto = 0.15 # 15%
            sub_total = desconto * valor_compra
            total = valor_compra - sub_total
    elif valor_compra >= 150:
        desconto = 0.1 # 10%
        sub_total = desconto * valor_compra
        total = valor_compra - sub_total
    else:
        desconto = 0
        sub_total = desconto * valor_compra
        total = valor_compra - sub_total
else:
    desconto = 0
    sub_total = desconto * valor_compra
    total = valor_compra - sub_total

print(f"Valor original: {valor_compra:.2f}\nDesconto aplicado: {sub_total:.2f}\nValor final: {total:.2f}")
'''