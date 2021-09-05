salario = float(input('Digite seu salário: '))


def calSalario(salario, porcen):
    resuPorce = salario * (porcen/100)
    novoSal = salario + resuPorce
    print('Novo salario: {:.2f}'.format(novoSal) + '\n' +
          'Reajuste ganho: {:.2f}'.format(resuPorce) + '\n'
          + 'Em percentual: {} %'.format(porcen) + '\n')


if salario >= 0 and salario <= 400.00:
    calSalario(salario, 15)
elif salario >= 400.01 and salario <= 800.00:
    calSalario(salario, 12)
elif salario >= 800.01 and salario <= 1200.00:
    calSalario(salario, 10)
elif salario >= 1200.01 and salario <= 2000.00:
    calSalario(salario, 7)
else:
    calSalario(salario, 4)
