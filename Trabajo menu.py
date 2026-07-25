import math
Bandera = True
while Bandera == True:
    print("¿Que desea hacer?")
    print("(1) Sumar")
    print("(2) Restar")
    print("(3) Multiplicar")
    print("(4) Dividir")
    print("(5) Potencia")
    print("(6) Salir")
    Desicion = int(input())
    if Desicion == int(1):
        print("Digite el primer numero a Sumar")
        Numero1 = int(input())
        print("Digite el segundo numero")
        Numero2 = int(input())
        Operacion = Numero1 + Numero2
        print("------------------")
        print(Operacion)
        print("------------------")
    if Desicion == int(2):
        print("Digite el primer numero a restar")
        Numero1 = int(input())
        print("Digite el segundo numero")
        Numero2 = int(input())
        Operacion = Numero1 - Numero2
        print("------------------")
        print(Operacion)
        print("------------------")
    if Desicion == int(3):
        print("digite el primer numero a multiplicar")
        Numero1 = int(input())
        print("Digite el segundo numero")
        Numero2 = int(input())
        Operacion = Numero1 * Numero2
        print("------------------")
        print(operacion)
        print("------------------")
    if Desicion == int(4):
        print("Digite el primer numero a dividir")
        Numero1 = int(input())
        print("Digite el segundo numero")
        Numero2 = int(input())
        Operacion = Numero1 / Numero2
        print("------------------")
        print(Operacion)
        print("------------------")
    if Desicion == int(5):
        print("Digite la base del numero")
        Numero1 = int(input())
        print("Digite el numero a elevar la base")
        Numero2 = int(input())
        Operacion = math.pow(Numero1, Numero2)
        print("------------------")
        print(Operacion)
        print("------------------")
    if Desicion == int(6):
        Bandera = False
    
print("Fin del menu")