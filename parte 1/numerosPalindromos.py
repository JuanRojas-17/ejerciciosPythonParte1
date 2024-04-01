num = input("Ingrese un numero: ")

pal = num[::-1]

if num == pal:
    print("Es un numero palindromo")
else:
    print("No es un numero palindromo")