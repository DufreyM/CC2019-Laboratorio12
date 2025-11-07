

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

n = int(input("Ingrese la potencia n: "))
resultado = list(map(lambda x: x ** n, numeros))

print("Lista original:", numeros)
print(f"Lista elevada a la potencia {n}:", resultado)
