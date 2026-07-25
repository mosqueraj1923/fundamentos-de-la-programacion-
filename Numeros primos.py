numero = int(input("Ingrese un número entero positivo: "))

es_primo = True

if numero <= 1:
    es_primo = False
else:
    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False

if es_primo:
    print("El número es primo")
else:
    print("El número no es primo")