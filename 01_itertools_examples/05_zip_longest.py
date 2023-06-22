from itertools import zip_longest

# Intial data
numbers = [1, 2, 3, 4, 5]
nombres = ['Camila', 'Ed', 'Jani']

print("Zip")
print(f"zip result = {list(zip(numbers, nombres))}")

print("Zip longest")
print(f"zip_longest = {list(zip_longest(numbers, nombres))}")