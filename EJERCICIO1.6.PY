Nota1 = int(input("indique de 1-100 la calificacion numero 1: "))
Nota2 = int(input("indique de 1-100 la calificacion numero 2: "))
Nota3 = int(input("indique de 1-100 la calificacion numero 3: "))
Nota4 = int(input("indique de 1-100 la calificacion numero 4: "))
Nota5 = int(input("indique de 1-100 la calificacion numero 5: "))

promedio = (Nota1 + Nota2 + Nota3 + Nota4 + Nota5) / 5

print(promedio)

if promedio >= 60:
    print("Usted ha aprovado")

elif promedio < 60:
    print("Usted ha reprovado")

mayor = Nota1

if Nota2 > mayor:
    mayor = Nota2

if Nota3 > mayor:
    mayor = Nota3

if Nota4 > mayor:
    mayor = Nota4

if Nota5 > mayor:
    mayor = Nota5

print("La nota mas alta es:", mayor)


menor = Nota1

if Nota2 < menor:
    menor = Nota2

if Nota3 < menor:
    menor = Nota3

if Nota4 < menor:
    menor = Nota4

print("La nota mas baja es:", menor)