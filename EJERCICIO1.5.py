print("💲Bienvenido. Este es un cajero automatico💲")
saldo = 2000000
A = str(print("A.Consultar saldo"))
B = str(print("B.Consignar"))
C = str(print("C.Retirar"))
D = str(print("D.Salir"))
i = input("Seleccione una opción: ")

if i == "A":
    print("Su saldo es de:", saldo)

elif i == "B":
    val = int(input("seleccione la cantidad a consignar: "))
    consigna = saldo + val
    print("Dinero consignado con exito. Su saldo actual es de:", consigna)

elif i == "C":
    retiro = int(input("indique la cantidad a retirar: "))
    if retiro > saldo: 
        print("la cantidad a retirar supera su saldo actual, porfavor solicite una menor cantidad")
        retiro = int(input(""))

    else:
        consigna = saldo - retiro
        print("Retirando... su saldo actual es de:", consigna)

elif i == "D":
    print("Saliendo...")

else:
    print("Porfavor, indique alguna de las opciones en el menu")