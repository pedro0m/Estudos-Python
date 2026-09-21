'''
2.1) Dado idade = 25 e tem_ingresso = True,
verifique se a pessoa pode entrar no show (precisa ser maior de 18 E ter ingresso).
'''
'''
idade = 25
tem_ingresso = False

pode_entrar = idade >= 18 and tem_ingresso == True
print(pode_entrar)
'''
'''
2.2) Dado dia = "sábado" e tem_dinheiro = False, 
verifique se a pessoa vai sair (sai se for sábado OU domingo, E tiver dinheiro).
'''
'''
dia = 'sabado'
tem_dinheiro = False

vai_sair = (dia == 'sabado' or dia == 'domingo') and tem_dinheiro == True
print(vai_sair)
'''
'''
2.3) Peça dois números ao usuário e diga se ambos são positivos.
'''
'''
n1 = int(input(': '))
n2 = int(input(': '))

e_positivo = n1 > 0 and n2 > 0
print(e_positivo)
'''
'''
2.4) Peça a idade e diga se a pessoa NÃO é maior de idade usando not.
'''
'''
idade = int(input('idade: '))

nao_maior = not idade >=18
print(nao_maior)
'''
'''
2.5) Um aluno passa se: nota >= 7 E frequencia >= 75. Peça os dois valores e diga se passou.
'''
'''
nota = int(input('nota: '))
frequencia = int(input('frequencia: '))

passa = nota >= 7 and frequencia >= 75
print(passa)
'''
'''
2.6) Desafio: peça um número e diga se ele está entre 10 e 20 (inclusive). Use and.
'''
'''
num = int(input('numero: '))

entre = num >= 10 and num <= 20
print(entre)
'''
'''
2.7) O que será impresso? Explique.
a = 5
b = 10
print(a > 3 and b < 20)
print(a > 10 or b > 5)
print(not (a == 5))
print(a > 3 and b > 20 or a < 10)
'''
'''
Resposta:
1print: True
2print: True
3print: False
4print: True
'''
'''
2.8) Desafio lógico: um sistema libera acesso se o usuário for admin OU (moderador E ativo).
Peça as três variáveis booleanas e mostre o resultado.
'''
'''
usuarioadm = False
moderador = True
ativo = False

liberado = usuarioadm == True or (moderador == True and ativo == True )
print(liberado)
'''