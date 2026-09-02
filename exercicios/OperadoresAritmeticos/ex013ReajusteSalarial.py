# Desafio 13
# Faça o algoritmo ler o salario de um funcionario e mostre seu novo salario com 15% de aumento

salario = float(input('Informe qual o seu salario : R$'))
# porcentagem = float(0.15)

aumento = salario * (0.15)

novo_salario = salario + aumento

print('O seu salario de agora é : {}'.format(salario))
print('O novo salario é de : {} '.format(novo_salario))
