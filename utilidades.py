"""
Este módulo contiene funciones auxiliares para el juego de adivinar números.
Incluye funciones para mostrar la introducción del juego, obtener un número aleatorio,
comparar números y preguntar al jugador si desea jugar de nuevo.
"""

import random

def intro():
    """Muestra la introducción del juego."""
    print(" " * 10,"¡Adivina el número!", " " * 10)
def obtener_numero_aleatorio():
    """Devuelve un número aleatorio entre 1 y 5.
    
    Returns:
        int: Número aleatorio.
    """
    return random.randint(1, 5)

def compara_numeros(numero_aleatorio, numero_intentado):
    """Compara el número intentado con el número aleatorio.
    
    Args:
        numero_aleatorio (int): El número que debe ser adivinado.
        numero_intentado (int): El número que la jugadora ha intentado adivinar.
    
    Returns:
        str: "PEQUEÑO" si el número intentado es mayor, 
        "GRANDE" si es menor, "IGUAL" si es correcto.
    """
    if numero_intentado > numero_aleatorio:
        return "PEQUEÑO"
    if numero_intentado < numero_aleatorio:
        return "GRANDE"
    return "IGUAL"

def jugar_de_nuevo():
    """Pregunta a la jugadora si desea jugar de nuevo.
    
    Returns:
        bool: True si quiere jugar de nuevo, False en caso contrario.
    """
    while True:
        respuesta = input("¿Quieres jugar de nuevo? (s/n): ").lower()
        if respuesta in ['s', 'n']:
            return respuesta == 's'
        print("Por favor, responde con 's' o 'n'.")
