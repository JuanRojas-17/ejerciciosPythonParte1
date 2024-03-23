num = int(input("Ingrese el primer numero: "))
divisor = int(input("Ingrese el divisor: "))

cociente = num // divisor 
resto = num%divisor

if resto == 0:
    print("Division exacta")
else:
    print("Division no exacta")

print("Cociente = ", cociente)
print("resto = ", resto)

