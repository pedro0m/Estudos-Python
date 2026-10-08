# imports
import random

# funcoes
def gerar_cpf():
    return "".join([str(random.randint(0, 9)) for _ in range(9)])

def gerar_subconjunto(conjunto):
    return set(random.sample(list(conjunto), random.randint(1, len(conjunto))))

# programa principal
conjunto = set()
while len(conjunto)<100:
    conjunto.add(gerar_cpf())

'''subconjunto = gerar_subconjunto(conjunto)
print("Conjunto:", conjunto)
print("Subconjunto:", subconjunto)'''
# TODO: agora é com você!

# Dicionario para armazenar os subconjuntos associados a cada esporte

sub_volei = gerar_subconjunto(conjunto)
sub_surf = gerar_subconjunto(conjunto)
sub_futebol = gerar_subconjunto(conjunto)
sub_judo = gerar_subconjunto(conjunto)

dicionario = {
    'Volei': sub_volei,
    'Surf': sub_surf,
    'Futebol': sub_futebol,
    'Judô': sub_judo
}

print(dicionario)

# Calcule a probabilidade de que uma pessoa sorteda aleatoriamente tenha assistido:
# 1. Judo ou Surfe
judo_surf = sub_judo.union(sub_surf)
probabilidade_1 = len(judo_surf) / len(conjunto)
# 2. Pelo menos dois esportes

# 3. Todos os esportes
# 4. Nenhum esporte