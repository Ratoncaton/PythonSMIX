imp1 = 18 #% de impuesto
extFiscal = 556.02 #pesos
imp2 = 14839.02 #pesos de impuesto

ingreso = float(input("Ingrese el ingreso anual:"))

if ingreso < 85528:
    impuesto = ((imp1 * ingreso) / 100) - extFiscal

else:
    impuesto = imp2 + (((ingreso - 85528) * 32) / 100)

impuesto = round(impuesto, 2)

if impuesto < 0:
    impuesto = 0

print("El impuesto es: ", impuesto, "pesos")

