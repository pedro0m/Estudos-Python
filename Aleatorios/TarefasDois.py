"""
1) Escreva um programa em Python que receba um número float x e verifique se ele está
estritamente entre 10 e 100 (sem incluir os extremos 10 e 100). Armazene o resultado em
uma variável booleana esta_no_intervalo e exiba o resultado.

x = float(input("Digite um número: "))
esta_no_intervalo = x > 10 and x < 100

print(esta_no_intervalo)
"""

"""
2)Dados dois números inteiros a e b, crie uma expressão booleana soma_par_e_maior que
retorne True apenas se a soma de a + b for um número par E o valor de a for estritamente
maior do que b.

a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
soma = a + b

somar_par_e_maior = soma % 2 == 0 and a > b

print(somar_par_e_maior)
"""

"""
3)Dada uma variável booleana chovendo e uma variável numérica temperatura (em °C),
construa a variável pode_passear que deve ser True quando NÃO estiver chovendo E a
temperatura for maior que 20 °C.

chovendo = False
temperatura = 10
pode_passear = chovendo == False and temperatura > 20

print(pode_passear)
"""
"""
4)Um cidadão tem direito à isenção de uma taxa se cumprir a seguinte regra de negócio:
● Ter renda mensal (renda) de até R$ 2.000,00 OU ser estudante cadastrado
(eh_estudante = True).
● ALÉM DISSO, ele NÃO pode ter dívidas ativas no sistema (tem_divida = False).
Escreva o código em Python declarando as variáveis de entrada e gerando a variável
isencao_aprovada.

renda = float(input('Qual sua renda mensal?: '))
eh_estudante = True
tem_divida = False
isencao_aprovada = (renda <= 2000 or eh_estudante == True) and not tem_divida

print(isencao_aprovada)
"""
"""
5) Um ano é considerado bissexto se cumprir a regra matemática:
1. É divisível por 4 E não é divisível por 100; OU
2. É divisível por 400.
Crie uma expressão booleana em Python armazenada na variável eh_bissexto que valide
um ano inteiro ano.

ano = 2028
eh_bissexto = (ano % 4 == 0 and not ano % 100 == 0) or ano % 400 == 0

print(eh_bissexto)
"""
"""
7) Uma conta de usuário é considerada segura e elegível para autenticação
avançada (acesso_seguro) se:
● O comprimento da senha (tam_senha) for maior ou igual a 8 caracteres.
● E tiver caractere especial (tem_especial = True).
● E o usuário for administrador (eh_admin = True) OU a conta tiver mais de 30 dias de
criação (dias_conta &gt; 30).

tam_senha = 8
tem_especial = True
eh_admin = True
dias_conta = 30
acesso_seguro = (tam_senha >= 8 and tem_especial == True) and (eh_admin == True or dias_conta > 30)

print(acesso_seguro)
"""
"""
8) Sem executar o código no interpretador Python, determine o valor booleano final
armazenado na variável resultado. Justifique o valor aplicando a ordem estrita de
precedência dos operadores.

Python
x = 8
y = 3
z = 2
w = True
resultado = not (x % y * z == 4) and (y ** z + x > 15 or not w)

Resposta: False
"""
"""
9) Um sistema financeiro automatizado aprova um empréstimo
(emprestimo_aprovado) se todas as exigências abaixo forem atendidas:
1. Renda mensal (renda) de pelo menos R$ 5.000,00 OU Score de crédito (score)
maior ou igual a 700.
2. Idade do solicitante (idade) entre 21 e 65 anos (inclusive).
3. O valor da prestação mensal (calculado por valor_emprestimo / parcelas) não pode
exceder 30% da renda mensal do solicitante.
Crie o script em Python que declare as entradas e monte a variável booleana final.

renda = float(input('Qual sua renda?: '))
score = int(input('Qual seu score?: '))
idade = int(input('Qual sua idade?: '))
valor_emprestimo = float(input('Quanto de emprestimo você deseja?: '))
parcelas = int(input('Em quantas parcelas?: '))
prestacao = valor_emprestimo / parcelas
emprestimo_aprovado = (renda >= 5000 or score >= 700) and (idade >= 21 and idade <= 65) and prestacao <= 0.30 * renda

print(emprestimo_aprovado)
"""
"""
10) Um servidor web autoriza o processamento de uma requisição de dados
(processar_requisicao) se:
● O usuário for autenticado (autenticado = True) E seu nível de acesso (nivel_acesso)
for maior ou igual a 3; OU se o usuário for um superusuário (super_usuario = True).
● E o servidor NÃO estiver sob ataque cibernético (sob_ataque = False) OU a
requisição vier de um IP da rede interna (ip_interno = True).
● E, por fim, a carga atual do processador (carga_cpu em porcentagem) for
estritamente menor que 90.0%.

autenticado = True
nivel_acesso = 3
super_usuario = True
sob_ataque = False
ip_interno = True
carga_cpu = 60.0

autorizacao_usuario = (autenticado and nivel_acesso >= 3) or super_usuario
seguranca_rede = (not sob_ataque) or ip_interno
sistema_estavel = carga_cpu < 90.0
processar_requisicao = autorizacao_usuario and seguranca_rede and sistema_estavel

print(processar_requisicao)
"""