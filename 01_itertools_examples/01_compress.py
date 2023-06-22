from itertools import compress

nombres = ['Camila', 'Ed', 'Jani', 'Fatima', 'Santiago', 'Juan']
mens = [0, 1, 0, 0, 1, 1]
# mens = [False, True, False, False,  True, True]

# Filtra elementos de los datos que tengan un elemento correspondiente
# en los selectores que se evalúe como Verdadero.
# compress(data, sel)
compress_iter = compress(nombres, mens)
print(list(compress_iter))
