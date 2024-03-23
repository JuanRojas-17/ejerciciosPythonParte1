caracter = input("Ingrese su caracter unico: ")

if caracter.isalpha():
    if caracter.isupper():
        print("Es letra mayuscula")
    else:
        print("Es letra minuscula")
elif caracter.isdigit():
    print("Es numero")
else:
    print("No es letra ni numero")