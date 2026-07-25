print("Digite el valor de su trangulo")
Nasteriscos = int(input())
i = 0
Bandera = True
while Bandera == True:
    if i == Nasteriscos:
        Bandera = False
    else:
        i = i + 1
        asterisco = str("*")
        procesos = i * asterisco
        print(procesos)
    
