"""
Exemplos de for in
"""

"""
for i in range (1, 11):
    if i % 2 == 0:
        print(f'{i} é par')
    else:
        print(f'{i} é impar')
        continue
"""
"""
for horas in range(24):
    for m in range(60):
        for s in range(60):
            print(f'{horas:02}:{m:02}:{s:02}')
"""

for num in range(5, 51):
    if num % 5 == 0:
        print(num)
        continue