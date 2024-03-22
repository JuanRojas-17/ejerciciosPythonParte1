def año(año_b):
    return (año_b%4==0 and año_b%100!=0) or (año_b%400==0)

año_b = int(input("Ingrese un año: "))

if año(año_b):
    print("Su año es bisiesto")
else:
    print("Su año no es bisiesto")