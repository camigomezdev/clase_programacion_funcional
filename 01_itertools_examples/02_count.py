from itertools import count

# Funciona con range pero de forma infinita
count_iter = count(start=1, step=2)
print(next(count_iter))
print(next(count_iter))
print(next(count_iter))

print("Init for")
for i in count_iter:
    print(i)
    if i > 100:
        break

print("End for")
print(next(count_iter))
print(next(count_iter))
print(next(count_iter))