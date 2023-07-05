from toolz import itertoolz

print("-----------")
print("Accumulate")
def add(x,y):
    print(f"{x=}, {y=}, result={x*y}")
    return x*y
# Se parece a Reduce pero te entrega un iterador con
# los resultados de cada operación
print(list(itertoolz.accumulate(add, [8, 2, 3, 4])))


print("-----------")
print("Frecuencies")
fruit = ["banano", "uva", "fresa", "banano", "fresa", "fresa"]
print(itertoolz.frequencies(fruit))


print("-----------")
print("Iterate sobre un elemento no iterable")
def inc(x):  return x + 10
counter = itertoolz.iterate(inc, 0)
print(next(counter))
print(next(counter))
print(next(counter))


print("-----------")
print("Drop n cantidad de elementos")
print(list(itertoolz.drop(2, [10, 20, 30, 40, 50])))

