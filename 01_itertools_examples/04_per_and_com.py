from itertools import (
    combinations, permutations, combinations_with_replacement)

# Intial data
nombres = ['Eduardo', 'Jani', 'Fatima']

print(f"Permutaciones de {nombres}")
permutations_iter = permutations(nombres)
for per in permutations_iter:
    print(per)

print("-------------")
print(f"Combinaciones de {nombres}")
combinations_iter = combinations(nombres, 2)
for com in combinations_iter:
    print(com)

print("-------------")
print(f"Combinaciones con elementos repetidos de {nombres}")
com_with_replace = combinations_with_replacement(nombres, 2)
for com_w_r in com_with_replace:
    print(com_w_r)
