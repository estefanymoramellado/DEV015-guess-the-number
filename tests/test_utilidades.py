import unittest
from utilidades import compara_numeros, obtener_numero_aleatorio

class TestUtilidades(unittest.TestCase):
    
    def test_compara_numeros(self):
        # Probar cuando el número intentado es menor que el número aleatorio
        self.assertEqual(compara_numeros(10, 5), "GRANDE")
        
        # Probar cuando el número intentado es mayor que el número aleatorio
        self.assertEqual(compara_numeros(5, 10), "PEQUEÑO")
        
        # Probar cuando el número intentado es igual al número aleatorio
        self.assertEqual(compara_numeros(5, 5), "IGUAL")
    
    def test_obtener_numero_aleatorio(self):
        # Probar si el número generado está dentro del rango esperado
        numero = obtener_numero_aleatorio()
        self.assertTrue(1 <= numero <= 5)

if __name__ == '__main__':
    unittest.main()
