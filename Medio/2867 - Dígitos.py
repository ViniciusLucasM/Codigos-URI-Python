import math
c = int(input('Digite a quantidade de teste que deseja realizar: '))

for i in range(c):
    n = int(input('Digite o 1º numero: '))
    m = int(input('Digite o 2º numero: '))
    digitos = int(math.log10(math.pow(n, m)) + 1)
    print(digitos)
