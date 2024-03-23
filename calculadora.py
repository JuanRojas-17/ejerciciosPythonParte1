print("--Bienvenido a la calculadora--")
input("Presione cualquier tecla para continuar")

num1 = int(input("Ingrese su primer numero real: "))
num2 = int(input("Ingrese su segundo numero real: "))

print("""

Estas son las operaciones disponibles:
      
      -suma
      -resta
      -multiplicacion
      -división

""")

operacion = input("Seleccione la operacion por favor: ")

if operacion == "suma":
    print("Su resultado es: ", num1 + num2)

elif operacion == "resta":
    print("Su resultado es: ", num1 - num2)

elif operacion == "multiplicacion":
    print("Su resultado es: ", num1 * num2)

elif operacion == "division":
    print("Su resultado es: ", num1 / num2)