'''s = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado']
c = len(s)-1
d = len(s)//2
print(s[c])
print(s[d])
# is the same result
'''

'''n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = n[::-1]

for p in range(len(n)-1,-1,-1):
    print(n[p])'''

'''num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

n = []
for p in range(len(num)-1,-1,-1):
    n.append(num[p])
print(n)'''


'''num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(len(num)):
    print(i+1)'''

'''d = [7,8,19,34,28]
r_comprehension = [n ** 2 for n in d]
print(r_comprehension)'''

'''l = ['banana', 'maça','melancia']
for p,fruta in enumerate(l):
    print(f'a fruta {fruta} esta na posição {p+1}')'''

'''n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(len(n)):
    n[i] = n[i] * 2
print(n)'''

'''n = []

for i in range(10):
    r = i+1*2
    n.append(r)
print(n)'''

'''pega o numero que acabou de ser adicionado. pega a pos dele e mult por *2'''

'''n = []

for i in range(1,11,1):
    n.append(i)
for b in range(1, len(n)):
    n[b] = n[b] * 2
print(n)'''

'''pega o numero que acabou de ser adicionado. pega a pos dele / e mult o numero por *2'''

'''n = []

for a in range(10):
    n.append(a+1)
    p = n.index(a+1)
    
print(n)'''

'''adiciona um numero na lista, pega a posição do numero que acabou de ser adicionado
pega o numero pela posição e multiplica por 2 e adiciona no mesmo lugar que estava antes
 e mostra a lista final'''

numero=[]
for indice in range(10):
    numero.append(indice+1)
    conta = numero[-1] * 2
    numero.insert(indice,conta)
    numero.pop(numero[-1])
print(numero)