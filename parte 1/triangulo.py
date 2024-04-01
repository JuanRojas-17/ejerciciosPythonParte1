a = float(input("Ingrese el lado a: "))
b = float(input("Ingrese el lado b: "))
c = float(input("Ingrese el lado c: "))

if a+b>c and a+c>b and b+c>a:
    if a==b==c:
        print("El triangulo es equilatero")
    elif a ==b or a == c or b==c:
        print("El triangulo es isosceles")
    else:
        print("El triangulo es escaleno")
else:
    print("No es un triangulo valido")