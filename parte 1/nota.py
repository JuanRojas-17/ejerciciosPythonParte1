nota1 = int(input("Ingrese la nota del primer certamen: "))
nota2 = int(input("Ingrese la nota del segundo certamen: "))
lab = int(input("Ingrese la nota del laboratorio: "))
nf = 60

nc = (nf - lab * 0.3) / 0.7
nota3 = 3 * nc - nota1 - nota2

nf = nc *0.7 + lab *0.3
if nota3>=0:
    print("Tu nota necesaria es: ", nota3)
elif nf >= 60:
    print("Ya aprobaste")