print("Digite una contraseña segura")
Contraseña = str(input())
i = 0
while True:
    print("Confirme su contraseña")
    Prueba = str(input())
    i = i + 1
    if Contraseña == Prueba:
        print("Acceso consedido")
        print("Sus itentos fueron", i)
        break
    else:
        print("Contraseña incorrecta")
        