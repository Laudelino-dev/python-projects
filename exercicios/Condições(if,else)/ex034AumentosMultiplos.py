# Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento. Para salarios superiores a R$1.250,00, calcule o aumento de 10%. Para salarios inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite aqui o seu salario R$:'))
if salario > 1250.00:
    novo_salario = salario + salario * 0.10
    print('Seu novo salario é de R$:{}'.format(novo_salario))
else:
    new_salario = salario + salario * 0.15
    print('Seu novo salario é de R$:{}'.format(new_salario))
