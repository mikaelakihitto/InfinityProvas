import functools

# Lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Função map() para obter uma nova lista com o quadrado de cada número
quadrados = list(map(lambda x: x**2,numeros))

# Função filter() para obter uma nova lista com números pares
pares = list(filter(lambda x: not x%2,numeros))

# Função reduce() para obter a soma de todos os números
soma_total = functools.reduce(lambda x,y: x+y,numeros)

# Resultados
print("Lista dos quadrados dos números:", quadrados)
print("Lista dos números pares:", pares)
print("Soma de todos os números:", soma_total)