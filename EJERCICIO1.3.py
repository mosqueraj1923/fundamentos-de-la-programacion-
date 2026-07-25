lado1 = input("definal el lado 1: ")
lado2 = input("definal el lado 2: ")
lado3 = input("definal el lado 3: ")

if (lado1 + lado2 > lado3) and (lado2 + lado3 > lado1) and (lado1 + lado3 > lado2):
    print("el triangulo es valido")

    if lado1 == lado2 == lado1:
        print("es un triangulo equilatero")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("es un triangulo isosceles")
    else:
        print("es un triangulo escaleno")

else:
    print("no es posible crear un triangulo con los datos dados")