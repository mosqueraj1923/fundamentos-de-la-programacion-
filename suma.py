print("Suma de numeros enteros, termina al digitar (-1)")
i = 0
Bandera = True
Resultado = 0
while Bandera == True:
    Numero = int(input())
    i = i + 1
    if Numero == -1:
        print(f"La suma de sus numeros es: {Resultado + -1}")
        print(f"Su promedio es: {Promedio}")
        Bandera == False
    else:
        Resultado = Resultado + Numero
        Promedio = Resultado / i 