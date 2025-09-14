## Verifica si un número es primo
n = int(input("Ingresa un número: "))
# Inicializa la variable es_primo como True
es_primo = True
# Un número es primo si es mayor que 1 y no tiene divisores aparte de 1 y sí mismo
if n <= 1:
    # Si n es 1 o menor, no es primo
    es_primo = False
else:
    #   Inicializa el divisor a 2
    i = 2
    # Revisa si n tiene divisores desde 2 hasta la raíz cuadrada de n
    while i * i <= n:
        # Si n es divisible por i, entonces no es primo
        if n % i == 0: 
            # Cambia es_primo a False y sale del bucle
            es_primo = False

            break
        # Incrementa el divisor
        i += 1
if es_primo:
    # Muestra el resultado
    print(f"{n} es primo")
else:
    # Muestra el resultado
    print(f"{n} no es primo")
    # Fin del programa