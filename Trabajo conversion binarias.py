#el simbolo de (%) es el operador de modulo, sirve para que en ves del resultado de la division
#nos de el residuo
print("Digite el numero a decodificar")
i = int(input())
binario = ""
while i > 0:
        residuo = i % 2
        binario = str(residuo) + binario
        i = i // 2
        
print(f"Su numero en binario es {binario}") 
      