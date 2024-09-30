"""Módulo del juego de adivinanza de números.

Este módulo contiene la lógica del juego en el que un jugador y
un ordenador intentan adivinar un número
generado aleatoriamente. 
El jugador puede ingresar un número entre 1 y 5, y el ordenador también hace
sus intentos de adivinanza. El juego continúa hasta que uno de los dos adivina el número correcto.
"""

from turnos import turno_jugadora, turno_ordenador
from utilidades import compara_numeros, obtener_numero_aleatorio

def juega():
    """Función principal del juego que gestiona los turnos de la jugadora y del ordenador.

    Esta función permite a la jugadora adivinar un número generado aleatoriamente por el ordenador
    y también permite al ordenador intentar adivinar el número elegido por la jugadora.
    
    El juego continúa hasta que uno de los dos jugadores adivine el número correcto.
    """
    intentos = 0
    low = 1
    high = 5
    numero_aleatorio = obtener_numero_aleatorio()

    while True:
        # Turno de la jugadora
        print("Es tu turno:")
        num_usuario = turno_jugadora()
        intentos += 1
        resultado = compara_numeros(numero_aleatorio, num_usuario)
        if resultado == "PEQUEÑO":
            print("El número es más PEQUEÑO, ¡intenta otra vez!")
            high = num_usuario - 1
        elif resultado == "GRANDE":
            print("El número es más GRANDE, ¡intenta otra vez!")
            low = num_usuario + 1
        else:
            print(
                f"¡Felicidades! Has adivinado el número {numero_aleatorio} "
                f"en {intentos} intentos."
            )
            break
        # Turno del ordenador
        print("Es el turno del ordenador:")
        num_ordenador = turno_ordenador(low, high)
        print(f"El ordenador adivina: {num_ordenador}")
        intentos += 1
        resultado = compara_numeros(numero_aleatorio, num_ordenador)
        if resultado == "PEQUEÑO":
            print("El número es más PEQUEÑO.")
            high = num_ordenador - 1
        elif resultado == "GRANDE":
            print("El número es más GRANDE.")
            low = num_ordenador + 1
        else:
            print(
              f"¡El ordenador ha adivinado el número {numero_aleatorio} "
              f"en {intentos} intentos!"
            )
