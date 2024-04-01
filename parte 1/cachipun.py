print("-----Bienvenido a cachipun-----")
marcador = {'A': 0, 'B': 0}

restld = {
    ('tijera', 'papel'): 'A',
    ('papel', 'tijera'): 'B',
    ('piedra', 'tijera'): 'A',
    ('piedra', 'papel'): 'B',
    ('tijera', 'piedra'): 'B',
    ('papel',  'piedra'): 'A',
}

while marcador['A'] < 3 and marcador['B'] < 3:
    jugadorA = input("Jugador A, ingrese un movimiento: ").lower()
    jugadorB = input("Jugador B, ingrese un movimiento: ").lower()
    
    if  jugadorA  not in ['tijera', 'papel', 'piedra'] or jugadorB not in ['tijera', 'papel', 'piedra']:
        print("Ingrese un movimiento correcto (tijera, papel, piedra)")
        continue

    if jugadorA == jugadorB:
        print("Empate")
    else:
        ganador = restld[(jugadorA, jugadorB)]
        print("Ganador", ganador)
        marcador[ganador] += 1

    print(f"{marcador['A']} - {marcador['B']}")

if marcador['A'] == 3:
    print("Juego finalizado. Jugador A gana")
else: 
    print("Juego finalizado. Jugador B gana")