X = [
    [1, 2, 3, 1],
    [4, 5, 6, 0],
    [7, 8, 9, -1]
]

Y = list(map(lambda i: list(map(lambda fila: fila[i], X)), range(len(X[0]))))

print("Matriz original (X):")
for fila in X:
    print(fila)
print("\nMatriz transpuesta (Y):")
for fila in Y:
    print(fila)
