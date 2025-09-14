# Tabla de multiplicar
n = int(input("Ingresa un número para la tabla de multiplicar: "))
# Imprime la tabla de multiplicar del número dado
print("tabla de mulltiplicar del", n)
#   Bucle para multiplicar el número por los números del 1 al 10
for i in range(1, 11):
    # Calcula el resultado de la multiplicación
    resultado = n * i
    # Muestra el resultado en formato "n x i = resultado"
    print (n, "x", i, "=", resultado)
    # Fin del programa