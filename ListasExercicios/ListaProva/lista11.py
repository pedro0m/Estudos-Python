'''
Exercício 1 Crie um conjunto chamado frutas contendo as seguintes 
frutas: "maçã", "banana", "laranja" e "maçã". Imprima o conjunto resultante e o 
número total de elementos.

frutas = {"maçã","banana","laranja","maçã"}

print(frutas, len(frutas))
'''
'''
Exercício 2 Dado o conjunto linguagens = {"Python", "Java", "C++"}, 
adicione a linguagem "JavaScript" utilizando o método .add() e 
tente adicionar novamente a linguagem "Python". Imprima o conjunto final.

linguagens = {"Python", "Java", "C++"}

linguagens.add("JavaScript")
linguagens.add("Python")
print(linguagens)
'''
'''
Exercício 3 Dado o conjunto numeros = {10, 20, 30, 40, 50}, 
verifique se o número 30 está presente no conjunto. Em seguida, 
verifique se o número 100 está presente. Imprima o resultado de ambas as verificações (Booleanos).

numeros = {10, 20, 30, 40, 50}

if 30 in numeros:
    print(True)
else:
    print(False)

if 100 in numeros:
    print(True)
else:
    print(False)
'''
'''
Exercício 4 Dado o conjunto alunos_presentes = {"Ana", "Bruno", "Carlos", "Daniela"}, 
remova o aluno "Bruno" utilizando o método .remove() ou .discard(). Imprima o conjunto atualizado.

alunos_presentes = {"Ana", "Bruno", "Carlos", "Daniela"}

alunos_presentes.remove("Bruno")
print(alunos_presentes)
'''
'''
Exercício 5 Dada a lista com elementos duplicados 
compras = ["pão", "leite", "pão", "ovos", "leite", "café"], 
converta essa lista em um conjunto para eliminar as duplicatas e, em seguida, 
converta-a de volta para uma lista. Imprima a lista final sem repetições.

compras = ["pão", "leite", "pão", "ovos", "leite", "café"]

compras_unico = set(compras)
compras_lista = list(compras_unico)
print(compras_lista)
'''
'''
Exercício 6 Dados os conjuntos de habilidades de dois desenvolvedores:
dev1 = {"Python", "SQL", "HTML"}
dev2 = {"Python", "JavaScript", "CSS"}
Crie um novo conjunto chamado todas_habilidades que contenha todas as 
habilidades dos dois desenvolvedores sem repetições.

dev1 = {"Python", "SQL", "HTML"}
dev2 = {"Python", "JavaScript", "CSS"}

todas_habilidades = dev1.union(dev2)
print(todas_habilidades)
'''
'''
Exercício 7  Dados os conjuntos de alunos matriculados em dois cursos diferentes:
curso_python = {"Ana", "Bruno", "Carla", "Daniel"}
curso_dados = {"Carla", "Daniel", "Eduardo", "Fernanda"}
Crie um conjunto chamado alunos_em_ambos contendo apenas os alunos que estão matriculados 
nos dois cursos ao mesmo tempo.

curso_python = {"Ana", "Bruno", "Carla", "Daniel"}
curso_dados = {"Carla", "Daniel", "Eduardo", "Fernanda"}

alunos_em_ambos = curso_python.intersection(curso_dados)
print(alunos_em_ambos)
'''
'''
Exercício 8 Dada a lista completa de convidados para um evento e o 
conjunto de pessoas que já confirmaram presença:
todos_convidados = {"Alice", "Bruno", "Caio", "Diana", "Eduardo"}
confirmados = {"Bruno", "Diana"}
Descubra quem ainda não confirmou presença no evento calculando a diferença entre os conjuntos.

todos_convidados = {"Alice", "Bruno", "Caio", "Diana", "Eduardo"}
confirmados = {"Bruno", "Diana"}

falta_confirmar = todos_convidados - confirmados
print(falta_confirmar)
'''
'''
Exercício 9 Dados dois conjuntos de preferências de produtos entre dois clientes:
cliente_A = {"Notebook", "Mouse", "Teclado", "Monitor"}
cliente_B = {"Notebook", "Headset", "Teclado", "Webcam"}
Encontre os produtos que pertencem a apenas um dos clientes 
(ou seja, produtos que não são comuns a ambos).

cliente_A = {"Notebook", "Mouse", "Teclado", "Monitor"}
cliente_B = {"Notebook", "Headset", "Teclado", "Webcam"}

incomum = cliente_A ^ cliente_B
print(incomum)
'''
'''
Exercício 10 Considere três conjuntos de dados de um serviço de streaming contendo 
e-mails de assinantes ativos, pessoas que clicaram em uma 
campanha promocional recente divulgada pelo serviço de streaming e pessoas que 
cancelaram a assinatura do streaming:
assinantes_ativos = ["ana@email.com", "bruno@email.com", "carla@email.com", "daniel@email.com", "ana@email.com"]
clicaram_email = {"carla@email.com", "daniel@email.com", "eduardo@email.com", "fernanda@email.com"}
cancelaram_recentemente = {"eduardo@email.com", "gabriel@email.com"}
Escreva um programa que responda às 4 perguntas seguintes:
Limpeza: converta a lista assinantes_ativos em um conjunto para remover eventuais e-mails duplicados.

Engajamento: descubra quais assinantes ativos demonstraram interesse abrindo o e-mail promocional

Reconquista: encontre os usuários que cancelaram recentemente e, 
apesar do cancelamento, abriram o e-mail, pois eles são os alvos ideais para uma oferta de retorno.

Potenciais clientes: identifique as pessoas que abriram o e-mail promocional, 
mas não são assinantes ativos e também não estão na lista de cancelados recentemente.

assinantes_ativos = ["ana@email.com", "bruno@email.com", "carla@email.com", "daniel@email.com", "ana@email.com"]
clicaram_email = {"carla@email.com", "daniel@email.com", "eduardo@email.com", "fernanda@email.com"}
cancelaram_recentemente = {"eduardo@email.com", "gabriel@email.com"}

limpeza = set(assinantes_ativos)
print(limpeza)
engajamento = limpeza.intersection(clicaram_email)
print(engajamento)
reconquista = cancelaram_recentemente.intersection(clicaram_email)
print(reconquista)
potenciais = limpeza.union(cancelaram_recentemente)
potenciais_clientes = clicaram_email - potenciais
print(potenciais_clientes)
'''