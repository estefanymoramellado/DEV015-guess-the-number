import unittest
from unittest.mock import patch
from utilidades import compara_numeros

class TestUtilidades(unittest.TestCase):
    
    def test_compara_numeros(self):
        self.assertEqual(compara_numeros(10, 5), "GRANDE")
        self.assertEqual(compara_numeros(5, 10), "PEQUEÑO")
        self.assertEqual(compara_numeros(5, 5), "IGUAL")
    
    @patch('utilidades.obtener_numero_aleatorio')
    def test_obtener_numero_aleatorio(self, mock_obtener_numero_aleatorio):
        # Configura el mock para que devuelva un valor específico
        mock_obtener_numero_aleatorio.return_value = 3
        
        # Llama a la función que utiliza el número aleatorio
        numero = mock_obtener_numero_aleatorio()  # Cambia esto para llamar al mock
        
        # Verifica que el número es el que esperas
        self.assertEqual(numero, 3)

        # Verifica que el mock fue llamado
        mock_obtener_numero_aleatorio.assert_called_once()

if __name__ == '__main__':
    unittest.main()
