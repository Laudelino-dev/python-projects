# Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa. O programa vai perguntar qual o valor da casa, o salario do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do sálario ou então o emprestimo será negado.

valorcasa = float(input('Qual o valor da casa que deseja comprar: '))
salario = float(input('Qual o seu salario atual R$: '))
anos = int(input('Deseja pagar em quantos anos: ')) * 12
prestaçao = valorcasa / anos
aprovar = salario * 0.30
if prestaçao <= aprovar:
    print(f'Parabens! Você pode comprar a casa, vai ficar com prestações de R$:{prestaçao:.2f} por um total de {anos} meses.')
else:
    print('Infelizmente não podemos te fornecer o emprestimo')
