# sentencia break
print("Ejecucion de la sentencia:")

contador = 0

while contador < 20 :
    contador += 2
    
    if contador == 6 :
        break
    
    print("iteracion ejecutada con break break " , contador)


while contador < 20 :
    contador += 2
    
    if contador == 6 :
        continue
    
    print("iteracion ejecutada con break break " , contador)

    
