import unittest
from unittest.mock import patch
from turnos import turno_jugadora, turno_ordenador

class TestTurnos(unittest.TestCase):

    def test_turno_ordenador(self):
        resultado = turno_ordenador(1, 5)
        self.assertIn(resultado, range(1, 6)) 

    @patch('builtins.input', side_effect=['3'])  
    def test_turno_jugadora(self, mock_input):
        resultado = turno_jugadora() 
        self.assertEqual(resultado, 3)

if __name__ == '__main__':
    unittest.main()
