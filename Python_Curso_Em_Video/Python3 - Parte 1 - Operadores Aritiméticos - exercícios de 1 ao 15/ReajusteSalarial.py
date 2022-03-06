salario = float(input('Qual o salário do funcionário?: R$'))
percertual_reajuste = int(input('Qual o percentual de reajuste?: '))
print('Um funcionário que ganhava R${}, com {}% de aumento, passa a receber R${:.2f}'.format(salario, percertual_reajuste, salario + (salario * percertual_reajuste/100)))