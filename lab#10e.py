c0 = int(input("Ingrese un numero :"))
pasos = 0
while c0 != 1:
    if c0 % 2 == 0:
        c0 = round(c0 / 2)
        print(c0)
        pasos += 1
    else:
        
        c0 = round(3 * c0 + 1)
        print(c0)
        pasos += 1
        
print("pasos:" , pasos)
