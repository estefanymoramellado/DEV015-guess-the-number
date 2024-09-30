"""
turnos.py

Este módulo contiene las funciones para gestionar los turnos del juego,
incluyendo el turno de la jugadora y el turno del ordenador.

Funciones:
- turno_jugadora(): Solicita un número al usuario y lo devuelve.
- turno_ordenador(low, high): Genera un número aleatorio dentro del rango dado.
"""
import random

def turno_jugadora():
    """Solicita al usuario que ingrese un número del 1 al 100.

    Returns:
        int: El número ingresado por el usuario.
    """
    while True:
        try:
            num_usuario = int(input("Inserta un número del 1 al 100: "))
            return num_usuario
        except ValueError:
            print("Por favor, introduce un número válido.")

def turno_ordenador(low, high):
    """Genera un número aleatorio para el turno del ordenador.

    Args:
        low (int): El límite inferior del rango.
        high (int): El límite superior del rango.

    Returns:
        int: Un número aleatorio dentro del rango [low, high].
    """
    return random.randint(low, high)
