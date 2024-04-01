print("----- Ecuacion de primer grado: ax + b = 0")

a = float(input("Ingrese 'a': "))

b = float(input("Ingrese 'b': "))

if a == 0:
    if b == 0:
        print("No hay solucion unica")
    else:
        print("Sin solucion")
else:
    solucion = -b / a
    print("Solucion unica =", solucion)