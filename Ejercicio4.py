# --------------------------------------------------------------
# Autor: Leonardo Mejía
# Curso: Teoría de la Computación
# Laboratorio No. 12
# Ejercicio 4 
# --------------------------------------------------------------

colores = ['rojo', 'verde', 'azul', 'amarillo', 'gris', 'blanco', 'negro']
borrar = ['amarillo', 'café', 'blanco']

resultado = list(filter(lambda x: x not in borrar, colores))
print("Lista original:", colores)
print("Elementos a borrar:", borrar)
print("Lista resultante:", resultado)
