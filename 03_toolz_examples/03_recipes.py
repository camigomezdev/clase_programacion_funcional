from toolz import recipes

def iseven(n):
    return n % 2 == 0

# countby cuenta cuantos elementos
# cumple con la condición dada y cuantos no 
print(recipes.countby(iseven, [12, 123,
                                31, 1234,
                                4, 5, 6,
                                8, 10]))

# Crea una lista de tumplas agrupando
# por elementos que cumplen la condición dada
print(list(recipes.partitionby(iseven,
                               [12, 123,
                                31, 1234,
                                4, 5, 6,
                                8, 10])))

