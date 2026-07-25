from email.mime import base


print("menu de figuras gometricas")
A = str(print("A. Area de un circulo"))
B = str(print("B. Area de un rectangulo"))
C = str(print("C. Area de un triangulo"))
D = str(print("D. perimetro de un cuadrado"))
E = str(print("E. Salir"))
i = input("que figura quiere desarrollar?: ")

if i == "A":
    radio = float(input("indique el radio del circulo: "))
    areaC = 3.14 * radio ** 2
    print("el area del circulo es:", areaC)

elif i == "B":
    base1 = float(input("indique la base del rectangulo: "))
    altura1 = float(input("indique la altura del rectangulo: "))
    areaRec = base1 * altura1
    print("el area del rectangulo es:", areaRec)

elif i == "C":
    base2 = float(input("indique la base del triangulo: "))
    altura2 = float(input("indique la altura del triangulo: "))
    areaT = base2*altura2/2
    print("el area de un triangulo es:", areaT)

elif i == "D":
    lado = float(input("indique el lado del cuadrado: "))
    peri = lado*4
    print("el perimetro del cuadrado es:", peri)
    

elif i == "E":
    print("Saliendo...")

else:
    print("no a indicado alguna de las opciones del menu")