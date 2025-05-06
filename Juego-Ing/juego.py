import sys
import random

def comparar(j1, j2):
    reglas = {
        "piedra": {"tijera": 1, "papel": -1, "piedra": 0},
        "papel": {"piedra": 1, "tijera": -1, "papel": 0},
        "tijera": {"papel": 1, "piedra": -1, "tijera": 0}
    }
    return reglas[j1][j2]

def main():
    if len(sys.argv) != 4:
        print("Uso: python juego.py <jugada1> <jugada2> <jugada3>")
        return

    opciones = ["piedra", "papel", "tijera"]
    humano = [jugada.lower() for jugada in sys.argv[1:]]
    maquina = [random.choice(opciones) for _ in range(3)]

    print("El programa elige:", ' '.join(maquina))

    puntos_humano = 0
    puntos_maquina = 0

    for h, m in zip(humano, maquina):
        resultado = comparar(h, m)
        if resultado == 1:
            puntos_humano += 1
        elif resultado == -1:
            puntos_maquina += 1

    print(f"Punteo: {puntos_humano} - {puntos_maquina}")
    if puntos_humano > puntos_maquina:
        print("Ganador: Humano")
    elif puntos_maquina > puntos_humano:
        print("Ganador: Programa")
    else:
        print("Empate")

if __name__ == "__main__":
    main()
