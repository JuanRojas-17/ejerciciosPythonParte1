palabra1 = input("Ingrese su primer palabra: ")
palabra2 = input("Ingrese su segunda palabra: ")

len1 = len(palabra1)
len2 = len(palabra2)

if len1 > len2:
    diff = len1 - len2
    print("La palabra", palabra1, "tiene", diff, "letras mas que", palabra2)
elif len1 < len2:
    diff = len2 - len1
    print("La palabra", palabra2, "tiene", diff, "letras mas que", palabra1)
else:
    print("Las palabras son iguales")