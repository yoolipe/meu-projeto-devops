import unittest
from meu_app import soma, subtrai, multiplica, divide, saudacao

class TestApp(unittest.TestCase):

    def test_soma(self):
        self.assertEqual(soma(2, 3), 5)
        self.assertEqual(soma(-1, 1), 0)
        self.assertEqual(soma(-1, -1), -2)
        self.assertEqual(soma(0, 0), 0)

    def test_subtrai(self):
        self.assertEqual(subtrai(5, 3), 2)
        self.assertEqual(subtrai(3, 5), -2)
        self.assertEqual(subtrai(-1, 1), -2)
        self.assertEqual(subtrai(0, 0), 0)

    def test_multiplica(self):
        self.assertEqual(multiplica(4, 3), 12)
        self.assertEqual(multiplica(-1, 5), -5)
        self.assertEqual(multiplica(-2, -3), 6)
        self.assertEqual(multiplica(0, 10), 0)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(10, -2), -5)
        self.assertEqual(divide(7, 2), 3.5)
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

    def test_saudacao(self):
        self.assertEqual(saudacao("Lipe"), "Olá, Lipe!")
        self.assertEqual(saudacao("Mundo"), "Olá, Mundo!")
        self.assertEqual(saudacao(""), "Olá, !")
        self.assertEqual(saudacao("123"), "Olá, 123!")

if __name__ == '__main__':
    unittest.main()
