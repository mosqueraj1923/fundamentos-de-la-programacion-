print("Digite el nivel que quiere concer")
def pa(pack):
    if pack == 1:
        numero = 1
    else:
        numero = pack * pa(pack - 1)
    
    return numero

def recursividadFibonacci(n):
    if n <= 1:
        suma = n
    else:
        suma = recursividadFibonacci(n - 1) + recursividadFibonacci(n - 2)
    
    return suma

def recursividadModulo(x):
    if x < 10:
        suma = x
    else:
        suma = x % 10 + recursividadModulo(float(x) / 10)
    
    return suma

# Main
numero = int(input())
for i in range(1, numero + 1, 1):
    print(recursividadFibonacci(i))
