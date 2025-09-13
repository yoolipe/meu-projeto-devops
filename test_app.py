# test_app.py
import unittest
from app import soma, subtrai, multiplica, divide, saudacao

class TestApp(unittest.TestCase):

    def test_soma(self):
        self.assertEqual(soma(2, 3), 5)

    def test_subtrai(self):
        self.assertEqual(subtrai(5, 3), 2)

    def test_multiplica(self):
        self.assertEqual(multiplica(4, 3), 12)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

    def test_saudacao(self):
        self.assertEqual(saudacao("Lipe"), "Olá, Lipe!")

if __name__ == '__main__':
    unittest.main()
