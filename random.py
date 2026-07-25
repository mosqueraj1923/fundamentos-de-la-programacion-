import random
Aleatorio = random.randint(1, 100)

print("Adivine el numero que se escogera al azar")
bandera = True
intentos = 1
print("Digite un numero")
while bandera == True:
    intentos = intentos + 1
    NumeroI = int(input())
    if NumeroI == Aleatorio:
        print("Has ganado")
        print(F"lo has conseguido en {intentos} intentos")
        Bandera = False
    elif NumeroI < Aleatorio:
        print("El numero es mas grande")
    else:
        print("El numero es menor")