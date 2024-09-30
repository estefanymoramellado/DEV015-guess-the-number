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
    intro()  
    while True:
        juega()  
        if not jugar_de_nuevo():
            print("Gracias por jugar. ¡Hasta luego!")
            break 

if __name__ == '__main__':
    main()
