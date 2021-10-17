def palindrome(frase):
    frase = frase.replace(' ', '')
    if str(frase) == str(frase)[::-1]:
        return True
    return False


frase = 'Wild imagination!'.upper().replace(',', '').replace('’', '').replace('!', '').replace('/', '')
validation = palindrome(frase)

print(validation)

