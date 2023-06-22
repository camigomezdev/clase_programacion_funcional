from toolz import functoolz


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    return x // y


def double(n):
    return n + n


print("---------")
print("Apply")
print(functoolz.apply(double, 2))

print("---------")
print("Juxt")
juxt_func = functoolz.juxt(add, sub, mul, div)
print(juxt_func)
print(juxt_func(8, 100))


print("-----------")
print("Flip")
print(functoolz.flip(div, 2, 6))

div_by_two = functoolz.flip(div, 2)
div_by_two(4)

juxt_w_flip = functoolz.juxt(
    add, functoolz.flip(sub), mul, functoolz.flip(div))
print(juxt_w_flip(10, 100))
