"""
Este módulo gestiona la lógica principal del juego de adivinanza de números.

La función principal inicia la introducción del juego y permite a los jugadores
jugar múltiples rondas, solicitando la opción de jugar de nuevo al final de cada partida.
"""

from utilidades import intro, jugar_de_nuevo
from juego import juega

def main():
    """Función principal del juego.

    Esta función se encarga de ejecutar la introducción del juego y 
    gestionar el bucle principal que permite jugar varias veces.
    """
    intro()  # Mostrar la introducción del juego
    # Bucle principal para permitir jugar varias veces
    while True:
        juega()  # Iniciar un nuevo juego
        if not jugar_de_nuevo():  # Preguntar si el jugador quiere jugar de nuevo
            print("Gracias por jugar. ¡Hasta luego!")
            break  # Salir del bucle si el jugador no desea continuar

if __name__ == '__main__':
    main()  # Ejecutar la función principal
