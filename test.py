from unittest import TestCase
frase = 'Wonderful-fool'.upper().replace(',', '').replace('’', '').replace('!', '').replace('/', '')
junto = ''.join(frase)

class teste(TestCase):

    def teste_nao_palindrome(self):
        var = junto != frase

    def teste_palindrome(self):
        var = junto == frase
