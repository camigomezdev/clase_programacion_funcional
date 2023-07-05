from itertools import cycle, product

# Intial data
nombres = ['Fatima', 'Ed', 'Jani']

print("-----------")
print("Cycle genera un ciclo infinito con los datos suministrados")
cycle_iter = cycle(nombres)

for x in range(20):
    print(next(cycle_iter))

# for name in cycle_iter:
#     print(name)

print("-----------")
print("Enumerate crea tuplas de cada" \
      "dato dado con un indice consecutivo")
for enum in enumerate(nombres, start=2):
    print(enum)

print("Product equivale a bucles for anidados"
      "en una expresión de generador.")
product_iter = product(range(3), nombres)
# product_iter = product(['a', 'b', 'x'], nombres)

for prod in product_iter:
    print(prod)
