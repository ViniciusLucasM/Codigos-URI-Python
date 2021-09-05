botao = input('')
while iter(botao):
    grau = float(input('Digite os graus desejados: '))

    if grau <= 360:
        if grau < 90 or grau == 360:
            print('Bom dia!!')
        elif grau < 180:
            print('Boa tarde!!')
        elif grau < 270:
            print('Boa noite!!')
        elif grau < 360:
            print('De madrugada!!')
        else:
            print('Bom dia!!')

        horas = float()
        if grau >= 270:
            horas = ((grau - 270.0) * 4.0) / 60.0
        else:
            horas = ((grau * 4.0) / 60.00) + 6.0

        minuto = float((horas * 60.0) % 60.0) - 1
        segundo = float(grau * 60.0)

        if segundo > 59:
            segundo = 0.0
            minuto += 1.0

        print("{}:{}:{}".format(int(horas), int(minuto), int(segundo)))
