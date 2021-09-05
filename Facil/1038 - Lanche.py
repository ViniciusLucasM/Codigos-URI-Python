numLanche = int(input('Digite o número do lanche desejado: '))
qtdLache = int(input('Digite a quantidade de laches desejado: '))

listaLanche = {'1': 'Cachorro Quente', '2': 'X-Salada',
               '3': 'X-Bacon', '4': 'Torrada Simples', '5': 'Refrigerante'}
listaPreco = {'Cachorro Quente': '4.00', 'X-Salada': '4.50', 'X-Bacon': '5.00',
              'Torrada Simples': '2.00', 'Refrigerante': '1.50'}


def calPreco(Nlanche, qtclanche):
    try:
        lanche = listaLanche[str(Nlanche)]
        if lanche in listaPreco:
            precoF = float(listaPreco[lanche]) * qtclanche
        else:
            print('Esse lanche não está no nosso cardápio')
    except KeyError:
        print('Esse lanche não está no nosso cardápio')
    print('O valor final da compra é R${:.2f}'.format(precoF))


calPreco(numLanche, qtdLache)
