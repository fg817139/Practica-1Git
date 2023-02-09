from random import randint
numeros_aleatorios = [randint(1,200)for _ in range(20)]
print(numeros_aleatorios)
numeros_aleatorios = filter(lambda n: n % 2 == 1, numeros_aleatorios)
print()
print(list(numeros_aleatorios))