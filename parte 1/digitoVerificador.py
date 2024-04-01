rol = input("Ingrese el rol: ")

rolInvertido = rol[::-1]

sum = 0
secuencia = [2, 3, 4, 5, 6, 7]
for i, digito in enumerate(rolInvertido):
    mlt = secuencia[i % 6]
    sum += int(digito * mlt)

rest = sum % 11

digVerf = 11 -rest

if digVerf == 11:
    digVerf = 0

print("Digito verificador: ", rol,"-",digVerf)