

num1 = int(input("Ingrese su primer numero: "))
num2 = int(input("Ingrese su segundo numero: "))

suma = 0
for i in range(num1 + 1, num2):
    suma += i
print("La suma es", suma)
