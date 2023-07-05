from functools import reduce

def add(a, b):
    print(f"{a=}, {b=}, result={a+b}")
    return a + b

data_list = [1, 2, 3, 4, 5, 6, 7]
result = reduce(add, data_list)

print(result)