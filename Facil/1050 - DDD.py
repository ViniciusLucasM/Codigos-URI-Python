ddd = int(input('Digite o DDD desejado: '))


lista = {'61': 'Brasilia', '71': 'Salvador',
         '11': 'São Paulo', '21': 'Rio de Janeiro',
         '32': 'Juiz de Fora', '29': 'Campinas',
         '27': 'Vitoria', '31': 'Belo Horizonte'}

try:
    print(lista[str(ddd)])
except KeyError:
    print('POR FAVOR DIGITE UM DDD VÁLIDO. OS DDDs VÁLIDOS '
          'SÃO 61, 71, 11, 21, 32, 29, 27, 31')
