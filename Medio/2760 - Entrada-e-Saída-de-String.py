var1, var2, var3 = '', '', ''
countvar1, countvar2, countvar3 = 0, 0, 0


def verficCarac(var1, var2, var3):
    if var1 > 100:
        print('')
        print('A 1ª Frase ultrapassou os 100 caracteres')
        print('')
    elif var2 > 100:
        print('')
        print('A 2ª Frase ultrapassou os 100 caracteres')
        print('')
    elif var3 > 100:
        print('')
        print('A 3ª Frase ultrapassou os 100 caracteres')
        print('')


while var1 == '' or var2 == '' or var3 == '':
    var1 = str(input('Digite a 1ª frase: '))
    var2 = str(input('Digite a 2ª frase: '))
    var3 = str(input('Digite a 3ª frase: '))

    if len(var1) > 100 or len(var2) > 100 or len(var3) > 100:
        verficCarac(len(var1), len(var2), len(var3))
        var1, var2, var3 = '', '', ''

print(var1 + var2 + var3)
print(var2 + var3 + var1)
print(var3 + var1 + var2)
print(var1[:10] + var2[:10] + var3[:10])
