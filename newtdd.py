from unittest import TestCase
import newcod


class teste(TestCase):

        def teste_nao_palindrome(self):
            var = newcod.inverso != newcod.junto
            valor_esperado = True
            self.assertEqual(var, valor_esperado)
            return 'false'

        def teste_palindrome(self):
            var = newcod.inverso == newcod.junto
            valor_esperado = True
            self.assertEqual(var, valor_esperado)
            return 'true'
