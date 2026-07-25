print("declare la distancia en kilometro")
kilometro = int(input())
print("a que desea convertirlo?")
print("1. metro")
print("2. centimetro")
print("3. milla")
i = int(input())

if i == 1:
    me = kilometro*1000
    print("habiendolo convertido da como resultado"+ str(me))
elif i == 2:
    cm = kilometro*100000
    print("habiendolo convertido da como resultado" + str(cm))
else:
    if i== 3:
        milla = kilometro/1.6
        print("habiendolo convertido da como resultado" + str(milla))