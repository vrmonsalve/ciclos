# Fibonacci secuencia hasta n términos
n = int(input("Ingresa un número: "))
# Inicializa los primeros dos términos de la secuencia
a, b = 0, 1
# Imprime los primeros dos términos
print(a, b, end=" ")
# Calcula los siguientes términos de la secuencia
for i in range (2, n):
    # Suma los dos términos anteriores para obtener el siguiente término
    c= a + b
    # Imprime el siguiente término
    print(c, end=" ")
    # Actualiza los valores de a y b para el siguiente ciclo
    a, b = b, c
# Fin del programa