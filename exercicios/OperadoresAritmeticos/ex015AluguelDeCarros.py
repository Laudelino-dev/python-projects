# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input('Quantos dias o carro foi alugado : '))
km = float(input('Quantos km foram rodados : '))
valor_dia = dias * 60
valor_km = km * 0.15
valor_total = valor_dia + valor_km
print('O carro ficou alugado num total de : {} dias'.format(dias))
print('O carro rodou um total de : {} km'.format(km))
print('Valor a se pagar por dias alugados : R${}'.format(valor_dia))
print('Valor a se pagar por km rodados : R${:.2f}'.format(valor_km))
print('De acordo com isso, o valor final a se pagar é de : R${:.2f}'.format(valor_total))
