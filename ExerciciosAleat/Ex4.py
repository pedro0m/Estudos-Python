tipo_cliente = input("Digite tipo de cliente: ")
compras = float(input("Digite valor total da compra: "))

if compras > 500:
    if tipo_cliente == "vip":
        desconto = compras * 0.2
        print(compras - desconto)
        
    elif tipo_cliente == "comun":
        desconto = compras * 0.1
        print(compras - desconto)
    else:
        print("Erro")
        
elif compras >= 200:
    if tipo_cliente == "vip":
        desconto = compras * 0.1
        print(compras - desconto)
        
    elif tipo_cliente == "comun":
        desconto = compras * 0.05
        print(compras - desconto)
    else:
        print('Erro')
else:
    desconto = 0
    print(compras - desconto)