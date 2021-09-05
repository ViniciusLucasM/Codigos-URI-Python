while True:
    try:
        try:
            lista = []
            num1 = int(input('Digite o 1º numero: '))
            num = int(input('Digite o 2º numero: '))
            validar = str(
                input('Deseja excluir todos os numeros? S/N: ')).upper()

            for i in str(num1):
                lista.append(i)

            if validar == 'NAO' or validar == 'N':
                for c in str(num):
                    lista.remove(c)
                resu = ''.join(lista)
                print(resu)
            elif validar == 'SIM' or validar == 'S':
                while str(num) in lista:
                    lista.remove(str(num))
                resu = ''.join(lista)
                print(resu)
            else:
                print('')
                print(
                    'Por favor digite uma das seguintes opicoes (SIM OU NAO)')
        except ValueError or KeyboardInterrupt:
            print('Por favor digite apenas numeros')
    except EOFError or KeyboardInterrupt:
        print('Obrigado por utilizar nosso programa :)')
        break
