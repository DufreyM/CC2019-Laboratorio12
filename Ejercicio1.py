# Lista original de diccionarios
D = [
    {'make': 'Nokia', 'model': 216, 'color': 'Black'},
    {'make': 'Apple', 'model': 2, 'color': 'Silver'},
    {'make': 'Huawei', 'model': 50, 'color': 'Gold'},
    {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
]

# Pedimos al usuario la clave por la cual ordenar
key_to_sort = input("Ingrese la clave para ordenar (make/model/color): ")

# Ordenamos usando una función lambda
D_sorted = sorted(D, key=lambda x: x[key_to_sort])

# Mostramos el resultado
print("\nLista ordenada por la clave:", key_to_sort)
for item in D_sorted:
    print(item)
