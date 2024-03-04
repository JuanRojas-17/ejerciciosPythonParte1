import math

numero = float(input("Ingrese un numero decimal:"))

decimal, _ = math.modf(numero)


print(decimal)