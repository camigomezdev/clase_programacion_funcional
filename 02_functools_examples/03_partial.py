from functools import partial

def multiply(x, y):
        return x * y

# create una funcion funcion que multiplica por 2
multiply_by_two = partial(multiply, 2)
print(multiply_by_two(4))
