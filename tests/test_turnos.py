import unittest
from turnos import turno_jugadora, turno_ordenador

class TestTurnos(unittest.TestCase):

    def test_turno_ordenador(self):
        resultado = turno_ordenador(1, 5)
        self.assertIn(resultado, range(1, 5))  # Verifica que el número esté en el rango correcto

if __name__ == '__main__':
    unittest.main()
