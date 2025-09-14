# Adivina el número
import random  
# Bienvenid@ e instrucciones

print("Bienvenido al juego: Adivina el número")
#   Informa al usuario sobre el rango del número
print("Estoy pensando en un número entre 1 y 100...")
# Genera un número aleatorio entre 1 y 100

numero_secreto = random.randint(1, 100) 
# Inicializa el contador de intentos
intento = 0  
# Bucle principal del juego
while True:
    try:
        numero = int(input("Ingresa tu número: "))
        intento += 1
        # Verifica si el número está dentro del rango válido

        if numero < 1 or numero > 100:
            print("Por favor ingresa un número entre 1 y 100.")
            #     si el numero es menor que el número secreto
        elif numero < numero_secreto:
            print("Muy bajo. Intenta con un número más grande.")
            #   Si el numero es mayor que el número secreto
        elif numero > numero_secreto:
            print("Muy alto. Intenta con un número más pequeño.")
            # Si el usuario adivina el número
        else:
            print(f"Correcto. El número era {numero_secreto}.")
            print(f"Lo adivinaste en {intento} intentos.")
            break
    except ValueError:
        print("Ingresa un número válido, no texto.")
        # Fin del programa