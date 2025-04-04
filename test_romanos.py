import unittest
from romanos import decimal_a_romano


def test_numeros_basicos(self):
    self.assertEqual(decimal_a_romano(1), "I")
    self.assertEqual(decimal_a_romano(5), "V")
    self.assertEqual(decimal_a_romano(10), "X")
    self.assertEqual(decimal_a_romano(50), "L")
    self.assertEqual(decimal_a_romano(100), "C")
    self.assertEqual(decimal_a_romano(500), "D")
    self.assertEqual(decimal_a_romano(1000), "M")

class TestDecimalARomano(unittest.TestCase):
    def test_unidad(self):
        self.assertEqual(decimal_a_romano(1), "I")
        

if __name__ == '__main__':
    unittest.main()
