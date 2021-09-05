while True:
    try:
        try:
            digi = input('Digite algo: ').replace('o', '0').replace(
                'O', '0').replace('l', '1').replace(',', '').replace(' ', '')
            if int(digi) > 2147483647:
                print('ERROR')
            else:
                print(digi)
        except ValueError:
            print('ERROR')
    except EOFError and KeyboardInterrupt:
        print('Obrigado por utilizar nosso programa :)')
        break
