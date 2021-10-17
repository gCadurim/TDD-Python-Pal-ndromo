frase = str('000').strip().upper()
removed = frase.replace(",", "/")
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]


def teste():
    return 'false'
print('Não')

def teste():
    return 'true'
print('Palíndromo')