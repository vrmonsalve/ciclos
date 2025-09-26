 # Calcula el factorial de un número dado por el usuario
n = int(input("Ingresa un número: "))
# Inicializa el factorial en 1
factorial = 1
# Calcula el factorial usando un bucle for
for i in range(1, n + 1):
    # Multiplica el factorial por el número actual
    factorial *= i
# Muestra el resultado final.
print(f"El factorial de {n} es {factorial}")
# Fin del Programa.