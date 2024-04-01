hora = int(input("Ingrese la hora actual:"))
cantidad = int(input("Ingrese la cantidad de horas:"))

nuevo = (hora + cantidad) %12

print("Dentro de", cantidad, "horas, el reloj marcara las", nuevo if nuevo != 0 else 12)
