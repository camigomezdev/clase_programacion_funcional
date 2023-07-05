from functools import singledispatch


@singledispatch
def add(a, b):
    raise NotImplementedError("Unsuported type")


@add.register(int)
def _(a, b):
    print("Type's argument:", type(a))
    return a + b


@add.register(list)
def _(a, b):
    print("Type's argument:", type(a))
    return sum(a) + sum(b)


print(add([3, 4, 5], [6, 5, 7]))
