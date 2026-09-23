'''s = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado']
c = len(s)-4
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

d = [7,8,19,34,28]
r_comprehension = [n ** 2 for n in d]
print(r_comprehension)