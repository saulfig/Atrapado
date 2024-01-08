income = float(input("Introduce el ingreso anual: "))

if income <= 85528:
	tax = income * 0.18 - 556.0
	print(tax)
# Escribe tu código aquí.
else :
    excedente = income - 85528
    tax = round(14839.2 + (excedente *0.32))

if tax < 0 :
    tax = 0.0
    
print("El impuesto es:", tax, "pesos")

# codigo del sandbox

income = float(input("Introduce el ingreso anual: "))

if income < 85528:
	tax = income * 0.18 - 556.02
else:
	tax = (income - 85528) * 0.32 + 14839.02

if tax < 0.0:
	tax = 0.0

tax = round(tax, 0)
print("El impuesto es:", tax, "pesos")
