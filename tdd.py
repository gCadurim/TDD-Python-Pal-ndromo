from unittest import TestCase
import __main__
from cod import frase1, frase2


class teste(TestCase):
    # def teste_palindrome(self):
    #   frase()
    def teste_palindrome(self):
        frase1()
        valor_esperado = 'palíndromo'
        self.assertEqual(frase1(), valor_esperado)

    def teste_nao_palindrome(self):
        frase2()
        valor_esperado = 'nao palíndromo'
        self.assertEqual(frase2(), valor_esperado)
